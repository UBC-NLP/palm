import asyncio
import os
from asyncio import Semaphore
import logging
from langchain.evaluation import load_evaluator
from langchain_openai import ChatOpenAI
import json
import aiofiles
import argparse
from utils import load_jsonl
import statistics

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
parser = argparse.ArgumentParser(description="Evaluate model predictions against references")
parser.add_argument('--output_judgements', type=str, required=True, help='local model path')
parser.add_argument('--vllm_model_id', type=str, required=True, help='model id for vLLM server')
parser.add_argument('--preds_file', type=str, required=True, help='data file containing responses')
parser.add_argument('--max_length', type=int, default=2048, help='max generated judgement length')
parser.add_argument('--criteria', type=str, default='correctness', help='max length')
parser.add_argument('--vllm_port', type=int, default=8000, help='The port where vLLM server is served locally')
parser.add_argument('--max_concurrency', type=int, default=100, help='Maximum number of concurrent evaluations')
args = parser.parse_args()

preds_data = load_jsonl(args.preds_file)
inference_server_url = f"http://localhost:{args.vllm_port}/v1"
llm = ChatOpenAI(
    model=args.vllm_model_id,
    openai_api_key="EMPTY",
    openai_api_base=inference_server_url,
    max_tokens=args.max_length,
    temperature=0,
)

criterias = [args.criteria]

os.makedirs('judgments', exist_ok=True)

async def evaluate_and_write_row(evaluator, row, file, semaphore, idx, total):
    async with semaphore:
        if row.get('input'):
            input_text = row['instruction'] + '\n' + row['input']
        else:
            input_text = row['instruction']
        
        try:
            eval_result = await evaluator.aevaluate_strings(
                prediction=row['model_response'],
                reference=row['output'],
                input=input_text
            )
            logging.info(f"Evaluated {idx+1}/{total} - Success")
        except Exception as e:
            eval_result = {"error": str(e)}
            logging.error(f"Evaluated {idx+1}/{total} - Error: {str(e)}")
        
        record = row.copy()
        record['eval_result'] = eval_result
        
        await file.write(json.dumps(record, ensure_ascii=False) + '\n')
        await file.flush()

async def process_criteria(criteria, preds_data, semaphore):
    evaluator = load_evaluator("labeled_score_string", llm=llm, criteria=criteria)
    export_file = f'judgments/{args.output_judgements}_{criteria}.jsonl'
    
    if os.path.exists(export_file):
        logging.info(f"File {export_file} already exists, skipping")
        return await calculate_average_score(export_file)
    
    async with aiofiles.open(export_file, 'w') as f:
        tasks = [
            evaluate_and_write_row(evaluator, row, f, semaphore, idx, len(preds_data)) 
            for idx, row in enumerate(preds_data)
        ]
        await asyncio.gather(*tasks)
    
    logging.info(f"Completed evaluation for criteria: {criteria}")
    return await calculate_average_score(export_file)

async def calculate_average_score(file_path):
    scores = []
    async with aiofiles.open(file_path, 'r') as f:
        async for line in f:
            try:
                record = json.loads(line)
                if 'eval_result' in record and 'score' in record['eval_result']:
                    scores.append(record['eval_result']['score'])
            except Exception as e:
                logging.error(f"Error processing line in {file_path}: {str(e)}")
    
    if scores:
        avg_score = statistics.mean(scores)
        return avg_score
    else:
        logging.warning(f"No valid scores found in {file_path}")
        return None

async def main():
    semaphore = Semaphore(args.max_concurrency)
    
    criteria_tasks = [
        process_criteria(criteria, preds_data, semaphore) 
        for criteria in criterias
    ]
    
    logging.info(f"Starting evaluation with {len(preds_data)} samples across {len(criterias)} criteria")
    results = await asyncio.gather(*criteria_tasks)
    
    for criteria, avg_score in zip(criterias, results):
        if avg_score is not None:
            logging.info(f"Average {criteria} score: {avg_score:.4f}/10")
        else:
            logging.info(f"Average {criteria} score: N/A (no valid scores found)")
    
    logging.info("All evaluations completed")

if __name__ == "__main__":
    asyncio.run(main())
