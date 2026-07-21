# PIN

## 案例程序

设置引脚输出高电平1秒，输出低电平1秒

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pin/uiflow_block_pin_demo1.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import machine
import time

while True:
  pin0.on()
  wait(1)
  pin0.off()
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pin/uiflow_block_pin_pinout.svg"> 

```python
machine.Pin(0, mode=machine.Pin.IN, pull=machine.Pin.PULL_UP)
```

- 设置引脚的方向
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pin/uiflow_block_pin_on.svg"> 

```python
pin0.on()
```
 
- 设置引脚为输出高电平

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pin/uiflow_block_pin_off.svg"> 

```python
pin0.off()
```

- 设置引脚为输出低电平

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pin/uiflow_block_pin_set_value.svg"> 

```python
pin0.value(0)
```

- 设置引脚的值
  - "0":低电平
  - "1":高电平


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pin/uiflow_block_pin_get_value.svg"> 

```python
str(pin0.value())
```

- 获取引脚读取的值


