# [Hat SPK2](/zh_CN/hat/Hat-SPK2)

## 案例程序

每隔一秒播放一个语调持续一秒，并调节音量到6

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk2/uiflow_block_hat_spk2_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_spk2_0 = hat.get(hat.SPEAKER_I2S)

while True:
  hat_spk2_0.playTone(220, 1, volume=6)
  wait(1)
  hat_spk2_0.playTone(247, 1, volume=6)
  wait(1)
  hat_spk2_0.playTone(131, 1, volume=6)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk2/uiflow_block_hat_spk2_play_cloud_wav.svg">

```python
hat_spk2_0.playCloudWAV('', volume=0)
```

- 通过提供的 URL 播放云端的 WAV 音频文件，并可以设置音量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk2/uiflow_block_hat_spk2_play_sing.svg">

```python
hat_spk2_0.playTone(220, 1, volume=0)
```

- 播放指定的音调(如 Low A)，持续1个节拍，并可以调整音量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk2/uiflow_block_hat_spk2_play_tone.svg">

```python
hat_spk2_0.playTone(220, 1, volume=0)
```

- 播放指定频率(如 220 Hz)的音调，持续1个节拍，音量也可以调整

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk2/uiflow_block_hat_spk2_play_wav_dropdown.svg">

```python
hat_spk2_0 = hat.get(hat.SPEAKER_I2S)
```

- 从本地选择一个 WAV 音频文件进行播放，并设置音量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk2/uiflow_block_hat_spk2_play_wav_rate.svg">

```python
hat_spk2_0.playWAV('', rate=44100, data_format=hat_spk2_0.F16B, channel=hat_spk2_0.CHN_LR, volume=0)
```

- 通过设置采样率、数据格式、声道和音量，播放指定的 WAV 文件

