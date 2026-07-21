# Qwen3.5-2B

## INT8 版本

1. [手动下载模型](https://huggingface.co/AXERA-TECH/Qwen3.5-2B-AX650-C128-P1152-CTX2047) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/Qwen3.5-2B-AX650-C128-P1152-CTX2047
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/Qwen3.5-2B-AX650-C128-P1152-CTX2047 $ ls -lh
total 3.4G
-rw-rw-r-- 1 m5stack m5stack  942 Mar 26 15:05 config.json
-rw-rw-r-- 1 m5stack m5stack 347K Mar 26 15:16 image.png
-rw-rw-r-- 1 m5stack m5stack 970M Mar 26 15:25 model.embed_tokens.weight.bfloat16.bin
-rw-rw-r-- 1 m5stack m5stack  278 Mar 26 15:05 post_config.json
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 17:22 qwen3_5_text_p128_l0_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:15 qwen3_5_text_p128_l10_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  60M Mar 26 15:17 qwen3_5_text_p128_l11_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:13 qwen3_5_text_p128_l12_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:13 qwen3_5_text_p128_l13_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:16 qwen3_5_text_p128_l14_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  60M Mar 26 15:18 qwen3_5_text_p128_l15_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:15 qwen3_5_text_p128_l16_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:09 qwen3_5_text_p128_l17_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:09 qwen3_5_text_p128_l18_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  60M Mar 26 15:18 qwen3_5_text_p128_l19_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:07 qwen3_5_text_p128_l1_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:13 qwen3_5_text_p128_l20_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:07 qwen3_5_text_p128_l21_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:07 qwen3_5_text_p128_l22_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  60M Mar 26 15:15 qwen3_5_text_p128_l23_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:09 qwen3_5_text_p128_l2_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  60M Mar 26 15:15 qwen3_5_text_p128_l3_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:09 qwen3_5_text_p128_l4_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:07 qwen3_5_text_p128_l5_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:09 qwen3_5_text_p128_l6_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  60M Mar 26 15:17 qwen3_5_text_p128_l7_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:13 qwen3_5_text_p128_l8_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  70M Mar 26 15:13 qwen3_5_text_p128_l9_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 530M Mar 26 15:21 qwen3_5_text_post.axmodel
-rw-rw-r-- 1 m5stack m5stack 6.2M Mar 26 15:05 qwen3_5_tokenizer.txt
-rw-rw-r-- 1 m5stack m5stack 354M Mar 26 15:18 qwen3_5_vision.axmodel
-rw-rw-r-- 1 m5stack m5stack  15K Mar 31 14:34 README.md
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
axllm run Qwen3.5-2B-AX650-C128-P1152-CTX2047/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm run Qwen3.5-2B-AX650-C128-P1152-CTX2047/
15:25:19.012 INF Init:218 | LLM init start
15:25:19.012 INF Init:226 | mixed attention enabled: full_attention_interval=4 ref_full_layer_idx=3
15:25:19.012 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 3
 96% | ##############################   |  26 /  27 [43.54s<45.21s, 0.60 count/s] init post axmodel ok,remain_cmm(4753 MB)       
15:26:02.876 INF Init:368 | max_token_len : 2047
15:26:02.876 INF Init:371 | kv_cache_size : 512, kv_cache_num: 2047
15:26:02.876 INF Init:374 | prefill_token_num : 128
15:26:02.876 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
15:26:02.876 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 128
15:26:02.876 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 256
15:26:02.876 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 384
15:26:02.876 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 512
15:26:02.876 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 768
15:26:02.876 INF Init:379 | grp: 7, prefill_max_kv_cache_num : 1024
15:26:02.876 INF Init:379 | grp: 8, prefill_max_kv_cache_num : 1152
15:26:02.876 INF Init:384 | prefill_max_token_num : 1152
15:26:02.876 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  27 /  27 [43.54s<43.54s, 0.62 count/s] embed_selector init ok
15:26:08.704 INF Init:695 | Qwen-VL token ids: vision_start=248053 image_pad=248056 video_pad=248057
15:26:08.704 INF Init:728 | VisionModule init ok: type=Qwen3VL, tokens_per_block=144, embed_size=2048, out_dtype=fp32
15:26:08.704 INF load_config:282 | load config: 
15:26:08.704 INF load_config:282 | {
15:26:08.704 INF load_config:282 |     "enable_repetition_penalty": false,
15:26:08.704 INF load_config:282 |     "enable_temperature": false,
15:26:08.704 INF load_config:282 |     "enable_top_k_sampling": true,
15:26:08.704 INF load_config:282 |     "enable_top_p_sampling": false,
15:26:08.704 INF load_config:282 |     "penalty_window": 20,
15:26:08.704 INF load_config:282 |     "repetition_penalty": 1.2,
15:26:08.704 INF load_config:282 |     "temperature": 0.9,
15:26:08.704 INF load_config:282 |     "top_k": 10,
15:26:08.704 INF load_config:282 |     "top_p": 0.8
15:26:08.704 INF load_config:282 | }
15:26:08.704 INF Init:448 | LLM init ok
Commands:
  /q, /exit  退出
  /reset     重置 kvcache
  /dd        删除一轮对话
  /pp        打印历史对话
Ctrl+C: 停止当前生成
VLM enabled: after each prompt, input image path (empty = text-only). Use "video:<frames_dir>" for video.
----------------------------------------
prompt >>
```

文本输入

```bash
prompt >> hello
image >> 
15:26:35.528 INF SetKVCache:749 | prefill_grpid:2 kv_cache_num:128 precompute_len:0 input_num_token:20
15:26:35.528 INF SetKVCache:757 | current prefill_max_token_num:1152
15:26:35.528 INF SetKVCache:760 | first run
15:26:35.540 INF Run:818 | input token num : 20, prefill_split_num : 1
15:26:35.540 INF Run:858 | prefill chunk p=0 history_len=0 grpid=1 kv_cache_num=0 input_tokens=20
15:26:35.540 INF Run:881 | prefill indices shape: p=0 idx_elems=128 idx_rows=1 pos_rows=0
15:26:35.985 INF Run:1023 | ttft: 445.55 ms
<think>
Thinking Process:

1.  **Analyze the Request:**
    *   Input: "hello"
    *   Intent: A greeting.
    *   Expected Outcome: A polite, friendly response acknowledging the greeting.

2.  **Determine the appropriate tone:**
    *   Friendly, helpful, and open.
    *   Use natural language (English).
    *   Keep it conversational.

3.  **Draft potential responses:**
    *   Option 1: Hello! How can I help you today?
    *   Option 2: Hi there! What's on your mind?
    *   Option 3: Hello! Welcome to [AI name], how are you doing?
    *   Option 4: Hello! I'm ready to help you with whatever you need.

4.  **Select the best response:**
    *   Option 1 is standard and helpful.
    *   Option 4 is also good.
    *   I'll go with a friendly greeting and an offer to assist.

5.  **Final Polish:** "Hello! How can I assist you today?" or "Hi there! I'm here to help with what you need."
    *   Let's keep it simple and welcoming.

6.  **Final Output Generation:** "Hello! How can I help you today?" (Simple, direct, helpful).
    *   Wait, the user's prompt is very short. I should respond in kind but be friendly.
    *   "Hello! How can I assist you today?"

    *   Wait, I should consider safety. Is this a sensitive request? No.

    *   Okay, final decision: "Hello! How can I help you today?"

    *(Self-Correction: Keep it slightly more conversational)*: "Hello! How are you doing? Anything I can help you with today?"

    *(Self-Correction: Even simpler)*: "Hello! How can I assist you?"

    Let's go with: "Hello! How can I help you today?"

    Wait, I need to make sure I don't violate any policies. No issues here.

    Okay, final choice: "Hello! How can I assist you today?"

    Wait, checking the system instruction again. "You are a helpful assistant."

    Okay, I'll respond with a friendly greeting and an offer of help.

    Final thought: Keep it short and sweet.

    Output: "Hello! How can I help you today?"

    Actually, maybe add a bit more warmth.

    Output: "Hello there! I'm here to help with whatever you need."

    Let's go with the helpful one.

    Output: "Hello! How can I assist you today?"

    Okay, I'm ready.
</think>

Hello! How can I help you today?

15:27:55.697 NTC Run:1145 | hit eos,avg 7.65 token/s
15:27:55.697 INF GetKVCache:721 | precompute_len:630, remaining:522
prompt >> 
```

图片输入

```bash
prompt >> 描述图片内容
image >> bus.jpg
15:30:48.052 INF EncodeForContent:1121 | Qwen-VL pixel_values[0] bytes=884736 min=0 max=255 (w=384 h=384 tp=2 ps=16 sm=2)
15:30:48.211 INF EncodeForContent:1144 | vision cache store: bus.jpg
15:30:48.214 INF SetKVCache:749 | prefill_grpid:3 kv_cache_num:256 precompute_len:0 input_num_token:168
15:30:48.214 INF SetKVCache:757 | current prefill_max_token_num:1152
15:30:48.214 INF SetKVCache:760 | first run
15:30:48.224 INF Run:818 | input token num : 168, prefill_split_num : 2
15:30:48.224 INF Run:858 | prefill chunk p=0 history_len=0 grpid=1 kv_cache_num=0 input_tokens=128
15:30:48.224 INF Run:881 | prefill indices shape: p=0 idx_elems=128 idx_rows=1 pos_rows=3
15:30:48.651 INF Run:858 | prefill chunk p=1 history_len=128 grpid=2 kv_cache_num=128 input_tokens=40
15:30:48.652 INF Run:881 | prefill indices shape: p=1 idx_elems=128 idx_rows=1 pos_rows=3
15:30:49.123 INF Run:1023 | ttft: 898.39 ms
<think>

</think>

好的，这张图片展示了一个阳光明媚的都市街景。画面中主要聚焦于几位行人和一辆行驶中的公交车。

以下是图片内容的详细描述：

---

### 场景与氛围
- **环境**：照片拍摄于一个铺着灰色地砖的广场或步行街，地面上有清晰的光影斑驳，表明天气晴朗。背景是一个浅黄色的建筑，有绿色的窗户和深色的阳台栏杆。
- **氛围**：整体氛围是日常、生动的城市生活场景，充满了动态感。

### 主要人物
1.  **前景左侧的男子**：
    -   一位中年男性，身穿白色上衣，似乎正在行走或驻足。
2.  **前景中间偏左的女子**：
    -   一位年轻女子，身穿粉色上衣和深色裤子，正从镜头前走过，背对着镜头。
3.  **前景右侧的男子**：
    -   一位青年男子，身穿红色T恤，正从左向右行走。
4.  **背景中的行人**：
    -   在更远处的建筑前，还有其他行人在走动，为场景增添了深度。

### 交通工具
-   **公交车**：一辆白色的公交车正从右向左行驶，位于画面的右侧和中间部分。车身上可以看到一些广告文字。

### 其他细节
-   背景中的建筑有多个阳台，部分阳台上有人活动。
-   整体构图利用了行人的动态和车辆的运动，营造出一种“在路上”的真实感。

15:31:30.923 NTC Run:1145 | hit eos,avg 7.56 token/s
15:31:30.923 INF GetKVCache:721 | precompute_len:352, remaining:800
prompt >> 
```

4. OpenAI API 兼容服务器模式

!> 注意|如果之前安装了基于 StackFlow 的 OpenAI API 服务，需要先执行 systemctl stop llm-openai-api 停止，或 sudo apt remove llm-openai-api 卸载，避免端口冲突。

```bash
axllm serve Qwen3.5-2B-AX650-C128-P1152-CTX2047/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm serve Qwen3.5-2B-AX650-C128-P1152-CTX2047/
15:32:07.050 INF Init:218 | LLM init start
15:32:07.050 INF Init:226 | mixed attention enabled: full_attention_interval=4 ref_full_layer_idx=3
15:32:07.050 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 3
 96% | ##############################   |  26 /  27 [42.29s<43.92s, 0.61 count/s] init post axmodel ok,remain_cmm(4753 MB)       
15:32:49.658 INF Init:368 | max_token_len : 2047
15:32:49.658 INF Init:371 | kv_cache_size : 512, kv_cache_num: 2047
15:32:49.658 INF Init:374 | prefill_token_num : 128
15:32:49.658 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
15:32:49.658 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 128
15:32:49.658 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 256
15:32:49.658 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 384
15:32:49.658 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 512
15:32:49.658 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 768
15:32:49.658 INF Init:379 | grp: 7, prefill_max_kv_cache_num : 1024
15:32:49.658 INF Init:379 | grp: 8, prefill_max_kv_cache_num : 1152
15:32:49.658 INF Init:384 | prefill_max_token_num : 1152
15:32:49.658 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  27 /  27 [42.29s<42.29s, 0.64 count/s] embed_selector init ok
15:32:55.225 INF Init:695 | Qwen-VL token ids: vision_start=248053 image_pad=248056 video_pad=248057
15:32:55.225 INF Init:728 | VisionModule init ok: type=Qwen3VL, tokens_per_block=144, embed_size=2048, out_dtype=fp32
15:32:55.225 INF load_config:282 | load config: 
15:32:55.225 INF load_config:282 | {
15:32:55.225 INF load_config:282 |     "enable_repetition_penalty": false,
15:32:55.225 INF load_config:282 |     "enable_temperature": false,
15:32:55.225 INF load_config:282 |     "enable_top_k_sampling": true,
15:32:55.225 INF load_config:282 |     "enable_top_p_sampling": false,
15:32:55.225 INF load_config:282 |     "penalty_window": 20,
15:32:55.225 INF load_config:282 |     "repetition_penalty": 1.2,
15:32:55.225 INF load_config:282 |     "temperature": 0.9,
15:32:55.225 INF load_config:282 |     "top_k": 10,
15:32:55.225 INF load_config:282 |     "top_p": 0.8
15:32:55.225 INF load_config:282 | }
15:32:55.225 INF Init:448 | LLM init ok
Starting server on port 8000 with model 'AXERA-TECH/Qwen3.5-2B'...
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
Models: AXERA-TECH/Qwen3.5-2B
```

使用 curl 调用 API

文本输入

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "AXERA-TECH/Qwen3.5-2B",
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
        "content": "<think>\nOkay, the user just said hello. I need to respond warmly and check if they're looking for help. Let me make sure to be friendly and offer assistance. Maybe ask what they need or if there's anything specific on their mind. Alright, keep it simple and inviting.\n</think>\n\nHello! 👋 How can I assist you today? Whether you need help with a task, want to chat, or need information, I'm here! 😊",
        "role": "assistant"
      }
    }
  ],
  "created": 1774942546,
  "id": "chatcmpl-cf39df0eb593a2af7bd7c088",
  "model": "AXERA-TECH/Qwen3.5-2B",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 0,
    "prompt_tokens": 0,
    "total_tokens": 0
  }
}
```

图片输入

```bash
echo "{\"model\": \"AXERA-TECH/Qwen3.5-2B\", \"messages\": [{\"role\": \"user\", \"content\": [{\"type\": \"text\", \"text\": \"简要描述图片内容\"}, {\"type\": \"image_url\", \"image_url\": {\"url\": \"data:image/jpeg;base64,$(base64 -w 0 bus.jpg)\"}}]}]}" > payload.json
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d @payload.json
```

返回结果：

```json
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "<think>\n这张图片展示了一个繁忙的街景，主要包含以下几个关键元素：\n\n1.  **主体对象**：一辆蓝白相间、带有绿色标志（看起来是“cero emisiones”或类似环保主题）的公交车停靠在路边，车身上似乎有“BOLILLA”的字样。\n2.  **人物活动**：\n    *   左上方有一位穿着深蓝色西装的男人正在行走。\n    *   左侧前景有一位穿着深色西装的男士，正看着镜头方向。\n    *   左侧前景还有一位穿着深色西装的女士，正低头看着自己的手或物品。\n    *   右侧前景有一位穿着深色西装的女士，背对镜头，正在行走。\n3.  **背景环境**：\n    *   街道背景是一栋黄色的多层建筑，有着深色的阳台和窗户。\n    *   天气看起来比较晴朗，光线充足。\n    *   地面上有斑马线。\n\n**总结**：这是一个典型的街头快照，捕捉了行人穿过街道、停靠在路边的公交车以及具有西班牙风情的建筑背景。\n</think>\n\n这张图片展示了一个典型的街景，主要包含以下内容：\n\n1.  **车辆**：一辆蓝白相间、带有绿色标志（看起来像是环保主题的巴士，车尾有“BOLILLA”字样）的公交车停在路边。\n2.  **行人**：\n    *   左侧前景有一位穿着深色西装的男士，正看向镜头方向。\n    *   在他身后的左侧，有一位穿着深色西装的女士，正在低头看手。\n    *   右侧有一位穿着深色西装的女士背对镜头在走。\n    *   背景中还有一位穿着深色西装的男士在行走。\n3.  **环境**：背景是一栋黄色的建筑，带有阳台和窗户，看起来是典型的西班牙街道风格。地面有斑马线，表明可能靠近人行道。\n\n整体画面捕捉了城市日常通勤或出行的瞬间。<|endoftext|><|im_start|>user\n```\n10",
        "role": "assistant"
      }
    }
  ],
  "created": 1774946884,
  "id": "chatcmpl-ca7eb0393684feb8e835348d",
  "model": "AXERA-TECH/Qwen3.5-2B",
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
import base64

