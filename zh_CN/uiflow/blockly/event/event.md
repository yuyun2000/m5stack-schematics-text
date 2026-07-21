# Event

## Loop

### 案例程序

- 循环打印 Hello M5

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_loop_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)

while True:
  print('Hello M5')
  wait_ms(2)
```


### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_loop.svg"> 

```python
while True:
  wait_ms(2)
```

- 无限循环执行包含在 Loop 内的程序

## Button

### 案例程序

- 通过回调或轮询的方式获取按键状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_button_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)

def multiBtnCb_AB():
  # global params
  print('Button A + B Pressed')
  pass
btn.multiBtnCb(btnA,btnB,multiBtnCb_AB)

def buttonA_wasPressed():
  # global params
  print('Button A Pressed')
  pass
btnA.wasPressed(buttonA_wasPressed)

while True:
  if btnB.wasPressed():
    print('Button B wasPressed')
  if btnC.isPressed():
    print('Button C Pressed')
  wait_ms(2)
```

### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_button_init.svg"> 

```python
btn = btn.attach([pin])
```

- 初始化按键， 并指定输入的引脚

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_button_callback.svg">

```python
def buttonA_wasPressed():
  # global params
  print('Button A Pressed')
  pass
btnA.wasPressed(buttonA_wasPressed)
```

- 绑定按键事件回调函数， 可选事件：
  - wasPressed
  - wasReleased
  - LongPress
  - wasDoublePress

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_button_callback_multi.svg"> 

```python
def multiBtnCb_AB():
  # global params
  print('Button A + B Pressed')
  pass
btn.multiBtnCb(btnA,btnB,multiBtnCb_AB)
```
- 绑定多按键事件回调函数， 仅支持双按键组合， 同时按下按键时触发。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_button_read.svg"> 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_button_read_status.svg"> 

```python
if btnB.wasPressed():
  print('Button B wasPressed')
if btnC.isPressed():
  print('Button C Pressed')
```

- 读取当前按键状态， 根据事件配置返回 True/False, 可选事件：
  - wasPressed
  - wasReleased
  - LongPress
  - wasDoublePress
  - Pressed
  - Released

## Software Timer

### 案例程序

- 配置软件定时器， 以100ms 为周期进行打印

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_software_timer_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)

@timerSch.event('timer1')
def ttimer1():
  # global params
  print('This is a software timer!')
  pass


timerSch.setTimer('timer1', 100, 0x00)
timerSch.run('timer1', 100, 0x00)
```

### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_software_timer_callback.svg"> 

```python
@timerSch.event('timer1')
def ttimer1():
  # global params
  pass
```

- 设置软件定时器回调函数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_software_timer_set.svg"> 

```python
timerSch.setTimer('timer1', 100, 0x00)
```

- 设置软件定时器周期，定时器模式支持以下配置：
  - PERIODIC 0x00：周期循环
  - ONE_SHOT 0x01：单次执行

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_software_timer_start.svg"> 

```python
timerSch.run('timer1', 100, 0x00)
```

- 开启软件定时器同时配置周期，定时器模式支持以下配置：
  - PERIODIC 0x00：周期循环
  - ONE_SHOT 0x01：单次执行


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_software_timer_stop.svg"> 

```python
timerSch.stop('timer1')
```

- 停止软件定时器

## Hardware Timer

### 案例程序

- 配置硬件定时器， 以100ms 为周期进行打印

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_hardware_timer_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)

def callback_timer3(_arg):
  # global params
  print('This is a hardware timer!')
  pass


timerSch.timer.init(period=100, mode=timerSch.timer.PERIODIC, callback=callback_timer3)
```

### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_hardware_timer_set.svg">

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/event/uiflow_block_hardware_timer_callback.svg"> 


```python
def callback_timer3(_arg):
  pass

timerSch.timer.init(period=100, mode=timerSch.timer.PERIODIC, callback=callback_timer3)
```

- 配置定时器周期， 定时器模式， 以及回调函数。定时器模式支持以下配置：
  - PERIODIC：周期循环
  - ONE_SHOT：单次执行


