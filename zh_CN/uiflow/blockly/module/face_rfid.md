# [Faces RFID](/zh_CN/module/faces_rfid)

## 案例程序

检测是否有 RFID 卡靠近，读取卡的 UID 和指定地址的字符串，并将"rfid"字符串写入卡片的地址1

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_rfid/uiflow_block_face_rfid_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import face

setScreenColor(0x222222)

faces_rfid = face.get(face.RFID)

while True:
  print((str('status：') + str((faces_rfid.isCardOn()))))
  print((str('read card：') + str((faces_rfid.readBlockStr((faces_rfid.isCardOn()))))))
  print((str('uid：') + str((faces_rfid.readUid()))))
  faces_rfid.writeBlock(1,'rfid')
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_rfid/uiflow_block_faces_rfid_cardOn.svg">

```python
faces_rfid.isCardOn()
```

- 检查 RFID 卡是否接近读取器。如果有卡片接近，系统会触发相应的操作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_rfid/uiflow_block_faces_rfid_readStr.svg">

```python
faces_rfid.readBlockStr((faces_rfid.isCardOn()
```

- 读取存储在 RFID 卡中某个地址的字符串信息。地址是 RFID 卡内存中的一个位置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_rfid/uiflow_block_faces_rfid_uid.svg">

```python
faces_rfid.readUid()
```

- 提取当前读取的 RFID 卡的 UID，这个 UID 是唯一的，可以用来唯一标识一张卡片

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_rfid/uiflow_block_faces_write_block.svg">

```python
faces_rfid.writeBlock(1,'rfid')
```

- 将指定的字符串数据写入到 RFID 卡的特定存储地址。写入的数据可以是任何文本信息

