# [Hat SPK](/zh_CN/hat/hat-spk)

## 案例程序

调节音量大小，并每隔一秒播放一个音调

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk/uiflow_block_hat_spk_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat
import time
import hat

setScreenColor(0x111111)

hat_spk_0 = hat.get(hat.SPEAKER)

hat_spk_0.setVolume(1)
while True:
  hat_spk_0.sing(220, 1)
  wait(1)
  hat_spk_0.sing(247, 1)
  wait(1)
  hat_spk_0.sing(247, 1)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk/uiflow_block_hat_speaker_sing.svg">

```python
hat_spk_0.sing(220, 1)
```

- 播放指定音调(如 Low A)持续 1 个节拍。这个块可以用来播放不同频率和时长的音符，适合做简单的音效或音乐演示

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk/uiflow_block_hat_speaker_tone.svg">

```python
hat_spk_0.tone(1800, 200)
```

- 设定扬声器发出指定频率的蜂鸣声。在此例中，频率设置为 1800 Hz，持续时间为 200 毫秒

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/spk/uiflow_block_hat_speaker_vol.svg">

```python
hat_spk_0.setVolume(1)
```

- 设置扬声器的音量。在此例中，音量设置为 1，可能是最大音量或其他数值范围内的一个设定

