# Jina CLIP v2

jina-clip-v2 是一个通用的多语言多模态文本与图像嵌入模型。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/jina-clip-v2) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/jina-clip-v2
```

**文件说明**

```bash
(ppocr) m5stack@raspberrypi:~/rsp/jina-clip-v2 $ ls -lh
total 1.7G
-rw-rw-r-- 1 m5stack m5stack  51K Oct 20 12:24 beach1.jpg
-rw-rw-r-- 1 m5stack m5stack    0 Oct 20 12:24 config.json
-rw-rw-r-- 1 m5stack m5stack 351M Oct 20 12:25 image_encoder.axmodel
drwxrwxr-x 2 m5stack m5stack 4.0K Oct 20 12:24 jina-clip-v2
-rw-rw-r-- 1 m5stack m5stack 1.3K Oct 20 12:24 README.md
-rw-rw-r-- 1 m5stack m5stack 3.2K Oct 20 12:24 run_axmodel.py
-rw-rw-r-- 1 m5stack m5stack 1.3G Oct 20 12:26 text_encoder.axmodel
``

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
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install torch pillow transformers timm torchvision
```

5. 运行

```bash
python run_axmodel.py
```

运行结果：

```bash
(clip) m5stack@raspberrypi:~/rsp/jina-clip-v2 $ python3 run_axmodel.py -i beach1.jpg -t "beautiful sunset over the beach" -iax ./image_encoder.axmodel -tax ./text_encoder.axmodel --hf_path ./jina-clip-v2
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.2 df480136
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.2 27910799
Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
A new version of the following files was downloaded from https://huggingface.co/jinaai/jina-clip-implementation:
- transform.py
. Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.
text -> image: 0.3140323
```