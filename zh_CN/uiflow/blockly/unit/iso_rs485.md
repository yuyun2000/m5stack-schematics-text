# [Unit RS485-ISO](/zh_CN/unit/iso485)

## 案例程序

设备发送和接收数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_rs485_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
RS485_0 = unit.get(unit.RS485, unit.PORTC)

RS485_0.init(1, baudrate=9600, data_bits=8, stop_bits=1, parity=None, ctrl_pin=None)
while True:
  RS485_0.write('hello'+"\r\n")
  print((str('data:') + str((RS485_0.read()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_init.svg">

```python
RS485_0.init(1, baudrate=9600, data_bits=8, stop_bits=1, parity=None, ctrl_pin=None)
```

- 初始化UART通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_any.svg">

```python
print(RS485_0.any())
```

- 保留缓存数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_read.svg">

```python
print(RS485_0.read())
```

- 读取全部数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_readline.svg">

```python
print(RS485_0.readline())
```

- 获取按行读取字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_read_characters.svg">

```python
print(RS485_0.read(10)) 
```

- 读取字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_read_coils.svg">

```python
print((str('coils:') + str((RS485_0.read_coils(1, 1, 0)))))
```

- 读取线圈状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_read_discrete_inputs.svg">

```python
print((str('discrete:') + str((RS485_0.read_discrete_inputs(1, 1, 0)))))
```

- 读取离散输入

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_read_holding_registers.svg">

```python
print((str('holding:') + str((RS485_0.read_holding_registers(1, 1, 0, True)))))
```

- 读取保持寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_read_input_registers.svg">

```python
print((str('input:') + str((RS485_0.read_discrete_inputs(1, 1, 0)))))
```

- 读取输入寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_write.svg">

```python
RS485_0.write('')
```

- 写入数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_write_line.svg">

```python
RS485_0.write(''+"\r\n")
```

- 按行写入数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_write_multiple_coils.svg">

```python
print((str('write multiple coils:') + str((RS485_0.write_multiple_coils(1, 1, 0)))))
```

- 写入多个线圈

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_write_multiple_registers.svg">

```python
print((str('write multiple register:') + str((RS485_0.write_multiple_registers(1, 1, 0, True)))))
```

- 写入多个寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_write_raw_data.svg">

```python
RS485_0.write(bytes([0, 0, 0]))
```

- 写入原始数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_write_single_coil.svg">

```python
print((str('write single coil:') + str((RS485_0.write_single_coil(1, 1, 0)))))
```

- 写入单个线圈

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/iso_rs485/uiflow_block_unit_iso485_write_single_register.svg">

```python
print((str('write single register:') + str((RS485_0.write_single_register(1, 1, 0, True)))))
```

- 写入单个寄存器

