# CLIP

1. [手动下载模型](https://huggingface.co/AXERA-TECH/LibCLIP) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/LibCLIP
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/LibCLIP $ ls -lh
total 157M
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 11 09:09 cnclip
-rw-rw-r-- 1 m5stack m5stack 156M Aug 11 09:08 coco_1000.tar
-rw-rw-r-- 1 m5stack m5stack 3.8K Aug 11 09:08 config.json
-rw-rw-r-- 1 m5stack m5stack 779K Aug 11 09:08 gradio_01.png
drwxrwxr-x 5 m5stack m5stack 4.0K Aug 11 09:08 install
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 11 09:08 pyclip
-rw-rw-r-- 1 m5stack m5stack 6.0K Aug 11 09:08 README.md
```

2. 创建虚拟环境

```bash
python -m venv clip
```

3. 激活虚拟环境

```bash
source clip/bin/activate
```

4. 安装依赖包

```bash
pip install -r pyclip/requirements.txt
```

5. 设置环境变量

```bash
export LD_PRELOAD=/usr/lib/
```

6. 复制动态库

```bash
cp install/lib/aarch64/libclip.so pyclip/

```

7. 解压测试图片

```bash
tar xf coco_1000.tar
```

8. 启动 Web 服务

```bash
python pyclip/gradio_example.py --ienc cnclip/cnclip_vit_l14_336px_vision_u16u8.axmodel --tenc cnclip/cnclip_vit_l14_336px_text_u16.axmodel --vocab cnclip/cn_vocab.txt --isCN 1 --db_path clip_feat_db_coco --image_folder coco_1000/
```

成功启动后信息如下

```bash
(clip) m5stack@raspberrypi:~/rsp/LibCLIP $ python pyclip/gradio_example.py --ienc cnclip/cnclip_vit_l14_336px_vision_u16u8.axmodel --tenc cnclip/cnclip_vit_l14_336px_text_u16.axmodel --vocab cnclip/cn_vocab.txt --isCN 1 --db_path clip_feat_db_coco --image_folder coco_1000/
Trying to load: /home/m5stack/rsp/LibCLIP/pyclip/aarch64/libclip.so

❌ Failed to load: /home/m5stack/rsp/LibCLIP/pyclip/aarch64/libclip.so
   /home/m5stack/rsp/LibCLIP/pyclip/aarch64/libclip.so: cannot open shared object file: No such file or directory
🔍 File not found. Please verify that libclip.so exists and the path is correct.

Trying to load: /home/m5stack/rsp/LibCLIP/pyclip/libclip.so
open libax_sys.so failed
open libax_engine.so failed
✅ Successfully loaded: /home/m5stack/rsp/LibCLIP/pyclip/libclip.so
可用设备: {'host': {'available': True, 'version': '', 'mem_info': {'remain': 0, 'total': 0}}, 'devices': {'host_version': 'V3.6.3_20250722020142', 'dev_version': 'V3.6.3_20250722020142', 'count': 1, 'devices_info': [{'temp': 62, 'cpu_usage': 1, 'npu_usage': 0, 'mem_info': {'remain': 7022, 'total': 7040}}]}}
[I][                             run][  31]: AXCLWorker start with devid 0

input size: 1
    name:    image [unknown] [unknown]
        1 x 3 x 336 x 336


output size: 1
    name: unnorm_image_features
        1 x 768

[I][              load_image_encoder][  50]: nchw 336 336
[I][              load_image_encoder][  60]: image feature len 768

input size: 1
    name:     text [unknown] [unknown]
        1 x 52


output size: 1
    name: unnorm_text_features
        1 x 768

[I][               load_text_encoder][  44]: text feature len 768
[I][                  load_tokenizer][  60]: text token len 52
100%|███████████████████████████████████| 1000/1000 [00:00<00:00, 163246.95it/s]
* Running on local URL:  http://0.0.0.0:7860
* To create a public link, set `share=True` in `launch()`.
```

9. 在浏览器中打开 http://127.0.0.1:7860 ，在文本框输出需要检索的内容，点击搜图。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/clip.png" width="100%" />
