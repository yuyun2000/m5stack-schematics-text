# Real-ESRGAN

Real-ESRGAN 是一种基于深度学习的图像超分辨率模型，能够在恢复低分辨率图像细节的同时有效去除噪声，适用于图像和视频的清晰化处理。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/Real-ESRGAN) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/Real-ESRGAN
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/Real-ESRGAN $ ls -lh
total 428K
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 13 09:12 ax630c
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 13 09:12 ax650
-rw-rw-r-- 1 m5stack m5stack    0 Aug 13 09:11 config.json
-rw-rw-r-- 1 m5stack m5stack 2.9K Aug 13 09:11 main.py
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 13 09:12 onnx
-rw-rw-r-- 1 m5stack m5stack 387K Aug 13 09:12 output_test_256.jpg
-rw-rw-r-- 1 m5stack m5stack 3.9K Aug 13 09:11 README.md
-rw-rw-r-- 1 m5stack m5stack  19K Aug 13 09:11 test_256.jpeg
```

2. 创建虚拟环境

```bash
python -m venv esrgan
```

3. 激活虚拟环境

```bash
source esrgan/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install argparse numpy opencv-python
```

5. 运行

```bash
python3 main.py --input test_256.jpeg --output test_256_20e.jpeg --model ax650/realesrgan-x4-256.axmodel
```

运行结果：

```bash
(esrgan) m5stack@raspberrypi:~/rsp/Real-ESRGAN $ python3 main.py --input test_256.jpeg --output test_256_20e.jpeg --model ax650/realesrgan-x4-256.axmodel
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.4 3dfd5692
input.1 [1, 256, 256, 3] uint8
1895 [1, 1024, 1024, 3] float32
Original Image Shape: (243, 243, 3)
Preprocessed Image Shape: (1, 256, 256, 3)
Inference Time: 454.03 ms
Output Shape: (1, 1024, 1024, 3)
Final Output Image Shape: (1024, 1024, 3)
```

原图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/test_256.jpeg" width="60%" />

输出：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/test_256_20e.jpeg" width="60%" />
