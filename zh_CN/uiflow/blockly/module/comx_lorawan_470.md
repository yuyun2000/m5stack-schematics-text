# [Module COMX LoRaWAN 470](/zh_CN/module/comx_lorawan470)

## 案例程序

使用 LoRaWAN 470 模块，通过 OTAA 模式进行入网连接，并定期发送数据负载并接收下行数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_LoRaWAN470_demo.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
from comx.LoRaWAN import LoRaWAN_470
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

flag = None

lora470 = LoRaWAN_470(tx=17, rx=16)
lora470.set_join_mode(0)
lora470.config_OTAA('', '', '')
lora470.set_frequency_band_mask('0400')
lora470.set_rx_window_param(0, 0, 505300000)
lora470.set_class_mode(2)
lora470.set_uplink_downlink_mode(1)
lora470.join(1, 1, 8, 8)
flag = False
while True:
  if not flag and lora470.check_join_status():
    flag = True
    print('Joined')
  if flag:
    lora470.send_data('M5STACK', 1, 5)
    print(lora470.check_downlink_data())
  wait(10)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_check_downlink_data.svg">

```python
lora470.check_downlink_data()
```

- 检查并接收从 LoRaWAN 网关发送到设备的下行数据。这是用于确认是否有数据从服务器传输到设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_check_join_status.svg">

```python
lora470.check_join_status()
```

- 检查设备是否成功加入 LoRaWAN 网络。设备在尝试连接到 LoRaWAN 网络时，会执行入网操作，这个块用于检查这个操作是否成功

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_check_sent_status.svg">

```python
lora470.check_uplink_status()
```

- 检查上行数据的发送状态。用于确认数据是否成功从设备发送到 LoRaWAN 网关

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_config.svg">

```python
lora470.set_frequency_band_mask('0001')
lora470.set_rx_window_param(0, 0, 505300000)
lora470.set_class_mode(0)
lora470.set_uplink_downlink_mode(1)
```

- 配置 LoRaWAN 通信的相关参数。包括以下设置：
  - Frequency band mask: 配置频率掩码，指定可以使用的频率范围。
  - RX window param: 设置接收窗口的参数。
  - RX1 offset: 配置接收窗口1的偏移量。
  - RX2 datarate: 配置接收窗口2的数据速率。
  - RX2 freq (Hz): 配置接收窗口2的频率。
  - Class mode: 设置设备的工作模式，常见模式为 Class A。
  - Uplink downlink mode: 配置上行和下行数据的频率模式，可以选择使用相同或不同的频率。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_config_mode.svg">

```python
lora470.config_OTAA('', '', '')
```

- 配置 LoRaWAN 设备使用 OTAA(Over-The-Air Activation)模式进行连接。需要输入设备的 EUI(设备标识符)、应用密钥(app key)、应用 EUI(应用标识符)等信息。OTAA 模式是一种动态的设备连接方法，通过网络服务器进行设备认证

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_get_abp_config.svg">

```python
lora470.get_ABP_config()
```

- 获取设备使用 ABP(Activation By Personalization)模式时的配置。这种模式下，设备直接使用预配置的会话密钥进行网络连接，而不需要动态加入网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_get_otaa_config.svg">

```python
lora470.get_OTAA_config()
```

- 获取设备在使用 OTAA 模式时的配置参数。这些参数包括设备的 EUI、应用 EUI 和应用密钥等

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_init.svg">

```python
LoRaWAN_470(tx=0, rx=0)
```

- 初始化 LoRaWAN 470设备的 TX(发送引脚)和 RX(接收引脚)。用于设置设备与其他硬件通信的引脚位置，以确保正确的数据传输和接收\

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_join_start.svg">

```python
lora470.join(1, 1, 8, 1)
```

- 开始加入 LoRaWAN 网络。这个块允许你配置设备自动加入网络的时间间隔(以秒为单位)和最大尝试次数。当启用“auto join”时，设备会在设置的时间间隔内尝试多次加入网络，直到成功或达到最大尝试次数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_join_stop.svg">

```python
lora470.join(0)
```

- 停止加入 LoRaWAN 网络的尝试。如果设备正在尝试加入网络，但你想要中途停止它，可以使用这个块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_receive_data.svg">

```python
lora470.receive_data()
```

- 从缓冲区接收下行数据。这将从 LoRaWAN 网络的下行链路接收数据包(例如从服务器到设备的消息)并处理

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_send_data.svg">

```python
lora470.send_data('')
```

- 发送数据载荷到 LoRaWAN 网络。你可以选择发送数据的确认模式(“unconfirm”表示不需要确认，“confirm”表示需要确认)。这允许设备将数据发送到服务器或其他设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_set_join_mode.svg">

```python
lora470.set_join_mode(0)
```

- 设置 LoRaWAN 设备的加入模式为 OTAA。OTAA(Over-The-Air Activation)是一种动态设备连接方法，通过网络服务器进行设备认证

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_470/uiflow_block_lorawan470_set_uplink_app_port.svg">

```python
lora470.set_uplink_app_port(1)
```

- 设置上行应用端口。LoRaWAN 通信使用端口来标识不同的应用或服务，这个块允许你在1到233之间设置设备使用的上行数据传输端口。这个端口号是传输数据时在 LoRaWAN 网络中使用的标识，用于区分不同的数据流或应用

