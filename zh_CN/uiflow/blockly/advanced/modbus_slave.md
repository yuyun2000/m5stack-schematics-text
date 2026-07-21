# Modbus Slave

## 案例程序

M5Stack设备作为Modbus RTU从站，通过功能码03（读取保持寄存器）向主站提供3个不断递增的16位寄存器值（D1/D2/D3），并可通过按键A触发数据更新。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_modbus_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from modbus.slave.rtu import ModbusSlave
import time

setScreenColor(0x222222)

inc = None
D1 = None
D2 = None
D3 = None
data_buf = None

title0 = M5Title(title="Slave Read Holding Register", x=62, fgcolor=0xFFFFFF, bgcolor=0xff3d00)
label0 = M5TextBox(16, 112, "From Slave to Master Send Register Data ", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(41, 209, "Press A", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label2 = M5TextBox(24, 55, "Text", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label3 = M5TextBox(139, 55, "Text", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
label4 = M5TextBox(257, 55, "Text", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)

def buttonA_wasPressed():
  global inc, D1, D2, D3, data_buf
  inc = inc + 1
  if inc >= 2:
    inc = 0
    modbus_s.update_process(3, 10, 3, [D1, D2, D3])
  pass
btnA.wasPressed(buttonA_wasPressed)


modbus_s = ModbusSlave(2, tx=17, rx=16, baudrate=9600, data_bits=8, stop_bits=1, parity=None, slaveID=4)
modbus_s.function_init(3, 10, 3)
D1 = 0
D2 = 0
D3 = 0
inc = 0
while True:
  data_buf = modbus_s.receive_req_create_pdu()
  if (modbus_s.find_function) == (3):
    modbus_s.create_slave_response(data_buf)
    wait_ms(10)
  if inc:
    D1 = D1 + 187
    D2 = D2 + 231
    D3 = D3 + 159
    if D1 >= 0XFFFF:
      D1 = 0
    if D2 >= 0XFFFF:
      D2 = 0
    if D3 >= 0XFFFF:
      D3 = 0
    label2.setText(str(D1))
    label3.setText(str(D2))
    label4.setText(str(D3))
  wait_ms(2)

```

## 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_fun_status.svg">

```python
print((str('code:') + str((1))))
```
- 获取功能码 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_get_address.svg">

```python
print(modbus_s.find_address)
```

- 获取设备地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_get_function.svg">

```python
print((str('code:') + str((modbus_s.find_function))))
```

- 获取功能码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_get_quantity.svg">

```python
print(modbus_s.find_quantity)
```

- 获取数据量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_init.svg">

```python
modbus_s = ModbusSlave(1, tx=17, rx=16, baudrate=9600, data_bits=7, stop_bits=1, parity=None, slaveID=1)
```

- 初始化UART参数
  - 波特率
  - 数据位
  - 校验位
  - 设备地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_init_func.svg">

```python
modbus_s.function_init(1, 0, 0)
```

- 初始化线圈状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_receive_adu.svg">

```python
print((str('ADU:') + str((modbus_s.receive_req_create_pdu()))))
```

- 接收ADU请求帧

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_send.svg">

```python
modbus_s.create_slave_response()
```

- 发送ADU响应缓冲区

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_slave/uiflow_block_modbus_slave_rtu_update_func.svg">

```python
modbus_s.update_process(1, 0, 0, [0, 0, 0])
```
- 更新功能参数
