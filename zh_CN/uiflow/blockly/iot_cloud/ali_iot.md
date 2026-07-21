# Ali IoT

\#> 创建产品与设备 | 使用 UIFlow Ali IoT 功能前请参考[Ali 物联网平台文档](https://help.aliyun.com/zh/iot/getting-started/overview-7?spm=a2c4g.11186623.0.i9)完成产品和设备的创建。

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from IoTcloud.Ali import AliIoT
import json

import time
import unit

setScreenColor(0x222222)
env2_0 = unit.get(unit.ENV2, unit.PORTA)

shadow_msg = None
raw_msg = None
user_msg = None

label0 = M5TextBox(16, 17, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)

def shadow_get_cb(payload):
  global shadow_msg, raw_msg, user_msg
  shadow_msg = payload
  label0.setText(str(shadow_msg))
  pass

def raw_down_cb(payload):
  global shadow_msg, raw_msg, user_msg
  raw_msg = payload
  label0.setText(str(raw_msg))
  pass

def user_get_cb(payload):
  global shadow_msg, raw_msg, user_msg
  user_msg = payload
  label0.setText(str(user_msg))
  pass


ali = AliIoT(device_id='223', product_key='a1kJNBURsxj', device_name='ENV_UNIT', region_id='cn-shanghai', password='CB57870ED7708E24863DF9A7BD8A65BE')
ali.subscribe_shadow_get_msg(shadow_get_cb)
ali.subscribe_raw_down_msg(raw_down_cb)
ali.subscribe_user_get_msg(user_get_cb)
ali.start()
while True:
  ali.publish_user_update_msg(str((json.dumps(({'Pressure':(env2_0.pressure),'Temperature':(env2_0.temperature),'Humidity':(env2_0.humidity)})))))
  ali.publish_shadow_update_msg(desiredStr='DEVICE_STATE')
  ali.publish_raw_up_msg(str('RAW MSG'))
  wait(3)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_init.svg">

```python
from IoTcloud.Ali import AliIoT
ali = AliIoT(device_id='', product_key='', device_name='', region_id='cn-qingdao', password='')
```

- 初始化客户端信息：
  - device_id, product_key, device_name 字段在 Aliyun 控制台中完成设备创建后生成。
  - region_id: 选择服务实例所在的区域，该信息会在阿里云控制台中显示。
  - password: 填入到 block 后将自动计算生成， UiFlow 中可切换至代码工作区进行查看。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_start.svg">

```python
ali.start()
```

- 启用客户端连接

\#> 消息发布与订阅 | UIFlow Ali IoT 目前提供了三种上下行的主题订阅，user、raw、shadow update。<br/>不同的主题订阅在阿里云控制台中的作用和显示方式会有所不同，例如 user 可以用于一般数据的交互， shadow update 主要用于设备状态的同步，raw 类型的主题数据，允许用户在阿里云控制台配置自定义的脚本去对数据进行处理。[了解更多详情， 请查看阿里云物联网文档页面](https://help.aliyun.com/zh/iot/getting-started/create-a-product-and-add-a-device?spm=a2c4g.11174283.2.2.2b5b4c07rTCDtX)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_publish_raw.svg">

```python
ali.publish_raw_up_msg(str('RAW MSG'))
```

- 发布 raw 类型消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_publish_shadow.svg">

```python
ali.publish_shadow_update_msg(desiredStr='DEVICE_STATE')
```

- 发布 shadow 设备状态消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_publish_user.svg">

```python
ali.publish_user_update_msg(str((json.dumps(({'Pressure':(env2_0.pressure),'Temperature':(env2_0.temperature),'Humidity':(env2_0.humidity)})))))
```

- 发布 user 常规消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_sub_raw.svg">

```python
def raw_down_cb(payload):
  global shadow_msg, raw_msg, user_msg
  raw_msg = payload
  pass

ali.subscribe_raw_down_msg(raw_down_cb)
```

- 订阅 raw 类型消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_sub_shadow.svg">

```python
def shadow_get_cb(payload):
  global shadow_msg, raw_msg, user_msg
  shadow_msg = payload
  pass

ali.subscribe_shadow_get_msg(shadow_get_cb)
```

- 订阅 shadow 设备状态消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/ali_iot/uiflow_block_aliiot_sub_user.svg">

```python
def user_get_cb(payload):
  global shadow_msg, raw_msg, user_msg
  user_msg = payload
  pass


ali.subscribe_user_get_msg(user_get_cb)
```

- 订阅 user 常规消息
