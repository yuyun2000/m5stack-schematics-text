# AI Pyramid - Sherpa-ONNX 语音识别

[Sherpa-ONNX](https://github.com/k2-fsa/sherpa-onnx) 是一个基于 ONNX Runtime 的轻量级语音识别和处理工具箱，专注于在本地设备上实现高性能、低延迟的流式与离线语音识别。该项目已完整支持 AI Pyramid 作为推理后端，并可充分利用 NPU 加速能力。详见 [官方文档](https://k2-fsa.github.io/sherpa/onnx/index.html)。

## 1. 获取模型文件

选择以下任一方式获取语音识别模型：

**方式一：手动下载**

访问 [SenseVoice 模型仓库](https://huggingface.co/M5Stack/SenseVoiceSmall-axmodel) 进行下载，随后上传到 AI Pyramid 设备。

**方式二：命令行克隆**

?> 依赖检查 | 若系统未安装 **git lfs**，请参考 [git lfs 安装指南](./install_git_lfs) 进行安装。

```bash
git clone https://huggingface.co/M5Stack/SenseVoiceSmall-axmodel
```

### 1.1 模型文件说明

克隆完成后，目录结构如下：

```bash
root@m5stack-AI-Pyramid:~/SenseVoiceSmall-axmodel# ls -lh
total 328K
drwxr-xr-x 2 root root 4.0K Jan  9 17:27 ax630c
drwxr-xr-x 2 root root 4.0K Jan  9 17:27 ax650
-rw-r--r-- 1 root root   24 Jan  9 17:27 README.md
drwxr-xr-x 2 root root 4.0K Jan  9 17:27 test_wavs
-rw-r--r-- 1 root root 309K Jan  9 17:27 tokens.txt
```

## 2. 获取预编译程序

下载 Sherpa-ONNX 的预编译二进制文件：

**方式一：手动下载**

访问 [Sherpa-ONNX Release 页面](https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.20/sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared.tar.bz2) 下载。

**方式二：命令行下载**

```bash
wget https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.20/sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared.tar.bz2
```

### 2.1 解压文件

```bash
tar xvf sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared.tar.bz2
rm sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared.tar.bz2
```

### 2.2 可执行程序说明

解压后的 bin 目录包含多个预编译程序，主要文件如下：

```bash
root@m5stack-AI-Pyramid:~/SenseVoiceSmall-axmodel# ls -lh sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/
total 42M
-rwxr-xr-x 1 1001 1001 1.8M Dec 17 21:10 sherpa-onnx
-rwxr-xr-x 1 1001 1001 1.8M Dec 17 21:10 sherpa-onnx-alsa
-rwxr-xr-x 1 1001 1001 1.7M Dec 17 21:10 sherpa-onnx-alsa-offline
-rwxr-xr-x 1 1001 1001 1.9M Dec 17 21:10 sherpa-onnx-microphone
-rwxr-xr-x 1 1001 1001 1.9M Dec 17 21:10 sherpa-onnx-microphone-offline
-rwxr-xr-x 1 1001 1001 1.7M Dec 17 21:10 sherpa-onnx-offline
-rwxr-xr-x 1 1001 1001 1.8M Dec 17 21:10 sherpa-onnx-vad-with-offline-asr
-rwxr-xr-x 1 1001 1001 1.8M Dec 17 21:10 sherpa-onnx-vad-alsa-offline-asr
...
```

## 3. 语音识别示例

### 3.1 离线文件识别

执行以下命令对单个音频文件进行识别：

```bash
./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-offline --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera test_wavs/en.wav
```

识别结果示例：

```bash
root@m5stack-AI-Pyramid:~/SenseVoiceSmall-axmodel# ./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-offline --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera test_wavs/en.wav
/k2-fsa/sherpa-onnx/sherpa-onnx/csrc/parse-options.cc:Read:373 ./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-offline --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera test_wavs/en.wav 

OfflineRecognizerConfig(feat_config=FeatureExtractorConfig(sampling_rate=16000, feature_dim=80, low_freq=20, high_freq=-400, dither=0, normalize_samples=True, snip_edges=False), model_config=OfflineModelConfig(transducer=OfflineTransducerModelConfig(encoder_filename="", decoder_filename="", joiner_filename=""), paraformer=OfflineParaformerModelConfig(model=""), nemo_ctc=OfflineNemoEncDecCtcModelConfig(model=""), whisper=OfflineWhisperModelConfig(encoder="", decoder="", language="", task="transcribe", tail_paddings=-1), fire_red_asr=OfflineFireRedAsrModelConfig(encoder="", decoder=""), tdnn=OfflineTdnnModelConfig(model=""), zipformer_ctc=OfflineZipformerCtcModelConfig(model=""), wenet_ctc=OfflineWenetCtcModelConfig(model=""), sense_voice=OfflineSenseVoiceModelConfig(model="ax650/model-10-seconds.axmodel", language="auto", use_itn=False), moonshine=OfflineMoonshineModelConfig(preprocessor="", encoder="", uncached_decoder="", cached_decoder=""), dolphin=OfflineDolphinModelConfig(model=""), canary=OfflineCanaryModelConfig(encoder="", decoder="", src_lang="", tgt_lang="", use_pnc=True), omnilingual=OfflineOmnilingualAsrCtcModelConfig(model=""), telespeech_ctc="", tokens="tokens.txt", num_threads=2, debug=False, provider="axera", model_type="", modeling_unit="cjkchar", bpe_vocab=""), lm_config=OfflineLMConfig(model="", scale=0.5, lodr_scale=0.01, lodr_fst="", lodr_backoff_id=-1), ctc_fst_decoder_config=OfflineCtcFstDecoderConfig(graph="", max_active=3000), decoding_method="greedy_search", max_active_paths=4, hotwords_file="", hotwords_score=1.5, blank_penalty=0, rule_fsts="", rule_fars="", hr=HomophoneReplacerConfig(lexicon="", rule_fsts=""))
Creating recognizer ...
recognizer created in 1.128 s
Started
Done!

test_wavs/en.wav
{"lang": "<|en|>", "emotion": "<|EMO_UNKNOWN|>", "event": "<|Speech|>", "text": "the tribal chieftain called for the boy and presented him with fifty pieces of gold", "timestamps": [0.90, 1.26, 1.56, 1.80, 2.16, 2.46, 2.76, 2.94, 3.12, 3.60, 3.96, 4.50, 4.74, 5.10, 5.52, 5.88, 6.24], "durations": [], "tokens":["the", " tri", "bal", " chief", "tain", " called", " for", " the", " boy", " and", " presented", " him", " with", " fifty", " pieces", " of", " gold"], "ys_log_probs": [], "words": []}
----
num threads: 2
decoding method: greedy_search
Elapsed seconds: 0.119 s
Real time factor (RTF): 0.119 / 7.152 = 0.017
```

### 3.2 带 VAD 的长音频分段识别

对较长的音频文件进行分段识别需要先获取 VAD（语音活动检测）模型。

**获取 VAD 模型**

```bash
wget https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/silero_vad.onnx
```

**获取测试音频**（或使用本地音频文件）

```bash
wget https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/Obama.wav
```

**执行长音频识别**

```bash
./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-vad-with-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera Obama.wav
```

识别结果示例：

```bash
root@m5stack-AI-Pyramid:~/SenseVoiceSmall-axmodel# ./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-vad-with-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera Obama.wav

/k2-fsa/sherpa-onnx/sherpa-onnx/csrc/parse-options.cc:Read:373 ./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-vad-with-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera Obama.wav 

VadModelConfig(silero_vad=SileroVadModelConfig(model="silero_vad.onnx", threshold=0.5, min_silence_duration=0.5, min_speech_duration=0.25, max_speech_duration=20, window_size=512, neg_threshold=-1), ten_vad=TenVadModelConfig(model="", threshold=0.5, min_silence_duration=0.5, min_speech_duration=0.25, max_speech_duration=20, window_size=256), sample_rate=16000, num_threads=1, provider="cpu", debug=False)
OfflineRecognizerConfig(feat_config=FeatureExtractorConfig(sampling_rate=16000, feature_dim=80, low_freq=20, high_freq=-400, dither=0, normalize_samples=True, snip_edges=False), model_config=OfflineModelConfig(transducer=OfflineTransducerModelConfig(encoder_filename="", decoder_filename="", joiner_filename=""), paraformer=OfflineParaformerModelConfig(model=""), nemo_ctc=OfflineNemoEncDecCtcModelConfig(model=""), whisper=OfflineWhisperModelConfig(encoder="", decoder="", language="", task="transcribe", tail_paddings=-1), fire_red_asr=OfflineFireRedAsrModelConfig(encoder="", decoder=""), tdnn=OfflineTdnnModelConfig(model=""), zipformer_ctc=OfflineZipformerCtcModelConfig(model=""), wenet_ctc=OfflineWenetCtcModelConfig(model=""), sense_voice=OfflineSenseVoiceModelConfig(model="ax650/model-10-seconds.axmodel", language="auto", use_itn=False), moonshine=OfflineMoonshineModelConfig(preprocessor="", encoder="", uncached_decoder="", cached_decoder=""), dolphin=OfflineDolphinModelConfig(model=""), canary=OfflineCanaryModelConfig(encoder="", decoder="", src_lang="", tgt_lang="", use_pnc=True), omnilingual=OfflineOmnilingualAsrCtcModelConfig(model=""), telespeech_ctc="", tokens="tokens.txt", num_threads=2, debug=False, provider="axera", model_type="", modeling_unit="cjkchar", bpe_vocab=""), lm_config=OfflineLMConfig(model="", scale=0.5, lodr_scale=0.01, lodr_fst="", lodr_backoff_id=-1), ctc_fst_decoder_config=OfflineCtcFstDecoderConfig(graph="", max_active=3000), decoding_method="greedy_search", max_active_paths=4, hotwords_file="", hotwords_score=1.5, blank_penalty=0, rule_fsts="", rule_fars="", hr=HomophoneReplacerConfig(lexicon="", rule_fsts=""))
Creating recognizer ...
Recognizer created!
Started
Reading: Obama.wav
Started!
9.286 -- 12.428: everybody all right everybody go ahead and have a seat
13.094 -- 14.988: how's everybody doing today
18.694 -- 20.748: how about tim spicer
25.894 -- 31.948: i am here with students at wakefield high school in arlington virginia
...
297.318 -- 314.284: you want to be a doctor or a teacher or a police officer you want to be a nurse or an architect a lawyer or a member of our military you're going to need a good education
315.174 -- 319.852: you've got to train for it and work for it and learn for it
320.518 -- 323.660: and this isn't just important for your own life and your own future
324.678 -- 333.004: what you make of your education will decide nothing less than the future of this country the future of america depends on you
num threads: 2
decoding method: greedy_search
Elapsed seconds: 23.002 s
Real time factor (RTF): 23.002 / 334.234 = 0.069
```

## 4. 麦克风实时识别

### 4.1 硬件要求

?> 硬件提示 | Sherpa-ONNX 提供的官方例程目前暂不支持 AI Pyramid 上的四通道内置麦克风，需要外接 USB 麦克风或其他兼容的音频输入设备。

### 4.2 获取麦克风设备列表

执行以下命令查看系统中可用的音频设备：

```bash
aplay -l
```

设备列表示例：

```bash
root@m5stack-AI-Pyramid:~/SenseVoiceSmall-axmodel# aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: Audio [Axera Audio], device 0: 2033000.i2s_mst-ES8311 HiFi es8311.0-0018-0 [2033000.i2s_mst-ES8311 HiFi es8311.0-0018-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Audio_1 [Axera Hdmi Audio], device 0: 10070000.i2s_mst-i2s-hifi i2s-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 2: Audio_2 [Axera Hdmi Audio], device 0: 10071000.i2s_mst-i2s-hifi i2s-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 3: Audio_3 [AB13X USB Audio], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

### 4.3 启动实时识别

执行以下命令开启麦克风实时识别（请根据实际情况修改麦克风设备名）：

```bash
./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-vad-alsa-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera plughw:3,0
```

?> 设备选择 | 将 `plughw:3,0` 替换为您实际使用的音频设备标识符。

实时识别结果示例：

```bash
root@m5stack-AI-Pyramid:~/SenseVoiceSmall-axmodel# ./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-vad-alsa-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera plughw:3,0
/k2-fsa/sherpa-onnx/sherpa-onnx/csrc/parse-options.cc:Read:373 ./sherpa-onnx-v1.12.20-axera-ax650-linux-aarch64-shared/bin/sherpa-onnx-vad-alsa-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axera plughw:3,0 

VadModelConfig(silero_vad=SileroVadModelConfig(model="silero_vad.onnx", threshold=0.5, min_silence_duration=0.5, min_speech_duration=0.25, max_speech_duration=20, window_size=512, neg_threshold=-1), ten_vad=TenVadModelConfig(model="", threshold=0.5, min_silence_duration=0.5, min_speech_duration=0.25, max_speech_duration=20, window_size=256), sample_rate=16000, num_threads=1, provider="cpu", debug=False)
OfflineRecognizerConfig(feat_config=FeatureExtractorConfig(sampling_rate=16000, feature_dim=80, low_freq=20, high_freq=-400, dither=0, normalize_samples=True, snip_edges=False), model_config=OfflineModelConfig(transducer=OfflineTransducerModelConfig(encoder_filename="", decoder_filename="", joiner_filename=""), paraformer=OfflineParaformerModelConfig(model=""), nemo_ctc=OfflineNemoEncDecCtcModelConfig(model=""), whisper=OfflineWhisperModelConfig(encoder="", decoder="", language="", task="transcribe", tail_paddings=-1), fire_red_asr=OfflineFireRedAsrModelConfig(encoder="", decoder=""), tdnn=OfflineTdnnModelConfig(model=""), zipformer_ctc=OfflineZipformerCtcModelConfig(model=""), wenet_ctc=OfflineWenetCtcModelConfig(model=""), sense_voice=OfflineSenseVoiceModelConfig(model="ax650/model-10-seconds.axmodel", language="auto", use_itn=False), moonshine=OfflineMoonshineModelConfig(preprocessor="", encoder="", uncached_decoder="", cached_decoder=""), dolphin=OfflineDolphinModelConfig(model=""), canary=OfflineCanaryModelConfig(encoder="", decoder="", src_lang="", tgt_lang="", use_pnc=True), omnilingual=OfflineOmnilingualAsrCtcModelConfig(model=""), telespeech_ctc="", tokens="tokens.txt", num_threads=2, debug=False, provider="axera", model_type="", modeling_unit="cjkchar", bpe_vocab=""), lm_config=OfflineLMConfig(model="", scale=0.5, lodr_scale=0.01, lodr_fst="", lodr_backoff_id=-1), ctc_fst_decoder_config=OfflineCtcFstDecoderConfig(graph="", max_active=3000), decoding_method="greedy_search", max_active_paths=4, hotwords_file="", hotwords_score=1.5, blank_penalty=0, rule_fsts="", rule_fars="", hr=HomophoneReplacerConfig(lexicon="", rule_fsts=""))
Creating recognizer ...
Recognizer created!
Current sample rate: 16000
Recording started!
Use recording device: plughw:3,0
Started. Please speak
 0: hello
 1: how are you
^C
Caught Ctrl + C. Exiting...
```