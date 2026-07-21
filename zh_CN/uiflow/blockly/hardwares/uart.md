# UART

## 案例程序

不断地在 uart1 和 uart2 之间交换数据，实现双向通信。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart_demo.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x292929)

label0 = M5TextBox(15, 106, "Slave Baud", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(12, 130, "115200", lcd.FONT_DejaVu40, 0x02c7fc, rotate=0)
label2 = M5TextBox(15, 20, "TX", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label3 = M5TextBox(139, 20, "RX", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label4 = M5TextBox(12, 40, "G17", lcd.FONT_DejaVu40, 0x00ff38, rotate=0)
label5 = M5TextBox(136, 40, "G16", lcd.FONT_DejaVu40, 0x00ff38, rotate=0)
label9 = M5TextBox(173, 106, "/", lcd.FONT_DejaVu72, 0xFFFFFF, rotate=0)
label10 = M5TextBox(199, 125, "PC default baud", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label11 = M5TextBox(224, 149, "115200", lcd.FONT_Default, 0xFFFFFF, rotate=0)

uart1 = machine.UART(1, tx=1, rx=3)
uart1.init(115200, bits=8, parity=None, stop=1)
uart2 = machine.UART(2, tx=17, rx=16)
uart2.init(115200, bits=8, parity=None, stop=1)
while True:
  if uart1.any():
    uart2.write(bytes(uart1.read()))
  if uart2.any():
    uart1.write(bytes(uart2.read()))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart.svg"> 

```python
uart1 = machine.UART(1, tx=14, rx=13)
uart1.init(9600, bits=8, parity=None, stop=1)
```

- 设置发送和接收引脚，并配置通信参数(波特率、数据位、奇偶校验和停止位)进行串行通信
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart_write_line.svg"> 

```python
uart1.write(''+"\r\n")
```
 
- 通过 uart1 发送字符串，然后发送回车换行符，以表示这一行的结束

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart_write.svg"> 

```python
uart1.write('')
```

- 通过 uart1 发送字符串 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart_write_raw_data.svg"> 

```python
uart1.write(bytes([0, 0, 0]))
```

- 通过 UART1 发送一个包含三个字节值的数组

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart_read.svg"> 

```python
str(uart1.read())
```

- 读取 UART1 接收的数据并将其转换为字符串形式输出


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart_read_characters.svg"> 

```python
label0.set_text(str(uart1.read(10)))
```

- 读取 UART1 接收的字节的数据，将其转换为字符串
  - "10":设置最大字节数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart_readline.svg"> 

```python
str(uart1.readline())
```

- 读取 UART1 接收的一行数据，并将其转换为字符串形式输出


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/uart/uiflow_block_uart_any.svg"> 

```python
str(uart1.any())
```

- 检查 UART1 接收缓冲区中是否有数据可读，并将结果转换为字符串形式输出


