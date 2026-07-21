# Modbus Master

## 案例程序

实现Modbus主站，通过按钮A触发读取从站地址4的保持寄存器数据并显示在屏幕上

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_modbus_master_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from modbus.master.uModBusSerial import uModBusSerial

setScreenColor(0x222222)

title0 = M5Title(title="Master Read Holding Register", x=60, fgcolor=0xFFFFFF, bgcolor=0xff0078)
label0 = M5TextBox(16, 212, "Press A Send Data", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(15, 69, "Text", lcd.FONT_DejaVu24, 0xe2ff00, rotate=0)

def buttonA_wasPressed():
  # global params
  label1.setText(str(modbus.read_holding_registers(4, 10, 3, False, timeout=)))
  pass
btnA.wasPressed(buttonA_wasPressed)


modbus = uModBusSerial(2, tx=17, rx=16, baudrate=9600, data_bits=8, stop_bits=1, parity=None, ctrl_pin=None)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_init.svg">

```python
modbus = uModBusSerial(1, tx=0, rx=0, baudrate=9600, data_bits=8, stop_bits=1, parity=None, ctrl_pin=None)
```

- UART 初始化配置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_read_coils.svg">

```python
print((str('address:') + str((modbus.read_coils(1, 1, 0, timeout=2000)))))
```

- 读取线圈状态


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_read_discrete_inputs.svg">

```python
print((str('address:') + str((modbus.read_discrete_inputs(1, 1, 0, timeout=2000)))))
```

- 读取离散输入

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_read_holding_registers.svg">

```python
print((str('address:') + str((modbus.read_holding_registers(1, 1, 0, True, timeout=2000)))))
```

- 读取保持寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_read_input_registers.svg">

```python
print((str('address:') + str((modbus.read_input_registers(1, 1, 0, True, timeout=2000)))))
```

- 读取输入寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_write_multiple_coils.svg">

```python
print((str('write address:') + str((modbus.write_multiple_registers(1, 1, 0, True, timeout=2000)))))
```

- 写多个线圈


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_write_multiple_registers.svg">

```python
print((str('write address:') + str((modbus.write_multiple_coils(1, 1, 0, timeout=2000)))))
```

- 写多个寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_write_single_coil.svg">

```python
print((str('write address:') + str((modbus.write_single_coil(1, 1, 0xFF00, timeout=2000)))))
```

- 写单个线圈


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/modbus_master/uiflow_block_modbus_master_u_write_single_register.svg">

```python
print((str('write address:') + str((modbus.write_single_register(1, 1, 0, True, timeout=2000)))))
```

- 写单个寄存器

