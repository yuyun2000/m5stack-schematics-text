# [Hat Vibrator](/zh_CN/hat/HAT-Vibrator)

## 案例程序

 每隔一秒加强一次震动强度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/vibrator/uiflow_block_hat_vibration_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_vibrator_0 = hat.get(hat.VIBRATOR)

while True:
  hat_vibrator_0.set_duty(10)
  wait(1)
  hat_vibrator_0.set_duty(30)
  wait(1)
  hat_vibrator_0.set_duty(50)
  wait(1)
  hat_vibrator_0.set_duty(70)
  wait(1)
  hat_vibrator_0.set_duty(100)
  wait(1)
  hat_vibrator_0.turn_off()
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/vibrator/uiflow_block_hat_vibrator_set_duty.svg">

```python
hat_vibrator_0.set_duty(50)
```

- 设置振动器的占空比(例如50%)，即控制振动器在每个周期内工作的时间比例

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/vibrator/uiflow_block_hat_vibrator_set_freq.svg">

```python
hat_vibrator_0.set_freq(10)
```

- 设置振动器的工作频率(例如10Hz)，控制振动器每秒钟振动的次数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/vibrator/uiflow_block_hat_vibrator_turn_off.svg">

```python
hat_vibrator_0.turn_off()
```

- 关闭振动器，停止其工作

