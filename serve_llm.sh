vllm serve $1 \
    --tensor-parallel-size $2 \
    --dtype auto \
    --disable-log-requests \
    --host 0.0.0.0 \
    --max-model-len 8000 \
   --max-seq-len-to-capture 4096 \
   --max-num-seqs 100 \
    --port $3
