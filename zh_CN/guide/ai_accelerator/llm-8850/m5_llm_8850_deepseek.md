# DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4

1. [点击下载模型](https://huggingface.co/AXERA-TECH/DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4) 并上传到 raspberrypi5。

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4$ ls -lh
total 2.9M
-rw-rw-r-- 1 m5stack m5stack    0 Aug 12 10:56 config.json
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 11:00 deepseek-r1-1.5b-gptq-int4-ax650
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 10:56 deepseek-r1_tokenizer
-rw-rw-r-- 1 m5stack m5stack 4.2K Aug 12 10:56 deepseek-r1_tokenizer.py
-rw-rw-r-- 1 m5stack m5stack 976K Aug 12 10:58 main_axcl_aarch64
-rw-rw-r-- 1 m5stack m5stack 999K Aug 12 10:58 main_axcl_x86
-rw-rw-r-- 1 m5stack m5stack 932K Aug 12 10:58 main_prefill
-rw-rw-r-- 1 m5stack m5stack  277 Aug 12 10:56 post_config.json
-rw-rw-r-- 1 m5stack m5stack 7.4K Aug 12 10:56 README.md
-rw-rw-r-- 1 m5stack m5stack  533 Aug 12 10:56 run_deepseek-r1_1.5b_gptq_int4_ax650.sh
-rw-rw-r-- 1 m5stack m5stack  538 Aug 12 10:56 run_deepseek-r1_1.5b_gptq_int4_axcl_aarch64.sh
-rw-rw-r-- 1 m5stack m5stack  534 Aug 12 10:56 run_deepseek-r1_1.5b_gptq_int4_axcl_x86.sh
```

2. 创建虚拟环境

```bash
python -m venv deepseek
```

3. 激活虚拟环境

```bash
source deepseek/bin/activate
```

4. 安装依赖包

```bash
pip install transformers jinja2
```

5. 启动 tokenizer 解析器

```bash
python deepseek-r1_tokenizer.py --port 12345
```

6. 运行 tokenizer 服务，Host ip 默认为 `localhost`，端口号设置为 `12345`，正在运行后信息如下：

```bash
(deepseek) m5stack@raspberrypi:~/rsp/DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4 $ python deepseek-r1_tokenizer.py --port 12345
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
151646 <｜begin▁of▁sentence｜> 151643 <｜end▁of▁sentence｜>
<｜begin▁of▁sentence｜>You are DeepSeek-R1, You are a helpful assistant.<｜User｜>hello world<｜Assistant｜>
[151646, 151646, 2610, 525, 18183, 39350, 10911, 16, 11, 1446, 525, 264, 10950, 17847, 13, 151644, 14990, 1879, 151645]
http://localhost:12345
```

?> 提示 | 以下操作需要新建一个 raspberrypi 的终端

7. 设置可执行权限

```bash
chmod +x main_axcl_aarch64 run_deepseek-r1_1.5b_gptq_int4_axcl_aarch64.sh
```

8. 启动 DeepSeek-R1-Distill-Qwen-1.5B 模型推理服务

```bash
./run_deepseek-r1_1.5b_gptq_int4_axcl_aarch64.sh
```

成功启动后信息如下：

```bash
m5stack@raspberrypi:~/rsp/DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4$ ./run_deepseek-r1_1.5b_gptq_int4_axcl_aarch64.sh
build time: Feb 13 2025 15:44:57
[I][                            Init][ 111]: LLM init start
bos_id: 151646, eos_id: 151643
  3% | ██                                |   1 /  31 [0.00s<0.09s, 333.33 count/s] tokenizer init
  100% | ████████████████████████████████ |  31 /  31 [28.78s<28.78s, 1.08 count/s] init post axmodel ok
[I][                            Init][ 226]: max_token_len : 1023
[I][                            Init][ 231]: kv_cache_size : 256, kv_cache_num: 1023
[I][                     load_config][ 282]: load config:
{
    "enable_repetition_penalty": false,
    "enable_temperature": true,
    "enable_top_k_sampling": true,
    "enable_top_p_sampling": false,
    "penalty_window": 20,
    "repetition_penalty": 1.2,
    "temperature": 0.9,
    "top_k": 10,
    "top_p": 0.8
}

[I][                            Init][ 288]: LLM init ok
Type "q" to exit, Ctrl+c to stop current running
>> hello
<think>
Alright, let me take a look at the user's message. They've greeted me with "You DeepSeek-R1, You are a helpful assistant." Seems like they're thanking me and expressing gratitude for the assistance I've provided before. They ended with "hello"—a friendly greeting in Chinese.

Hmm, they might be testing the AI's response generation capabilities. Maybe they're checking if I can understand their greeting properly or just trying to get feedback. I should respond in a friendly and professional manner, acknowledging their gratitude and offering further assistance. Perhaps they were expecting some interaction but didn't see the response yet. I'll keep it open to see if they have a specific question in mind.
</think>

Hello! I'm DeepSeek-R1, an AI assistant ready to help you with any questions or tasks you may have. How can I assist you today?

[N][                             Run][ 610]: hit eos,avg 13.29 token/s

>>
```

| 模型                                    | 量化方式 | tftt (ms) | token/s |
| --------------------------------------- | -------- | --------- | ------- |
| DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4 | w4a16    | -         | 13.29   |
