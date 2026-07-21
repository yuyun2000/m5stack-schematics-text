# Atom Printer

\#> 功能说明 | Atom Printer 的默认固件在配置 Wi-Fi 连接后将自动连接至服务器， 其他设备在 UiFlow 中可以通过使用 Atom Printer Block, 通过配置与设备一致的 token, 来实现远程打印控制。

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/atom_printer/uiflow_block_mqtt_printer_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from MediaTrans.Mqtt_Printer import Mqtt_Printer

setScreenColor(0x222222)
def buttonA_wasPressed():
  # global params
  mqtt.text_print('Hello', 10, 0)
  pass
btnA.wasPressed(buttonA_wasPressed)


mqtt = Mqtt_Printer('94:B9:7E:AC:41:81')
mqtt.start()
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/atom_printer/uiflow_block_mqtt_printer_set_topic.svg">

```python
from MediaTrans.Mqtt_Printer import Mqtt_Printer
mqtt = Mqtt_Printer('94:B9:7E:AC:41:81')
mqtt.start()
```

- 设置 Atom Printer 设备的 Topic (Mac 地址)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/atom_printer/uiflow_block_mqtt_printer_print_text.svg">

```python
mqtt.text_print('Hai', 10, 0)
```

- 控制打印文本信息， 并设置打印坐标位置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/atom_printer/uiflow_block_mqtt_printer_bar_print.svg">

```python
mqtt.bar_print('1234')
```

- 控制打印 BarCode

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/atom_printer/uiflow_block_mqtt_printer_qr_print.svg">

```python
mqtt.qr_print('1234')
```

- 控制打印 QRCode
