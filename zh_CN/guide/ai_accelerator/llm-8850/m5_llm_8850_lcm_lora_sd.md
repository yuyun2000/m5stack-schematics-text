# lcm-lora-sd

1. [手动下载模型](https://huggingface.co/AXERA-TECH/lcm-lora-sdv1-5) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/lcm-lora-sdv1-5
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/lcm-lora-sdv1-5 $ ls -lh
total 100K
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 11 17:10 asserts
-rw-rw-r-- 1 m5stack m5stack    0 Aug 11 17:09 config.json
-rw-rw-r-- 1 m5stack m5stack 1.2K Aug 11 17:09 Disclaimer.md
-rw-rw-r-- 1 m5stack m5stack 1.5K Aug 11 17:09 LICENSE
drwxrwxr-x 4 m5stack m5stack 4.0K Aug 11 17:14 models
-rw-rw-r-- 1 m5stack m5stack 5.7K Aug 11 17:09 README.md
-rw-rw-r-- 1 m5stack m5stack  117 Aug 11 17:09 requirements.txt
-rw-rw-r-- 1 m5stack m5stack  23K Aug 11 17:09 run_img2img_axe_infer.py
-rw-rw-r-- 1 m5stack m5stack  23K Aug 11 17:09 run_img2img_onnx_infer.py
-rw-rw-r-- 1 m5stack m5stack 7.8K Aug 11 17:09 run_txt2img_axe_infer_new.py
-rw-rw-r-- 1 m5stack m5stack 7.3K Aug 11 17:09 run_txt2img_axe_infer.py
-rw-rw-r-- 1 m5stack m5stack 7.4K Aug 11 17:09 run_txt2img_onnx_infer.py
```

2. 创建虚拟环境

```bash
python -m venv sd
```

3. 激活虚拟环境

```bash
source sd/bin/activate
```

4. 安装依赖包

```bash
sudo apt install cmake -y
pip install -r requirements.txt
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
```

- 文生图

```bash
python run_txt2img_axe_infer.py
```

运行结果：

```bash
(sd) m5stack@raspberrypi:~/rsp/lcm-lora-sdv1-5$ python run_txt2img_axe_infer.py
[INFO] Available providers:  ['AXCLRTExecutionProvider']
prompt: Self-portrait oil painting, a beautiful cyborg with golden hair, 8k
text_tokenizer: ./models/tokenizer
text_encoder: ./models/text_encoder
unet_model: ./models/unet.axmodel
vae_decoder_model: ./models/vae_decoder.axmodel
time_input: ./models/time_input_txt2img.npy
save_dir: ./txt2img_output_axe.png
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.4 9215b7e5
text encoder take 4466.2ms
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 972f38ca
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 972f38ca
load models take 22582.9ms
unet once take 433.6ms
unet once take 433.5ms
unet once take 433.3ms
unet once take 433.5ms
unet loop take 1736.7ms
vae inference take 914.2ms
save image take 254.3ms
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/txt2img_output_axe.png" width="40%" />

- 图生图

```bash
python run_txt2img_axe_infer.py
```

运行结果：

```bash
(sd) m5stack@raspberrypi:~/rsp/lcm-lora-sdv1-5$ python run_txt2img_axe_infer.py
[INFO] Available providers:  ['AXCLRTExecutionProvider']
prompt: Self-portrait oil painting, a beautiful cyborg with golden hair, 8k
text_tokenizer: ./models/tokenizer
text_encoder: ./models/text_encoder
unet_model: ./models/unet.axmodel
vae_decoder_model: ./models/vae_decoder.axmodel
time_input: ./models/time_input_txt2img.npy
save_dir: ./txt2img_output_axe.png
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.4 9215b7e5
text encoder take 2962.1ms
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 972f38ca
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 972f38ca
load models take 14483.6ms
unet once take 433.6ms
unet once take 433.3ms
unet once take 433.2ms
unet once take 433.4ms
unet loop take 1736.4ms
vae inference take 914.0ms
save image take 233.2ms
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/lcm_lora_sdv1-5_imgGrid_output.png" width="60%" />
