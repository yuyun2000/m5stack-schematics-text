# Whisper

- 本小节只指导如何在 Raspberry Pi 5 上运行预编译好的基于 Whipser Small 的语音转文字示例；
- 模型转换、示例源码编译请参考 [whisper.axcl](https://github.com/ml-inory/whisper.axcl)。

1. **下载**

```bash
git clone https://github.com/ml-inory/whisper.axcl.git
```

2. **编译**

```bash
cd whisper.axcl
mkdir -p build && cd build
cmake -DCMAKE_INSTALL_PREFIX=../install -DCMAKE_BUILD_TYPE=Release ..
make install -j4
```

3. **预编译模型**

预编译模型下载 [百度网盘](https://pan.baidu.com/s/1tOHVMZCin0A68T5HmKRJyg?pwd=axyz)

- [Hugging Face whisper-tiny](https://huggingface.co/M5Stack/whisper-tiny-axmodel)

- [Hugging Face whisper-base](https://huggingface.co/M5Stack/whisper-base-axmodel)

- [Hugging Face whisper-small](https://huggingface.co/M5Stack/whisper-small-axmodel)

4. **运行 Whisper**

```bash
cd install
./whisper -w ../demo.wav
```

**运行结果：**

```bash
(base) axera@raspberrypi:~/qtang/whisper.axcl/install $ ./whisper -w ../demo.wav
encoder: ../models/small-encoder.axmodel
decoder_main: ../models/small-decoder-main.axmodel
decoder_loop: ../models/small-decoder-loop.axmodel
wav_file: ../demo.wav
language: zh
Load encoder take 3336.25 ms
Load decoder_main take 6091.89 ms
Load decoder_loop take 5690.05 ms
Read positional_embedding
Encoder run take 190.26 ms
First token: 17556       take 51.49ms
Next Token: 20844        take 30.15 ms
Next Token: 7781         take 30.21 ms
Next Token: 20204        take 30.20 ms
Next Token: 28455        take 30.17 ms
Next Token: 31962        take 30.02 ms
Next Token: 6336         take 30.09 ms
Next Token: 254          take 30.22 ms
Next Token: 2930         take 30.14 ms
Next Token: 236          take 30.14 ms
Next Token: 36135        take 30.12 ms
Next Token: 15868        take 30.18 ms
Next Token: 252          take 30.01 ms
Next Token: 1546         take 30.17 ms
Next Token: 46514        take 30.17 ms
Next Token: 50257        take 30.15 ms
All Token: take 503.68ms, 31.77 token/s
All take 735.09ms
Result: 甚至出现交易几乎停滞的情况
(base) axera@raspberrypi:~/qtang/whisper.axcl/install $
```
