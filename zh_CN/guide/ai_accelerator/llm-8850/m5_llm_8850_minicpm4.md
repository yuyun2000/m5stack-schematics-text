# MiniCPM4-0.5B

MiniCPM4-0.5B 是一款轻量级、约 5 亿参数的高效多语言对话模型，具备良好的理解与生成能力，适用于资源受限环境。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/MiniCPM4-0.5B) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/MiniCPM4-0.5B
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/MiniCPM4-0.5B $ ls -lh
total 4.4M
-rw-rw-r-- 1 m5stack m5stack    0 Aug 12 10:58 config.json
-rw-rw-r-- 1 m5stack m5stack 967K Aug 12 11:00 main_ax650
-rw-rw-r-- 1 m5stack m5stack 1.7M Aug 12 11:00 main_axcl_aarch64
-rw-rw-r-- 1 m5stack m5stack 1.8M Aug 12 11:00 main_axcl_x86
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 11:00 minicpm4-0.5b-int8-ctx-ax630c
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 11:00 minicpm4-0.5b-int8-ctx-ax650
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 11:00 minicpm4_tokenizer
-rw-rw-r-- 1 m5stack m5stack 7.1K Aug 12 10:58 minicpm4_tokenizer_uid.py
-rw-rw-r-- 1 m5stack m5stack  277 Aug 12 10:58 post_config.json
-rw-rw-r-- 1 m5stack m5stack 5.2K Aug 12 10:58 README.md
-rw-rw-r-- 1 m5stack m5stack  642 Aug 12 10:58 run_minicpm4_0.5b_int8_ctx_ax630c.sh
-rw-rw-r-- 1 m5stack m5stack  639 Aug 12 10:58 run_minicpm4_0.5b_int8_ctx_ax650.sh
```

2. 创建虚拟环境

```bash
python -m venv minicpm
```

3. 激活虚拟环境

```bash
source minicpm/bin/activate
```

4. 安装依赖包

```bash
pip install transformers jinja2
```

5. 启动 tokenizer 解析器

```bash
python minicpm4_tokenizer_uid.py --port 12345
```

6. 运行 tokenizer 服务，Host ip 默认为 localhost，端口号设置为 12345，正在运行后信息如下：

```bash
(minicpm) m5stack@raspberrypi:~/rsp/MiniCPM4-0.5B $ python minicpm4_tokenizer_uid.py --port 12345
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
Server running at http://0.0.0.0:12345
```

?> 提示 | 以下操作需要新建一个 raspberrypi 的终端

7. 设置可执行权限

```bash
chmod +x main_axcl_aarch64
```

8. 启动 MiniCPM4-0.5B 模型推理服务

```bash
./main_axcl_aarch64 --system_prompt "You are MiniCPM4, created by ModelBest. You are a helpful assistant." --kvcache_path "./kvcache" --template_filename_axmodel "minicpm4-0.5b-int8-ctx-ax650/MiniCPMForCausalLM_p128_l%d_together.axmodel" --axmodel_num 24 --tokenizer_type 2 --url_tokenizer_model "http://127.0.0.1:12345" --filename_post_axmodel "minicpm4-0.5b-int8-ctx-ax650/MiniCPMForCausalLM_post.axmodel" --filename_tokens_embed "minicpm4-0.5b-int8-ctx-ax650/model.embed_tokens.weight.bfloat16.bin" --tokens_embed_num 73448 --tokens_embed_size 1024 --use_mmap_load_embed 0 --live_print 1 --devices 0
```

成功启动后信息如下：

```bash
m5stack@raspberrypi:~/rsp/MiniCPM4-0.5B$ ./main_axcl_aarch64 --system_prompt "You are MiniCPM4, created by ModelBest. You are a helpful assistant." --kvcache_path "./kvcache" --template_filename_axmodel "minicpm4-0.5b-int8-ctx-ax650/MiniCPMForCausalLM_p128_l%d_together.axmodel" --axmodel_num 24 --tokenizer_type 2 --url_tokenizer_model "http://127.0.0.1:12345" --filename_post_axmodel "minicpm4-0.5b-int8-ctx-ax650/MiniCPMForCausalLM_post.axmodel" --filename_tokens_embed "minicpm4-0.5b-int8-ctx-ax650/model.embed_tokens.weight.bfloat16.bin" --tokens_embed_num 73448 --tokens_embed_size 1024 --use_mmap_load_embed 0 --live_print 1 --devices 0
[I][                            Init][ 136]: LLM init start
[I][                            Init][  34]: connect http://127.0.0.1:12345 ok
[I][                            Init][  57]: uid: 9f086096-ff95-40cd-91f0-7551875c5e61
bos_id: 1, eos_id: 73440
  3% | ██                                |   1 /  27 [0.51s<13.72s, 1.97 count/s] tokenizer init ok
  100% | ████████████████████████████████ |  27 /  27 [22.21s<22.21s, 1.22 count/s] init post axmodel ok,remain_cmm(6450 MB)
