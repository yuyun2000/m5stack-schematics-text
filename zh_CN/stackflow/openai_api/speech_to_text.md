# 语音转文本

通过API接口实现输入语音转换输出文本。

## 准备工作

案例程序执行前需在设备中安装对应的model模型包。模型包安装教程可参考[模型列表](/zh_CN/stackflow/openai_api/models)章节。模型详细介绍参考[模型介绍](/zh_CN/stackflow/models/list)章节。

在运行本示例程序之前，请确保已在 LLM 设备上完成以下准备工作：

1. 使用 apt 包管理工具安装 **SenseVoice** 模型包。

```bash
apt install llm-model-sense-voice-small-10s-ax650
```

2. 安装 `ffmpeg` 工具。

```bash
apt install ffmpeg
```

3. 安装完成后，重启 OpenAI 服务以使新模型生效。

```bash
systemctl restart llm-openai-api
```


## 案例程序

在 PC 端通过 OpenAI API 传入音频文件实现语音转换文本功能，案例程序执行前将下方 `base_url` 的IP部分修改为设备实际IP地址。


```python
from openai import OpenAI
client = OpenAI(
    api_key="sk-",
    base_url="http://192.168.20.186:8000/v1"
)

audio_file = open("speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="sense-voice-small-10s-ax650",
  file=audio_file
)

print(transcript)
```


## 请求参数


| 参数名称        | 类型   | 必选 | 示例值       | 描述                                                                                           |
| --------------- | ------ | ---- | ------------ | ---------------------------------------------------------------------------------------------- |
| file            | file   | 是   | -            | 要转录的音频文件对象（非文件名），支持格式包括 flac、mp3、mp4、mpeg、mpga、m4a、ogg、wav、webm |
| model           | string | 是   | sense-voice-small-10s-ax650 | SenseVoice 模型支持中英日粤韩等多语言自动识别 |
| language        | string | 否   | -           | 模型内部自动识别语言 |
| response_format | string | 否   | json         | 返回格式，目前仅支持 `json`，默认值为 `json`                                                   |



## 返回示例


```bash
Transcription(text=' Thank you. Thank you everybody. All right everybody go ahead and have a seat. How\'s everybody doing today? .....', 
logprobs=None, task='transcribe', language='en', duration=334.234, segments=12, sample_rate=16000, channels=1, bit_depth=16)
```