with open("bus.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

url = "http://localhost:8000/v1/chat/completions"
payload = {
    "model": "AXERA-TECH/Qwen3.5-2B",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "描述图片内容"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        }
    ]
}

response = requests.post(url, json=payload)
print(response.json())
```

```shell
m5stack@raspberrypi:~/rsp $ python test_img.py 
{'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': '<think>\n\n</think>\n\n这是一张在阳光明媚的街道上拍摄的城市街景照片，画面聚焦于一辆蓝色的电动公交车和几位行人。\n\n**主要元素描述：**\n\n- **电动公交车**：\n  - 公交车车身主要是浅蓝色，侧面印有醒目的白色大写字母 “B” 标志（代表“Barrio de Los Buscadores”或类似品牌）、一个黄色的叶子图标（象征环保），以及绿色字体的标语 “Cero Emisiones”（零排放）。\n  - 车牌部分显示为白色背景上的红色条纹，是西班牙的典型车牌样式。\n  - 车辆停在路边，车头朝向镜头方向。\n\n- **行人**：\n  - 前景中有四位行人，其中一位男士穿着深色西装外套和牛仔裤，正在行走。\n  - 他旁边有一位女士，穿着浅色上衣和深色裙子，手提一个包。\n  - 她们似乎在交谈或经过拍摄者附近。\n  - 在他们身后，还有更多行人在走动，包括一位穿白色衣服的人和一个穿橙色上衣的人。\n\n- **背景环境**：\n  - 公交车后方是一栋米黄色的建筑，有多个窗户和阳台，阳台上装有黑色金属栏杆。\n  - 建筑上方可以看到一些绿色植物和遮阳篷。\n  - 整体色调温暖明亮，光线强烈，显示出这是一个白天晴朗的日子。\n\n**氛围与意义：**\n\n这张照片捕捉了一个日常生活的瞬间，突出了现代城市的公共交通工具与市民生活之间的融合。电动公交车的出现暗示了城市对环保政策的响应，营造出一种积极、有序且充满活力的城市氛围。构图采用了略微低角度的拍摄方式，使得公交车显得更加突出且富有层次感。\n\n---\n\n**总结：**  \n这是一张描绘西班牙街头的照片，主角是一辆主打环保理念的蓝色电动公交车，周围是繁忙而和谐的城市人群，背景建筑典雅，整体画面明亮生动，体现了现代都市的绿色出行趋势与现代生活节奏。', 'role': 'assistant'}}], 'created': 1774946974, 'id': 'chatcmpl-bc929988d8dcc06d0a6a06c3', 'model': 'AXERA-TECH/Qwen3.5-2B', 'object': 'chat.completion', 'usage': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0}}
```

## INT4 版本

1. [手动下载模型](https://huggingface.co/AXERA-TECH/Qwen3.5-2B-AX650-GPTQ-Int4-C128-P1152-CTX2047) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/Qwen3.5-2B-AX650-GPTQ-Int4-C128-P1152-CTX2047
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/Qwen3.5-2B-AX650-GPTQ-Int4-C128-P1152-CTX2047 $ ls -lh
total 2.8G
-rw-rw-r-- 1 m5stack m5stack  942 Mar 31 14:34 config.json
-rw-rw-r-- 1 m5stack m5stack 347K Mar 31 14:36 image.png
-rw-rw-r-- 1 m5stack m5stack 970M Mar 31 14:39 model.embed_tokens.weight.bfloat16.bin
-rw-rw-r-- 1 m5stack m5stack  278 Mar 31 14:34 post_config.json
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:36 qwen3_5_text_p128_l0_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:35 qwen3_5_text_p128_l10_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  33M Mar 31 14:36 qwen3_5_text_p128_l11_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:34 qwen3_5_text_p128_l12_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:34 qwen3_5_text_p128_l13_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:34 qwen3_5_text_p128_l14_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  33M Mar 31 14:37 qwen3_5_text_p128_l15_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:35 qwen3_5_text_p128_l16_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:35 qwen3_5_text_p128_l17_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:35 qwen3_5_text_p128_l18_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  33M Mar 31 14:37 qwen3_5_text_p128_l19_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:36 qwen3_5_text_p128_l1_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:34 qwen3_5_text_p128_l20_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:35 qwen3_5_text_p128_l21_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:34 qwen3_5_text_p128_l22_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  33M Mar 31 14:37 qwen3_5_text_p128_l23_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:36 qwen3_5_text_p128_l2_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  33M Mar 31 14:36 qwen3_5_text_p128_l3_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:36 qwen3_5_text_p128_l4_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:36 qwen3_5_text_p128_l5_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:36 qwen3_5_text_p128_l6_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  33M Mar 31 14:37 qwen3_5_text_p128_l7_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:36 qwen3_5_text_p128_l8_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  40M Mar 31 14:36 qwen3_5_text_p128_l9_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 530M Mar 31 14:38 qwen3_5_text_post.axmodel
-rw-rw-r-- 1 m5stack m5stack 6.2M Mar 31 14:34 qwen3_5_tokenizer.txt
-rw-rw-r-- 1 m5stack m5stack 354M Mar 31 14:38 qwen3_5_vision.axmodel
-rw-rw-r-- 1 m5stack m5stack  15K Mar 31 14:34 README.md
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
axllm run Qwen3.5-2B-AX650-GPTQ-Int4-C128-P1152-CTX2047/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm run Qwen3.5-2B-AX650-GPTQ-Int4-C128-P1152-CTX2047/
16:59:14.537 INF Init:218 | LLM init start
16:59:14.537 INF Init:226 | mixed attention enabled: full_attention_interval=4 ref_full_layer_idx=3
16:59:14.537 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 3
 96% | ##############################   |  26 /  27 [32.03s<33.26s, 0.81 count/s] init post axmodel ok,remain_cmm(5442 MB)       
16:59:46.882 INF Init:368 | max_token_len : 2047
16:59:46.882 INF Init:371 | kv_cache_size : 512, kv_cache_num: 2047
16:59:46.882 INF Init:374 | prefill_token_num : 128
16:59:46.882 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
16:59:46.882 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 128
16:59:46.882 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 256
16:59:46.882 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 384
16:59:46.882 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 512
16:59:46.882 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 768
16:59:46.882 INF Init:379 | grp: 7, prefill_max_kv_cache_num : 1024
16:59:46.882 INF Init:379 | grp: 8, prefill_max_kv_cache_num : 1152
16:59:46.882 INF Init:384 | prefill_max_token_num : 1152
16:59:46.882 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  27 /  27 [32.03s<32.03s, 0.84 count/s] embed_selector init ok
16:59:52.497 INF Init:695 | Qwen-VL token ids: vision_start=248053 image_pad=248056 video_pad=248057
16:59:52.497 INF Init:728 | VisionModule init ok: type=Qwen3VL, tokens_per_block=144, embed_size=2048, out_dtype=fp32
16:59:52.497 INF load_config:282 | load config: 
16:59:52.497 INF load_config:282 | {
16:59:52.497 INF load_config:282 |     "enable_repetition_penalty": false,
16:59:52.497 INF load_config:282 |     "enable_temperature": false,
16:59:52.497 INF load_config:282 |     "enable_top_k_sampling": true,
16:59:52.497 INF load_config:282 |     "enable_top_p_sampling": false,
16:59:52.497 INF load_config:282 |     "penalty_window": 20,
16:59:52.497 INF load_config:282 |     "repetition_penalty": 1.2,
16:59:52.497 INF load_config:282 |     "temperature": 0.9,
16:59:52.497 INF load_config:282 |     "top_k": 10,
16:59:52.497 INF load_config:282 |     "top_p": 0.8
16:59:52.497 INF load_config:282 | }
16:59:52.497 INF Init:448 | LLM init ok
Commands:
  /q, /exit  退出
  /reset     重置 kvcache
  /dd        删除一轮对话
  /pp        打印历史对话
Ctrl+C: 停止当前生成
VLM enabled: after each prompt, input image path (empty = text-only). Use "video:<frames_dir>" for video.
----------------------------------------
prompt >> 
```

