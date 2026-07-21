# [Unit QRCode](/zh_CN/unit/Unit-QRCode)

## 案例程序

> 自动扫描二维码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
qrcode_0 = unit.get(unit.QRCODE, unit.PORTA)

qrcode_0.init_device_mode(0, 0x21)
qrcode_0.set_trigger_mode(0)
qrcode_0.set_manual_scan(1)
while True:
  if qrcode_0.get_qrcode_data_status():
    print(qrcode_0.get_qrcode_data(False))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_init_mode.svg">

```python
qrcode_0.init_device_mode(0, 0x21)
```

- 创建 QRCode Unit 对象

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_clear_current_data_status.svg">

```python
qrcode_0.clear_qrcode_data_status()
```

- 清除 QRCode Unit 触发标志

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_get_current_data_status.svg">

```python
print(qrcode_0.get_qrcode_data_status())
```

- 获取自动或手动触发模式状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_get_data_format.svg">

```python
print(qrcode_0.get_qrcode_data(False))
```

- 扫描二维码并获取字符串中的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_get_data_length.svg">

```python
print(qrcode_0.get_qrcode_data_length())
```

- 扫描二维码并获取可用数据长度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_get_device_info.svg">

```python
print(qrcode_0.get_device_info(0xFE))
```

- 获取此设备的固件版本详细信息和 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_get_trigger_button.svg">

```python
print(qrcode_0.get_trigger_button_status())
```

- 获取触发按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_get_trigger_mode.svg">

```python
print(qrcode_0.get_trigger_mode())
```

- 获取自动或手动触发模式状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_set_i2c_address.svg">

```python
qrcode_0.set_device_i2c_address(0x21)
```

- 用户可以更改 i2c 地址，此地址应介于 0x01 和 0x7F 之间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_set_manual_scan.svg">

```python
qrcode_0.set_manual_scan(1)
```

- 设置手动扫描方式
  - 1：start 关闭
  - 0：stop 打开

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/qrcode/uiflow_block_unit_qrcode_set_trigger_mode.svg">

```python
qrcode_0.set_trigger_mode(0)
```

- 将触发模式设置为自动或手动(键)
  - 0：AUTO 自动
  - 1：MANUAL 手动
