# AI Pyramid - CosyVoice2 音色克隆

CosyVoice2 是一个基于大语言模型的高品质语音合成系统，能够合成自然流畅的语音内容。本文档提供一套兼容 OpenAI API 的完整调用方式，用户只需安装相应的 StackFlow 软件包即可快速使用。

## 1. 准备工作

参考 [AI Pyramid 软件包更新](/zh_CN/stackflow/ai_pyramid/software_update)，完成以下依赖包和模型的安装：

```bash
apt update
```

安装核心依赖包：

```bash
apt install lib-llm llm-sys llm-cosy-voice llm-openai-api
```

安装 CosyVoice2 模型：

```bash
apt install llm-model-cosyvoice2-0.5b-ax650
```

?> 模型更新提示 | 每次安装新模型后，需要手动执行 `systemctl restart llm-openai-api` 命令以更新模型列表。

?> 性能说明 | CosyVoice2 是一个高性能的神经网络语音生成模型，虽然能够合成自然流畅的语音，但在资源有限的设备上会有以下限制：最大生成音频长度为 27 秒，首次加载模型可能需要较长时间。请根据应用场景合理调整音频长度预期。

## 2. 基础调用示例

### 使用 Curl 调用

```bash
curl http://127.0.0.1:8000/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "CosyVoice2-0.5B-ax650",
    "response_format": "wav",
    "input": "君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。"
  }' \
  -o output.wav
```

### 使用 Python 调用

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key="sk-",
    base_url="http://127.0.0.1:8000/v1"
)

speech_file_path = Path(__file__).parent / "output.wav"
with client.audio.speech.with_streaming_response.create(
  model="CosyVoice2-0.5B-ax650",
  voice="prompt_data",
  response_format="wav",
  input='君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。',
) as response:
  response.stream_to_file(speech_file_path)
```

## 3. 音色克隆

### 3.1 获取克隆脚本

选择以下任一方式获取 CosyVoice2 克隆脚本：

**方式一：手动下载**

访问 [CosyVoice2 脚本仓库](https://huggingface.co/M5Stack/CosyVoice2-scripts) 下载，随后上传到 AI Pyramid 设备。

**方式二：命令行克隆**

?> 依赖检查 | 若系统未安装 **git lfs**，请参考 [git lfs 安装指南](./install_git_lfs) 进行安装。

```bash
git clone --recurse-submodules https://huggingface.co/M5Stack/CosyVoice2-scripts
```

### 3.2 目录结构说明

克隆完成后，目录结构如下：

```bash
root@m5stack-AI-Pyramid:~/CosyVoice2-scripts# ls -lh
total 28K
drwxr-xr-x 2 root root 4.0K Jan  9 10:26 asset
drwxr-xr-x 2 root root 4.0K Jan  9 10:26 CosyVoice-BlankEN
drwxr-xr-x 2 root root 4.0K Jan  9 10:27 frontend-onnx
drwxr-xr-x 3 root root 4.0K Jan  9 10:26 pengzhendong
-rw-r--r-- 1 root root   24 Jan  9 10:26 README.md
-rw-r--r-- 1 root root  103 Jan  9 10:26 requirements.txt
drwxr-xr-x 3 root root 4.0K Jan  9 10:26 scripts
```

### 3.3 处理音频样本

#### 步骤 1：创建虚拟环境

进入 CosyVoice2-scripts 目录。

```bash
cd CosyVoice2-scripts/
```

?> 初次操作 | 首次创建 Python 虚拟环境需执行 `apt install python3.10-venv`。

```bash
python3 -m venv cosyvoice
```

#### 步骤 2：激活虚拟环境

```bash
source cosyvoice/bin/activate
```

#### 步骤 3：安装依赖包

```bash
pip3 install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
```

```bash
pip install -r requirements.txt
```

#### 步骤 4：运行处理脚本

执行音色处理脚本，生成音色特征文件：

```bash
python3 scripts/process_prompt.py --prompt_text asset/zh_woman1.txt --prompt_speech asset/zh_woman1.wav --output zh_woman1
```

脚本执行成功示例输出：

```bash
(cosyvoice) root@m5stack-AI-Pyramid:~/CosyVoice2-scripts# python3 scripts/process_prompt.py --prompt_text asset/zh_woman1.txt --prompt_speech asset/zh_woman1.wav --output zh_woman1
2026-01-09 10:41:18.655905428 [W:onnxruntime:Default, device_discovery.cc:164 DiscoverDevicesForPlatform] GPU device discovery failed: device_discovery.cc:89 ReadFileContents Failed to open file: "/sys/class/drm/card1/device/vendor"
prompt_text 希望你以后能够做的比我还好呦。
fmax 8000
prompt speech token size: torch.Size([1, 87])
```

### 3.4 部署音色到模型目录

将处理好的音色特征文件复制到模型数据目录：

```bash
cp -r zh_woman1 /opt/m5stack/data/CosyVoice2-0.5B-ax650/
```

重启模型服务以加载新的音色配置：

```bash
systemctl restart llm-sys
```

?> 音色替换说明 | 若要替换默认克隆音色，修改 `/opt/m5stack/data/models/mode_CosyVoice2-0.5B-ax650.json` 文件中的 `prompt_dir` 字段为新的音色目录即可。每次替换音色后需要重新初始化模型服务。

## 4. 使用克隆音色调用

### 使用 Curl 调用

```bash
curl http://127.0.0.1:8000/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "CosyVoice2-0.5B-ax650",
    "voice": "zh_woman1",
    "response_format": "wav",
    "input": "君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。"
  }' \
  -o output.wav
