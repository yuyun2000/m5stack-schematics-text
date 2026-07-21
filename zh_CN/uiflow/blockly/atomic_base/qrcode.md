# [Atomic QRCode Base](/zh_CN/atom/ATOM%20QR-CODE_v1.1(Excluding%20Atom))

## 案例程序

实现按钮控制的二维码扫描功能，按下按钮A时启动扫描，松开后停止

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode/uiflow_block_base_qrcode_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.QRCode import QRCode

scan_data = None

qr = QRCode()
while True:
  if btnA.isPressed():
    qr.trigger(0)
  else:
    qr.trigger(1)
  if qr.status():
    scan_data = qr.read()
    if scan_data != None:
      print(scan_data)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode/uiflow_block_base_qrcode_init.svg">

```python
from base.QRCode import QRCode
qr = QRCode()
```

- 初始化 Atomic QRCode

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode/uiflow_block_base_qrcode_trigger.svg">

```python
qr.trigger(control)
```

- QRCode 扫描控制：
  - ON: 0
  - OFF: 1


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode/uiflow_block_base_qrcode_status.svg">

```python
qr.status()
```

- QRCode 扫描状态：
  - True: 扫描成功
  - False: 未扫描到内容

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode/uiflow_block_base_qrcode_read.svg">

```python
qr.read()
```

- 读取扫描结果字符串