```bash
prompt >> hello
image >> 
17:00:15.381 INF SetKVCache:749 | prefill_grpid:2 kv_cache_num:128 precompute_len:0 input_num_token:20
17:00:15.381 INF SetKVCache:757 | current prefill_max_token_num:1152
17:00:15.381 INF SetKVCache:760 | first run
17:00:15.391 INF Run:818 | input token num : 20, prefill_split_num : 1
17:00:15.391 INF Run:858 | prefill chunk p=0 history_len=0 grpid=1 kv_cache_num=0 input_tokens=20
17:00:15.391 INF Run:881 | prefill indices shape: p=0 idx_elems=128 idx_rows=1 pos_rows=0
17:00:15.790 INF Run:1023 | ttft: 399.12 ms
<think>

</think>

Hello! How can I assist you?

17:00:16.925 NTC Run:1145 | hit eos,avg 10.58 token/s
17:00:16.925 INF GetKVCache:721 | precompute_len:32, remaining:1120
prompt >> 
```

4. OpenAI API 兼容服务器模式

!> 注意|如果之前安装了基于 StackFlow 的 OpenAI API 服务，需要先执行 systemctl stop llm-openai-api 停止，或 sudo apt remove llm-openai-api 卸载，避免端口冲突。

```bash
axllm serve Qwen3.5-2B-AX650-GPTQ-Int4-C128-P1152-CTX2047/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm serve Qwen3.5-2B-AX650-GPTQ-Int4-C128-P1152-CTX2047/
16:52:20.702 INF Init:218 | LLM init start
16:52:20.702 INF Init:226 | mixed attention enabled: full_attention_interval=4 ref_full_layer_idx=3
16:52:20.702 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 3
 96% | ##############################   |  26 /  27 [32.64s<33.89s, 0.80 count/s] init post axmodel ok,remain_cmm(5442 MB)       
16:52:53.660 INF Init:368 | max_token_len : 2047
16:52:53.660 INF Init:371 | kv_cache_size : 512, kv_cache_num: 2047
16:52:53.660 INF Init:374 | prefill_token_num : 128
16:52:53.660 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
16:52:53.660 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 128
16:52:53.660 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 256
16:52:53.660 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 384
16:52:53.660 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 512
16:52:53.660 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 768
16:52:53.660 INF Init:379 | grp: 7, prefill_max_kv_cache_num : 1024
16:52:53.660 INF Init:379 | grp: 8, prefill_max_kv_cache_num : 1152
16:52:53.660 INF Init:384 | prefill_max_token_num : 1152
16:52:53.660 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  27 /  27 [32.64s<32.64s, 0.83 count/s] embed_selector init ok
16:52:59.446 INF Init:695 | Qwen-VL token ids: vision_start=248053 image_pad=248056 video_pad=248057
16:52:59.446 INF Init:728 | VisionModule init ok: type=Qwen3VL, tokens_per_block=144, embed_size=2048, out_dtype=fp32
16:52:59.455 INF load_config:282 | load config: 
16:52:59.455 INF load_config:282 | {
16:52:59.455 INF load_config:282 |     "enable_repetition_penalty": false,
16:52:59.455 INF load_config:282 |     "enable_temperature": false,
16:52:59.455 INF load_config:282 |     "enable_top_k_sampling": true,
16:52:59.455 INF load_config:282 |     "enable_top_p_sampling": false,
16:52:59.455 INF load_config:282 |     "penalty_window": 20,
16:52:59.455 INF load_config:282 |     "repetition_penalty": 1.2,
16:52:59.455 INF load_config:282 |     "temperature": 0.9,
16:52:59.455 INF load_config:282 |     "top_k": 10,
16:52:59.455 INF load_config:282 |     "top_p": 0.8
16:52:59.455 INF load_config:282 | }
16:52:59.455 INF Init:448 | LLM init ok
Starting server on port 8000 with model 'AXERA-TECH/Qwen3.5-2B'...
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
Models: AXERA-TECH/Qwen3.5-2B
```

