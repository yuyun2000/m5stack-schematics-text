# Qwen2.5-0.5B

1. [手动下载模型](https://huggingface.co/AXERA-TECH/Qwen2.5-0.5B-Instruct-GPTQ-Int4) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/Qwen2.5-0.5B-Instruct-GPTQ-Int4
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/Qwen2.5-0.5B-Instruct-GPTQ-Int4 $ ls -lh
total 2.9M
-rw-rw-r-- 1 m5stack m5stack    0 Aug 12 10:30 config.json
-rw-rw-r-- 1 m5stack m5stack 976K Aug 12 10:30 main_axcl_aarch64
-rw-rw-r-- 1 m5stack m5stack 999K Aug 12 10:30 main_axcl_x86
-rw-rw-r-- 1 m5stack m5stack 932K Aug 12 10:30 main_prefill
-rw-rw-r-- 1 m5stack m5stack  277 Aug 12 10:30 post_config.json
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 10:30 qwen2.5-0.5b-gptq-int4-ax650
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 10:30 qwen2.5_tokenizer
-rw-rw-r-- 1 m5stack m5stack 4.2K Aug 12 10:30 qwen2.5_tokenizer.py
-rw-rw-r-- 1 m5stack m5stack 7.3K Aug 12 10:30 README.md
-rw-rw-r-- 1 m5stack m5stack  520 Aug 12 10:30 run_qwen2.5_0.5b_gptq_int4_ax650.sh
-rw-rw-r-- 1 m5stack m5stack  525 Aug 12 10:30 run_qwen2.5_0.5b_gptq_int4_axcl_aarch64.sh
-rw-rw-r-- 1 m5stack m5stack  521 Aug 12 10:30 run_qwen2.5_0.5b_gptq_int4_axcl_x86.sh
```

\#> 提示 | 如果之前已经创建了 **qwen** 的虚拟环境，不需要重新创建，只需要激活即可

2. 创建虚拟环境

```bash
python -m venv qwen
```

3. 激活虚拟环境

```bash
source qwen/bin/activate
```

4. 安装依赖包

```bash
pip install transformers jinja2
```

5. 启动 tokenizer 解析器

```bash
python qwen2.5_tokenizer.py --port 12345
```

6. 运行 tokenizer 服务，Host ip 默认为 localhost，端口号设置为 12345，运行后信息如下：

```bash
(qwen) m5stack@raspberrypi:~/rsp/Qwen2.5-0.5B-Instruct-GPTQ-Int4 $ python qwen2.5_tokenizer.py --port 12345
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
None None 151645 <|im_end|>
<|im_start|>system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.<|im_end|>
<|im_start|>user
hello world<|im_end|>
<|im_start|>assistant

[151644, 8948, 198, 2610, 525, 1207, 16948, 11, 3465, 553, 54364, 14817, 13, 1446, 525, 264, 10950, 17847, 13, 151645, 198, 151644, 872, 198, 14990, 1879, 151645, 198, 151644, 77091, 198]
http://localhost:12345
```

?> 提示 | 以下操作需要新建一个 raspberrypi 的终端。

7. 设置可执行权限

```bash
chmod +x main_axcl_aarch64 run_qwen2.5_0.5b_gptq_int4_axcl_aarch64.sh
```

8. 启动 Qwen2.5 模型推理服务

```bash
./run_qwen2.5_0.5b_gptq_int4_axcl_aarch64.sh
```

成功启动后信息如下：

```bash
m5stack@raspberrypi:~/rsp/Qwen2.5-0.5B-Instruct-GPTQ-Int4$ ./run_qwen2.5_0.5b_gptq_int4_axcl_aarch64.sh
build time: Feb 13 2025 15:44:57
[I][                            Init][ 111]: LLM init start
bos_id: -1, eos_id: 151645
  3% | ██                                |   1 /  27 [0.00s<0.05s, 500.00 count/s] tokenizer init
  96% | ███████████████████████████████   |  26 /  27 [8.35s<8.67s, 3.11 count/s] init 23 axmodel ok
  100% | ████████████████████████████████ |  27 /  27 [11.63s<11.63s, 2.32 count/s] init post axmodel ok
[I][                            Init][ 226]: max_token_len : 1024
[I][                            Init][ 231]: kv_cache_size : 128, kv_cache_num: 1024
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
Hello! How can I help you today? Let me know if you would like me to assist with anything else.

[N][                             Run][ 610]: hit eos,avg 27.05 token/s

>>
```