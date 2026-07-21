# Remote

\#> 简介 | 通过 Remote 功能创建一个由控件组成的网页，可用于远程控制 M5Stack 设备。该页面与设备的 API KEY 相关联，将长期保存在 M5 服务中，并提供固定的访问链接，用户可随时随地访问与分享设备信息或远程操控设备。<br/>注意事项：<br/>1. 该功能需使用在线版 UiFlow<br/>2. 离线下载运行时，需添加 WiFi 连接程序至 setup. [查看 WiFi 连接程序说明](/zh_CN/uiflow/blockly/hardwares/network)<br/>3. 使用前需先推送程序，然后才可以获取访问页面的二维码 / URL

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote/uiflow_block_remote_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
remoteInit()

setScreenColor(0x111111)

x = None

def _remote_ON_OFF(x):
  if x == 1:
    rgb.setColorAll(0x3333ff)
  else:
    rgb.setColorAll(0x000000)

def _remote_Bright(x):
  rgb.setBrightness(x)


lcd.qrcode('http://flow-remote.m5stack.com/?remote=undefined', 72, 32, 176)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote/uiflow_block_remote_set_qrcode.svg">

```python
lcd.qrcode('http://flow-remote.m5stack.com/?remote=undefined', 72, 32, 176)
```

- 设置生成网页的二维码显示位置与大小。注： 网页首次运行后， 将自动更新代码中 URL 的 remote 参数，因此该 API 需先通过 UiFlow 在线模式运行一次。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote/uiflow_block_remote_set_title.svg">

- 设置远程页面的标题

\#> 控件变量 | 除了 button 控件外，其他涉及输入参数的控件使用前需要点击 Block 左上角齿轮按钮添加变量， 在其程序内部使用相同名称的变量获取传入的参数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote/uiflow_block_remote_add_switch.svg">

```python
def _remote_SwitchName(x):
  pass
```

- 添加切换开关控件

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote/uiflow_block_remote_add_button.svg">

```python
def _remote_ButtonName():
  pass
```

- 添加按键控件

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote/uiflow_block_remote_add_slider.svg">

```python
def _remote_SliderName(x):
  pass
```

- 添加滑动条控件

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote/uiflow_block_remote_add_label.svg">

```python
def _remote_LabelName(x):
  pass
```

- 添加标签显示控件

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote/uiflow_block_remote_add_input.svg">

```python
def _remote_InputName(x):
  pass
```

- 添加文本输入控件
