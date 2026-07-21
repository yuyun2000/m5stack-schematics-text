# [Atomic QRCode2 Base](/zh_CN/atom/Atomic%20QRCode2%20Base)

## 案例程序

点击 ButtonA 按钮，点亮 QR-Code2 LED 灯，触发扫描，扫描成功输出数据到控制台。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.QRCode2 import QRCode2
import time

data = None

qrcode2 = QRCode2(1)

def qrcode2_event_cb(qrdata):
  global data
  data = qrdata
  print(data.decode())
  pass

qrcode2.set_event_cb(qrcode2_event_cb)

def buttonA_wasPressed():
  global data
  qrcode2.set_trigger_key()
  pass
btnA.wasPressed(buttonA_wasPressed)

print(qrcode2.get_firmware_version())
print(qrcode2.get_hardware_model())
qrcode2.set_light_brightness(75)
qrcode2.set_trigger_mode(0)

while True:
  qrcode2.event_poll_loop()
  wait_ms(100)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_init.svg">

```python
qrcode2 = QRCode2(1)
```

- 创建一个 QRCode2 对象，初始化硬件接口。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_get_baudrate.svg">

```python
print(qrcode2.get_baudrate())
```

- 获取当前的波特率(baud rate),返回 int 类型数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_get_data.svg">

```python
print(qrcode2.get_data(False))
```

- 获取当前存储的 QR 码数据。参数 False 用于指示是否对返回的数据进行处理。如果 QR 码已经成功读取，这将返回 QR 码中的数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_get_data_length.svg">

```python
print(qrcode2.get_data_length())
```

- 获取当前存储的 QR 码数据的长度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_get_firmware_version.svg">

```python
print(qrcode2.get_firmware_version())
```

- 获取固件版本型号。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_get_hardware_model.svg">

```python
print(qrcode2.get_hardware_model())
```

- 获取硬件型号。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_set_baudrate.svg">

```python
qrcode2.set_baudrate(115200)
```

- 设置波特率为 115200。配置串行通信的速率。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_set_light_brightness.svg">

```python
qrcode2.set_light_brightness(57)
```

- 设置 LED 辅助灯的亮度为 57%。以便在光线不足的情况下也能成功扫描 QR 码。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_set_trigger_cmd.svg">

```python
qrcode2.set_trigger_cmd(0x01)
```

- 设置触发模式。控制 QR 码扫描器的行为，例如是否连续扫描、单次扫描。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_set_trigger_key.svg">

```python
qrcode2.set_trigger_key()
```

- 设置或触发扫描动作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_set_trigger_mode.svg">

```python
qrcode2.set_trigger_mode(5)
```

- 设置 QR 码扫描设备的触发模式。AUTO：自动触发，MANUAL：手动触发。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_set_callback.svg">

```python
data = None

def qrcode2_event_cb(qrdata):
  global data
  data = qrdata
  pass
```

- 回调函数，扫描成功后触发，并获取扫描结果赋值变量 date。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/qrcode2/uiflow_block_atom_qrcode2_callback_in_loop.svg">

```python
while True:
  qrcode2.event_poll_loop()
  wait_ms(100)
  wait_ms(2)
```

- 轮询 QRCode2 模块以检查是否有新的 QR 码被扫描。
