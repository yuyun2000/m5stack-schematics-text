# [Module COMMU](/zh_CN/module/commu)

## 案例程序

初始化 CAN、I2C 和 RS485 通信模块，然后在循环中根据中断和数据状态进行读取和处理，生成随机数据并通过 CAN 和 RS485 发送，同时进行 I2C 设备的扫描与状态检测

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_commu_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module
import time

setScreenColor(0x3a3a3a)
rand = None
temp_data = None

com = module.get(module.COMMU)

import random

com.commu_can_init(3, 15)
i2c = com.commu_i2c_init(21, 22, 0x44, 100000)
rs485 = com.commu_uart_init(2, 17, 16, 115200, 8, None, 1)
print((str('I2C Device:') + str((i2c.scan()))))
while True:
  if com.commu_can_interrupt_occur():
    print((str('CAN Message:') + str((com.commu_can_read_message(1)))))
    print((str('CAN ID:') + str((com.commu_can_id))))
  if i2c.available():
    print('TRUE')
    print((str('I2C Device:') + str((i2c.scan()))))
  else:
    print('FALSE')
  if rs485.any():
    print((str('RS485 Data:') + str((rs485.read()).decode())))
  rand = random.randint(10000000, 16777215)
  wait(1)
  temp_data = [(rand & 0xff0000) >> 16, (rand & 0x00ff00) >> 8, rand & 0xff]
  com.commu_can_send_message(0x100, temp_data)
  print((str('temp data:') + str(temp_data)))
  wait(1)
  rs485.write(str(rand))
  print((str('rand data:') + str(rand)))
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_available_msg.svg">

```python
com.commu_can_available_message()
```

- 检查 CAN 总线上是否有可用的消息。如果有可用消息，它会返回 True，否则返回 False。这通常用于判断是否有新数据需要读取

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_clear_interrupt.svg">

```python
com.commu_can_clear_interrupts()
```

- 清除 CAN 模块的中断标志。这通常用于重置中断状态，以便 CAN 模块可以继续处理新的中断或消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_config_rate.svg">

```python
com.commu_can_config_rate(15)
```

- 配置 CAN 总线的通信速率。你可以选择不同的速率(如500KBPS)来匹配你的网络设置。这对于确保通信的稳定性和兼容性非常重要

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_debug.svg">

```python
com.commu_can_debug(True)
```

- 启用或禁用 CAN 模块的调试信息输出。启用后，调试信息会被打印出来，通常用于诊断和调试 CAN 通信问题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_init.svg">

```python
com.commu_can_init(3, 15)
```

- 初始化 CAN 模块，设置工作模式和通信速率。你可以选择不同的模式(如 ANY 模式)和速率(如500KBPS)，以适应不同的应用需求

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_interrupt_occur.svg">

```python
com.commu_can_interrupt_occur()
```

- 检查 CAN 模块的中断引脚是否发生了中断。如果发生中断，它会返回 True，否则返回 False。这个块用于检测中断事件的发生，以便在需要时处理它们

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_read_msg.svg">

```python
com.commu_can_read_message(1)
```

- 从 CAN 总线上读取消息。你可以选择读取的消息类型(如 LIST)，以获取当前总线上传输的数据。这是从 CAN 总线接收数据的关键步骤

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_remote_id.svg">

```python
com.commu_can_id
```

- 发送远程帧请求以请求带有特定 CAN ID 的设备返回数据。这在需要从其他节点获取特定信息时非常有用

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_reset.svg">

```python
com.commu_can_reset()
```

- 重置 CAN 模块，将其恢复到初始状态。这通常用于清除错误或重新初始化 CAN 模块，以确保正常运行

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_send_msg.svg">

```python
com.commu_can_send_message(0x100, [0, 0, 0])
```

- 发送一条带有特定 CAN ID 的数据消息到 CAN 总线。你可以定义数据列表，以决定要发送的数据内容。这是进行设备间通信的主要方法

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_can_set_mode.svg">

```python
com.commu_can_set_mode(0x00)
```

- 将 CAN 模块设置为“NORMAL”模式。这意味着 CAN 模块将正常参与总线上的通信，而不是处于静默或仅接收模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_available.svg">

```python
i2c.available()
```

- 检查在 I2C 总线上的可用地址，并将它们返回为一个列表。这个块有助于检测连接到 I2C 总线的设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_get_data_in_list.svg">

```python
[][0]
```

- 从列表中的索引位置获取数据。在此示例中，它将从索引 0 中获取数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_init.svg">

```python
com.commu_i2c_init(21, 22, 0x50, 100000)
```

