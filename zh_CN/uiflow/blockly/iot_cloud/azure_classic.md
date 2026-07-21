# Azure Classic

#>创建产品与设备|使用 UIFlow Azure Classic 功能前请通过[Azure IoT 中心](https://learn.microsoft.com/zh-cn/azure/iot-hub/create-hub?tabs=portal)完成产品和设备的创建。

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from IoTcloud.Azure import IoT_Hub
import json

import time
import unit

setScreenColor(0xffffff)
env21 = unit.get(unit.ENV2, unit.PORTA)
rgb1 = unit.get(unit.RGB, unit.PORTB)

msg = None
fun_msg = None
data = None
status = None
humid_data = None
temp_data = None

label0 = M5TextBox(13, 161, "Text", lcd.FONT_Default, 0x000000, rotate=0)
label1 = M5TextBox(0, 56, "Temp:", lcd.FONT_UNICODE, 0x000000, rotate=0)
label2 = M5TextBox(146, 56, "Humid:", lcd.FONT_UNICODE, 0x000000, rotate=0)
label3 = M5TextBox(80, 63, "Text", lcd.FONT_Default, 0x000000, rotate=0)
label4 = M5TextBox(230, 63, "Text", lcd.FONT_Default, 0x000000, rotate=0)
label5 = M5TextBox(0, 129, "Receive messages:", lcd.FONT_UNICODE, 0x000000, rotate=0)
label6 = M5TextBox(0, 95, "RGB:", lcd.FONT_UNICODE, 0x000000, rotate=0)
label7 = M5TextBox(80, 102, "Text", lcd.FONT_Default, 0x000000, rotate=0)
label8 = M5TextBox(55, 10, "UIFlow Azure IoT", lcd.FONT_UNICODE, 0x000000, rotate=0)

def azure_desired_cb(payload):
  global msg, fun_msg, data, status, humid_data, temp_data
  msg = payload
  label0.setText(str(msg))

def azure_direct_rgb(payload, rid):
  global msg, fun_msg, data, status, humid_data, temp_data
  fun_msg = payload
  label0.setText(str(fun_msg))
  if '"ON"' == fun_msg:
    label7.setText('ON')
    rgb1.setColorAll(0xffffff)
    azure.update_twin_reported_properties(rgb='ON')
    status = 204
  elif '"OFF"' == fun_msg:
    label7.setText('OFF')
    rgb1.setColorAll(0x000000)
    azure.update_twin_reported_properties(rgb='OFF')
    status = 204
  else:
    status = 400

  azure.response_direct_method(data, rid, body='success')

def azure_C2D_cb(msg_data):
  global msg, fun_msg, data, status, humid_data, temp_data
  msg = msg_data
  label0.setText(str(msg))
  pass

azure = IoT_Hub(connection_string='HostName=m5stack-iot.azure-devices.net;DeviceId=m5stack-uiflow;SharedAccessKey=9CpxoulAHSDX+wP2IlehvtDo3AYHNGNKpcDrVpQQVIo=')
azure.subscribe_twin_desired_response(azure_desired_cb)
azure.subscribe_direct_method('rgb', azure_direct_rgb)
azure.subscribe_C2D_message(azure_C2D_cb)
azure.start()
label0.setText(str(azure.retrieve_twin_properties()))
while True:
  humid_data = env21.humidity
  temp_data = env21.temperature
  label3.setText(str(temp_data))
  label4.setText(str(humid_data))
  data = {temp:temp_data,humid:humid_data}
  azure.publish_D2C_message(str((json.dumps(data))))
  wait(5)
  wait_ms(2)
```


## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_init_central.svg">

```python
from IoTcloud.Azure import IoT_Central
azure = IoT_Central(scope_id='', device_id='', device_key='')
```

- 初始化 Azure IoT Central 客户端信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_init_iothub.svg">

```python
from IoTcloud.Azure import IoT_Hub
azure = IoT_Hub(connection_string='')
```

- 初始化 Azure IoT Hub 客户端信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_start.svg">

```python
azure.start()
```

- 启用客户端连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_publish.svg">

```python
azure.publish_D2C_message(str(''))
```

- 发布数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_sub.svg">

```python
def azure_C2D_cb(msg_data):
  msg = msg_data
  pass

azure.subscribe_C2D_message(azure_C2D_cb)
```

- 订阅数据


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_retrieve_twin_property.svg">

```python
azure.update_twin_reported_properties(key1='value',key2='value')
```

- 上传数据至云端设备实例(Device Twin)


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_sub_direct.svg">

```python
def azure_direct_fun(payload, rid):
  global methodmsg
  methodmsg = payload

  azure.response_direct_method(0, rid, body='')

```

- direct_method 信息订阅

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_sub_twin_desired.svg">

```python
def azure_desired_cb(payload):
  msg = payload

azure.subscribe_twin_desired_response(azure_desired_cb)
```

- 上传数据至云端设备实例(Device Twin) 响应 callback

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/azure_classic/uiflow_block_azure_update_property.svg">

```python
azure.retrieve_twin_properties()
```

- 获取云端设备实例(Device Twin)拥有的属性

