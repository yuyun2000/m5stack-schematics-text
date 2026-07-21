# AWS

#>创建产品与设备|使用 UIFlow AWS 功能前请通过[AWS Management Console](https://aws.amazon.com/)完成产品和设备的创建。

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/aws/uiflow_block_aws_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
from IoTcloud.AWS import AWS
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

label0 = M5Label('Text', x=40, y=42, color=0x000, font=FONT_MONT_38, parent=None)
label1 = M5Label('Text', x=43, y=134, color=0x000, font=FONT_MONT_38, parent=None)

def fun_subtopic_(topic_data):
  # global params
  label0.set_text(str(topic_data))
  pass

aws = AWS(things_name='UIFlow_TEST', host='，xxxx-ats.iot.ap-southeast-1.amazonaws.com', port=8883, keepalive=60, cert_file_path="/flash/res/certificate.pem.crt", private_key_path="/flash/res/private.pem.key")
aws.subscribe(str('subtopic'), fun_subtopic_)
aws.start()
while True:
  aws.publish(str('pubtopic'),str('hello'))
  wait(4)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/aws/uiflow_block_aws_init.svg">


```python
from IoTcloud.AWS import AWS
aws = AWS(things_name='', host='', port=0, keepalive=0, cert_file_path='', private_key_path='')
```

- 初始化客户端信息：
  - 点击初始化 block 的添加按钮，依次导入设备证书(Device certificate)+设备私钥(Private Key File), 注意： 默认的密钥和证书文件名过长，尽可能将其进行修改为较短的字符串
  - things name 为我们的创建的设备名称，需要与 AWS Management Console 中的名称保持一致
  - 复制 AWS Management Console->Settings 中的 Endpoint 字段， 将其填入到 HOST 参数中
  - 端口参数我们使用 MQTT 服务端口8883
  - keepalive 为60 
  - 有关更多服务端口信息请参考[AWS 官方文档](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html?icmpid=docs_iot_console).


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/aws/uiflow_block_aws_start.svg">

```python
aws.start()
```

- 启用客户端连接


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/aws/uiflow_block_aws_publish.svg">

```python
aws.publish(topic,msg)
```

- 消息发布

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/aws/uiflow_block_aws_sub.svg">

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/iot_cloud/aws/uiflow_block_aws_get_topic_data.svg">

```python
def fun_subtopic_(topic_data):
  # global params
  print(topic_data)
  pass

```

- 消息订阅回调函数