- 初始化 I2C 总线，定义数据线 (SDA) 和时钟线 (SCL) 的引脚、设备地址 (0x50) 和通信频率 (100000 Hz)。这个块用于设置 I2C 通信的参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_read_data.svg">

```python
i2c.read_data(0, i2c_bus.UINT8LE)
```

- 从 I2C 设备读取数据。你可以指定读取的数据量(num)和数据类型(UINT8LE 表示无符号8位小端数据)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_read_mem_data.svg">

```python
i2c.read_mem_data(0, 0, i2c_bus.UINT8LE)
```

- 从 I2C 设备的指定寄存器(reg)读取指定数量的数据(num)，数据类型为 UINT8LE。此块通常用于从设备的特定寄存器中读取数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_read_reg.svg">

```python
i2c.read_reg(0x00, 0)
```

- 从寄存器 0x00 开始读取指定字节数的数据。在此示例中，它尝试读取 0 字节的数据。通常用于从 I2C 设备的寄存器中读取少量数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_read_req.svg">

```python
i2c.read_u8(0x00)
```

- 从寄存器 0x00 读取一个字节的数据。此块直接读取一个字节的信息，适用于读取单字节寄存器值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_read_res.svg">

```python
i2c.read_u16(0x00, byteorder="big")
```

- 从寄存器 0x00 读取一个短数据(两个字节)，并以大端格式进行解码(big)。大端解码意味着高位字节在前

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_scan.svg">

```python
i2c.scan()
```

- 扫描 I2C 总线上连接的所有设备，返回检测到的设备地址。这个块用于检查 I2C 总线上的设备是否连接和通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_write_big.svg">

```python
i2c.write_u16(0x00, 0x0000, byteorder="big")
```

- 将一个短数据(两个字节)0x0000 写入寄存器 0x00，并以大端格式编码(big)。大端编码意味着数据的高位字节先写入

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_write_byte.svg">

```python
i2c.write_u8(0x00, 0x00)
```

- 将一个字节 0x00 写入寄存器 0x00。此块用于写入单个字节的数据到特定寄存器中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_write_data.svg">

```python
i2c.write_data(0, i2c_bus.UINT8LE)
```

- 将指定类型的数据 0 写入设备，数据类型为 UINT8LE(8位无符号整数，使用小端格式)。这通常用于写入通用数据，而不指定寄存器地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_write_mem_data.svg">

```python
i2c.write_mem_data(0, 0, i2c_bus.UINT8LE)
```

- 将数据 0 写入寄存器 0，数据类型为 UINT8LE(8位无符号整数，小端格式)。此块用于将特定类型的数据写入指定的寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_i2c_write_mem_list.svg">

```python
i2c.write_mem_list(0, [0, 0, 0])
```

- 将一个列表中的字节(在这里是 [0, 0, 0])写入寄存器 0。此块用于将多个字节的数据一次性写入指定的寄存器地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_uart_any.svg">

```python
uart.any()
```

- 此块用于检查 UART 接口中是否有剩余的数据在缓存中。它通常用于处理连续的数据传输，确保缓存的数据都被读取或处理

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_uart_init.svg">

```python
com.commu_uart_init(1, 1, 3, 9600, 8, None, 1)
```

- 初始化 UART 端口(端口编号 1)，使用指定的配置进行串行通信。这里配置为：发送引脚 Tx pin 为 1，接收引脚 Rx pin 为 3，波特率为 9600，数据位数 8，无校验位，停止位 1

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_uart_read.svg">

```python
uart.read()
```

- 读取 UART 接口中的所有可用数据。此块通常用于接收完整的数据帧或读取连续发送的数据流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_uart_readline.svg">

```python
uart.readline()
```

- 读取 UART 接口中的一行数据，直到遇到换行符为止。这通常用于逐行读取串口传输的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_uart_read_characters.svg">

```python
uart.read(0)
```

- 从 UART 接口读取指定字节数的数据。在这个例子中，读取 0 字节的数据，实际使用时应设置要读取的字节数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_uart_write.svg">

```python
uart.write('')
```

- 将指定的字符串数据通过 UART 接口发送出去。这个块用于向串行设备发送文本或命令

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_uart_write_line.svg">

```python
uart.write(''+"\r\n")
```

- 将指定的字符串数据作为一行写入 UART 接口，并在末尾自动添加换行符。这通常用于发送一行文本数据，类似于 println 功能

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/commu/uiflow_block_module_commu_uart_write_raw_data.svg">

```python
uart.write(bytes([0, 0, 0]))
```

- 该块用于通过 UART 接口发送原始数据列表。你可以创建一个包含多个字节的列表，然后将这些字节数据通过 UART 发送出去。这通常用于需要发送二进制数据或特定格式数据的应用场景
