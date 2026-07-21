# Echo STT

\#> 功能说明 | Atom Voice 在烧录了 STT 固件的后， 语音转换文本时除了会在串口打印出文本信息以外， 还会将起其文本信息上传至服务器。其他设备在 UiFlow 中可以通过使用 Echo STT Block, 通过配置与设备一致的 token, 来获取对应的 STT 的文本内容。

## Get Toekn

功能使用前需使用[M5Burner](/zh_CN/uiflow/m5burner/intro)为 Atom Voice 烧录 STT 固件并获取 Token (在 UiFlow 中初始化 Echo STT 远程功能需使用该字段)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/echo_stt/uiflow_block_echo_stt_get_token_01.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/echo_stt/uiflow_block_echo_stt_get_token_02.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/echo_stt/uiflow_block_echo_stt_get_token_03.jpg" width="70%">

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/echo_stt/uiflow_block_echo_stt_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from echo import Echo
import wifiCfg

setScreenColor(0x222222)
stt_data = None

wifiCfg.autoConnect(lcdShow=False)

def echo_callback(*args):
  global stt_data
  stt_data = args[0]
  print(stt_data)
  pass


echo = Echo(str('500291857fbc58d4336dbe4e30d49797'))
echo.set_callback(echo_callback)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/echo_stt/uiflow_block_echo_stt_init.svg">

```python
from echo import Echo
echo = Echo(str('500291857fbc58d4336dbe4e30d49797'))
echo.set_callback(echo_callback)
```

- 初始化 Echo STT 数据获取功能， 并配置匹配的设备 token.

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/echo_stt/uiflow_block_echo_stt_get_text.svg">

```python
echo.recv_text
```

- 获取返回的 STT 文本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/echo_stt/uiflow_block_echo_stt_recv_data.svg">

```python

def echo_callback(*args):
  global stt_data
  stt_data = args[0]
  print(stt_data)
  pass
```

- 新 STT 文本消息回调函数
