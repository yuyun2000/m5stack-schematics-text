# Qwen3-0.6B

1. [手动下载模型](https://huggingface.co/AXERA-TECH/Qwen3-0.6B) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/Qwen3-0.6B
```

**文件说明**

```bash
m5stack@raspberrypi:~/Qwen3-0.6B $ ls -lh
total 1.4G
-rw-rw-r-- 1 m5stack m5stack  585 Mar 23 10:06 config.json
-rw-rw-r-- 1 m5stack m5stack 297M Mar 23 10:08 model.embed_tokens.weight.bfloat16.bin
-rw-rw-r-- 1 m5stack m5stack  279 Mar 23 10:06 post_config.json
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l0_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l10_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l11_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l12_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l13_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l14_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l15_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l16_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l17_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l18_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l19_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:06 qwen3_p128_l1_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l20_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l21_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l22_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l23_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:06 qwen3_p128_l24_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:06 qwen3_p128_l25_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l26_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:06 qwen3_p128_l27_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l2_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l3_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l4_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l5_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l6_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:06 qwen3_p128_l7_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:06 qwen3_p128_l8_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  26M Mar 23 10:07 qwen3_p128_l9_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 162M Mar 23 10:08 qwen3_post.axmodel
-rw-rw-r-- 1 m5stack m5stack 162M Mar 23 10:08 qwen3_post.axmodel.onnx
-rw-rw-r-- 1 m5stack m5stack 1.6M Mar 23 10:06 qwen3_tokenizer.txt
-rw-rw-r-- 1 m5stack m5stack 8.3K Mar 23 10:06 README.md
```

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
axllm run Qwen3-0.6B/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm run Qwen3-0.6B/
10:29:26.165 INF Init:218 | LLM init start
10:29:26.165 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 1
 96% | ##############################   |  30 /  31 [25.23s<26.07s, 1.19 count/s] init post axmodel ok,remain_cmm(1660 MB)       
10:29:51.705 INF Init:368 | max_token_len : 2559
10:29:51.705 INF Init:371 | kv_cache_size : 1024, kv_cache_num: 2559
10:29:51.705 INF Init:374 | prefill_token_num : 128
10:29:51.705 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
10:29:51.705 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 512
10:29:51.705 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 1024
10:29:51.705 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 1536
10:29:51.705 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 2048
10:29:51.705 INF Init:384 | prefill_max_token_num : 2048
10:29:51.705 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  31 /  31 [25.23s<25.23s, 1.23 count/s] embed_selector init ok
10:29:51.706 INF load_config:282 | load config: 
10:29:51.706 INF load_config:282 | {
10:29:51.706 INF load_config:282 |     "enable_repetition_penalty": false,
10:29:51.706 INF load_config:282 |     "enable_temperature": false,
10:29:51.706 INF load_config:282 |     "enable_top_k_sampling": false,
10:29:51.706 INF load_config:282 |     "enable_top_p_sampling": false,
10:29:51.706 INF load_config:282 |     "penalty_window": 20,
10:29:51.706 INF load_config:282 |     "repetition_penalty": 1.2,
10:29:51.706 INF load_config:282 |     "temperature": 0.9,
10:29:51.706 INF load_config:282 |     "top_k": 10,
10:29:51.706 INF load_config:282 |     "top_p": 0.8
10:29:51.706 INF load_config:282 | }
10:29:51.706 INF Init:448 | LLM init ok
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
10:31:07.924 INF SetKVCache:749 | prefill_grpid:2 kv_cache_num:512 precompute_len:0 input_num_token:20
10:31:07.924 INF SetKVCache:757 | current prefill_max_token_num:2048
10:31:07.924 INF SetKVCache:760 | first run
10:31:07.935 INF Run:818 | input token num : 20, prefill_split_num : 1
10:31:07.935 INF Run:858 | prefill chunk p=0 history_len=0 grpid=1 kv_cache_num=0 input_tokens=20
10:31:07.935 INF Run:881 | prefill indices shape: p=0 idx_elems=128 idx_rows=1 pos_rows=0
10:31:08.194 INF Run:1023 | ttft: 258.47 ms
<think>
Okay, the user just said "hello". I need to respond appropriately. Since they're greeting me, I should acknowledge their greeting. Maybe say "Hello!" in a friendly way. Let me check if there's any specific context I should consider, but the user didn't mention anything else. I should keep it simple and welcoming. Alright, time to send a response.
</think>

Hello! How can I assist you today? 😊

10:31:17.024 NTC Run:1145 | hit eos,avg 10.19 token/s
10:31:17.024 INF GetKVCache:721 | precompute_len:110, remaining:1938
prompt >> 
```

4. OpenAI API 兼容服务器模式

!> 注意|如果之前安装了基于 StackFlow 的 OpenAI API 服务，需要先执行 systemctl stop llm-openai-api 停止，或 sudo apt remove llm-openai-api 卸载，避免端口冲突。

```bash
axllm serve Qwen3-0.6B/
```

```bash
m5stack@raspberrypi-4g-test:~/rsp $ axllm serve Qwen3-0.6B/
10:32:31.358 INF Init:218 | LLM init start
10:32:31.359 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 1
 96% | ##############################   |  30 /  31 [25.22s<26.06s, 1.19 count/s] init post axmodel ok,remain_cmm(1660 MB)       
10:32:56.890 INF Init:368 | max_token_len : 2559
10:32:56.890 INF Init:371 | kv_cache_size : 1024, kv_cache_num: 2559
10:32:56.890 INF Init:374 | prefill_token_num : 128
10:32:56.890 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
10:32:56.890 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 512
10:32:56.890 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 1024
10:32:56.890 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 1536
10:32:56.890 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 2048
10:32:56.890 INF Init:384 | prefill_max_token_num : 2048
10:32:56.890 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  31 /  31 [25.22s<25.22s, 1.23 count/s] embed_selector init ok
10:32:56.891 INF load_config:282 | load config: 
10:32:56.891 INF load_config:282 | {
10:32:56.891 INF load_config:282 |     "enable_repetition_penalty": false,
10:32:56.891 INF load_config:282 |     "enable_temperature": false,
10:32:56.891 INF load_config:282 |     "enable_top_k_sampling": false,
10:32:56.891 INF load_config:282 |     "enable_top_p_sampling": false,
10:32:56.891 INF load_config:282 |     "penalty_window": 20,
10:32:56.891 INF load_config:282 |     "repetition_penalty": 1.2,
10:32:56.891 INF load_config:282 |     "temperature": 0.9,
10:32:56.891 INF load_config:282 |     "top_k": 10,
10:32:56.891 INF load_config:282 |     "top_p": 0.8
10:32:56.891 INF load_config:282 | }
10:32:56.891 INF Init:448 | LLM init ok
Starting server on port 8000 with model 'AXERA-TECH/Qwen3-0.6B'...
API URLs:
  GET  http://127.0.0.1:8000/health
  GET  http://127.0.0.1:8000/v1/models
  POST http://127.0.0.1:8000/v1/chat/completions
  GET  http://192.168.20.53:8000/health
  GET  http://192.168.20.53:8000/v1/models
  POST http://192.168.20.53:8000/v1/chat/completions
  GET  http://192.168.52.127:8000/health
  GET  http://192.168.52.127:8000/v1/models
  POST http://192.168.52.127:8000/v1/chat/completions
Aliases:
  GET  http://127.0.0.1:8000/models
  POST http://127.0.0.1:8000/chat/completions
  GET  http://192.168.20.53:8000/models
  POST http://192.168.20.53:8000/chat/completions
  GET  http://192.168.52.127:8000/models
  POST http://192.168.52.127:8000/chat/completions
OpenAI API Server starting on http://0.0.0.0:8000
Max concurrency: 1
Models: AXERA-TECH/Qwen3-0.6B
```

使用 curl 调用 API

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "AXERA-TECH/Qwen3-0.6B",
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
        "content": "<think>\nOkay, the user just said \"hello\". I need to respond appropriately. Since they didn't ask a question, I should acknowledge their greeting. Maybe say \"Hello!\" and offer help. Keep it friendly and open-ended. Let them know I'm here to assist. Make sure the response is simple and positive.\n</think>\n\nHello! How can I assist you today? 😊",
        "role": "assistant"
      }
    }
  ],
  "created": 1774924618,
  "id": "chatcmpl-9f276740b36bdd6e96cfe9eb",
  "model": "AXERA-TECH/Qwen3-0.6B",
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
    "model": "AXERA-TECH/Qwen3-0.6B",
    "messages": [{"role": "user", "content": "hello"}]
}

response = requests.post(url, json=payload)
print(response.json())
```

```shell
m5stack@raspberrypi:~ $ python test.py 
{'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': '<think>\nOkay, the user just said "hello". I need to respond appropriately. Since they didn\'t ask a question, I should acknowledge their greeting. Maybe say "Hello!" and offer help. Keep it friendly and open-ended. Let them know I\'m here to assist. Make sure the response is simple and positive.\n</think>\n\nHello! How can I assist you today? 😊', 'role': 'assistant'}}], 'created': 1774924866, 'id': 'chatcmpl-a0edfdac69ee3b7fe87e373e', 'model': 'AXERA-TECH/Qwen3-0.6B', 'object': 'chat.completion', 'usage': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0}}
```

| 模型         | 量化方式 | tftt (ms) | token/s |
| ------------ | -------- | --------- | ------- |
| Qwen3-0.6B   | w8a16    | 670.51    | 12.88   |
| Qwen3-1.7B   | w8a16    | 796.38    | 7.38    |
| Qwen2.5-0.5B | w4a16    | -         | 27.05   |
| Qwen2.5-1.5B | w4a16    | -         | 15.06   |
