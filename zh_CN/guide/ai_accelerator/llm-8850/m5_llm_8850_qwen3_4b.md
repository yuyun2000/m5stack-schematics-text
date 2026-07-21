# Qwen3-1.7B

1. [手动下载模型](https://huggingface.co/AXERA-TECH/Qwen3-4B) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/Qwen3-4B
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/Qwen3-4B$ ls -lh
total 5.4G
-rw-rw-r-- 1 m5stack m5stack  584 Mar 23 09:34 config.json
-rw-rw-r-- 1 m5stack m5stack 742M Mar 23 09:47 model.embed_tokens.weight.bfloat16.bin
-rw-rw-r-- 1 m5stack m5stack  279 Mar 23 09:34 post_config.json
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:42 qwen3_p128_l0_together.axmodel.onnx
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:47 qwen3_p128_l10_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:47 qwen3_p128_l11_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:42 qwen3_p128_l12_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:42 qwen3_p128_l13_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:45 qwen3_p128_l14_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:45 qwen3_p128_l15_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:45 qwen3_p128_l16_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:40 qwen3_p128_l17_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:45 qwen3_p128_l18_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:46 qwen3_p128_l19_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:35 qwen3_p128_l1_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:43 qwen3_p128_l20_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:42 qwen3_p128_l21_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:40 qwen3_p128_l22_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:45 qwen3_p128_l23_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:37 qwen3_p128_l24_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:37 qwen3_p128_l25_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:40 qwen3_p128_l26_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:37 qwen3_p128_l27_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:35 qwen3_p128_l28_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:37 qwen3_p128_l29_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:35 qwen3_p128_l2_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:37 qwen3_p128_l30_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:37 qwen3_p128_l31_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:40 qwen3_p128_l32_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:40 qwen3_p128_l33_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:45 qwen3_p128_l34_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:40 qwen3_p128_l35_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:35 qwen3_p128_l3_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:42 qwen3_p128_l4_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:42 qwen3_p128_l5_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:35 qwen3_p128_l6_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:35 qwen3_p128_l7_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:47 qwen3_p128_l8_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 120M Mar 23 09:47 qwen3_p128_l9_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 405M Mar 23 09:41 qwen3_post.axmodel
-rw-rw-r-- 1 m5stack m5stack 1.6M Mar 23 09:34 qwen3_tokenizer.txt
-rw-rw-r-- 1 m5stack m5stack 8.6K Mar 23 09:34 README.md
```

\#> 提示 | 如果之前已经安装了 **axllm** ，不需要重复安装。

2. 安装 axllm

```bash
curl -fsSL https://raw.githubusercontent.com/AXERA-TECH/ax-llm/axllm/install.sh | bash
```

安装成功后可以在终端输出以下信息：

```bash
m5stack@raspberrypi:~ $ axllm 
Usage:
  axllm run <model_path> [options]    Run interactive chat mode
  axllm serve <model_path> [options]  Run HTTP API server mode

Arguments:
  model_path    Path to model directory containing config.json and model files

Serve options:
  --port <port> Server port (default: 8000)

Embedding model config:
  Set "is_embedding": true in config.json to enable /v1/embeddings.

Model directory structure:
  model_path/
    ├── config.json          # Model configuration
    ├── tokenizer.txt        # Tokenizer model
    ├── *.axmodel            # AXera model files
    └── post_config.json     # Post-processing config (optional)
```

3. 终端聊天模式

```bash
axllm run Qwen3-4B/
```

```bash
17:46:21.615 INF Init:218 | LLM init start
17:46:21.615 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 1
 97% | ###############################  |  38 /  39 [88.17s<90.49s, 0.43 count/s] init post axmodel ok,remain_cmm(1798 MB)       
17:47:50.101 INF Init:368 | max_token_len : 2559
17:47:50.101 INF Init:371 | kv_cache_size : 1024, kv_cache_num: 2559
17:47:50.101 INF Init:374 | prefill_token_num : 128
17:47:50.101 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
17:47:50.101 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 256
17:47:50.101 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 512
17:47:50.101 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 1024
17:47:50.101 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 1536
17:47:50.101 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 2048
17:47:50.101 INF Init:384 | prefill_max_token_num : 2048
17:47:50.101 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  39 /  39 [88.17s<88.17s, 0.44 count/s] embed_selector init ok
17:47:50.101 INF load_config:282 | load config: 
17:47:50.101 INF load_config:282 | {
17:47:50.101 INF load_config:282 |     "enable_repetition_penalty": false,
17:47:50.101 INF load_config:282 |     "enable_temperature": false,
17:47:50.101 INF load_config:282 |     "enable_top_k_sampling": false,
17:47:50.101 INF load_config:282 |     "enable_top_p_sampling": false,
17:47:50.101 INF load_config:282 |     "penalty_window": 20,
17:47:50.101 INF load_config:282 |     "repetition_penalty": 1.2,
17:47:50.101 INF load_config:282 |     "temperature": 0.9,
17:47:50.101 INF load_config:282 |     "top_k": 10,
17:47:50.101 INF load_config:282 |     "top_p": 0.8
17:47:50.101 INF load_config:282 | }
17:47:50.101 INF Init:448 | LLM init ok
Commands:
  /q, /exit  退出
  /reset     重置 kvcache
  /dd        删除一轮对话
  /pp        打印历史对话
Ctrl+C: 停止当前生成
----------------------------------------
prompt >> 
```

```bash
prompt >> hello
17:48:52.068 INF SetKVCache:749 | prefill_grpid:2 kv_cache_num:256 precompute_len:0 input_num_token:20
17:48:52.068 INF SetKVCache:757 | current prefill_max_token_num:2048
17:48:52.068 INF SetKVCache:760 | first run
17:48:52.079 INF Run:818 | input token num : 20, prefill_split_num : 1
17:48:52.079 INF Run:858 | prefill chunk p=0 history_len=0 grpid=1 kv_cache_num=0 input_tokens=20
17:48:52.080 INF Run:881 | prefill indices shape: p=0 idx_elems=128 idx_rows=1 pos_rows=0
17:48:52.915 INF Run:1023 | ttft: 835.52 ms
<think>
Okay, the user said "hello". I need to respond appropriately. Since they're greeting me, I should respond in a friendly and welcoming manner. Maybe start with a greeting back, like "Hello!" or "Hi there!". Then, I can ask how I can assist them today. I should keep it simple and open-ended so they feel comfortable to share what they need help with. Let me make sure the tone is positive and helpful. Also, check if there's any specific context I need to consider, but since the user just said hello, there's no prior conversation. Alright, time to put it all together.
</think>

Hello! How can I assist you today? 😊

17:49:31.155 NTC Run:1145 | hit eos,avg 3.69 token/s
17:49:31.155 INF GetKVCache:721 | precompute_len:161, remaining:1887
prompt >> 
```

4. OpenAI API 兼容服务器模式

!> 注意|如果之前安装了基于 StackFlow 的 OpenAI API 服务，需要先执行 systemctl stop llm-openai-api 停止，或 sudo apt remove llm-openai-api 卸载，避免端口冲突。

```bash
axllm serve Qwen3-4B/
```

```bash
17:49:53.780 INF Init:218 | LLM init start
17:49:53.780 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 1
 97% | ###############################  |  38 /  39 [88.00s<90.32s, 0.43 count/s] init post axmodel ok,remain_cmm(1798 MB)       
17:51:22.101 INF Init:368 | max_token_len : 2559
17:51:22.101 INF Init:371 | kv_cache_size : 1024, kv_cache_num: 2559
17:51:22.101 INF Init:374 | prefill_token_num : 128
17:51:22.101 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
17:51:22.101 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 256
17:51:22.101 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 512
17:51:22.101 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 1024
17:51:22.101 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 1536
17:51:22.101 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 2048
17:51:22.101 INF Init:384 | prefill_max_token_num : 2048
17:51:22.101 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  39 /  39 [88.00s<88.00s, 0.44 count/s] embed_selector init ok
17:51:22.101 INF load_config:282 | load config: 
17:51:22.101 INF load_config:282 | {
17:51:22.101 INF load_config:282 |     "enable_repetition_penalty": false,
17:51:22.101 INF load_config:282 |     "enable_temperature": false,
17:51:22.101 INF load_config:282 |     "enable_top_k_sampling": false,
17:51:22.101 INF load_config:282 |     "enable_top_p_sampling": false,
17:51:22.101 INF load_config:282 |     "penalty_window": 20,
17:51:22.101 INF load_config:282 |     "repetition_penalty": 1.2,
17:51:22.101 INF load_config:282 |     "temperature": 0.9,
17:51:22.101 INF load_config:282 |     "top_k": 10,
17:51:22.101 INF load_config:282 |     "top_p": 0.8
17:51:22.101 INF load_config:282 | }
17:51:22.101 INF Init:448 | LLM init ok
Starting server on port 8000 with model 'AXERA-TECH/Qwen3-4B'...
API URLs:
  GET  http://127.0.0.1:8000/health
  GET  http://127.0.0.1:8000/v1/models
  POST http://127.0.0.1:8000/v1/chat/completions
  GET  http://192.168.20.57:8000/health
  GET  http://192.168.20.57:8000/v1/models
  POST http://192.168.20.57:8000/v1/chat/completions
  GET  http://172.17.0.1:8000/health
  GET  http://172.17.0.1:8000/v1/models
  POST http://172.17.0.1:8000/v1/chat/completions
  GET  http://172.18.0.1:8000/health
  GET  http://172.18.0.1:8000/v1/models
  POST http://172.18.0.1:8000/v1/chat/completions
  GET  http://172.19.0.1:8000/health
  GET  http://172.19.0.1:8000/v1/models
  POST http://172.19.0.1:8000/v1/chat/completions
  GET  http://198.18.0.1:8000/health
  GET  http://198.18.0.1:8000/v1/models
  POST http://198.18.0.1:8000/v1/chat/completions
Aliases:
  GET  http://127.0.0.1:8000/models
  POST http://127.0.0.1:8000/chat/completions
  GET  http://192.168.20.57:8000/models
  POST http://192.168.20.57:8000/chat/completions
  GET  http://172.17.0.1:8000/models
  POST http://172.17.0.1:8000/chat/completions
  GET  http://172.18.0.1:8000/models
  POST http://172.18.0.1:8000/chat/completions
  GET  http://172.19.0.1:8000/models
  POST http://172.19.0.1:8000/chat/completions
  GET  http://198.18.0.1:8000/models
  POST http://198.18.0.1:8000/chat/completions
OpenAI API Server starting on http://0.0.0.0:8000
Max concurrency: 1
Models: AXERA-TECH/Qwen3-4B
```

使用 curl 调用 API

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "AXERA-TECH/Qwen3-4B",
    "messages": [
      {"role": "user", "content": "hello"}
    ]
  }'
```

返回结果：

```json
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "<think>\nOkay, the user said \"hello\". I need to respond appropriately. Since they're just greeting me, I should respond in a friendly and welcoming manner. Maybe say hello back and ask how I can assist them. Keep it simple and open-ended so they feel comfortable to share more. No need for any complex language here. Just a basic, polite response.\n</think>\n\nHello! How can I assist you today? 😊",
        "role": "assistant"
      }
    }
  ],
  "created": 1774950905,
  "id": "chatcmpl-ae43bd2b336b8e9f6dfed1b9",
  "model": "AXERA-TECH/Qwen3-4B",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 0,
    "prompt_tokens": 0,
    "total_tokens": 0
  }
}
```

使用 python 调用 API

```shell
pip install openai
```

```python
import requests

url = "http://localhost:8000/v1/chat/completions"
payload = {
    "model": "AXERA-TECH/Qwen3-4B",
    "messages": [{"role": "user", "content": "hello"}]
}

response = requests.post(url, json=payload)
print(response.json())
```

```shell
m5stack@raspberrypi:~ $ python test.py 
{'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': '<think>\nOkay, the user said "hello". I need to respond appropriately. Since they\'re just greeting me, I should respond in a friendly and welcoming manner. Maybe say hello back and ask how I can assist them. Keep it simple and open-ended so they feel comfortable to share more. No need for any complex language here. Just a basic, polite response.\n</think>\n\nHello! How can I assist you today? 😊', 'role': 'assistant'}}], 'created': 1774950963, 'id': 'chatcmpl-a8a9aed94d190feeab483079', 'model': 'AXERA-TECH/Qwen3-4B', 'object': 'chat.completion', 'usage': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0}}
```