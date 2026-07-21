# [Hat Servo](/zh_CN/hat/hat-servo)

## 案例程序

每隔一秒转动舵机一次

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/servo/uiflow_block_hat_servo_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_servo_0 = hat.get(hat.SERVO)

while True:
  hat_servo_0.write_angle(0)
  wait(1)
  hat_servo_0.write_angle(90)
  wait(1)
  hat_servo_0.write_angle(180)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/servo/uiflow_block_servo_hat_angle.svg">

```python
hat_servo_0.write_angle(0)
```

- 这个块用于设置舵机旋转到指定的角度(单位是度)。在此例中，设置为 0 度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/servo/uiflow_block_servo_hat_write.svg">

```python
hat_servo_0.write_us(600)
```

- 这个块用于直接写入脉冲宽度给舵机，单位为微秒。在此例中，设置了 600 微秒的脉冲宽度

