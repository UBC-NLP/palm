import json
import asyncio
import os
import aiohttp
import aiofiles
import argparse
from transformers import AutoTokenizer
from utils import load_jsonl
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from aiohttp import ClientError
import logging

parser = argparse.ArgumentParser(description="A script that uses an integer argument")
parser.add_argument('--model_path', type=str, help='model local path')
parser.add_argument('--vllm_model_id', type=str, help='model id from vLLM')
parser.add_argument('--data_path', type=str, help='data file containing instructions in JSONL format')
parser.add_argument('--max_length', type=int, default=4096, help='max length for generated response')
parser.add_argument('--vllm_port', type=int, help='The port where vLLM server is served locally')
args = parser.parse_args()


model_id = args.model_path.split('/')[-1]
vllm_model_id = args.vllm_model_id

tokenizer = AutoTokenizer.from_pretrained(args.model_path)

os.makedirs('responses', exist_ok=True)

BATCH_SIZE = 100
OUTPUT_JSONL_FILE = f"responses/{model_id}.jsonl"
MAX_RETRIES = 3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_retry(retry_state):
    exception = retry_state.outcome.exception()
    logger.error(f"Error occurred: {exception}. Retrying...")

@retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(ClientError),
    before_sleep=log_retry
)

@retry(stop=stop_after_attempt(MAX_RETRIES), wait=wait_exponential(multiplier=1, min=4, max=10))
async def gen_response(prompt, session, url=f"http://0.0.0.0:{args.vllm_port}/v1/completions"):
    prompt = f"""{prompt}"""
    messages = [{"role": "user", "content": prompt}]
    formatted_message = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "model": vllm_model_id,
        "prompt": formatted_message,
        "max_tokens": args.max_length - len(tokenizer.encode(formatted_message)) - 5,
        "temperature": 0
    }

    async with session.post(url, json=data, headers=headers, timeout=600) as response:
        response.raise_for_status()
        result = await response.json()
        return result['choices'][0]['text']

async def process_document(document, session):
    try:
        if document['input']:
            prompt = f"""{document['instruction']}\n{document['input']}"""
        else:
            prompt = document['instruction']
        generated_response = await gen_response(prompt, session)
        result = {
            "id": document['id'],
            "instruction": document['instruction'],
            "input": document['input'],
            "output": document['output'],
            "model_response": generated_response,
            "success": True
        }
    except Exception as e:
        print(f"Error processing document {document['id']}: {str(e)}")
        result = {
            "id": document['id'],
            "instruction": document['instruction'],
            "input": document['input'],
            "output": document['output'],
            "model_response": None,
            "success": False,
            "error": str(e)
        }
    return result

async def process_batch(batch, session):
    tasks = [process_document(document, session) for document in batch]
    return await asyncio.gather(*tasks)

async def write_results(results):
    async with aiofiles.open(OUTPUT_JSONL_FILE, mode='a', encoding="utf-8") as f:
        for result in results:
            await f.write(json.dumps(result, ensure_ascii=False) + '\n')

async def process_documents():
    data = load_jsonl(args.data_path)
    connector = aiohttp.TCPConnector(limit=BATCH_SIZE)
    async with aiohttp.ClientSession(connector=connector) as session:
        for i in range(0, len(data), BATCH_SIZE):
            batch = data[i:i+BATCH_SIZE]
            results = await process_batch(batch, session)
            await write_results(results)
            print(f"Processed batch {i//BATCH_SIZE + 1}")
            
            # Retry failed requests
            failed_documents = [doc for doc in results if not doc['success']]
            if failed_documents:
                print(f"Retrying {len(failed_documents)} failed requests...")
                retry_results = await process_batch(failed_documents, session)
                await write_results(retry_results)

def main():
    asyncio.run(process_documents())

if __name__ == "__main__":
    main()
