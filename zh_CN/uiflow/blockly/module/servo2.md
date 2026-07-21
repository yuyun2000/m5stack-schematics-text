# [Module13.2 Servo2](/zh_CN/module/servo2)

## 案例程序

让舵机在 0 和 90 角度来回旋转

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/servo2/uiflow_block_servo2_example.svg">


```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time
setScreenColor(0x222222)
servo2 = module.get(module.SERVO2)

while True:
  servo2.position(0, 0)
  wait_ms(100)
  servo2.position(0, 90)
  wait_ms(100)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/servo2/uiflow_block_servo2_degree.svg">

```python
servo2.position(ch, deg)
```

- 设置舵机旋转角度：
  - ch: 0-15
  - deg: 0-180

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/servo2/uiflow_block_servo2_duty.svg">

```python
servo2.position(ch, duty=0)
```

- 设置舵机脉冲占空比：
  - ch: 0-15
  - duty: 0-100


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/servo2/uiflow_block_servo2_pulse.svg">

```python
servo2.position(ch, us=400)
```

- 设置舵机脉冲时间：
  - ch: 0-15
  - duty: 400-2500us

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/servo2/uiflow_block_servo2_release.svg">

```python
servo2.release(ch)
```

- 释放舵机电源：
  - ch: 0-15

