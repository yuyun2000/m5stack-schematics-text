# MeloTTS

- 本小节只指导如何在 Raspberry Pi 5 上运行预编译好的 MeloTTS 文字转语音示例；
- 模型转换、示例源码编译请参考 [melotts.axcl](https://github.com/ml-inory/melotts.axcl)。

1. **下载**

```bash
git clone https://github.com/ml-inory/melotts.axcl.git
chmod +x build_aarch64.sh
./build_aarch64.sh
```

2. **预编译模型**

```bash
cd melotts.axcl
./download_models.sh
```

预编译模型下载：

- [Hugging Face MeloTTS-Chinese](https://huggingface.co/M5Stack/MeloTTS-Chinese-ax650)
- [Hugging Face MeloTTS-English](https://huggingface.co/M5Stack/MeloTTS-English-ax650)
- [Hugging Face MeloTTS-Japanese](https://huggingface.co/M5Stack/MeloTTS-Japanese-ax650)
- [Hugging Face MeloTTS-Spanish](https://huggingface.co/M5Stack/MeloTTS-Spanish-ax650)

3. **编译**

aarch64 平台

```
./build_aarch64.sh
```

4. **运行 MeloTTS**

在 melotts.axcl 项目根目录下运行：

```bash
./install/melotts -s 句子
```

```bash
./install/melotts -e ../MeloTTS-English-ax650/encoder-en.onnx -d ../MeloTTS-English-ax650/decoder-en-au.axmodel -l ../MeloTTS-English-ax650/lexicon-en.txt -t ../MeloTTS-English-ax650/tokens-en.txt --g ../MeloTTS-English-ax650/g-en-au.bin -s "M5Stack is a leading provider of IoT solutions, committed to providing developers worldwide with convenient and flexible development components and tools. "
```

**运行结果：**

```bash
m5stack@raspberrypi5:~/melotts.axcl $ ./install/melotts -e ../MeloTTS-English-ax650/encoder-en.onnx -d ../MeloTTS-English-ax650/decoder-en-au.axmodel -l ../MeloTTS-English-ax650/lexicon-en.txt -t ../MeloTTS-English-ax650/tokens-en.txt --g ../MeloTTS-English-ax650/g-en-au.bin -s "M5Stack is a leading provider of IoT solutions, committed to providing developers worldwide with convenient and flexible development components and tools. "
encoder: ../MeloTTS-English-ax650/encoder-en.onnx
decoder: ../MeloTTS-English-ax650/decoder-en-au.axmodel
lexicon: ../MeloTTS-English-ax650/lexicon-en.txt
token: ../MeloTTS-English-ax650/tokens-en.txt
sentence: M5Stack is a leading provider of IoT solutions, committed to providing developers worldwide with convenient and flexible development components and tools.
wav: output.wav
speed: 0.800000
sample_rate: 44100
Load encoder
Load decoder model
Encoder run take 535.47ms
decoder slice num: 9
Decode slice(1/9) take 40.15ms
Decode slice(2/9) take 39.87ms
Decode slice(3/9) take 39.86ms
Decode slice(4/9) take 39.75ms
Decode slice(5/9) take 40.19ms
Decode slice(6/9) take 39.79ms
Decode slice(7/9) take 39.77ms
Decode slice(8/9) take 39.82ms
Decode slice(9/9) take 40.34ms
Saved audio to output.wav
```
