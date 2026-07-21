# Blynk BLE

通过 BLE 连接 Blynk App, 实现手机端无线控制。注：仅带 PSRAM 机型(如 M5Fire, M5Core2)支持。该功能仅支持 Blynk legacy, 新版本的 Blynk 已没有提供 BLE 支持。

## 案例程序

1.在 Blynk legacy 中创建新工程， 选择 ESP32 Dev Board, 选择接入方式为 BLE, 同时记录下 AUTH TOKEN。按照下图步骤添加组件， 其中 BLE 连接为必要组件。

2.使用 Blynk 控制 M5StackFire 的 RGB 灯条颜色和亮度，并在屏幕上实时显示


## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/blynk_ble/uiflow_block_blynk_init.svg">

```python
from ble import blynk
blynk.init('Device Name', 'Token', blynk.BLE)
```

- 初始化 blynk 配置，输入设备名称与 App 端的 token

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/blynk_ble/uiflow_block_blynk_event_write.svg">

```python
def blynk_write_all(*args):
  global msg, num
  num, msg = args[0], args[1]
  pass

blynk.handle_event('write v*', blynk_write_all)
```

- 从 App 端接收即将写入的指定虚拟端口的数据，如果不指定设为 V*

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/blynk_ble/uiflow_block_blynk_event_read.svg">

```python

def blynk_read_all(*args):
  global num
  num = args[0]
  pass

blynk.handle_event('read v*', blynk_read_all)
```

- 读取 App 端指定的虚拟端口号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/blynk_ble/uiflow_block_blynk_notify.svg">

```python
blynk.notify('')
```

- 向 App 发送系统级消息通知

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/blynk_ble/uiflow_block_blynk_on_event.svg">

```python
def blynk_connected():
  # global params
  print('connected')
  pass


blynk.handle_event('connected', blynk_connected)
```

- 事情监听回调函数注册， 支持事件：
  - connected
  - disconnected


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/blynk_ble/uiflow_block_blynk_tweet.svg">

```python
blynk.tweet('')
```

- 向 Twitter 客户端发送消息通知


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/blynk_ble/uiflow_block_blynk_virtual_write.svg">

```python
blynk.virtual_write(1, '')
```

- 向虚拟端口号写入数据

