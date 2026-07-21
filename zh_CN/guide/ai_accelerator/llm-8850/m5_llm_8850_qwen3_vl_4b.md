# Qwen3-VL-4B-Instruct-GPTQ-Int4

1. [手动下载模型](https://huggingface.co/M5Stack/Qwen3-VL-4B-Instruct-GPTQ-Int4-axmodel) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/M5Stack/Qwen3-VL-4B-Instruct-GPTQ-Int4-axmodel
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/Qwen3-VL-4B-Instruct-GPTQ-Int4-axmodel $ ls -lh
total 7.4M
drwxrwxr-x 2 m5stack m5stack 4.0K Nov  7 11:48 images
-rwxrwxr-x 1 m5stack m5stack 7.3M Nov  7 15:55 main_axcl_aarch64
drwxrwxr-x 2 m5stack m5stack 4.0K Nov  7 11:49 Qwen3-VL-4B-Instruct-ax8850
drwxrwxr-x 2 m5stack m5stack 4.0K Nov  7 11:42 qwen3-vl-tokenizer
-rw-rw-r-- 1 m5stack m5stack   24 Nov  7 16:02 README.md
-rwxrwxr-x 1 m5stack m5stack  715 Nov  7 16:19 run_image_axcl_aarch64.sh
-rwxrwxr-x 1 m5stack m5stack  715 Nov  7 16:20 run_video_axcl_aarch64.sh
-rwxrwxr-x 1 m5stack m5stack 9.4K Nov  7 14:42 tokenizer_images.py
-rwxrwxr-x 1 m5stack m5stack 9.3K Nov  7 14:41 tokenizer_video.py
drwxr-xr-x 2 m5stack m5stack 4.0K Nov  7 12:04 video
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
(qwen) m5stack@raspberrypi:~/rsp/Qwen3-VL-4B-Instruct-GPTQ-Int4-axmodel $ python tokenizer_images.py 
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
m5stack@raspberrypi:~/rsp/Qwen3-VL-4B-Instruct-GPTQ-Int4-axmodel $ ./run_image_axcl_aarch64.sh
[I][                            Init][ 163]: LLM init start
[I][                            Init][  34]: connect http://127.0.0.1:8080 ok
bos_id: -1, eos_id: 151645
img_start_token: 151652
img_context_token: 151655
  2% | █                                 |   1 /  39 [0.01s<0.20s, 200.00 count/s] tokenizer init ok[I][                            Init][  45]: LLaMaEmbedSelector use mmap
  5% | ██                                |   2 /  39 [0.01s<0.10s, 400.00 count/s] embed_selector init ok
[I][                             run][  30]: AXCLWorker start with devid 0
 10% |  █      ███                                                     |   3 /  39 [8.26s<80.56s, 0.48 count/s] init 18 axmodel ok,devid(0) re 94% | █████████████████████████████████████████████████████ █ ██ |  37 /  39 [73.09s<79.18s, 0.49 count/s] init 8 axmodel ok,devid(0) remain_100% | ████████████████████████████████ |  39 /  39 [81.89s<84.05s, 0.46 count/s] init post axmodel ok,remain_cmm(1894 MB)2299 MB)
input size: 1
    name: hidden_states [unknown] [unknown] 
        1 x 576 x 512 x 3 size:884736


output size: 4
    name: hidden_states_out 
        144 x 2560 size:1474560

    name: deepstack_feature_0 
        144 x 2560 size:1474560

    name: deepstack_feature_1 
        144 x 2560 size:1474560

    name: deepstack_feature_2 
        144 x 2560 size:1474560

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
|     0|           1443|
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
[E][                     load_config][ 278]: config file(post_config.json) open failed
[W][                            Init][ 453]: load postprocess config(post_config.json) failed
[I][                            Init][ 457]: LLM init ok
Type "q" to exit, Ctrl+c to stop current running
prompt >> Describe the content of the image
image >> images/recoAll_attractions_1.jpg
[I][                     EncodeImage][ 531]: pixel_values size 1
[I][                     EncodeImage][ 532]: grid_h 24 grid_w 24
[I][                     EncodeImage][ 580]: image encode time : 196.322998 ms, size : 1
[I][                          Encode][ 622]: input_ids size:171
[I][                          Encode][ 630]: offset 15
[I][                          Encode][ 659]: img_embed.size:1, 368640
[I][                          Encode][ 673]: out_embed size:437760
[I][                          Encode][ 674]: input_ids size 171
[I][                          Encode][ 676]: position_ids size:171
[I][                             Run][ 698]: input token num : 171, prefill_split_num : 2
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:43
[I][                             Run][ 909]: ttft: 984.20 ms
This image captures a classic view of the Giza Pyramids in Egypt, set against a vast, clear blue sky.

In the foreground, the desert sands stretch out, with a few small figures of people visible, providing a sense of scale. The most prominent structure is the Great Pyramid of Giza, its massive stone blocks forming a steep, triangular silhouette. To its left, the smaller Pyramid of Khafre is visible, and to its right, the Pyramid of Menkaure can be seen, though less distinct.