[I][                            Init][ 237]: max_token_len : 1023
[I][                            Init][ 240]: kv_cache_size : 128, kv_cache_num: 1023
[I][                            Init][ 248]: prefill_token_num : 128
[I][                            Init][ 252]: grp: 1, prefill_max_token_num : 1
[I][                            Init][ 252]: grp: 2, prefill_max_token_num : 128
[I][                            Init][ 252]: grp: 3, prefill_max_token_num : 512
[I][                            Init][ 256]: prefill_max_token_num : 512
________________________
|    ID| remain cmm(MB)|
========================
|     0|           6450|
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
[I][                     load_config][ 282]: load config:
{
    "enable_repetition_penalty": false,
    "enable_temperature": false,
    "enable_top_k_sampling": true,
    "enable_top_p_sampling": false,
    "penalty_window": 20,
    "repetition_penalty": 1.2,
    "temperature": 0.9,
    "top_k": 1,
    "top_p": 0.8
}

[I][                            Init][ 279]: LLM init ok
Type "q" to exit, Ctrl+c to stop current running
[E][                    load_kvcache][ 100]: k_cache ./kvcache/k_cache_0.bin or v_cache ./kvcache/v_cache_0.bin not exist
[W][                            main][ 223]: load kvcache from path: ./kvcache failed,generate kvcache
[I][          GenerateKVCachePrefill][ 336]: input token num : 25, prefill_split_num : 1 prefill_grpid : 2
[I][          GenerateKVCachePrefill][ 373]: input_num_token:25
[E][                    save_kvcache][  49]: save kvcache failed
[E][                            main][ 227]: save kvcache failed
[I][                            main][ 229]: generate kvcache to path: ./kvcache
[I][                            main][ 236]: precompute_len: 25
[I][                            main][ 237]: system_prompt: You are MiniCPM4, created by ModelBest. You are a helpful assistant.
prompt >> hello
[I][                      SetKVCache][ 629]: prefill_grpid:2 kv_cache_num:128 precompute_len:25 input_num_token:10
[I][                      SetKVCache][ 632]: current prefill_max_token_num:384
[I][                             Run][ 870]: input token num : 10, prefill_split_num : 1
[I][                             Run][ 902]: input_num_token:10
[I][                             Run][1031]: ttft: 212.91 ms
Hi, Iam a MiniCPM seriesmodel, developedby Modelbestand OpenBMB. Formore information,please visit https://github.com/OpenBMB/

[N][                             Run][1183]: hit eos,avg 21.05 token/s

[I][                      GetKVCache][ 598]: precompute_len:71, remaining:441
prompt >>
```

| 模型          | 量化方式 | tftt (ms) | token/s |
| ------------- | -------- | --------- | ------- |
| MiniCPM4-0.5B | w8a16    | 212.91    | 21.05   |
