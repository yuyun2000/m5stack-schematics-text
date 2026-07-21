
# [Hat 8Servo](/zh_CN/hat/hat-8servos)

## 案例程序

控制多个舵机循环每隔一秒转动一个角度，你可以继续添加舵机数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo/uiflow_block_8servo_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_servos_1 = hat.get(hat.SERVOS)

hat_servos_1.SetAngle(1, 0)
hat_servos_1.SetAngle(2, 0)
hat_servos_1.SetAngle(3, 0)
hat_servos_1.SetAngle(4, 0)
wait(1)
hat_servos_1.SetAngle(1, 90)
hat_servos_1.SetAngle(2, 90)
hat_servos_1.SetAngle(3, 90)
hat_servos_1.SetAngle(4, 90)
wait(1)
hat_servos_1.SetAngle(1, 180)
hat_servos_1.SetAngle(2, 180)
hat_servos_1.SetAngle(3, 180)
hat_servos_1.SetAngle(4, 180)
wait(1)
hat_servos_1.SetAngle(1, 90)
hat_servos_1.SetAngle(2, 90)
hat_servos_1.SetAngle(3, 90)
hat_servos_1.SetAngle(4, 90)
wait(1)
hat_servos_1.SetAngle(1, 0)
hat_servos_1.SetAngle(2, 0)
hat_servos_1.SetAngle(3, 0)
hat_servos_1.SetAngle(4, 0)
wait(1)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo/uiflow_block_hat_servos_angle.svg">

```python
hat_servos_0.SetAngle(1, 0)
```

- 设置指定编号的舵机旋转角度，当前角度为0度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo/uiflow_block_hat_servos_write.svg">

```python
hat_servos_0.SetPulse(1, 600)
```

- 设置指定编号的舵机脉冲宽度，当前值为600微秒

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo/uiflow_block_servos_set_all.svg">

```python
hat_servos_0.SetRGB(0xff0000)
```

- 设置所有灯珠的颜色，当前为红色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo/uiflow_block_servos_set_all_rgb.svg">

```python
hat_servos_0.SetRGB(0x000000)
```

- 通过指定红、绿、蓝三个值来设置 RGB 灯条的颜色，当前值为(0,0,0)，即黑色(灯灭)

