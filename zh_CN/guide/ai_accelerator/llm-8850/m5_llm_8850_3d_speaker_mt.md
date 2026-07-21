# 3D-Speaker-MT

3D-Speaker-MT 是一种多任务学习的说话人识别模型，能够同时进行说话人验证、辨认等任务，在多场景下实现高精度的语音身份识别。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/3D-Speaker-MT.axera) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/3D-Speaker-MT.axera
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/3D-Speaker-MT.axera $ ls -lh
total 64K
-rwxrwxr-x 1 m5stack m5stack 7.7K Sep 29 14:39 ax_meeting_transc_demo.py
drwxrwxr-x 4 m5stack m5stack 4.0K Sep 29 14:39 ax_model
-rwxrwxr-x 1 m5stack m5stack    0 Sep 29 14:39 config.json
-rwxrwxr-x 1 m5stack m5stack  33K Sep 29 14:39 model.py
-rwxrwxr-x 1 m5stack m5stack 3.4K Sep 29 14:39 README.md
-rwxrwxr-x 1 m5stack m5stack   74 Sep 29 14:39 requirements.txt
drwxrwxr-x 5 m5stack m5stack 4.0K Sep 29 14:39 utils
drwxrwxr-x 2 m5stack m5stack 4.0K Sep 29 14:39 wav
```

2. 创建虚拟环境

```bash
python -m venv speaker
```

3. 激活虚拟环境

```bash
source speaker/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install -r requirements.txt
```

5. 运行

```bash
python3 ax_meeting_transc_demo.py --output_dir output_dir --wav_file wav/vad_example.wav
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