使用 curl 调用 API

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "AXERA-TECH/Qwen3.5-2B",
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
        "content": "<think>\nThinking Process\n\nThis is the user's first message:\n\"hello\".\n\nAs an AI model, I need a polite response.\n I will greet back in English.\n Since the user did not specify the topic, I should ask for what they need help with, to initiate the conversation.\n\n Let's start with a warm and friendly greeting.\n \"Hello there, what can I help you to do today?\"\n\n Or \"Hello there! How can I help you?\"\n\n Now let's finalize the greeting.\n The message is \"hello\", but the context is a new conversation, so no specific context needs to be discussed.\n Let's just say: \"Hello! What can I help you?\"\n\n Wait, I need to keep it concise and polite.\n So, \"Hello! How can I help you today?\"\n\n Now, the user has said \"hello\" and I need to respond in a way that invites them to share the topic, but also keep it simple.\n\n Okay, let's proceed.\n</think>\n\nHello there! How can I help you with that",
        "role": "assistant"
      }
    }
  ],
  "created": 1774947323,
  "id": "chatcmpl-7734d230c3af3ffb94f2f649",
  "model": "AXERA-TECH/Qwen3.5-2B",
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
    "model": "AXERA-TECH/Qwen3.5-2B",
    "messages": [{"role": "user", "content": "hello"}]
}

response = requests.post(url, json=payload)
print(response.json())
```

```shell
m5stack@raspberrypi:~ $ python test.py 
{'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': '<think>\n\n</think>\n\nHello! How can I assist you?', 'role': 'assistant'}}], 'created': 1774947396, 'id': 'chatcmpl-47a2aef113856c0b9479bafc', 'model': 'AXERA-TECH/Qwen3.5-2B', 'object': 'chat.completion', 'usage': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0}}
```