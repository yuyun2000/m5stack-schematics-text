
# Pin Servo

## 案例程序

初始化引脚用于一般舵机控制(50Hz, 500-2500us), 实现角度控制。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/pin_servo/uiflow_block_pin_servo_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *
from servo import Servo
import time

setScreenColor(0x222222)

servo0 = Servo(26,50,500,2500,180)
while True:
  servo0.write_angle(0)
  wait(1)
  servo0.write_angle(180)
  wait(1)
  servo0.write_us(500)
  wait(1)
  servo0.write_us(2500)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/pin_servo/uiflow_block_pin_servo_init.svg"> 


```python
from servo import Servo
servo0 = Servo(26,50,500,2500,180)
```

- 舵机初始化设置：
  - Pin: 引脚
  - freq: 舵机信号频率
  - min: 最小脉冲宽度
  - max: 最大脉冲宽度
  - angle angle: 舵机角度范围

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/pin_servo/uiflow_block_pin_servo_write_angle.svg"> 

```python
servo0.write_angle(180)
```

- 控制舵机转动指定角度


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/pin_servo/uiflow_block_pin_servo_write_us.svg"> 


```python
servo0.write_us(2500)
```

- 控制驱动信号输出周期的高电平时间


