# RIFE

RIFE 是一种基于深度学习的实时视频插帧模型，能够高效预测中间帧以提升视频帧率，适用于视频流畅化与动画制作等领域。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/RIFE.axera) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/RIFE.axera
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/RIFE.axera $ ls -lh
total 52K
-rw-rw-r-- 1 m5stack m5stack 1.1K Sep 29 14:28 build_config.json
-rw-rw-r-- 1 m5stack m5stack    0 Sep 29 14:28 config.json
drwxrwxr-x 2 m5stack m5stack 4.0K Sep 29 14:28 model
-rw-rw-r-- 1 m5stack m5stack 6.9K Sep 29 14:28 ms_ssim.py
-rw-rw-r-- 1 m5stack m5stack 1.8K Sep 29 14:28 README.md
-rw-rw-r-- 1 m5stack m5stack   88 Sep 29 14:28 requirements.txt
-rw-rw-r-- 1 m5stack m5stack 9.2K Sep 29 14:28 run_axmodel.py
-rw-rw-r-- 1 m5stack m5stack 9.2K Sep 29 14:28 run_onnx.py
drwxrwxr-x 2 m5stack m5stack 4.0K Sep 29 14:28 video
```

2. 创建虚拟环境

```bash
python -m venv rife
```

3. 激活虚拟环境

```bash
source rife/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install -r requirements.txt
```

5. 运行

```bash
python3 run_axmodel.py --model ./model/rife_x2_720p.axmodel --video ./video/demo.mp4
```

运行结果：

```bash
(rife) m5stack@raspberrypi:~/rsp/RIFE.axera $ python3 run_axmodel.py --model ./model/rife_x2_720p.axmodel --video ./video/demo.mp4
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.2 77cdc0c2
./video/demo.mp4, 128.0 frames in total, 25.0FPS to 50.0FPS
The audio will be merged after interpolation process
 99%|██████████████████████████████████████▋| 127/128.0 [02:45<00:01,  1.30s/it]
```
