# 文本转语音

通过 API 接口实现输入文本转换输出语音文件。

## 准备工作

案例程序执行前需在设备中安装对应的 model 模型包。模型包安装教程可参考[模型列表](/zh_CN/stackflow/openai_api/models)章节。模型详细介绍参考[模型介绍](/zh_CN/stackflow/models/list)章节。

#> 提示 | AI Pyramid 有专属的带音色克隆的文本转语音，可参考 [CosyVoice](/zh_CN/stackflow/ai_pyramid/cosy_voice) 章节。

在运行本示例程序之前，请确保已在 LLM 设备上完成以下准备工作：

1. 使用 apt 包管理工具安装 `llm-model-melotts-en-us` 模型包。

```bash
apt install llm-model-melotts-en-us
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

在 PC 端通过 OpenAI API 传入文本信息实现文本转换语音功能，案例程序执行前将下方`base_url`的 IP 部分修改为设备实际 IP 地址。

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key="sk-",
    base_url="http://192.168.20.186:8000/v1"
)

speech_file_path = Path(__file__).parent / "speech.mp3"
with client.audio.speech.with_streaming_response.create(
  model="melotts-en-us",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
) as response:
  response.stream_to_file(speech_file_path)
```

## 请求参数

| 参数名称        | 类型   | 必选 | 示例值               | 描述                                                                     |
| --------------- | ------ | ---- | -------------------- | ------------------------------------------------------------------------ |
| input           | string | 是   | "你好，欢迎使用系统" | 要生成音频的文本内容，最大长度为 1024 个字符                             |
| model           | string | 是   | melotts-zh-cn        | 可用的 TTS 模型，包括 `melotts-ja-jp`、`melotts-zh-cn` 和 `melotts-en-us` 等|
| voice           | -      | 否   | -                    | MeloTTS 模型不支持语音风格选择                                                   |
| response_format | string | 否   | mp3                  | 音频输出格式，支持 `mp3`, `opus`, `aac`, `flac`, `wav`, `pcm` 等         |
| speed           | number | 否   | 1.0                  | 生成语音的速度，范围为 0.25 ~ 2.0，默认值为 1.0                          |

## 返回示例

- 语音文件数据将会存放至示例程序中的 `speech_file_path` 路径下。
