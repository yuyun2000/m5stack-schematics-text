# LivePortrait

LivePortrait 是一种基于深度学习的人像驱动生成模型，可将静态人像转换为具有真实表情与动作的动态视频效果。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/LivePortrait) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/LivePortrait
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/LivePortrait $ ls -lh
total 16K
drwxrwxr-x 3 m5stack m5stack 4.0K Aug 13 09:41 assets
-rw-rw-r-- 1 m5stack m5stack    0 Aug 13 09:41 config.json
drwxrwxr-x 5 m5stack m5stack 4.0K Aug 13 09:41 python
-rw-rw-r-- 1 m5stack m5stack 5.7K Aug 13 09:41 README.md
```

2. 创建虚拟环境

```bash
python -m venv lvpr
```

3. 激活虚拟环境

```bash
source lvpr/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install -r python/requirements.txt
pip install requests tqdm
```

## Image

**运行：**

```bash
python ./python/infer.py --source ./assets/examples/source/s0.jpg --driving ./assets/examples/driving/d8.jpg --models ./python/axmodels/ --output-dir ./axmodel_infer
```

运行结果：

```bash
(lvpr) m5stack@raspberrypi:~/rsp/LivePortrait $ python ./python/infer.py --source ./assets/examples/source/s0.jpg --driving ./assets/examples/driving/d8.jpg --models ./python/axmodels/ --output-dir ./axmodel_infer
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 144960ad
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 144960ad
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 0f7260e8
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 144960ad
FaceAnalysisDIY warmup time: 0.237s
LandmarkRunner warmup time: 0.183s
2025-08-13 10:04:42.914 | INFO     | __main__:main:727 - Start making driving motion template...
2025-08-13 10:04:43.782 | INFO     | __main__:main:747 - Prepared pasteback mask done.
2025-08-13 10:04:44.565 | INFO     | __main__:main:787 - The output of image-driven portrait animation is an image.
2025-08-13 10:04:50.566 | DEBUG    | __main__:warp_decode:647 - warp time: 5.997s
2025-08-13 10:04:50.902 | INFO     | __main__:main:881 - Animated image: ./axmodel_infer/s0--d8.jpg
2025-08-13 10:04:50.902 | INFO     | __main__:main:882 - Animated image with concat: ./axmodel_infer/s0--d8_concat.jpg
2025-08-13 10:04:50.920 | DEBUG    | __main__:<module>:894 - LivePortrait axmodel infer time: 18.068s
```

**原图：**

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/s0--d8_concat.jpg" width="60%" />

**输出：**

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/s0--d8.jpg" width="60%" />

## Video

**运行：**

```bash
python ./python/infer.py --source ./assets/examples/source/s0.jpg --driving ./assets/examples/driving/d0.mp4 --models ./python/axmodels/ --output-dir ./axmodel_infer
```

运行结果：

```bash
(lvpr) m5stack@raspberrypi:~/rsp/LivePortrait $ python ./python/infer.py --source ./assets/examples/source/s0.jpg --driving ./assets/examples/driving/d0.mp4 --models ./python/axmodels/ --output-dir ./axmodel_infer

[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 144960ad
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 144960ad
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 0f7260e8
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 144960ad
FaceAnalysisDIY warmup time: 0.213s
LandmarkRunner warmup time: 0.180s
2025-08-13 10:14:47.779 | INFO     | __main__:main:727 - Start making driving motion template...
2025-08-13 10:15:04.110 | INFO     | __main__:main:747 - Prepared pasteback mask done.
2025-08-13 10:15:04.903 | INFO     | __main__:main:785 - The animated video consists of 78 frames.
2025-08-13 10:15:11.468 | DEBUG    | __main__:warp_decode:647 - warp time: 6.561s
2025-08-13 10:25:50.630 | DEBUG    | __main__:warp_decode:647 - warp time: 8.343s
2025-08-13 10:25:51.493 | INFO     | __main__:has_audio_stream:114 - Error occurred while probing video: ./assets/examples/driving/d0.mp4, you may need to install ffprobe! (https://ffmpeg.org/download.html) Now set audio to false!
2025-08-13 10:25:54.608 | INFO     | __main__:main:870 - Animated video: ./axmodel_infer/s0--d0.mp4
2025-08-13 10:25:54.609 | INFO     | __main__:main:871 - Animated video with concat: ./axmodel_infer/s0--d0_concat.mp4
2025-08-13 10:25:54.644 | DEBUG    | __main__:<module>:894 - LivePortrait axmodel infer time: 670.930s
```

**原视频：** <video src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/s0--d0_concat.mp4" width="60%" controls autoplay muted loop></video>

**输出：** <video src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/s0--d0.mp4" width="60%" controls autoplay muted loop></video>
