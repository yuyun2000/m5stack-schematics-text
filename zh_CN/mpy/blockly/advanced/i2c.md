## I2C

>I2C通信,读写寄存器。

### Scan地址

```python

import i2c_bus

#i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, addr, freq=400000)

i2c0 = i2c_bus.easyI2C((sda, scl), 0x68, freq=400000)

# True or False
if i2c0.available():
    print(i2c0.available())
    # return a list
    print(i2c0.scan())

```

### 读/写寄存器 v1

```python

#向reg写入1个byte
i2c0.write_u8(reg, data)

#向reg连续写入2个byte
i2c0.write_u16(reg, data, byteorder='big')

#向reg连续写入4个byte
i2c0.write_u32(reg, data, byteorder='big')

#读取reg1个byte
i2c0.read_u8(reg)

#连续读取reg2个byte
i2c0.read_u16(reg, byteorder='big')

#连续读取reg4个byte
i2c0.read_u32(reg, byteorder='big')

#连续读取N个byte
i2c0.read(num)

#连续读取reg N个byte
i2c0.read_reg(reg, num)

#大小端模式
#byteorder = "little" or "big"(default)

```

### 读/写寄存器 v2

```python

#format_type
# UINT8LE
# UINT16LE
# UINT32LE
# INT8LE
# INT16LE
# INT32LE
# UINT8BE
# UINT16BE
# UINT32BE
# INT8BE
# INT16BE
# INT32BE

#向reg写入1个指定类型数据
i2c0.write_mem_data(reg, data, format_type)

#写入1个指定类型数据
i2c0.write_data(data, format_type)

#向reg连续写入List中的数据
i2c0.write_list(data)

#向reg连续写入N个指定类型数据
i2c0.write_mem_list(reg, data, num)

#连续读取1个指定类型数据
i2c0.read_data(num, format_type)

#连续读取reg N个指定类型数据
i2c0.read_mem_data(reg, num, format_type)

```

### 案例程序

- 读取DHT12传感器温湿度数值

```python
import i2c_bus
import time

i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x5C, freq=400000)
while True:
  hum = i2c0.read_mem_data(0x00, 2, i2c_bus.INT8LE)
  print(hum[0]+hum[1]*0.1)
  wait_ms(100)
  tem = i2c0.read_mem_data(0x02, 2, i2c_bus.INT8LE)
  print(tem[0]+tem[1]*0.1)
  wait_ms(100)
```