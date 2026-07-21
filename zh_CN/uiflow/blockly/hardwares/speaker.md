# Speaker

#>扬声器频率设置：| 由于一般人的听力范围在20~20KHz,所以当你将频率设置得过低，或过高时，是听不到它的声音的

## Speaker For M5Core

### 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_speaker_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
setScreenColor(0x222222)

speaker.setVolume(90)
speaker.sing(220, 1)
speaker.tone(1800, 200)
```

### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_speaker.svg"> 

```python
speaker.tone(1800, 200)
```

- 设置播放声音频率与持续时间


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_speaker_volume.svg"> 

```python
speaker.setVolume(1)
```

- 设置播放音量
  - 音量范围： 0-100


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_speaker_tone.svg"> 

```python
speaker.sing(220, 1)
```

- 播放指定 tone 与节拍


## Speaker For M5Core2

### 案例程序

- 控制播放 tone

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_core2_speaker_play_tone_example.svg"> 

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

speaker.playTone(554, 1, volume=6)
speaker.playTone(554, 1, volume=6)
```


- 控制播放本地 wav 文件

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_core2_speaker_play_local_wav_example.svg"> 

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

speaker.playWAV("res/ding.wav", volume=6)
wait(1)
speaker.playWAV('res/ding.wav', rate=44100, data_format=speaker.F16B, channel=speaker.CHN_LR, volume=6)
```


### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_core2_speaker_play_freq.svg"> 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_core2_speaker_play_tone.svg"> 


```python
speaker.playTone(554, 1, volume=6)
```

- 播放指定 tone(频率), 同时设置播放音量大小
  - 音量范围： 0-6

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_core2_speaker_play_wav_file.svg"> 

```python
speaker.playWAV("res/ding.wav", volume=6)
```

- 播放本机文件系统中的 wav 文件， 同时设置播放音量大小

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_core2_speaker_play_local_wav_file_path.svg"> 

```python
speaker.playWAV('res/ding.wav', rate=44100, data_format=speaker.F16B, channel=speaker.CHN_LR, volume=6)
```

- 播放本机文件系统`res/filename.wav`或 SD 卡`/sd/filename.wav`中的 wav 文件，同时指定采样率和音频数据格式和声道

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_core2_speaker_play_upload_wav_file.svg"> 

```python
speaker.playWAV("res/ding.wav", volume=0)
```


- 在线编程模式下，提供接口上传 wav 文件至设备， 点击+号进行上传操作。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/speaker/uiflow_block_core2_speaker_play_url_wav_file.svg"> 

```python
speaker.playCloudWAV('https://xxxxx.wav', volume=6)
```

- 填入 URL 播放云端 wav 文件

#>注意事项： | 仅支持 WAV 类型文件且最大不超过500KB, 为防止文件过大，建议使用16000采样频率，16 Bit WAV 文件


