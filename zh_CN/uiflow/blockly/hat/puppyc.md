# [Hat Puppyc](/zh_CN/hat/hat-puppyc)

## 案例程序

每隔一秒变化一次所有舵机角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/puppyc/uiflow_block_hat_puppyc_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_puppyC_0 = hat.get(hat.PUPPY)

while True:
  hat_puppyC_0.SetAllAngle(0, 90, 180, 0)
  wait(1)
  hat_puppyC_0.SetAllAngle(90, 180, 0, 90)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/puppyc/uiflow_block_hat_puppy_all_angle.svg">

```python
hat_puppyC_0.SetAllAngle(0, 0, 0, 0)
```

- 用于设置多个舵机的角度，从 0 到 3 四个舵机的角度可以同时设置，数值代表每个舵机的旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/puppyc/uiflow_block_hat_puppy_angle.svg">

```python
hat_puppyC_0.SetAngle(0, 0)
```

- 用于单独设置某个舵机的旋转角度，可以指定舵机编号并设置它的旋转角度

