# SenseVoice

SenseVoice 是一种语音识别与理解模型，能够高效、准确地将语音内容转化为文本，并支持多语言和多场景的语音处理。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/SenseVoice) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/SenseVoice
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/SenseVoice $ ls -lh
total 464K
-rw-rw-r-- 1 m5stack m5stack  11K Aug 12 16:38 am.mvn
-rw-rw-r-- 1 m5stack m5stack 369K Aug 12 16:38 chn_jpn_yue_eng_ko_spectok.bpe.model
-rw-rw-r-- 1 m5stack m5stack    0 Aug 12 16:38 config.json
-rw-rw-r-- 1 m5stack m5stack  108 Aug 12 16:38 download_dataset.sh
-rw-rw-r-- 1 m5stack m5stack  893 Aug 12 16:38 download_utils.py
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 16:38 embeddings
-rw-rw-r-- 1 m5stack m5stack  17K Aug 12 16:38 frontend.py
-rw-rw-r-- 1 m5stack m5stack 1.1K Aug 12 16:38 LICENSE
-rw-rw-r-- 1 m5stack m5stack 1.6K Aug 12 16:38 main.py
-rw-rw-r-- 1 m5stack m5stack 3.2K Aug 12 16:38 print_utils.py
-rw-rw-r-- 1 m5stack m5stack 1.5K Aug 12 16:38 README.md
-rw-rw-r-- 1 m5stack m5stack   71 Aug 12 16:38 requirements.txt
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 16:38 sensevoice_ax650
-rw-rw-r-- 1 m5stack m5stack 9.1K Aug 12 16:38 SenseVoiceAx.py
-rw-rw-r-- 1 m5stack m5stack 2.5K Aug 12 16:38 test_wer.py
-rw-rw-r-- 1 m5stack m5stack 4.7K Aug 12 16:38 tokenizer.py
```

2. 创建虚拟环境

```bash
python -m venv sensevoice
```

3. 激活虚拟环境

```bash
source sensevoice/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install -r requirements.txt
```

5. 运行

```bash
python main.py -i test.mp3
```

| 参数名称      | 说明                                     | 默认值 |
| ------------- | ---------------------------------------- | ------ |
| --input/-i    | 输入音频文件                             | -      |
| --language/-l | 识别语言，支持 auto, zh, en, yue, ja, ko | auto   |

\#> 说明 | 首次运行会自动下载模型。

运行结果如下：

```bash
(sensevoice) m5stack@raspberrypi:~/rsp/SenseVoice $ python main.py -i test_en.mp3
[INFO] Available providers:  ['AXCLRTExecutionProvider']
input_audio: test_en.mp3
language: auto
use_itn: True
model_path: /home/m5stack/rsp/SenseVoice/models/SenseVoice/sensevoice_ax650/sensevoice.axmodel
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.0 156de6f7
RTF: 0.015400904924311537    Latency: 0.463259220123291s  Total length: 30.08s
['You want to be a nurse or an archi', "A lawyer or a member of our military. you''re going to need a", 'Eduducation for every single one of those caree', 'Not drop out of school and just drop into a good j', "You''ve got to train for it", "And learn for it. And this isn't just impo", 'lifeIn your own future. what you make', 'Will decide nothing less than the future of this country..']
```
