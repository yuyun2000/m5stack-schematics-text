# InternVL3-1B

1. [手动下载模型](https://huggingface.co/AXERA-TECH/InternVL3-1B) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/InternVL3-1B
```

**文件说明**

```bash
(axcl) m5stack@raspberrypi5:~/InternVL3-1B $ ls -lh
total 17M
-rw-r--r-- 1 m5stack m5stack 3.8K Jul 25 16:04 config.json
-rw-r--r-- 1 m5stack m5stack 3.9K Jul 25 16:04 gradio_demo.py
drwxr-xr-x 2 m5stack m5stack 4.0K Jul 25 16:06 internvl3_1b_ax650
drwxr-xr-x 2 m5stack m5stack 4.0K Jul 25 16:04 internvl3_tokenizer
-rw-r--r-- 1 m5stack m5stack 6.6K Jul 25 16:04 internvl3_tokenizer.py
-rw-r--r-- 1 m5stack m5stack 6.4M Jul 25 16:05 main_api_ax650
-rw-r--r-- 1 m5stack m5stack 1.9M Jul 25 16:05 main_api_axcl_x86
-rw-r--r-- 1 m5stack m5stack 6.3M Jul 25 16:05 main_ax650
-rw-r--r-- 1 m5stack m5stack 1.8M Jul 25 16:05 main_axcl_x86
-rw-r--r-- 1 m5stack m5stack  277 Jul 25 16:04 post_config.json
-rw-r--r-- 1 m5stack m5stack 6.0K Jul 25 16:04 README.md
-rw-r--r-- 1 m5stack m5stack  495 Jul 25 16:04 run_internvl_3_1b_448_api_ax650.sh
-rw-r--r-- 1 m5stack m5stack  516 Jul 25 16:04 run_internvl_3_1b_448_api_axcl_x86.sh
-rw-r--r-- 1 m5stack m5stack  506 Jul 25 16:04 run_internvl_3_1b_448_ax650.sh
-rw-r--r-- 1 m5stack m5stack  527 Jul 25 16:04 run_internvl_3_1b_448_axcl_x86.sh
-rw-r--r-- 1 m5stack m5stack  50K Jul 25 16:04 ssd_car.jpg
```

2. 启动 tokenizer 解析器

```bash
python internvl3_tokenizer.py --port 12345
```

3. 运行 tokenizer 服务，Host ip 默认为 localhost，端口号设置为 12345，正在运行后信息如下：

```bash
(axcl) m5stack@raspberrypi5:~/InternVL3-1B $ python internvl3_tokenizer.py --port 12345
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
None None 151645 <|im_end|> 151665 151667
context_len is  256
prompt is <|im_start|>system
你是书生·万象, 英文名是InternVL, 是由上海人工智能实验室、清华大学及多家合作单位联合开发的多模态大语言模型.<|im_end|>
<|im_start|>user
你好
<img></img>
<|im_end|>
<|im_start|>assistant
47
http://0.0.0.0:12345

```

4. 运行 InternVL3-1B

```bash
m5stack@raspberrypi5:~/InternVL3-1B $ chmod +x main_axcl_aarch64 run_internvl_3_1b_448_axcl_aarch64.sh
```

5. 测试图片

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/ssd_car.jpg" width="70%" />

6. 输出信息

```bash
m5stack@raspberrypi5:~/InternVL3-1B $ ./run_internvl_3_1b_448_axcl_aarch64.sh
[I][                            Init][ 160]: LLM init start
[I][                            Init][  34]: connect http://0.0.0.0:12345 ok
bos_id: -1, eos_id: 151645
img_start_token: 151665
img_context_token: 151667
input size: 1
    name:    image [unknown] [unknown]
        1 x 3 x 448 x 448 size:2408448


output size: 1
    name:   output
        1 x 256 x 896 size:917504

[I][                            Init][ 265]: IMAGE_CONTEXT_TOKEN: 151667, IMAGE_START_TOKEN: 151665
[I][                            Init][ 290]: image encoder input nchw@float32
[I][                            Init][ 320]: image encoder output float32

[I][                            Init][ 330]: image_encoder_height : 448, image_encoder_width: 448
[I][                            Init][ 332]: max_token_len : 2047
[I][                            Init][ 335]: kv_cache_size : 128, kv_cache_num: 2047
[I][                            Init][ 343]: prefill_token_num : 128
[I][                            Init][ 347]: grp: 1, prefill_max_token_num : 1
[I][                            Init][ 347]: grp: 2, prefill_max_token_num : 128
[I][                            Init][ 347]: grp: 3, prefill_max_token_num : 256
[I][                            Init][ 347]: grp: 4, prefill_max_token_num : 384
[I][                            Init][ 347]: grp: 5, prefill_max_token_num : 512
[I][                            Init][ 347]: grp: 6, prefill_max_token_num : 640
[I][                            Init][ 347]: grp: 7, prefill_max_token_num : 768
[I][                            Init][ 347]: grp: 8, prefill_max_token_num : 896
[I][                            Init][ 347]: grp: 9, prefill_max_token_num : 1024
[I][                            Init][ 351]: prefill_max_token_num : 1024
________________________
|    ID| remain cmm(MB)|
========================
|     0|           5764|
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
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

[I][                            Init][ 448]: LLM init ok
Type "q" to exit, Ctrl+c to stop current running
prompt >> Please describe this image
```