The pyramids are bathed in bright sunlight, casting long, dark shadows that emphasize their monumental scale and the precision of their construction. The clear, cloudless sky creates a dramatic contrast with the ancient, enduring stone, evoking a sense of timeless grandeur and mystery.

This scene is one of the most iconic and recognizable in the world, symbolizing the enduring legacy of ancient Egypt and the awe-inspiring achievements of its civilization.

[N][                             Run][1062]: hit eos,avg 5.92 token/s

prompt >> 
```

9. 停止 images tokenizer 解析器，并启动 video tokenizer 解析器

```bash
python tokenizer_video.py
```

10. 运行 video tokenizer 服务，Host ip 默认为 localhost，端口号设置为 8080，运行后信息如下：

```bash
(qwen) m5stack@raspberrypi:~/rsp/Qwen3-VL-4B-Instruct-GPTQ-Int4-axmodel $ python tokenizer_video.py
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
m5stack@raspberrypi:~/rsp/Qwen3-VL-4B-Instruct-GPTQ-Int4-axmodel $ ./run_video_axcl_aarch64.sh
[I][                            Init][ 163]: LLM init start
[I][                            Init][  34]: connect http://127.0.0.1:8080 ok
bos_id: -1, eos_id: 151645
img_start_token: 151652
img_context_token: 151656
  2% | █                                 |   1 /  39 [0.00s<0.12s, 333.33 count/s] tokenizer init ok[I][                            Init][  45]: LLaMaEmbedSelector use mmap
  5% | ██                                |   2 /  39 [0.00s<0.08s, 500.00 count/s] embed_selector init ok
[I][                             run][  30]: AXCLWorker start with devid 0
100% | ████████████████████████████████ |  39 /  39 [67.42s<67.42s, 0.58 count/s] init post axmodel ok,remain_cmm(1894 MB)299 MB))
input size: 1
    name: hidden_states [unknown] [unknown] 
        1 x 576 x 512 x 3 size:884736


output size: 4
    name: hidden_states_out 
        144 x 2560 size:1474560

    name: deepstack_feature_0 
        144 x 2560 size:1474560

    name: deepstack_feature_1 
        144 x 2560 size:1474560

    name: deepstack_feature_2 
        144 x 2560 size:1474560

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
|     0|           1443|
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
[E][                     load_config][ 278]: config file(post_config.json) open failed
[W][                            Init][ 453]: load postprocess config(post_config.json) failed
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
[I][                     EncodeImage][ 580]: image encode time : 938.083008 ms, size : 5
[I][                          Encode][ 622]: input_ids size:747
[I][                          Encode][ 630]: offset 15
[I][                          Encode][ 659]: img_embed.size:5, 368640
[I][                          Encode][ 664]: offset:159
[I][                          Encode][ 664]: offset:303
[I][                          Encode][ 664]: offset:447
[I][                          Encode][ 664]: offset:591
[I][                          Encode][ 673]: out_embed size:1912320
[I][                          Encode][ 674]: input_ids size 747
[I][                          Encode][ 676]: position_ids size:747
[I][                             Run][ 698]: input token num : 747, prefill_split_num : 6
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:128
[I][                             Run][ 732]: input_num_token:107
[I][                             Run][ 909]: ttft: 3385.97 ms
This video appears to be a static, low-angle shot of an indoor hallway or corridor, likely in a modern building or office. The scene is composed of several key elements:

- **The Setting**: The hallway is lined with dark, polished, reflective tiles that create a sleek, contemporary look. The reflections on the floor and walls add depth to the scene. On the right wall, there are two small, green-lit exit signs, indicating a fire safety feature. Below them, a red fire extinguisher is mounted on the wall, and a small, white control panel or thermostat is also visible.

- **The People**: Two individuals are present in the frame. One, wearing a white t-shirt with a blue graphic and dark pants, is walking away from the camera, moving toward the elevator or stairwell. The second person, dressed in a dark shirt and shorts, is also walking away, slightly to the right of the first person. Their movement is captured in motion, suggesting the video was taken in a moment of activity.

- **The Technology**: In the foreground, there are three laptops, each displaying a blue screen with a glowing, abstract image that resembles a jellyfish or a similar organic form. The laptops are placed on a gray, curved stand or cart, which is positioned near the wall. The laptops are connected to a network of cables, suggesting they are part of a monitoring or surveillance system. The laptops are not in use, as they are displaying a static image, which may indicate they are in standby mode or are being used for a specific purpose, such as monitoring or recording.

- **The Overall Atmosphere**: The scene is calm and uncluttered, with a focus on the technology and the movement of the people. The lighting is soft and ambient, and the overall mood is one of quiet observation, as if the viewer is being invited to watch the scene unfold.

The video seems to be a snapshot of a moment in time, capturing the interplay between human activity and technology in a modern, well-maintained environment. The presence of the laptops and the fire safety equipment suggests that this is a space that is monitored and maintained for safety and efficiency.

[N][                             Run][1062]: hit eos,avg 5.94 token/s

prompt >> 
```