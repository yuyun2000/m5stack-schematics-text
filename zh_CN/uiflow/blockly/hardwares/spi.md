# SPI


## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/spi/uiflow_block_spi_init.svg"> 

```python
spi2 = machine.SPI(1, 500000, sck=machine.Pin(-1), miso=machine.Pin(-1), mosi=machine.Pin(-1), firstbit=machine.SPI.MSB, polarity=0, phase=0)
```

- 初始化 SPI 接口，设置波特率、引脚和其他通信参数。
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/spi/uiflow_block_spi_deinit.svg"> 

```python
spi2.deinit()
```
 
- 取消初始化 SPI 接口，停止其工作并释放相关资源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/spi/uiflow_block_spi_write.svg"> 

```python
spi2.write(_)
```

- 通过 SPI 接口发送缓冲区 buf 中的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/spi/uiflow_block_spi_write_readinto.svg"> 

```python
spi2.write_readinto(_, _)
```

- 通过 SPI 接口发送 write_buf 中的数据，并同时接收数据到 read_buf 中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/spi/uiflow_block_spi_read.svg"> 

```python
str(spi2.read(0))
```

- 从 SPI 接口读取指定字节数的数据，并将其转换为字符串输出

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/spi/uiflow_block_spi_write_readinto.svg"> 

```python
spi2.readinto(_)
```

- 从 SPI 接口读取数据，并将其存储到缓冲区 buf 中

