# [Unit Vibrator](/zh_CN/unit/vibrator)

## 案例程序

> 使震动电机震动

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vibrator/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
vibrator_0 = unit.get(unit.VIBRATOR, unit.PORTA)

def buttonA_wasPressed():
  # global params
  vibrator_0.off()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  vibrator_0.on(10)
  pass
btnB.wasPressed(buttonB_wasPressed)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vibrator/uiflow_block_vibrator_off.svg">

```python
vibrator_0.off()
```

- 关闭电机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vibrator/uiflow_block_vibrator_on.svg">

```python
vibrator_0.on(10)
```

- 设置振动占空比

