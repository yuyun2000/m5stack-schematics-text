# Vibration

## 案例程序

设置震动强度，并间隔1秒震动一次

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/vibration/uiflow_block_vibration_demo.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

power.setVibrationIntensity(255)
while True:
  power.setVibrationEnable(True)
  wait(1)
  power.setVibrationEnable(False)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/vibration/uiflow_block_vibration_set_motor_on.svg"> 

```python
power.setVibrationEnable(True)
```

- 开启电机震动
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/vibration/uiflow_block_vibration_set_motor_off.svg"> 

```python
power.setVibrationEnable(False)
```
 
- 关闭电机震动

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/vibration/uiflow_block_vibration_set_motor_vibrate_time.svg"> 

```python
power.setVibrationEnable(True)
  wait(2)
  power.setVibrationEnable(False)
  wait_ms(2)
```

- 设置震动时间时长

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/vibration/uiflow_block_vibration_set_motor_vibrate_intensity.svg"> 

```python
power.setVibrationIntensity(255)
```

- 设置震动强度(0-255)，数值越大震动强度越大


