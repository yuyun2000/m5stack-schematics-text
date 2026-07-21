# [Module USB](/zh_CN/module/usb)

## 案例程序

初始化鼠标 HID HOST, 接鼠标后读取光标 x,y 坐标和按键状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_usb_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time
setScreenColor(0x222222)

usb = module.get(module.USBHOST)

usb.max3421e_init(sclk=18, mosi=23, miso=19, cs=5, irq=35)
usb.hid_init()
while True:
  usb.hid_poll()
  if usb.mouse_button_status(1):
    print('mouse button left click')
  if usb.mouse_button_status(2):
    print('mouse button right click')
  if usb.mouse_button_status(4):
    print('mouse button center click')
  print((str('X:') + str((usb.mouse_cursor_x))))
  print((str('Y:') + str((usb.mouse_cursor_y))))
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_module_usb_init_max3421.svg">

```python
import module
usb = module.get(module.USBHOST)
usb.max3421e_init(sclk=18, mosi=23, miso=19, cs=5, irq=35)
```

- 初始化 Module USB

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_usb_init.svg">

```python
usb.hid_init()
```

- 初始化 Mouse HID Host


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_usb_hid_poll.svg">


```python
usb.hid_poll()
```

- 刷新输入设备状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_usb_mouse_get_click_status.svg">

```python
usb.mouse_button_status(status):
```

- 获取按键状态：
  - status:
    - left:1
    - right:2
    - left+right:3
    - center:4
    - left+center:5
    - right+center:6
    - left+right+center:7
- 返回值：
  - True/False


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_usb_mouse_cutsor.svg">

```python
usb.mouse_cursor_x
usb.mouse_cursor_y
```

- 获取输入设备光标位置


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_usb_read_output_pin_value.svg">

```python
usb.write_output_pin(PIN,0)
```

- 模块拓展输出 IO, 控制输出电平
  - PIN:0-4

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_usb_read_input_pin.svg">

```python
usb.read_input_pin(PIN)
```

- 模块拓展输入 IO, 读取输入电平
  - PIN:0-4

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/usb/uiflow_block_usb_read_output_pin.svg">

```python
usb.read_output_pin(PIN)
```

- 模块拓展输出组 IO, 读取输出电平：
  - PIN:0-4


