# LoRa Bus

LoRa Bus 功能是 LoRa 和 Modbus 协议的结合， 使用时需搭配拓展 LoRa Module 433/868。

## LoRa Bus Master

### 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_master_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *
from libs.lorabus import Lorabus

setScreenColor(0x222222)

bus = Lorabus()

label0 = M5TextBox(31, 219, "WriteData 1", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(117, 206, "Write Data 2", lcd.FONT_Default, 0xFFFFFF, rotate=0)
title0 = M5Title(title="LoRaBus Master", x=100, fgcolor=0xFFFFFF, bgcolor=0xff0072)
label2 = M5TextBox(210, 219, "Slave Read", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label3 = M5TextBox(25, 64, "Slave Data:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label4 = M5TextBox(114, 64, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label5 = M5TextBox(25, 120, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label6 = M5TextBox(309, -108, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)

def buttonA_wasPressed():
  # global params
  if bus.master_write_registers(0x10, 0x0000, [11, 22, 33, 44, 55]):
    label5.setText('Data 1 Send Sucess')
  else:
    label5.setText('Data 1 Send Unsucess')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  if bus.master_write_message(0x10, 0x0000, '12345'):
    label5.setText('Data 2 Send Sucess')
  else:
    label5.setText('Data 2 Send Unsucess')
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  # global params
  label4.setText(str(bus.master_read_register(0x10, 0x0000, 3)))
  pass
btnC.wasPressed(buttonC_wasPressed)


bus.lorabus_init(cs=5, rst=26, irq=36)
bus.config_bus(freq=433000000)
```

### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_master_init.svg"> 

```python
from libs.lorabus import Lorabus

bus = Lorabus()
bus.lorabus_init(cs=5, rst=26, irq=36)
bus.config_bus(freq=433000000)
```

- 初始化 LoRaBus, 配置 cs, reset, IRQ 引脚以及 LoRa 工作频率。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_master_write_message.svg"> 

```python
bus.master_write_message(0x10, 0x0000, '12345')
```

- 向从机指定寄存器写入字符串


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_master_write_register.svg"> 

```python
bus.master_write_registers(0x10, 0x0000, [11, 22, 33, 44, 55])
```
- 向从机指定寄存器写入数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_master_read_register.svg"> 

```python
print(bus.master_read_register(0x10, 0x0000, 3))
```

- 读取从机指定寄存器内容

## LoRa Bus Slave

### 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_slave_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *
from libs.lorabus import Lorabus

setScreenColor(0x222222)

print2 = None

bus = Lorabus()

title0 = M5Title(title="Title", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
title1 = M5Title(title="LoRaBus Slave", x=110, fgcolor=0xFFFFFF, bgcolor=0xff003b)
label5 = M5TextBox(6, 112, "Update Data:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label0 = M5TextBox(6, 67, "Recv Data:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label6 = M5TextBox(105, 112, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(91, 67, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label2 = M5TextBox(41, 215, "Update 1", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label3 = M5TextBox(129, 215, "Update 2", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label4 = M5TextBox(220, 215, "Update 3", lcd.FONT_Default, 0xFFFFFF, rotate=0)

def buttonA_wasPressed():
  global print2
  print2 = [11, 22, 33]
  bus.slave_set_readfifo(0x0000, print2)
  label6.setText(str(print2))
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global print2
  print2 = [45, 67, 89]
  bus.slave_set_readfifo(0x0000, print2)
  label6.setText(str(print2))
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global print2
  print2 = [123, 234, 345]
  bus.slave_set_readfifo(0x0000, print2)
  label6.setText(str(print2))
  pass
btnC.wasPressed(buttonC_wasPressed)


bus.lorabus_init(cs=5, rst=26, irq=36)
bus.config_bus(freq=433000000)
bus.slave_bus_init(0x10, 5, 10)
while True:
  if bus.slave_receive_req_create_pdu():
    label1.setText(str(bus.slave_get_writefifo(0x0000, 10)))
  wait_ms(2)
```

### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_slave_init.svg"> 

```python
from libs.lorabus import Lorabus

bus.lorabus_init(cs=5, rst=26, irq=36)
bus.config_bus(freq=433000000)
bus.slave_bus_init(0x10, 5, 10)
```

- 初始化 LoRaBus 为 slave, 配置 cs, reset, IRQ 引脚以及 LoRa 工作频率， slave 的本机地址以及消息队列大小。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_slave_receive.svg"> 

```python
bus.slave_receive_req_create_pdu()
```

- 监听数据帧请求

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_slave_set_readfifo.svg"> 

```python
print2 = [11, 22, 33]
bus.slave_set_readfifo(0x0000, print2)
```

- 设置读取数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/lorabus/uiflow_block_lorabus_slave_get_writefifo.svg"> 

```python
bus.slave_get_writefifo(0x0000, 10)
```

- 获取写入数据

