# [Unit RFID](/zh_CN/unit/rfid)

## 案例程序

> 检测靠近的 IDCard 并返回数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rfid/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
rfid_0 = unit.get(unit.RFID, unit.PORTA)

while True:
  print(rfid_0.isCardOn())
  if rfid_0.isCardOn():
    print(rfid_0.readUid())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rfid/uiflow_block_rfid_cardOn.svg">

```python
print(rfid_0.isCardOn())
```

- RFID 卡片靠近返回1

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rfid/uiflow_block_rfid_readStr.svg">

```python
print(rfid_0.readBlockStr(1))
```

- 从地址读取数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rfid/uiflow_block_rfid_uid.svg">

```python
print(rfid_0.readUid())
```

- 返回 RFID 卡片的 UID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rfid/uiflow_block_write_block.svg">

```python
rfid_0.writeBlock(1,'M5Stack')
```

- 向地址写入数据