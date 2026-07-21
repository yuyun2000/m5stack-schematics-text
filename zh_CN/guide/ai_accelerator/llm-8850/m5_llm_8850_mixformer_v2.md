# MixFormerV2

MixFormerV2 是一种改进型的统一Transformer目标跟踪模型，通过融合特征提取与匹配过程，提升跟踪的精度与速度。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/MixFormerV2) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/MixFormerV2
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/MixFormerV2 $ ls -lh
total 63M
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 11 18:28 ax630c
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 11 18:28 ax650
-rw-rw-r-- 1 m5stack m5stack  63M Aug 11 18:28 car.avi
-rw-rw-r-- 1 m5stack m5stack    0 Aug 11 18:28 config.json
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 11 18:28 onnx
-rw-rw-r-- 1 m5stack m5stack 4.0K Aug 11 18:28 README.md
-rw-rw-r-- 1 m5stack m5stack  15K Aug 11 18:28 run_mixformer2_axmodel.py
-rw-rw-r-- 1 m5stack m5stack  14K Aug 11 18:28 run_mixformer2_onnx.py
```

2. 创建虚拟环境

```bash
python -m venv mixformer
```

3. 激活虚拟环境

```bash
source mixformer/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install argparse numpy opencv-python glob2
```

5. 运行

```bash
python3 run_mixformer2_axmodel.py --model-path ax650/mixformer_v2.axmodel --frame-path car.avi -r 10
```

运行结果：

```bash
(mixformer) m5stack@raspberrypi:~/rsp/MixFormerV2 $ python3 run_mixformer2_axmodel.py --model-path ax650/mixformer_v2.axmodel --frame-path car.avi -r 10
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.4-dirty 4ff37520-dirty
====================type================= [1079, 482] <class 'list'> <class 'list'>
第一帧初始化完毕！
Video: tracking     1011.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Video: tracking     8.0fps
Reached the maximum number of frames (10). Exiting loop.
video: average finale average tracking fps 121.2 fps
```
