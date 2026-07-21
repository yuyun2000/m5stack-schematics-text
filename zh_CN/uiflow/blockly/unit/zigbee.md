# [Unit ZigBee](/zh_CN/unit/zigbee)

## 案例程序

Zigbee协调器控制程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_zigbee_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x6b0000)
zigbee_2 = unit.get(unit.ZIGBEE, unit.PORTC)

dummy = None
rand = None

title0 = M5Title(title="ZIGBEE-COORINATOR", x=80, fgcolor=0xFFFFFF, bgcolor=0xc89500)
label0 = M5TextBox(16, 40, "STATUS:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label1 = M5TextBox(92, 40, "label1", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label2 = M5TextBox(16, 84, "SEND DATA:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label3 = M5TextBox(128, 84, "label3", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label4 = M5TextBox(16, 129, "RECV DATA:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label5 = M5TextBox(128, 129, "label5", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label6 = M5TextBox(47, 219, "SEND", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label7 = M5TextBox(128, 219, "CHANGE", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label8 = M5TextBox(205, 219, "GET PARAM", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

import random

def buttonA_wasPressed():
  global dummy, rand
  zigbee_2.send_payload(rand)
  label3.setText(str(rand))
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global dummy, rand
  zigbee_2.set_param_module(1, 0x1617, 20, 1, 0x2345, 6, 1, '')
  zigbee_2.reboot_module()
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global dummy, rand
  dummy = 1
  zigbee_2.reboot_module()
  pass
btnC.wasPressed(buttonC_wasPressed)

dummy = 1
zigbee_2.reboot_module()
label1.setText(str(zigbee_2.version_module()))
wait(1.5)
while True:
  if dummy:
    label1.setText(str(zigbee_2.get_param_module(0)))
    wait(1.5)
    label1.setText(str(zigbee_2.get_param_module(1)))
    wait(1.5)
    label1.setText(str(zigbee_2.get_param_module(3)))
    wait(1.5)
    label1.setText(str(zigbee_2.get_param_module(4)))
    wait(1.5)
    label1.setText(str(zigbee_2.get_param_module(5)))
    wait(1.5)
    label1.setText(str(zigbee_2.get_param_module(9)))
    wait(1.5)
    label1.setText(str(zigbee_2.get_param_module(16)))
    wait(1.5)
    label1.setText(str(zigbee_2.get_param_module(40)))
    wait(1.5)
    label1.setText(str(zigbee_2.get_param_module(44)))
    wait(1.5)
    dummy = 0
  rand = random.randint(1000000, 9999999)
  if zigbee_2.check_payload():
    label5.setText(str(zigbee_2.recv_payload()))
  wait_ms(100)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_uart_init.svg">

```python
zigbee_0.uart_port_id(1)
```

- 串口初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_check_payload.svg">

```python
print(zigbee_0.check_payload())
```

- 负载数据检查

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_get_param.svg">

```python
print((str('param:') + str((zigbee_0.get_param_module(0)))))
```

- 获取参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_get_version.svg">

```python
print(zigbee_0.version_module())
```

- 获取版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_recv_payload.svg">

```python
print(zigbee_0.recv_payload())
```

- 接收负载数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_send_payload.svg">

```python
zigbee_0.send_payload('hello')
```

- 发送负载数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_set_core_baudrate.svg">

```python
zigbee_0.core_baudrate(38400)
```

- 设置核心波特率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_set_module.svg">

```python
zigbee_0.set_param_module(1, 0x1617, 20, 1, 0x2345, 6, 0, '')
```

- 设置模块（参数/模式等，具体含义依上下文而定 ）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/zigbee/uiflow_block_unit_zigbee_set_reboot.svg">

```python
zigbee_0.reboot_module()
```

- 设置重启

