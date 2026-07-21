## UART

>通过UART发送和接收数据。

```python

# 创建串口实例
uart1 = machine.UART(1, tx=1, rx=3)

# 初始化串口
uart1.init(115200, bits=8, parity=None, stop=1)

# 缓存区中是否有内容
uart1.any()

# 读取缓存区中的内容
uart1.read()

# 向串口写入内容
uart1.write('Hello')

# 读/写案例
while True:
    if uart1.any():
        print(uart1.read())
        uart1.write('Hello')

```