```

### 使用 Python 调用

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key="sk-",
    base_url="http://127.0.0.1:8000/v1"
)

speech_file_path = Path(__file__).parent / "output.wav"
with client.audio.speech.with_streaming_response.create(
  model="CosyVoice2-0.5B-ax650",
  voice="zh_woman1",
  response_format="wav",
  input='君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。',
) as response:
  response.stream_to_file(speech_file_path)
```

### 案例演示

运行案例需要安装 Open Ai 依赖库和重启 Ollama 服务。

```python
pip3 install openai
```

```python
systemctl restart llm-*
```

```python
# main.py

from pathlib import Path
from openai import OpenAI
import subprocess


def main():
    # Initialize the OpenAI client
    client = OpenAI(
        api_key="sk-",  # Replace with your actual API key
        base_url="http://127.0.0.1:8000/v1"
    )

    # Temporary file paths
    base_dir = Path(__file__).parent
    raw_audio_path = base_dir / "temp_raw.wav"
    transcoded_audio_path = base_dir / "temp_48k_stereo.wav"

    print("=== Interactive Speech Synthesis Mode ===")
    print("Enter text and press Enter to generate speech.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        # 1. Read user input
        input_text = input("Enter text (quit/exit to stop): ").strip()

        # Exit condition
        if input_text.lower() in ["quit", "exit"]:
            print("Exiting program...")
            break

        if not input_text:
            print("Error: Input text cannot be empty.\n")
            continue

        try:
            # 2. Generate raw audio from the TTS API
            print("Generating speech...")
            with client.audio.speech.with_streaming_response.create(
                model="CosyVoice2-0.5B-ax650",
                voice="zh_woman1",
                response_format="wav",
                input=input_text,
            ) as response:
                response.stream_to_file(raw_audio_path)

            # 3. Transcode to 48 kHz stereo WAV using FFmpeg
            print("Transcoding audio...")
            ffmpeg_cmd = [
                "ffmpeg",
                "-y",                    # Overwrite output file if it exists
                "-i", str(raw_audio_path),
                "-ar", "48000",          # Set sample rate to 48 kHz
                "-ac", "2",              # Set channel count to stereo
                "-f", "wav",
                str(transcoded_audio_path)
            ]

            # Run transcoding
            # Remove stdout/stderr redirection if you need FFmpeg logs for debugging
            subprocess.run(
                ffmpeg_cmd,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            # 4. Play the transcoded audio with tinyplay
            print("Playing audio...\n")
            tinyplay_cmd = ["tinyplay", str(transcoded_audio_path)]
            subprocess.run(tinyplay_cmd, check=True)

        except subprocess.CalledProcessError as e:
            print(
                f"Command execution failed. Please make sure FFmpeg and tinyplay "
                f"are installed and available in PATH: {e}\n"
            )
        except Exception as e:
            print(f"An error occurred: {e}\n")
        finally:
            # Remove temporary files
            raw_audio_path.unlink(missing_ok=True)
            transcoded_audio_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
```
