# sherpa-onnx

[sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) 是一个基于 ONNX Runtime 的轻量级语音识别/语音处理工具箱，专注于在本地设备上实现高性能、低延迟的流式与离线识别。目前已经支持 LLM8850 作为推理后端。且支持 NPU 加速。[官方文档](https://k2-fsa.github.io/sherpa/onnx/index.html)

1. [手动下载模型](https://huggingface.co/M5Stack/SenseVoiceSmall-axmodel) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/M5Stack/SenseVoiceSmall-axmodel
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/SenseVoiceSmall-axmodel $ ls -lh
total 328K
drwxrwxr-x 2 m5stack m5stack 4.0K Dec  9 11:55 ax630c
drwxrwxr-x 2 m5stack m5stack 4.0K Dec  9 11:55 ax650
-rw-rw-r-- 1 m5stack m5stack   24 Dec  9 11:54 README.md
drwxrwxr-x 2 m5stack m5stack 4.0K Dec  9 11:54 test_wavs
-rw-rw-r-- 1 m5stack m5stack 309K Dec  9 11:54 tokens.txt
```

2. 获取预编译程序 [手动下载链接](https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.19/sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared.tar.bz2)

```bash
wget https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.19/sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared.tar.bz2
```

```bash
tar xvf sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared.tar.bz2
rm sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared.tar.bz2
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/SenseVoiceSmall-axmodel $ ls -lh sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/
total 47M
-rwxr-xr-x 1 m5stack m5stack 1.9M Dec  8 12:04 sherpa-onnx
-rwxr-xr-x 1 m5stack m5stack 1.9M Dec  8 12:04 sherpa-onnx-alsa
-rwxr-xr-x 1 m5stack m5stack 1.9M Dec  8 12:04 sherpa-onnx-alsa-offline
-rwxr-xr-x 1 m5stack m5stack 389K Dec  8 12:04 sherpa-onnx-alsa-offline-audio-tagging
-rwxr-xr-x 1 m5stack m5stack 453K Dec  8 12:04 sherpa-onnx-alsa-offline-speaker-identification
-rwxr-xr-x 1 m5stack m5stack 710K Dec  8 12:04 sherpa-onnx-keyword-spotter
-rwxr-xr-x 1 m5stack m5stack 710K Dec  8 12:04 sherpa-onnx-keyword-spotter-alsa
-rwxr-xr-x 1 m5stack m5stack 903K Dec  8 12:04 sherpa-onnx-keyword-spotter-microphone
-rwxr-xr-x 1 m5stack m5stack 2.1M Dec  8 12:04 sherpa-onnx-microphone
-rwxr-xr-x 1 m5stack m5stack 2.1M Dec  8 12:04 sherpa-onnx-microphone-offline
-rwxr-xr-x 1 m5stack m5stack 582K Dec  8 12:04 sherpa-onnx-microphone-offline-audio-tagging
-rwxr-xr-x 1 m5stack m5stack 582K Dec  8 12:04 sherpa-onnx-microphone-offline-speaker-identification
-rwxr-xr-x 1 m5stack m5stack 1.9M Dec  8 12:04 sherpa-onnx-offline
-rwxr-xr-x 1 m5stack m5stack 389K Dec  8 12:04 sherpa-onnx-offline-audio-tagging
-rwxr-xr-x 1 m5stack m5stack 389K Dec  8 12:04 sherpa-onnx-offline-denoiser
-rwxr-xr-x 1 m5stack m5stack 389K Dec  8 12:04 sherpa-onnx-offline-language-identification
-rwxr-xr-x 1 m5stack m5stack 1.9M Dec  8 12:04 sherpa-onnx-offline-parallel
-rwxr-xr-x 1 m5stack m5stack 325K Dec  8 12:04 sherpa-onnx-offline-punctuation
-rwxr-xr-x 1 m5stack m5stack 389K Dec  8 12:04 sherpa-onnx-offline-source-separation
-rwxr-xr-x 1 m5stack m5stack 517K Dec  8 12:04 sherpa-onnx-offline-speaker-diarization
-rwxr-xr-x 1 m5stack m5stack 2.4M Dec  8 12:04 sherpa-onnx-offline-tts
-rwxr-xr-x 1 m5stack m5stack 2.6M Dec  8 12:04 sherpa-onnx-offline-tts-play
-rwxr-xr-x 1 m5stack m5stack 2.4M Dec  8 12:04 sherpa-onnx-offline-tts-play-alsa
-rwxr-xr-x 1 m5stack m5stack 2.2M Dec  8 12:04 sherpa-onnx-offline-websocket-server
-rwxr-xr-x 1 m5stack m5stack 2.4M Dec  8 12:04 sherpa-onnx-offline-zeroshot-tts
-rwxr-xr-x 1 m5stack m5stack 389K Dec  8 12:04 sherpa-onnx-online-punctuation
-rwxr-xr-x 1 m5stack m5stack 645K Dec  8 12:04 sherpa-onnx-online-websocket-client
-rwxr-xr-x 1 m5stack m5stack 2.2M Dec  8 12:04 sherpa-onnx-online-websocket-server
-rwxr-xr-x 1 m5stack m5stack 261K Dec  8 12:04 sherpa-onnx-pa-devs
-rwxr-xr-x 1 m5stack m5stack 389K Dec  8 12:04 sherpa-onnx-vad
-rwxr-xr-x 1 m5stack m5stack 389K Dec  8 12:04 sherpa-onnx-vad-alsa
-rwxr-xr-x 1 m5stack m5stack 1.9M Dec  8 12:04 sherpa-onnx-vad-alsa-offline-asr
-rwxr-xr-x 1 m5stack m5stack 582K Dec  8 12:04 sherpa-onnx-vad-microphone
-rwxr-xr-x 1 m5stack m5stack 2.1M Dec  8 12:04 sherpa-onnx-vad-microphone-offline-asr
-rwxr-xr-x 1 m5stack m5stack 2.1M Dec  8 12:04 sherpa-onnx-vad-microphone-simulated-streaming-asr
-rwxr-xr-x 1 m5stack m5stack 2.0M Dec  8 12:04 sherpa-onnx-vad-with-offline-asr
-rwxr-xr-x 1 m5stack m5stack 2.0M Dec  8 12:04 sherpa-onnx-vad-with-online-asr
-rwxr-xr-x 1 m5stack m5stack 195K Dec  8 12:04 sherpa-onnx-version
```

3. 语音文件识别。

```bash
./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-offline --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl test_wavs/en.wav
```

识别结果如下：

```bash
m5stack@raspberrypi:~/rsp/SenseVoiceSmall-axmodel $ ./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-offline --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl test_wavs/en.wav 
/k2-fsa/sherpa-onnx/sherpa-onnx/csrc/parse-options.cc:Read:373 ./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-offline --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl test_wavs/en.wav 

OfflineRecognizerConfig(feat_config=FeatureExtractorConfig(sampling_rate=16000, feature_dim=80, low_freq=20, high_freq=-400, dither=0, normalize_samples=True, snip_edges=False), model_config=OfflineModelConfig(transducer=OfflineTransducerModelConfig(encoder_filename="", decoder_filename="", joiner_filename=""), paraformer=OfflineParaformerModelConfig(model=""), nemo_ctc=OfflineNemoEncDecCtcModelConfig(model=""), whisper=OfflineWhisperModelConfig(encoder="", decoder="", language="", task="transcribe", tail_paddings=-1), fire_red_asr=OfflineFireRedAsrModelConfig(encoder="", decoder=""), tdnn=OfflineTdnnModelConfig(model=""), zipformer_ctc=OfflineZipformerCtcModelConfig(model=""), wenet_ctc=OfflineWenetCtcModelConfig(model=""), sense_voice=OfflineSenseVoiceModelConfig(model="ax650/model-10-seconds.axmodel", language="auto", use_itn=False), moonshine=OfflineMoonshineModelConfig(preprocessor="", encoder="", uncached_decoder="", cached_decoder=""), dolphin=OfflineDolphinModelConfig(model=""), canary=OfflineCanaryModelConfig(encoder="", decoder="", src_lang="", tgt_lang="", use_pnc=True), omnilingual=OfflineOmnilingualAsrCtcModelConfig(model=""), telespeech_ctc="", tokens="tokens.txt", num_threads=2, debug=False, provider="axcl", model_type="", modeling_unit="cjkchar", bpe_vocab=""), lm_config=OfflineLMConfig(model="", scale=0.5, lodr_scale=0.01, lodr_fst="", lodr_backoff_id=-1), ctc_fst_decoder_config=OfflineCtcFstDecoderConfig(graph="", max_active=3000), decoding_method="greedy_search", max_active_paths=4, hotwords_file="", hotwords_score=1.5, blank_penalty=0, rule_fsts="", rule_fars="", hr=HomophoneReplacerConfig(lexicon="", rule_fsts=""))
Creating recognizer ...
recognizer created in 4.263 s
Started
Done!

test_wavs/en.wav
{"lang": "<|en|>", "emotion": "<|EMO_UNKNOWN|>", "event": "<|Speech|>", "text": "the tribal chieftain called for the boy and presented him with fifty pieces of gold", "timestamps": [0.90, 1.26, 1.56, 1.80, 2.16, 2.46, 2.76, 2.94, 3.12, 3.60, 3.96, 4.50, 4.74, 5.10, 5.52, 5.88, 6.24], "durations": [], "tokens":["the", " tri", "bal", " chief", "tain", " called", " for", " the", " boy", " and", " presented", " him", " with", " fifty", " pieces", " of", " gold"], "ys_log_probs": [], "words": []}
----
num threads: 2
decoding method: greedy_search
Elapsed seconds: 0.105 s
Real time factor (RTF): 0.105 / 7.152 = 0.015
```

4. 带 VAD 分段语音文件识别。

获取 VAD 模型

```bash
wget https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/silero_vad.onnx
```

获取长语音文件或自备

```bash
wget https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/Obama.wav
```

开始识别

```bash
./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-vad-with-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl Obama.wav
```

识别结果如下：

```bash
m5stack@raspberrypi:~/rsp/SenseVoiceSmall-axmodel $ ./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-vad-with-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl Obama.wav 
/k2-fsa/sherpa-onnx/sherpa-onnx/csrc/parse-options.cc:Read:373 ./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-vad-with-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl Obama.wav 

VadModelConfig(silero_vad=SileroVadModelConfig(model="silero_vad.onnx", threshold=0.5, min_silence_duration=0.5, min_speech_duration=0.25, max_speech_duration=20, window_size=512, neg_threshold=-1), ten_vad=TenVadModelConfig(model="", threshold=0.5, min_silence_duration=0.5, min_speech_duration=0.25, max_speech_duration=20, window_size=256), sample_rate=16000, num_threads=1, provider="cpu", debug=False)
OfflineRecognizerConfig(feat_config=FeatureExtractorConfig(sampling_rate=16000, feature_dim=80, low_freq=20, high_freq=-400, dither=0, normalize_samples=True, snip_edges=False), model_config=OfflineModelConfig(transducer=OfflineTransducerModelConfig(encoder_filename="", decoder_filename="", joiner_filename=""), paraformer=OfflineParaformerModelConfig(model=""), nemo_ctc=OfflineNemoEncDecCtcModelConfig(model=""), whisper=OfflineWhisperModelConfig(encoder="", decoder="", language="", task="transcribe", tail_paddings=-1), fire_red_asr=OfflineFireRedAsrModelConfig(encoder="", decoder=""), tdnn=OfflineTdnnModelConfig(model=""), zipformer_ctc=OfflineZipformerCtcModelConfig(model=""), wenet_ctc=OfflineWenetCtcModelConfig(model=""), sense_voice=OfflineSenseVoiceModelConfig(model="ax650/model-10-seconds.axmodel", language="auto", use_itn=False), moonshine=OfflineMoonshineModelConfig(preprocessor="", encoder="", uncached_decoder="", cached_decoder=""), dolphin=OfflineDolphinModelConfig(model=""), canary=OfflineCanaryModelConfig(encoder="", decoder="", src_lang="", tgt_lang="", use_pnc=True), omnilingual=OfflineOmnilingualAsrCtcModelConfig(model=""), telespeech_ctc="", tokens="tokens.txt", num_threads=2, debug=False, provider="axcl", model_type="", modeling_unit="cjkchar", bpe_vocab=""), lm_config=OfflineLMConfig(model="", scale=0.5, lodr_scale=0.01, lodr_fst="", lodr_backoff_id=-1), ctc_fst_decoder_config=OfflineCtcFstDecoderConfig(graph="", max_active=3000), decoding_method="greedy_search", max_active_paths=4, hotwords_file="", hotwords_score=1.5, blank_penalty=0, rule_fsts="", rule_fars="", hr=HomophoneReplacerConfig(lexicon="", rule_fsts=""))
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
Elapsed seconds: 6.061 s
Real time factor (RTF): 6.061 / 334.234 = 0.018
```

5. 麦克风实时非流式识别。

获取麦克风设备列表

```bash
aplay -l
```

```bash
m5stack@raspberrypi:~/rsp/SenseVoiceSmall-axmodel $ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: vc4hdmi0 [vc4-hdmi-0], device 0: MAI PCM i2s-hifi-0 [MAI PCM i2s-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: vc4hdmi1 [vc4-hdmi-1], device 0: MAI PCM i2s-hifi-0 [MAI PCM i2s-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 2: Audio [AB13X USB Audio], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

开启实时非流式识别

```bash
./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-vad-alsa-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl plughw:2,0 # 注意要替换成实际的麦克风设备名
```

识别结果如下：

```bash
m5stack@raspberrypi:~/rsp/SenseVoiceSmall-axmodel $ ./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-vad-alsa-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl plughw:2,0
/k2-fsa/sherpa-onnx/sherpa-onnx/csrc/parse-options.cc:Read:373 ./sherpa-onnx-v1.12.19-axcl-linux-aarch64-shared/bin/sherpa-onnx-vad-alsa-offline-asr --silero-vad-model=silero_vad.onnx --sense-voice-model=ax650/model-10-seconds.axmodel --tokens=tokens.txt --provider=axcl plughw:2,0 

VadModelConfig(silero_vad=SileroVadModelConfig(model="silero_vad.onnx", threshold=0.5, min_silence_duration=0.5, min_speech_duration=0.25, max_speech_duration=20, window_size=512, neg_threshold=-1), ten_vad=TenVadModelConfig(model="", threshold=0.5, min_silence_duration=0.5, min_speech_duration=0.25, max_speech_duration=20, window_size=256), sample_rate=16000, num_threads=1, provider="cpu", debug=False)
OfflineRecognizerConfig(feat_config=FeatureExtractorConfig(sampling_rate=16000, feature_dim=80, low_freq=20, high_freq=-400, dither=0, normalize_samples=True, snip_edges=False), model_config=OfflineModelConfig(transducer=OfflineTransducerModelConfig(encoder_filename="", decoder_filename="", joiner_filename=""), paraformer=OfflineParaformerModelConfig(model=""), nemo_ctc=OfflineNemoEncDecCtcModelConfig(model=""), whisper=OfflineWhisperModelConfig(encoder="", decoder="", language="", task="transcribe", tail_paddings=-1), fire_red_asr=OfflineFireRedAsrModelConfig(encoder="", decoder=""), tdnn=OfflineTdnnModelConfig(model=""), zipformer_ctc=OfflineZipformerCtcModelConfig(model=""), wenet_ctc=OfflineWenetCtcModelConfig(model=""), sense_voice=OfflineSenseVoiceModelConfig(model="ax650/model-10-seconds.axmodel", language="auto", use_itn=False), moonshine=OfflineMoonshineModelConfig(preprocessor="", encoder="", uncached_decoder="", cached_decoder=""), dolphin=OfflineDolphinModelConfig(model=""), canary=OfflineCanaryModelConfig(encoder="", decoder="", src_lang="", tgt_lang="", use_pnc=True), omnilingual=OfflineOmnilingualAsrCtcModelConfig(model=""), telespeech_ctc="", tokens="tokens.txt", num_threads=2, debug=False, provider="axcl", model_type="", modeling_unit="cjkchar", bpe_vocab=""), lm_config=OfflineLMConfig(model="", scale=0.5, lodr_scale=0.01, lodr_fst="", lodr_backoff_id=-1), ctc_fst_decoder_config=OfflineCtcFstDecoderConfig(graph="", max_active=3000), decoding_method="greedy_search", max_active_paths=4, hotwords_file="", hotwords_score=1.5, blank_penalty=0, rule_fsts="", rule_fars="", hr=HomophoneReplacerConfig(lexicon="", rule_fsts=""))
Creating recognizer ...
Recognizer created!
Current sample rate: 16000
Recording started!
Use recording device: plughw:2,0
Started. Please speak
 0: hello
 1: how are you
^C
Caught Ctrl + C. Exiting...
```