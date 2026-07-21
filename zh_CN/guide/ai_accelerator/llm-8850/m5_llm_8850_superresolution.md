# SuperResolution

SuperResolution 是一种通过深度学习或其他算法将低分辨率图像转换为高分辨率图像的模型，用于提升图像细节和视觉质量。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/SuperResolution) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/SuperResolution
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/SuperResolution $ ls -lh
total 20K
-rw-rw-r-- 1 m5stack m5stack 3.8K Sep  4 18:49 config.json
drwxrwxr-x 4 m5stack m5stack 4.0K Sep  4 18:49 model_convert
drwxrwxr-x 5 m5stack m5stack 4.0K Sep  4 19:12 python
-rw-rw-r-- 1 m5stack m5stack 2.3K Sep  4 18:49 README.md
drwxrwxr-x 2 m5stack m5stack 4.0K Sep  4 19:03 video
```

2. 创建虚拟环境

```bash
python -m venv sr
```

3. 激活虚拟环境

```bash
source sr/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install  opencv-python torch torchvision tqdm scikit-image
```

5. 运行

```bash
python python/run_axmodel.py --model model_convert/axmodel/edsr_baseline_x2_1.axmodel --dir_demo video/test_1920x1080.mp4
```

运行结果：

```bash
(sr) m5stack@raspberrypi:~/rsp/SuperResolution $ python python/run_axmodel.py --model model_convert/axmodel/edsr_baseline_x2_1.axmodel --dir_demo video/test_1920x1080.mp4 
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.2 6bff2f67
100%|█████████████████████████████████████████| 267/267 [06:21<00:00,  1.43s/it]
Total time: 275.618 seconds for 267 frames
Average time: 1.032 seconds for each frame

```

原视频截图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/source.png" width="90%" />

输出视频截图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/super_resolution.png" width="90%" />
