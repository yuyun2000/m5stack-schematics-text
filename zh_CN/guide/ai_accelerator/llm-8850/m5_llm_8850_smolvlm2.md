# SmolVLM2-500M-Video-Instruct

SmolVLM2-500M-Video-Instruct 是一款轻量级多模态视频语言模型，能够理解和生成基于视频内容的文本，并支持指令式交互。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/SmolVLM2-500M-Video-Instruct) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/SmolVLM2-500M-Video-Instruct
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/SmolVLM2-500M-Video-Instruct $ ls -lh
total 40K
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 09:12 assets
-rw-rw-r-- 1 m5stack m5stack    0 Aug 12 09:12 config.json
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 09:12 embeds
-rw-rw-r-- 1 m5stack m5stack  10K Aug 12 09:12 infer_axmodel.py
-rw-rw-r-- 1 m5stack m5stack 2.5K Aug 12 09:12 README.md
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 09:12 smolvlm2_axmodel
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 09:12 smolvlm2_tokenizer
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 09:12 utils
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 09:13 vit_model
```

2. 创建虚拟环境

```bash
python -m venv smolvlm
```

3. 激活虚拟环境

```bash
source smolvlm/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install transformers torch torchvision tqdm pillow num2words onnx onnxruntime
```

5. 运行

```bash
python infer_axmodel.py --axmodel_path smolvlm2_axmodel/ --vit_model vit_model/vision_model.axmodel --hf_model smolvlm2_tokenizer/ -i assets/bee.jpg
```

测试图片：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/bee.jpg" width="70%" />

运行结果：

```bash
(smolvlm) m5stack@raspberrypi:~/rsp/SmolVLM2-500M-Video-Instruct $ python infer_axmodel.py --axmodel_path smolvlm2_axmodel/ --vit_model vit_model/vision_model.axmodel --hf_model smolvlm2_tokenizer/ -i assets/bee.jpg
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.1-patch1-dirty 59be8f11-dirty
You have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0.
Init InferenceSession:   0%|                                                                                       | 0/32 [00:00<?, ?it/s][INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.1-patch1-dirty 59be8f11-dirty
Init InferenceSession: 100%|██████████████████████████████████████████████████████████████████████████████| 32/32 [00:10<00:00,  2.98it/s]
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.1-patch1-dirty 59be8f11-dirty
Model loaded successfully!
slice_indices: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Slice prefill done: 0
Slice prefill done: 1
Slice prefill done: 2
Slice prefill done: 3
Slice prefill done: 4
Slice prefill done: 5
Slice prefill done: 6
Slice prefill done: 7
Slice prefill done: 8
answer >>  The image depicts a close-up view of a pink flower with a bee on it. The bee, which appears to be a bumblebee, is perched on the flower's center, which is surrounded by a cluster of other flowers. The bee is in the process of collecting nectar from the flower, which is a common behavior for bees. The flower itself has a yellow center with a cluster of yellow stamens surrounding it. The petals of the flower are a vibrant shade of pink, and the bee is positioned very close to the camera, making it the focal point of the image. The background is slightly blurred, but it appears to be a garden or a field with other flowers and plants, contributing to the overall natural setting of the image.
```
