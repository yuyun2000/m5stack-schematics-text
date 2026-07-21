# I2C Master

## 案例程序

扫描 i2c 设备地址并打印到串口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_i2c_master_demo.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import i2c_bus

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
 i2c_bus.easyI2C(i2c_bus.PORTA, 0x00, freq=400000)
i2c0.addr=(0x68)
print(i2c0.scan())
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_set.svg"> 

```python
i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x00, freq=400000)
```

- 在 PORTA 上初始化一个 I2C 总线，设置通信频率
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_set_C.svg"> 

```python
i2c0 = i2c_bus.easyI2C((0, 0), 0x00, freq=400000)
```
 
- 在指定的 GPIO 引脚上初始化一个 I2C 总线，设置设备地址和通信频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_set_slave_addr.svg"> 

```python
i2c0.addr=(0x68)
```

- 设置 i2c 通讯地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_available.svg"> 

```python
str(i2c0.available())
```

- 检查 i2c0 总线上的设备是否可用，并将结果转换为字符串形式输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_scan.svg"> 

```python
str(i2c0.scan())
```

- 扫描 i2c0 总线上的所有 I2C 设备，并将找到的设备地址列表转换为字符串形式输出。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_read_req.svg"> 

```python
str(i2c0.read_u8((i2c0.scan())))
```

- 从扫描到的 I2C 设备中读取一个字节的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_read_res.svg"> 

```python
str(i2c0.read_u16(0x00, byteorder="big"))
```

- 从指定的 I2C 设备地址读取 16 位数据(按大端或小端字节顺序)，并将其转换为字符串形式输出


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_read_reg.svg"> 

```python
str(i2c0.read_reg(0x00, 0))
```

- 从指定的 I2C 设备地址和寄存器中读取指定字节数的数据，并将其转换为字符串输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_read_mem_data.svg"> 

```python
str(i2c0.read_mem_data(0, 0, i2c_bus.UINT8LE))
```

- 从指定的 I2C 设备地址和寄存器中读取指定类型的数据，并将其转换为字符串输出。数据类型可以选择为 UINT8LE、UINT16LE、UINT32LE 等。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_read_data.svg"> 

```python
str(i2c0.read_data(0, i2c_bus.UINT8LE))
```

- 从指定的 I2C 设备地址读取指定类型的数据，并将其转换为字符串输出。数据类型可以选择为 UINT8LE、UINT16LE、UINT32LE 等。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_get_data_in_list.svg"> 

```python
str([][0])
```

- 从列表 data_list 中获取指定索引的元素，并将其转换为字符串输出

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_write_byte.svg"> 

```python
i2c0.write_u8(0x00, 0x00)
```

- 向指定的 I2C 设备寄存器写入一个字节的数据


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_write_big.svg"> 

```python
i2c0.write_u16(0x00, 0x0000, byteorder="big")
```

- 向指定的 I2C 设备寄存器写入一个 16 位的数据，可以选择大端或小端字节序进行编码


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_write_mem_data.svg"> 

```python
i2c0.write_mem_data(0, 0, i2c_bus.UINT8LE)
```

- 向 I2C 设备的寄存器地址 0 写入一个 UINT8LE 类型的数据 0。数据类型可以根据需要选择为 UINT8LE、UINT16LE、UINT32LE 等

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_write_data.svg"> 

```python
i2c0.write_data(0, i2c_bus.UINT8LE)
```

- 向 I2C 设备发送指定类型的数据


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/i2c%20master/uiflow_block_iic_write_mem_list.svg"> 

```python
i2c0.write_mem_list(0, [0, 0, 0])
```

- 向指定的 I2C 设备寄存器写入字节数据列表