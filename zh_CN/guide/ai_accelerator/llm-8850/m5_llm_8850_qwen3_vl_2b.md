# Qwen3-VL-2B-Instruct

1. [手动下载模型](https://huggingface.co/M5Stack/Qwen3-VL-2B-Instruct-axmodel) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/M5Stack/Qwen3-VL-2B-Instruct-axmodel
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/Qwen3-VL-2B-Instruct-axmodel $ ls -lh
total 7.4M
drwxrwxr-x 2 m5stack m5stack 4.0K Oct 28 09:37 images
-rwxrwxr-x 1 m5stack m5stack 7.3M Nov  7 15:55 main_axcl_aarch64
-rwxrwxr-x 1 m5stack m5stack  276 Nov  7 11:58 post_config.json
drwxrwxr-x 2 m5stack m5stack 4.0K Oct 28 09:38 Qwen3-VL-2B-Instruct-ax8850
drwxrwxr-x 2 m5stack m5stack 4.0K Oct 28 09:31 qwen3-vl-tokenizer
-rw-rw-r-- 1 m5stack m5stack   24 Nov  7 14:12 README.md
-rwxrwxr-x 1 m5stack m5stack  715 Nov  7 14:17 run_image_axcl_aarch64.sh
-rwxrwxr-x 1 m5stack m5stack  715 Nov  7 14:17 run_video_axcl_aarch64.sh
-rwxrwxr-x 1 m5stack m5stack 9.4K Nov  7 14:42 tokenizer_images.py
-rwxrwxr-x 1 m5stack m5stack 9.3K Nov  7 14:41 tokenizer_video.py
drwxrwxr-x 2 m5stack m5stack 4.0K Nov  7 11:26 video
```

#> 提示 | 如果之前已经创建了 **qwen** 的虚拟环境，不需要重新创建，只需要激活即可。

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

5. 启动 images tokenizer 解析器

```bash
python tokenizer_images.py 
```

6. 运行 images tokenizer 服务，Host ip 默认为 localhost，端口号设置为 8080，运行后信息如下：

```bash
(qwen) m5stack@raspberrypi:~/rsp/Qwen3-VL-2B-Instruct-axmodel $ python tokenizer_images.py 
None None 151645 <|im_end|>
[151644, 8948, 198, 2610, 525, 264, 10950, 17847, 13, 151645, 198, 151644, 872, 198, 151652, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151655, 151653, 74785, 419, 2168, 13, 151645, 198, 151644, 77091, 198]
281
[151644, 8948, 198, 2610, 525, 264, 10950, 17847, 13, 151645, 198, 151644, 872, 198, 14990, 1879, 151645, 198, 151644, 77091, 198]
21
http://localhost:8080
```

?> 提示 | 以下操作需要新建一个 raspberrypi 的终端。

7. 设置可执行权限

```bash
chmod +x main_axcl_aarch64 run_image_axcl_aarch64.sh
```

8. 启动 Qwen3 模型图片推理服务

```bash
./run_image_axcl_aarch64.sh
```

成功启动后信息如下：

```bash
m5stack@raspberrypi:~/rsp/Qwen3-VL-2B-Instruct-axmodel $ ./run_image_axcl_aarch64.sh 
[I][                            Init][ 163]: LLM init start
[I][                            Init][  34]: connect http://127.0.0.1:8080 ok
bos_id: -1, eos_id: 151645
img_start_token: 151652
img_context_token: 151655
  3% | ██                                |   1 /  31 [0.01s<0.19s, 166.67 count/s] tokenizer init ok[I][                            Init][  45]: LLaMaEmbedSelector use mmap
  6% | ███                               |   2 /  31 [0.01s<0.09s, 333.33 count/s] embed_selector init ok
[I][                             run][  30]: AXCLWorker start with devid 0
 80% | ███████████████████████████████████████████████ █ █           |  24 /  31 [45.28s<56.14s, 0.55 count/s] init 26 axmodel ok,devid(0) rem100% | ████████████████████████████████ |  31 /  31 [61.71s<61.71s, 0.50 count/s] init post axmodel ok,remain_cmm(3341 MB)3665 MB)
input size: 1
    name: hidden_states [unknown] [unknown] 
        1 x 576 x 512 x 3 size:884736


output size: 4
    name: hidden_states_out 
        144 x 2048 size:1179648

    name: deepstack_feature_0 
        144 x 2048 size:1179648

    name: deepstack_feature_1 
        144 x 2048 size:1179648

    name: deepstack_feature_2 
        144 x 2048 size:1179648

[I][                            Init][ 268]: IMAGE_CONTEXT_TOKEN: 151655, IMAGE_START_TOKEN: 151652
[I][                            Init][ 329]: image encoder output float32

