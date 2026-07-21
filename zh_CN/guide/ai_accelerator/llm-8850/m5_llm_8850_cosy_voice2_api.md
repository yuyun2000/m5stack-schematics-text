# CosyVoice2-API

我们提供一套兼容 OpenAI API 的使用方式，只需要安装 StackFlow 包即可。

## 准备工作

1. 参考[RaspberryPi & LLM8850 软件包获取教程](/zh_CN/stackflow/raspberrypi/software)，完成以下模型包和软件包的安装。

```bash
sudo apt install lib-llm llm-sys llm-cosy-voice llm-openai-api
```

```bash
sudo apt install llm-model-cosyvoice2-0.5b-axcl
```

?> 注意 |每次安装新模型后，需要手动执行 **sudo systemctl restart llm-openai-api** 更新模型列表。

?> 注意 | CosyVoice2 是一个基于 LLM 的语音生成模型，能够合成自然流畅的语音，但由于资源或设计限制，每次生成的音频长度有限。当前版本生成的音频最大长度为 27s，第一次加载模型较慢，请耐心等待。

## Curl 调用

```bash
curl http://127.0.0.1:8000/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "CosyVoice2-0.5B-axcl",
    "response_format": "wav",
    "input": "君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。"
  }' \
  -o output.wav
```

## Python 调用

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key="sk-",
    base_url="http://127.0.0.1:8000/v1"
)

speech_file_path = Path(__file__).parent / "output.wav"
with client.audio.speech.with_streaming_response.create(
  model="CosyVoice2-0.5B-axcl",
  voice="prompt_data",
  response_format="wav",
  input='君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。',
) as response:
  response.stream_to_file(speech_file_path)
```

## 音色克隆

1. [手动下载模型](https://huggingface.co/M5Stack/CosyVoice2-scripts) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone --recurse-submodules https://huggingface.co/M5Stack/CosyVoice2-scripts
```

**文件说明**

```bash
m5stack@raspberrypi:~/rsp/CosyVoice2-scripts $ ls -lh
total 28K
drwxrwxr-x 2 m5stack m5stack 4.0K Nov  6 15:18 asset
drwxrwxr-x 2 m5stack m5stack 4.0K Nov  6 15:18 CosyVoice-BlankEN
drwxrwxr-x 2 m5stack m5stack 4.0K Nov  6 15:19 frontend-onnx
drwxrwxr-x 3 m5stack m5stack 4.0K Nov  6 15:18 pengzhendong
-rw-rw-r-- 1 m5stack m5stack   24 Nov  6 15:18 README.md
-rw-rw-r-- 1 m5stack m5stack  103 Nov  6 15:18 requirements.txt
drwxrwxr-x 3 m5stack m5stack 4.0K Nov  6 15:18 scripts
```

2. 创建虚拟环境

```bash
python -m venv cosyvoice
```

3. 激活虚拟环境

```bash
source cosyvoice/bin/activate
```

4. 安装依赖包

```bash
pip install -r requirements.txt
``` 

5. 运行 process_prompt 脚本

```bash
python3 scripts/process_prompt.py --prompt_text  asset/zh_woman1.txt --prompt_speech asset/zh_woman1.wav --output zh_woman1
```

成功生成音频特征文件

```bash
(cosyvoice) m5stack@raspberrypi:~/rsp/CosyVoice2-scripts $ python3 scripts/process_prompt.py --prompt_text  asset/zh_woman1.txt --prompt_speech asset/zh_woman1.wav --output zh_woman1
2025-11-06 15:54:43.619688866 [W:onnxruntime:Default, device_discovery.cc:164 DiscoverDevicesForPlatform] GPU device discovery failed: device_discovery.cc:89 ReadFileContents Failed to open file: "/sys/class/drm/card1/device/vendor"
prompt_text 希望你以后能够做的比我还好呦。
fmax 8000
prompt speech token size: torch.Size([1, 87])
```

6. 复制 'zh_woman1' 文件到模型目录，并重新初始化模型。

```bash
cp -r zh_woman1 /opt/m5stack/data/CosyVoice2-0.5B-axcl/
```

```bash
sudo systemctl restart llm-sys # 重置模型配置
```

?> 提示 | 如果想替换默认克隆音色，修改 **/opt/m5stack/data/models/mode_CosyVoice2-0.5B-axcl.json** 文件中的 **prompt_dir** 字段为替换的目录即可。每次替换音色需要重新初始化模型。

## Curl 调用

```bash
curl http://127.0.0.1:8000/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "CosyVoice2-0.5B-axcl",
    "voice": "zh_woman1",
    "response_format": "wav",
    "input": "君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。"
  }' \
  -o output.wav
```

## Python 调用

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key="sk-",
    base_url="http://127.0.0.1:8000/v1"
)

speech_file_path = Path(__file__).parent / "output.wav"
with client.audio.speech.with_streaming_response.create(
  model="CosyVoice2-0.5B-axcl",
  voice="zh_woman1",
  response_format="wav",
  input='君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。',
) as response:
  response.stream_to_file(speech_file_path)
```