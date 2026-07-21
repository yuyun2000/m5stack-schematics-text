# [Module LoRa868](/zh_CN/module/lora868)

## 案例程序

设置按钮A按下时发送字符串“Hello”，并定义接收回调函数以打印收到的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

packet_size = None
check = None

lora868 = module.get(module.LORA868)

def lora868_callback(size):
  global packet_size, check
  packet_size = size
  if packet_size:
    check = lora868.read_packet()
    print(check)
  pass

def buttonA_wasPressed():
  global packet_size, check
  lora868.set_begin_packet()
  lora868.write_packet([0x48, 0x65, 0x6C, 0x6C, 0x6F])
  lora868.set_end_packet()
  pass
btnA.wasPressed(buttonA_wasPressed)

lora868.init_lora_module(cs=5, rst=13, irq=34)
lora868.set_lora_config(freq=868000000, band=125000, TxPow=17, sync=0x34, spreadfactor=7, crate=5, preamble=8, CRC=False)
lora868.set_receive_callback_handler(lora868_callback)
```

## 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_init.svg">

```python
import module
lora868 = module.get(module.LORA868)
lora868.init_lora_module(cs=5, rst=13, irq=34)
```

- 初始化 LoRa 模组，并指定相关 CS, RST, IRQ 引脚


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_config.svg">

```python
lora868.set_lora_config(freq=868000000, band=125000, TxPow=17, sync=0x34, spreadfactor=7, crate=5, preamble=8, CRC=False)
```

- 初始化 LoRa 配置：
  - freq:工作频率
  - band:带宽：
    - 7.8 kHz
    - 10.4 kHz
    - 15.6 kHz
    - 20.8kHz
    - 31.25 kHz
    - 41.7 kHz
    - 62.5 kHz
    - 125 kHz
    - 250 kHz
    - 500 kHz
  - TxPow:发射功率：
    - 0-20dBm
  - sync:同步字
  - spreadfactor:扩频因子：
    - 6-12
  - crate:C/R 编码率：
    - C/5-8
  - preamble:前导码长度
  - CRC:是否开启 CRC 校验

- 详细配置参数含义与作用范围请参考[sx127x datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/sx1278.pdf)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_print_msg.svg">

```python
lora868.write_str_packet('')
```

- 发送字符串数据帧


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_begin_packet.svg">

```python
lora868.set_begin_packet()
```

- 初始化数据帧

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_write_buffer.svg">

```python
lora868.write_packet([0x48, 0x65, 0x6C, 0x6C, 0x6F])
```

- 向数据帧 buffer 写入数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_end_packet.svg">

```python
lora868.set_end_packet()
```

- 完成数据帧编辑， 执行发送


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_receive_callback.svg">

```python
lora868.set_receive_callback_handler(lora868_callback)
```

- 初始化接收回调函数


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_callback.svg">

```python
def lora868_callback(size):
  global packet_size
  packet_size = size
  pass
```

- 定义接收回调函数， 传入值为数据帧数据大小。并通过下方数据读取， RSSI 读取， SNR 读取等相关 API, 在 callback 中获取数据帧内容。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_message.svg">

```python
lora868.read_str_packet()
```

- 接收数据， 并转换为字符串


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_read.svg">

```python
lora868.read_packet()
```

- 接收原始数据 Bytearray


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_packet_rssi.svg">

```python
lora868.get_rssi()
```

- 获取当前数据帧 RSSI 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_packet_snr.svg">

```python
lora868.get_snr()
```

- 获取当前数据帧 SNR 值


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_sleep_mode.svg">

```python
lora868.set_sleep_mode()
```

- 进入睡眠模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lora868/uiflow_block_lora868_stand_by_mode.svg">

```python
lora868.set_standby_mode()
```

- 进入待机模式