[I][                            Init][ 341]: max_token_len : 2047
[I][                            Init][ 344]: kv_cache_size : 1024, kv_cache_num: 2047
[I][                            Init][ 352]: prefill_token_num : 128
[I][                            Init][ 356]: grp: 1, prefill_max_token_num : 1
[I][                            Init][ 356]: grp: 2, prefill_max_token_num : 128
[I][                            Init][ 356]: grp: 3, prefill_max_token_num : 256
[I][                            Init][ 356]: grp: 4, prefill_max_token_num : 384
[I][                            Init][ 356]: grp: 5, prefill_max_token_num : 512
[I][                            Init][ 356]: grp: 6, prefill_max_token_num : 640
[I][                            Init][ 356]: grp: 7, prefill_max_token_num : 768
[I][                            Init][ 356]: grp: 8, prefill_max_token_num : 896
[I][                            Init][ 356]: grp: 9, prefill_max_token_num : 1024
[I][                            Init][ 356]: grp: 10, prefill_max_token_num : 1152
[I][                            Init][ 360]: prefill_max_token_num : 1152
________________________
|    ID| remain cmm(MB)|
========================
|     0|           2899|
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
[I][                     load_config][ 282]: load config: 
{
    "enable_repetition_penalty": false,
    "enable_temperature": true,
    "enable_top_k_sampling": true,
    "enable_top_p_sampling": false,
    "penalty_window": 30,
    "repetition_penalty": 1,
    "temperature": 0.2,
    "top_k": 10,
    "top_p": 0.8
}

[I][                            Init][ 457]: LLM init ok
Type "q" to exit, Ctrl+c to stop current running
prompt >> Describe the content of the image
image >> images/recoAll_attractions_1.jpg
[I][                     EncodeImage][ 531]: pixel_values size 1
[I][                     EncodeImage][ 532]: grid_h 24 grid_w 24
[I][                     EncodeImage][ 580]: image encode time : 191.645004 ms, size : 1
[I][                          Encode][ 622]: input_ids size:171
[I][                          Encode][ 630]: offset 15
[I][                          Encode][ 659]: img_embed.size:1, 294912
[I][                          Encode][ 673]: out_embed size:350208
[I][                          Encode][ 674]: input_ids size 171
[I][                          Encode][ 676]: position_ids size:171
[I][                             Run][ 698]: input token num : 171, prefill_split_num : 2
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:43
[I][                             Run][ 909]: ttft: 596.82 ms
This is a photograph of the Great Pyramids of Giza, the three largest and most famous pyramids in the world, located in the Giza Plateau in Egypt. The image captures the pyramids under a clear blue sky, with the vast, sandy desert landscape surrounding them. The pyramids are constructed from large stone blocks, and their massive, stepped structures are clearly visible. In the foreground, a few small figures can be seen, providing a sense of scale to the immense structures. The image is a clear and detailed depiction of the iconic ancient monuments.

[N][                             Run][1062]: hit eos,avg 7.80 token/s

prompt >> 
```

9. 停止 images tokenizer 解析器，并启动 video tokenizer 解析器

```bash
python tokenizer_video.py
```

10. 运行 video tokenizer 服务，Host ip 默认为 localhost，端口号设置为 8080，运行后信息如下：

```bash
(qwen) m5stack@raspberrypi:~/rsp/Qwen3-VL-2B-Instruct-axmodel $ python tokenizer_video.py 
None None 151645 <|im_end|>
[151644, 8948, 198, 2610, 525, 264, 10950, 17847, 13, 151645, 198, 151644, 872, 198, 151652, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151656, 151653, 74785, 419, 2168, 13, 151645, 198, 151644, 77091, 198]
281
[151644, 8948, 198, 2610, 525, 264, 10950, 17847, 13, 151645, 198, 151644, 872, 198, 14990, 1879, 151645, 198, 151644, 77091, 198]
21
http://localhost:8080
```

11. 启动 Qwen3 模型视频推理服务

```bash
./run_video_axcl_aarch64.sh
```

成功启动后信息如下：

```bash
m5stack@raspberrypi:~/rsp/Qwen3-VL-2B-Instruct-axmodel $ ./run_video_axcl_aarch64.sh 
[I][                            Init][ 163]: LLM init start
[I][                            Init][  34]: connect http://127.0.0.1:8080 ok
bos_id: -1, eos_id: 151645
img_start_token: 151652
img_context_token: 151656
  3% | ██                                |   1 /  31 [0.00s<0.09s, 333.33 count/s] tokenizer init ok[I][                            Init][  45]: LLaMaEmbedSelector use mmap
  6% | ███                               |   2 /  31 [0.00s<0.06s, 500.00 count/s] embed_selector init ok
