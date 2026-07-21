# [Unit UHF-RFID](/zh_CN/unit/uhf_rfid)

## 案例程序

实现标签读取与数据锁定的完整流程

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_rfiduhf_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
uhf_rfid_0 = unit.get(unit.UHF_RFID, unit.PORTC)

epc_no = None

uhf_rfid_0.set_region(uhf_rfid_0.REGIN_CN_800MHZ)
uhf_rfid_0.automatic_freq_hopping(0x00)
print(uhf_rfid_0.get_region())
print(uhf_rfid_0.get_channel_freq())
epc_no = 0
while not epc_no:
  epc_no = uhf_rfid_0.single_polling()
print(epc_no)
while not (uhf_rfid_0.select_tag_param(epc_no)):
  pass
print(uhf_rfid_0.get_select_tag_param())
epc_no = 0
while not epc_no:
  epc_no = uhf_rfid_0.read_memory_bank(2, 2, 0x00, 'FFFF3333')
print(epc_no[0])
print(epc_no[1])
epc_no = 0
while not epc_no:
  epc_no = uhf_rfid_0.lock_data_store(0, 2, 2, 0, 0, 0, 1, 1, 0, 0, 'FFFF3333')
print('Lock Success')
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_uart_init.svg">

```python
uhf_rfid_0.uart_port_id(1)
```

- 模块 UART 接口初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_automatic_freq_hopping.svg">

```python
uhf_rfid_0.automatic_freq_hopping(0xFF)
```

- 模块自动跳频

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_get_channel_freq.svg">

```python
print((str('freq:') + str((uhf_rfid_0.get_channel_freq()))))
```

- 获取模块信道频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_get_device_info.svg">

```python
print((str('info:') + str((uhf_rfid_0.get_device_info(0x00)))))
```

- 获取模块设备信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_get_region.svg">

```python
print((str('code:') + str((uhf_rfid_0.get_region()))))
```

- 获取模块工作区域

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_get_select_tag_param.svg">

```python
print((str('tag:') + str((uhf_rfid_0.get_select_tag_param()))))
```

- 获取模块选卡参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_get_tx_power.svg">

```python
print((str('tx:') + str((uhf_rfid_0.get_tx_power()))))
```

- 获取模块发射功率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_lock_data_store.svg">

```python
print(uhf_rfid_0.lock_data_store(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ''))
```

- 锁定模块数据存储区

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_multiple_polling_stop.svg">

```python
uhf_rfid_0.multiple_polling_stop()
```

- 停止模块多标签轮询

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_multi_reading_count.svg">

```python
def uhf_rfid_eQuAncb(epc_no, dBm):
  global EPC1, dBm1
  EPC1 = epc_no
  dBm1 = dBm
  pass


print(uhf_rfid_0.multiple_polling_read(uhf_rfid_eQuAncb, 100))
```

- 模块多标签读取计数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_read_memory.svg">

```python
print(uhf_rfid_0.read_memory_bank(0, 0, 0x00, ''))
```

- 读取模块存储器数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_set_channel_freq.svg">

```python
uhf_rfid_0.set_channel_freq(920.375)
```

- 设置模块信道频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_set_region.svg">

```python
uhf_rfid_0.set_region(uhf_rfid_0.REGIN_CN_900MHZ)
```

- 设置模块工作区域

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_set_select_mode.svg">

```python
uhf_rfid_0.set_select_mode(0x00)
```

- 设置模块选卡模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_set_select_tag.svg">

```python
print((str('param:') + str((uhf_rfid_0.select_tag_param('EPC')))))
```

- 设置模块选卡

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_set_tx_power.svg">

```python
uhf_rfid_0.set_tx_power(0)
```

- 设置模块发射功率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_single_polling.svg">

```python
print((str('reading:') + str((uhf_rfid_0.single_polling()))))
```

- 模块单标签轮询

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_sleep.svg">

```python
uhf_rfid_0.sleep()
```

- 模块进入休眠状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_wakeup.svg">

```python
uhf_rfid_0.wakeup()
```

- 唤醒模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_write_custom_command.svg">

```python
print((str('list:') + str((uhf_rfid_0.write_customer_command([0, 0, 0], True)))))
```

- 向模块写入自定义命令

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uhf_rfid/uiflow_block_uhf_rfid_write_memory.svg">

```python
print(uhf_rfid_0.write_memory_bank('', 0, 0x00, ''))
```

- 向模块存储器写入数据
