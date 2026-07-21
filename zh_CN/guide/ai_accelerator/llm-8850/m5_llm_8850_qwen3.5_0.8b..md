# Qwen3.5-0.8B

## INT8 版本

1. [手动下载模型](https://huggingface.co/AXERA-TECH/Qwen3.5-0.8B-AX650-C128-P1152-CTX2047) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/Qwen3.5-0.8B-AX650-C128-P1152-CTX2047
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/Qwen3.5-0.8B-AX650-C128-P1152-CTX2047 $ ls -lh
total 1.5G
-rw-rw-r-- 1 m5stack m5stack  944 Mar 31 14:32 config.json
-rw-rw-r-- 1 m5stack m5stack 347K Mar 31 14:33 image.png
-rw-rw-r-- 1 m5stack m5stack 485M Mar 31 14:36 model.embed_tokens.weight.bfloat16.bin
-rw-rw-r-- 1 m5stack m5stack  278 Mar 31 14:32 post_config.json
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l0_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l10_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  22M Mar 31 14:33 qwen3_5_text_p128_l11_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l12_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:33 qwen3_5_text_p128_l13_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l14_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  22M Mar 31 14:33 qwen3_5_text_p128_l15_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l16_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l17_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l18_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  22M Mar 31 14:33 qwen3_5_text_p128_l19_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l1_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l20_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l21_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:33 qwen3_5_text_p128_l22_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  22M Mar 31 14:33 qwen3_5_text_p128_l23_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l2_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  22M Mar 31 14:33 qwen3_5_text_p128_l3_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:33 qwen3_5_text_p128_l4_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:33 qwen3_5_text_p128_l5_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:33 qwen3_5_text_p128_l6_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  22M Mar 31 14:33 qwen3_5_text_p128_l7_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l8_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  29M Mar 31 14:32 qwen3_5_text_p128_l9_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 265M Mar 31 14:33 qwen3_5_text_post.axmodel
-rw-rw-r-- 1 m5stack m5stack 6.2M Mar 31 14:32 qwen3_5_tokenizer.txt
-rw-rw-r-- 1 m5stack m5stack 109M Mar 31 14:33 qwen3_5_vision.axmodel
-rw-rw-r-- 1 m5stack m5stack  15K Mar 31 14:32 README.md
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
axllm run Qwen3.5-0.8B-AX650-C128-P1152-CTX2047/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm run Qwen3.5-0.8B-AX650-C128-P1152-CTX2047/
14:41:37.557 INF Init:218 | LLM init start
14:41:37.557 INF Init:226 | mixed attention enabled: full_attention_interval=4 ref_full_layer_idx=3
14:41:37.557 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 3
 96% | ##############################   |  26 /  27 [32.56s<33.82s, 0.80 count/s] init post axmodel ok,remain_cmm(1726 MB)       
14:42:10.435 INF Init:368 | max_token_len : 2047
14:42:10.435 INF Init:371 | kv_cache_size : 512, kv_cache_num: 2047
14:42:10.435 INF Init:374 | prefill_token_num : 128
14:42:10.435 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
14:42:10.435 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 128
14:42:10.435 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 256
14:42:10.435 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 384
14:42:10.435 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 512
14:42:10.435 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 768
14:42:10.435 INF Init:379 | grp: 7, prefill_max_kv_cache_num : 1024
14:42:10.435 INF Init:379 | grp: 8, prefill_max_kv_cache_num : 1152
14:42:10.435 INF Init:384 | prefill_max_token_num : 1152
14:42:10.435 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  27 /  27 [32.56s<32.56s, 0.83 count/s] embed_selector init ok
14:42:13.222 INF Init:695 | Qwen-VL token ids: vision_start=248053 image_pad=248056 video_pad=248057
14:42:13.222 INF Init:728 | VisionModule init ok: type=Qwen3VL, tokens_per_block=144, embed_size=1024, out_dtype=fp32
14:42:13.232 INF load_config:282 | load config: 
14:42:13.232 INF load_config:282 | {
14:42:13.232 INF load_config:282 |     "enable_repetition_penalty": false,
14:42:13.232 INF load_config:282 |     "enable_temperature": false,
14:42:13.232 INF load_config:282 |     "enable_top_k_sampling": true,
14:42:13.232 INF load_config:282 |     "enable_top_p_sampling": false,
14:42:13.232 INF load_config:282 |     "penalty_window": 20,
14:42:13.232 INF load_config:282 |     "repetition_penalty": 1.2,
14:42:13.232 INF load_config:282 |     "temperature": 0.9,
14:42:13.232 INF load_config:282 |     "top_k": 10,
14:42:13.232 INF load_config:282 |     "top_p": 0.8
14:42:13.232 INF load_config:282 | }
14:42:13.232 INF Init:448 | LLM init ok
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
14:43:19.813 INF SetKVCache:749 | prefill_grpid:2 kv_cache_num:128 precompute_len:0 input_num_token:20
14:43:19.813 INF SetKVCache:757 | current prefill_max_token_num:1152
14:43:19.813 INF SetKVCache:760 | first run
14:43:19.844 INF Run:818 | input token num : 20, prefill_split_num : 1
14:43:19.844 INF Run:858 | prefill chunk p=0 history_len=0 grpid=1 kv_cache_num=0 input_tokens=20
14:43:19.844 INF Run:881 | prefill indices shape: p=0 idx_elems=128 idx_rows=1 pos_rows=0
14:43:20.176 INF Run:1023 | ttft: 331.98 ms
<think>

</think>

Hello! How can I assist you today?

14:43:21.328 NTC Run:1145 | hit eos,avg 11.28 token/s
14:43:21.329 INF GetKVCache:721 | precompute_len:33, remaining:1119
prompt >> 
```

图片输入

```bash
prompt >> 描述图片内容
image >> bus.jpg
15:03:56.868 INF EncodeForContent:1048 | vision cache hit (disk): bus.jpg
15:03:56.868 INF EncodeForContent:1057 | vision cache hit (mem): bus.jpg
15:03:56.869 INF SetKVCache:749 | prefill_grpid:3 kv_cache_num:256 precompute_len:0 input_num_token:168
15:03:56.869 INF SetKVCache:757 | current prefill_max_token_num:1152
15:03:56.869 INF SetKVCache:760 | first run
15:03:56.883 INF Run:818 | input token num : 168, prefill_split_num : 2
15:03:56.883 INF Run:858 | prefill chunk p=0 history_len=0 grpid=1 kv_cache_num=0 input_tokens=128
15:03:56.883 INF Run:881 | prefill indices shape: p=0 idx_elems=128 idx_rows=1 pos_rows=3
15:03:57.213 INF Run:858 | prefill chunk p=1 history_len=128 grpid=2 kv_cache_num=128 input_tokens=40
15:03:57.213 INF Run:881 | prefill indices shape: p=1 idx_elems=128 idx_rows=1 pos_rows=3
15:03:57.573 INF Run:1023 | ttft: 690.20 ms
<think>

</think>

这是一张充满生活气息的城市街景照片，捕捉了几个行人正在行走的生动场景：

**核心人物：**
- 图片左侧有一位穿着米色风衣的男士，他双臂交叉抱在胸前，正侧身向前走，神情显得放松而随性。他的蓝色牛仔裤和浅棕色靴子很合身。
- 在他右侧，一位戴墨镜的男士正大步向前行走，阳光洒在他的脸上。
- 在图像的更右侧，还有一位穿着黑色外套的男子，同样在步行，似乎与左侧的两人同行。

**环境背景：**
- 他们行走在一条铺砌的城市街道上。在背景中，是一栋米黄色的两层建筑，可以看到带有黑色铁艺栏杆的阳台和一些窗户。建筑外墙略显陈旧，带有一种温暖的色调。
- 街道两侧有绿树点缀，为繁忙的都市带来了一抹绿色，也增添了画面的层次感。
- 上方有一辆黄色的公交车，停在街道旁或缓慢前行，暗示了这是一个公共交通密集或繁忙的路段。

**光影与氛围：**
- 整体光线明亮，看起来是一个晴朗的白天。阳光从左上方照射下来，使得建筑物的阴影清晰可见。
- 整个场景给人一种现代、忙碌但又充满生活情趣的感觉，像是都市中常见的日常漫步。

15:04:21.718 NTC Run:1145 | hit eos,avg 11.18 token/s
15:04:21.718 INF GetKVCache:721 | precompute_len:306, remaining:846
prompt >> 
```

4. OpenAI API 兼容服务器模式

!> 注意|如果之前安装了基于 StackFlow 的 OpenAI API 服务，需要先执行 systemctl stop llm-openai-api 停止，或 sudo apt remove llm-openai-api 卸载，避免端口冲突。

```bash
axllm serve Qwen3.5-0.8B-AX650-C128-P1152-CTX2047/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm serve Qwen3.5-0.8B-AX650-C128-P1152-CTX2047/
14:43:55.658 INF Init:218 | LLM init start
14:43:55.658 INF Init:226 | mixed attention enabled: full_attention_interval=4 ref_full_layer_idx=3
14:43:55.658 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 3
 96% | ##############################   |  26 /  27 [24.75s<25.71s, 1.05 count/s] init post axmodel ok,remain_cmm(1726 MB)       
14:44:20.726 INF Init:368 | max_token_len : 2047
14:44:20.726 INF Init:371 | kv_cache_size : 512, kv_cache_num: 2047
14:44:20.726 INF Init:374 | prefill_token_num : 128
14:44:20.726 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
14:44:20.726 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 128
14:44:20.726 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 256
14:44:20.726 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 384
14:44:20.726 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 512
14:44:20.726 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 768
14:44:20.726 INF Init:379 | grp: 7, prefill_max_kv_cache_num : 1024
14:44:20.726 INF Init:379 | grp: 8, prefill_max_kv_cache_num : 1152
14:44:20.726 INF Init:384 | prefill_max_token_num : 1152
14:44:20.726 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  27 /  27 [24.76s<24.76s, 1.09 count/s] embed_selector init ok
14:44:22.548 INF Init:695 | Qwen-VL token ids: vision_start=248053 image_pad=248056 video_pad=248057
14:44:22.548 INF Init:728 | VisionModule init ok: type=Qwen3VL, tokens_per_block=144, embed_size=1024, out_dtype=fp32
14:44:22.549 INF load_config:282 | load config: 
14:44:22.549 INF load_config:282 | {
14:44:22.549 INF load_config:282 |     "enable_repetition_penalty": false,
14:44:22.549 INF load_config:282 |     "enable_temperature": false,
14:44:22.549 INF load_config:282 |     "enable_top_k_sampling": true,
14:44:22.549 INF load_config:282 |     "enable_top_p_sampling": false,
14:44:22.549 INF load_config:282 |     "penalty_window": 20,
14:44:22.549 INF load_config:282 |     "repetition_penalty": 1.2,
14:44:22.549 INF load_config:282 |     "temperature": 0.9,
14:44:22.549 INF load_config:282 |     "top_k": 10,
14:44:22.549 INF load_config:282 |     "top_p": 0.8
14:44:22.549 INF load_config:282 | }
14:44:22.549 INF Init:448 | LLM init ok
Starting server on port 8000 with model 'AXERA-TECH/Qwen3.5-0.8B'...
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
Models: AXERA-TECH/Qwen3.5-0.8B
```

使用 curl 调用 API

文本输入

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "AXERA-TECH/Qwen3.5-0.8B",
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
        "content": "<think>\n\n</think>\n\nHello! How can I help you today? 😊",
        "role": "assistant"
      }
    }
  ],
  "created": 1774939526,
  "id": "chatcmpl-b20b79080c31da7684e1f7f6",
  "model": "AXERA-TECH/Qwen3.5-0.8B",
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
echo "{\"model\": \"AXERA-TECH/Qwen3.5-0.8B\", \"messages\": [{\"role\": \"user\", \"content\": [{\"type\": \"text\", \"text\": \"描述图片内容\"}, {\"type\": \"image_url\", \"image_url\": {\"url\": \"data:image/jpeg;base64,$(base64 -w 0 bus.jpg)\"}}]}]}" > payload.json
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
        "content": "<think>\n\n</think>\n\n这是一张充满生活气息的街景照片，拍摄于晴朗的白天，阳光充足，画面色彩鲜明。\n\n**主要人物与行为：**\n\n- 画面左侧有一位男士，身穿米色针织开衫、蓝色牛仔裤和棕色短靴，脚踩浅棕色鞋子，面带微笑地边走边拍照。他身后还有两名行人，其中一人穿着深色上衣，另一人部分被遮挡。\n- 画面右侧前景中，可以看到另一名男子的脚部和腿部，似乎正在行走或站立，穿着深色长裤。\n- 整体来看，这似乎是街头摄影或记录场景的照片，人物动作自然，场景真实。\n\n**背景环境：**\n\n- 背景是一栋米黄色的多层建筑，具有典型的欧洲或南欧建筑风格，窗户带有阳台和铁艺栏杆。\n- 建筑前方停着一辆大型公共汽车（巴士），车身呈深色，车窗反射阳光。\n- 巴士旁有绿色树木和部分建筑物，增添了自然与城市的融合感。\n- 地面是铺砌的街道，光线明亮，影子清晰，说明是晴天。\n\n**整体氛围：**\n\n照片传达出一种轻松、日常、充满活力的街头氛围，适合用于记录城市日常、旅行故事或摄影作品集。构图自然流畅，细节丰富，真实感强。\n\n--- \n\n如需提取文字内容（如车牌号、时间、坐标等），可进一步提供更多信息。目前仅从视觉层面呈现该街景与人物。<|endoftext|><|im_start|>assistant: <think>\n\n</think>\n\n这张图片展示了一个阳光明媚的街景，可能拍摄于中国的某个城市（如广州或成都）。\n\n以下是画面的主要细节：\n\n1.  **场景背景**：\n    *   背景是一栋典型的**多层黄褐色建筑**，带有阳台和装饰性铁艺栏杆，这是中国许多老城区或现代新区常见的外墙风格。\n    *   建筑前方停着一辆**大型公共汽车**，车身颜色较暗（可能是灰色或深蓝色）。\n    *   地面上可以看到一些**绿色树木**和**路灯**，表明这是一个城市街道。\n\n2.  **主要人物**：\n    *   画面左侧有一位**青年男性**，他留着短发，穿着一件**米色的针织开衫**和蓝色牛仔裤，脚上穿着棕色的短靴或拖鞋。他面带微笑，身体微微前倾，看起来正在与镜头前的某人（可能是摄影师）互动或交谈。\n    *   在他身后，可以看到另一位穿着深色衣物的行人（部分被遮挡）。\n    *   右侧前景中，似乎还站着另一位穿着深色裤子的行人。\n\n3.  **整体氛围**：\n    *   照片光线明亮，色彩鲜艳。\n    *   人物神态轻松自然，像是正在享受一次愉快的街头漫步。\n\n总的来说，这是一张捕捉日常街景的瞬间，生动地描绘了城市生活中人们互动的场景。由于图片中的人物和背景可能属于特定的地理区域，如果您能提供更多关于此地的背景信息（如城市名、具体事件等），我可以尝试给出更详细的描述或提取关键信息。",
        "role": "assistant"
      }
    }
  ],
  "created": 1774941492,
  "id": "chatcmpl-d4f0745dbfbe6b29dcbc9fc2",
  "model": "AXERA-TECH/Qwen3.5-0.8B",
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
    "model": "AXERA-TECH/Qwen3.5-0.8B",
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
{'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': '<think>\n\n</think>\n\n详细描述\n\n这是一张在晴朗白日内拍摄的街头实景照片，画面主体为三名男性与一辆蓝色长途巴士。\n\n在前景的街道（地面有网格状路缘石和树木树影）上，有三位男性并排从左向右行走。\n\n- **最左侧男子**：身穿浅色无袖上衣和蓝色牛仔裤，脚穿棕色靴子，脚后跟有白色鞋油痕迹。他左手拿着一本打开的书或笔记本，右手似乎握着手机。他正低头注视书本。\n\n- **中间男子**：穿着深蓝色西装外套和白色衬衫，系着一条蓝色领结。他正侧身回头望向左侧男子，表情轻松自然，嘴巴微张，像在与对方交谈。\n\n- **最右侧男子**：穿着浅米色衬衫和蓝色牛仔裤，脚穿棕色鞋子，鞋跟有磨损痕迹。他双手插在裤兜里，正面向巴士方向微笑，表情友好。\n\n画面后方是一辆大型蓝色长途巴士，停靠在建筑物旁。巴士上有白色“Misión de la Unión”（联合联盟的使命）和“Misión de la Unión”字样，字体为白色衬线体。巴士窗户和阳台上有金属栏杆。\n\n背景是一栋米黄色的建筑物，有多扇带有黑色铁艺栏杆的窗户，窗户旁有几株绿树。\n\n整体光线明亮，色调温暖，构图自然，展现了一次日常友好的交流场景。<|endoftext|><|im_start|>', 'role': 'assistant'}}], 'created': 1774941672, 'id': 'chatcmpl-1586d7485977d98d86709893', 'model': 'AXERA-TECH/Qwen3.5-0.8B', 'object': 'chat.completion', 'usage': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0}}
```

## INT4 版本

1. [手动下载模型](https://huggingface.co/AXERA-TECH/Qwen3.5-0.8B-AX650-GPTQ-Int4-C128-P1152-CTX2047) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/Qwen3.5-0.8B-AX650-GPTQ-Int4-C128-P1152-CTX2047
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/Qwen3.5-0.8B-AX650-GPTQ-Int4-C128-P1152-CTX2047 $ ls -lh
total 1.3G
-rw-rw-r-- 1 m5stack m5stack  944 Mar 31 14:33 config.json
-rw-rw-r-- 1 m5stack m5stack 347K Mar 31 14:35 image.png
-rw-rw-r-- 1 m5stack m5stack 485M Mar 31 14:38 model.embed_tokens.weight.bfloat16.bin
-rw-rw-r-- 1 m5stack m5stack  278 Mar 31 14:33 post_config.json
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l0_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l10_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  13M Mar 31 14:35 qwen3_5_text_p128_l11_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l12_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l13_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l14_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  13M Mar 31 14:35 qwen3_5_text_p128_l15_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l16_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l17_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l18_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  13M Mar 31 14:35 qwen3_5_text_p128_l19_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l1_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l20_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l21_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l22_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  13M Mar 31 14:35 qwen3_5_text_p128_l23_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:35 qwen3_5_text_p128_l2_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  13M Mar 31 14:35 qwen3_5_text_p128_l3_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:35 qwen3_5_text_p128_l4_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l5_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:35 qwen3_5_text_p128_l6_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  13M Mar 31 14:35 qwen3_5_text_p128_l7_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l8_together.axmodel
-rw-rw-r-- 1 m5stack m5stack  18M Mar 31 14:34 qwen3_5_text_p128_l9_together.axmodel
-rw-rw-r-- 1 m5stack m5stack 265M Mar 31 14:37 qwen3_5_text_post.axmodel
-rw-rw-r-- 1 m5stack m5stack 6.2M Mar 31 14:33 qwen3_5_tokenizer.txt
-rw-rw-r-- 1 m5stack m5stack 109M Mar 31 14:35 qwen3_5_vision.axmodel
-rw-rw-r-- 1 m5stack m5stack  16K Mar 31 14:33 README.md
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
axllm run Qwen3.5-0.8B-AX650-GPTQ-Int4-C128-P1152-CTX2047/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm run Qwen3.5-0.8B-AX650-GPTQ-Int4-C128-P1152-CTX2047/
14:54:37.954 INF Init:218 | LLM init start
14:54:37.954 INF Init:226 | mixed attention enabled: full_attention_interval=4 ref_full_layer_idx=3
14:54:37.954 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 3
 96% | ##############################   |  26 /  27 [26.55s<27.57s, 0.98 count/s] init post axmodel ok,remain_cmm(1971 MB)       
14:55:04.815 INF Init:368 | max_token_len : 2047
14:55:04.815 INF Init:371 | kv_cache_size : 512, kv_cache_num: 2047
14:55:04.815 INF Init:374 | prefill_token_num : 128
14:55:04.815 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
14:55:04.815 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 128
14:55:04.815 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 256
14:55:04.815 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 384
14:55:04.815 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 512
14:55:04.815 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 768
14:55:04.815 INF Init:379 | grp: 7, prefill_max_kv_cache_num : 1024
14:55:04.815 INF Init:379 | grp: 8, prefill_max_kv_cache_num : 1152
14:55:04.815 INF Init:384 | prefill_max_token_num : 1152
14:55:04.815 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  27 /  27 [26.55s<26.55s, 1.02 count/s] embed_selector init ok
14:55:07.552 INF Init:695 | Qwen-VL token ids: vision_start=248053 image_pad=248056 video_pad=248057
14:55:07.552 INF Init:728 | VisionModule init ok: type=Qwen3VL, tokens_per_block=144, embed_size=1024, out_dtype=fp32
14:55:07.562 INF load_config:282 | load config: 
14:55:07.562 INF load_config:282 | {
14:55:07.562 INF load_config:282 |     "enable_repetition_penalty": false,
14:55:07.562 INF load_config:282 |     "enable_temperature": false,
14:55:07.562 INF load_config:282 |     "enable_top_k_sampling": true,
14:55:07.562 INF load_config:282 |     "enable_top_p_sampling": false,
14:55:07.562 INF load_config:282 |     "penalty_window": 20,
14:55:07.562 INF load_config:282 |     "repetition_penalty": 1.2,
14:55:07.562 INF load_config:282 |     "temperature": 0.9,
14:55:07.562 INF load_config:282 |     "top_k": 10,
14:55:07.562 INF load_config:282 |     "top_p": 0.8
14:55:07.562 INF load_config:282 | }
14:55:07.562 INF Init:448 | LLM init ok
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
14:55:43.350 INF SetKVCache:749 | prefill_grpid:2 kv_cache_num:128 precompute_len:0 input_num_token:20
14:55:43.350 INF SetKVCache:757 | current prefill_max_token_num:1152
14:55:43.350 INF SetKVCache:760 | first run
14:55:43.372 INF Run:818 | input token num : 20, prefill_split_num : 1
14:55:43.372 INF Run:858 | prefill chunk p=0 history_len=0 grpid=1 kv_cache_num=0 input_tokens=20
14:55:43.372 INF Run:881 | prefill indices shape: p=0 idx_elems=128 idx_rows=1 pos_rows=0
14:55:43.689 INF Run:1023 | ttft: 317.07 ms
<think>

</think>

Hello! I am **Qwen**, a big language model developed by Alibaba Cloud and Tongyi, and it is capable to do many tasks, such as answering questions, writing stories, and code generation.

How can I assist you today?

14:55:47.765 NTC Run:1145 | hit eos,avg 13.00 token/s
14:55:47.766 INF GetKVCache:721 | precompute_len:73, remaining:1079
```

4. OpenAI API 兼容服务器模式

!> 注意|如果之前安装了基于 StackFlow 的 OpenAI API 服务，需要先执行 systemctl stop llm-openai-api 停止，或 sudo apt remove llm-openai-api 卸载，避免端口冲突。

```bash
axllm serve Qwen3.5-0.8B-AX650-GPTQ-Int4-C128-P1152-CTX2047/
```

```bash
m5stack@raspberrypi:~/rsp $ axllm serve Qwen3.5-0.8B-AX650-GPTQ-Int4-C128-P1152-CTX2047/
14:56:16.690 INF Init:218 | LLM init start
14:56:16.690 INF Init:226 | mixed attention enabled: full_attention_interval=4 ref_full_layer_idx=3
14:56:16.690 INF run:30 | AXCLWorker start with devid 0
tokenizer_type = 3
 96% | ##############################   |  26 /  27 [20.88s<21.68s, 1.25 count/s] init post axmodel ok,remain_cmm(1971 MB)       
14:56:37.883 INF Init:368 | max_token_len : 2047
14:56:37.883 INF Init:371 | kv_cache_size : 512, kv_cache_num: 2047
14:56:37.883 INF Init:374 | prefill_token_num : 128
14:56:37.883 INF Init:379 | grp: 1, prefill_max_kv_cache_num : 1
14:56:37.883 INF Init:379 | grp: 2, prefill_max_kv_cache_num : 128
14:56:37.883 INF Init:379 | grp: 3, prefill_max_kv_cache_num : 256
14:56:37.883 INF Init:379 | grp: 4, prefill_max_kv_cache_num : 384
14:56:37.883 INF Init:379 | grp: 5, prefill_max_kv_cache_num : 512
14:56:37.883 INF Init:379 | grp: 6, prefill_max_kv_cache_num : 768
14:56:37.883 INF Init:379 | grp: 7, prefill_max_kv_cache_num : 1024
14:56:37.883 INF Init:379 | grp: 8, prefill_max_kv_cache_num : 1152
14:56:37.883 INF Init:384 | prefill_max_token_num : 1152
14:56:37.883 INF Init:27 | LLaMaEmbedSelector use mmap
100% | ################################ |  27 /  27 [20.88s<20.88s, 1.29 count/s] embed_selector init ok
14:56:39.807 INF Init:695 | Qwen-VL token ids: vision_start=248053 image_pad=248056 video_pad=248057
14:56:39.807 INF Init:728 | VisionModule init ok: type=Qwen3VL, tokens_per_block=144, embed_size=1024, out_dtype=fp32
14:56:39.807 INF load_config:282 | load config: 
14:56:39.807 INF load_config:282 | {
14:56:39.807 INF load_config:282 |     "enable_repetition_penalty": false,
14:56:39.807 INF load_config:282 |     "enable_temperature": false,
14:56:39.807 INF load_config:282 |     "enable_top_k_sampling": true,
14:56:39.807 INF load_config:282 |     "enable_top_p_sampling": false,
14:56:39.807 INF load_config:282 |     "penalty_window": 20,
14:56:39.807 INF load_config:282 |     "repetition_penalty": 1.2,
14:56:39.807 INF load_config:282 |     "temperature": 0.9,
14:56:39.807 INF load_config:282 |     "top_k": 10,
14:56:39.807 INF load_config:282 |     "top_p": 0.8
14:56:39.807 INF load_config:282 | }
14:56:39.807 INF Init:448 | LLM init ok
Starting server on port 8000 with model 'AXERA-TECH/Qwen3.5-0.8B'...
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
Models: AXERA-TECH/Qwen3.5-0.8B
```

使用 curl 调用 API

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "AXERA-TECH/Qwen3.5-0.8B",
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
        "content": "<think>\n用户说：\"hello\"，这是用户对 AI 的打招呼方式，希望用中文回复。我确认收到请求，将友好回应。\n\n</think>\n\n你好！很高兴与你交流！😊\n\n我是 Qwen 吗？（Qwen 是阿里巴巴通义大模型系列的名字。）\n\n如果你有任何具体问题、任务或想聊天的内容，随时告诉我！",
        "role": "assistant"
      }
    }
  ],
  "created": 1774940309,
  "id": "chatcmpl-8c11153ba97527d4d02b39b0",
  "model": "AXERA-TECH/Qwen3.5-0.8B",
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
    "model": "AXERA-TECH/Qwen3.5-0.8B",
    "messages": [{"role": "user", "content": "hello"}]
}

response = requests.post(url, json=payload)
print(response.json())
```

```shell
m5stack@raspberrypi:~ $ python test.py 
{'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': '<think>\n\n</think>\n\n嘿，你好！🍎 我是**Qwen**，由阿里巴巴的通义大模型研发的超大规模语言模型。我可以帮助你：\n\n- 写故事、写文章\n- 聊天、解答问题\n- 编程、写代码\n- 翻译、翻译文本', 'role': 'assistant'}}], 'created': 1774940550, 'id': 'chatcmpl-1bff24b99d86294591bec54b', 'model': 'AXERA-TECH/Qwen3.5-0.8B', 'object': 'chat.completion', 'usage': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0}}
```