[I][                             run][  30]: AXCLWorker start with devid 0
 16% | █████████ ██                                       |   4 /  31 [6.09s<47.22s, 0.66 count/s] init 7 axmodel ok,devid(0) remain_cmm(-1 MB 93% | ███████████████████████████████████████████████████████████     |  29 /  31 [39.21s<43.41s, 0.71 count/s] init 13 axmodel ok,devid(0) r100% | ████████████████████████████████ |  31 /  31 [45.05s<46.55s, 0.67 count/s] init post axmodel ok,remain_cmm(3341 MB)3665 MB)
input size: 1
    name: hidden_states [unknown] [unknown] 
        1 x 576 x 512 x 3 size:884736


output size: 4
    name: hidden_states_out 
        144 x 2048 size:1179648

    name: deepstack_feature_0 
        144 x 2048 size:1179648

    name: deepstack_feature_1 
        144 x 2048 size:1179648

    name: deepstack_feature_2 
        144 x 2048 size:1179648

[I][                            Init][ 268]: IMAGE_CONTEXT_TOKEN: 151656, IMAGE_START_TOKEN: 151652
[I][                            Init][ 329]: image encoder output float32

[I][                            Init][ 341]: max_token_len : 2047
[I][                            Init][ 344]: kv_cache_size : 1024, kv_cache_num: 2047
[I][                            Init][ 352]: prefill_token_num : 128
[I][                            Init][ 356]: grp: 1, prefill_max_token_num : 1
[I][                            Init][ 356]: grp: 2, prefill_max_token_num : 128
[I][                            Init][ 356]: grp: 3, prefill_max_token_num : 256
[I][                            Init][ 356]: grp: 4, prefill_max_token_num : 384
[I][                            Init][ 356]: grp: 5, prefill_max_token_num : 512
[I][                            Init][ 356]: grp: 6, prefill_max_token_num : 640
[I][                            Init][ 356]: grp: 7, prefill_max_token_num : 768
[I][                            Init][ 356]: grp: 8, prefill_max_token_num : 896
[I][                            Init][ 356]: grp: 9, prefill_max_token_num : 1024
[I][                            Init][ 356]: grp: 10, prefill_max_token_num : 1152
[I][                            Init][ 360]: prefill_max_token_num : 1152
________________________
|    ID| remain cmm(MB)|
========================
|     0|           2899|
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
[I][                     load_config][ 282]: load config: 
{
    "enable_repetition_penalty": false,
    "enable_temperature": true,
    "enable_top_k_sampling": true,
    "enable_top_p_sampling": false,
    "penalty_window": 30,
    "repetition_penalty": 1,
    "temperature": 0.2,
    "top_k": 10,
    "top_p": 0.8
}

[I][                            Init][ 457]: LLM init ok
Type "q" to exit, Ctrl+c to stop current running
prompt >> Describe the content of the video
video >> video
video/out_0001.jpg
video/out_0002.jpg
video/out_0003.jpg
video/out_0004.jpg
video/out_0005.jpg
video/out_0006.jpg
video/out_0007.jpg
video/out_0008.jpg
video/out_0009.jpg
[I][                     EncodeImage][ 531]: pixel_values size 5
[I][                     EncodeImage][ 532]: grid_h 24 grid_w 24
[I][                     EncodeImage][ 580]: image encode time : 915.744019 ms, size : 5
[I][                          Encode][ 622]: input_ids size:747
[I][                          Encode][ 630]: offset 15
[I][                          Encode][ 659]: img_embed.size:5, 294912
[I][                          Encode][ 664]: offset:159
[I][                          Encode][ 664]: offset:303
[I][                          Encode][ 664]: offset:447
[I][                          Encode][ 664]: offset:591
[I][                          Encode][ 673]: out_embed size:1529856
[I][                          Encode][ 674]: input_ids size 747
[I][                          Encode][ 676]: position_ids size:747
[I][                             Run][ 698]: input token num : 747, prefill_split_num : 6
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:107
[I][                             Run][ 909]: ttft: 2033.21 ms
The video captures a person walking through a modern, well-lit hallway. The individual, seen from behind, is wearing a white t-shirt with a blue graphic on the back and dark pants. They are moving towards a glass door, which is part of a larger set of doors, possibly in a building's entrance or a corridor.

The hallway features dark, polished tiles with a subtle, elegant pattern. A green emergency exit sign is visible on the wall, indicating the direction to the exit. To the right of the person, a laptop is placed on a stand, its screen displaying a blue image, possibly a video or a live feed. The laptop is connected to a cable, suggesting it might be used for monitoring or communication purposes.

The overall atmosphere of the scene is clean, professional, and modern, with a focus on safety and technology. The person's movement and the surrounding environment suggest a routine activity, such as entering a building or checking on a system.

[N][                             Run][1062]: hit eos,avg 7.77 token/s

prompt >> 
```