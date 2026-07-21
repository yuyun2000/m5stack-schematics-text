# [Module COMX LoRaWAN 915](/zh_CN/module/comx_lorawan915)

## 案例程序

使用 LoRaWAN 915 模块，通过 OTAA 模式进行入网连接，配置频段和数据速率等参数，并定期发送数据负载并接收下行数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_LoRaWAN915_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from comx.LoRaWAN import LoRaWAN_915
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

flag = None

lora915 = LoRaWAN_915(tx=17, rx=16)
lora915.set_join_mode(0)
lora915.config_OTAA('', '', '')
lora915.set_frequency_band_mask('0002')
lora915.set_rx_window_param(0, 0, 923300000)
lora915.set_class_mode(2)
lora915.set_uplink_downlink_mode(2)
lora915.join(1, 1, 8, 8)
flag = False
while True:
  if not flag and lora915.check_join_status():
    flag = True
    print('Joined')
  if flag:
    lora915.send_data('M5STACK', 1, 5)
    print(lora915.check_downlink_data())
  wait(10)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_check_downlink_data.svg">

```python
lora915.check_downlink_data()
```

- 检查并接收下行数据。这个块用于检查 LoRaWAN 网络是否有数据发送到设备并接收该数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_check_join_status.svg">

```python
lora915.check_join_status()
```

- 检查设备加入 LoRaWAN 网络的状态。这个块用于确认设备是否成功加入 LoRaWAN 网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_check_sent_status.svg">

```python
lora915.check_uplink_status()
```

- 检查上行数据的状态。这个块用于确认设备发送的上行数据是否成功传输到 LoRaWAN 网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_config.svg">

```python
lora915.set_frequency_band_mask('0001')
lora915.set_rx_window_param(0, 0, 923300000)
lora915.set_class_mode(0)
lora915.set_uplink_downlink_mode(1)
```

- 配置 LoRaWAN 通信参数。这个块包括以下设置：
  - frequency band mask: 设置频率带的掩码范围，在这里范围是915.2 MHz 到916.6 MHz。
  - RX window param: 配置接收窗口参数。
  - RX1 offset: 设置第一个接收窗口的频率偏移量。
  - RX2 datarate: 设置第二个接收窗口的数据速率 (在此示例中为 SF12 BW125)。
  - RX2 freq: 设置第二个接收窗口的频率 (在此示例中为923300000 Hz)。
  - class mode: 设置设备的类别模式 (在此示例中为 classA)。
  - uplink downlink: 设置上行和下行数据的频率模式 (在此示例中为相同频率模式)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_config_mode.svg">

```python
lora915.config_OTAA('', '', '')
```

- 配置 LoRaWAN 的 OTAA(Over The Air Activation)模式。
  - device eui: 设备的 EUI(唯一标识符)，用于在 LoRaWAN 网络中唯一标识该设备。
  - app key: 应用程序密钥，用于确保设备与网络之间的通信安全。
  - app eui: 应用程序 EUI，用于识别应用程序的唯一标识符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_get_abp_config.svg">

```python
lora915.get_ABP_config()
```

- 获取 ABP(Activation By Personalization)模式的配置参数。在 ABP 模式下，设备直接使用预先配置的密钥和参数加入网络，不需要通过 OTAA 过程

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_get_otaa_config.svg">

```python
lora915.get_OTAA_config()
```

- 获取 OTAA 模式的配置参数。这个块用于读取当前设备在 OTAA 模式下的配置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_init.svg">

```python
LoRaWAN_915(tx=0, rx=0)
```

- 初始化 LoRaWAN 915MHz 频段的发送(TX)和接收(RX)引脚。这些引脚用于与 LoRaWAN 模块的通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_join_start.svg">

```python
lora915.join(1, 1, 8, 1)
```

- 启动设备加入 LoRaWAN 网络的过程。
  - open: 设置是否自动重新加入网络。当选择“auto join”时，设备会在失去连接后自动尝试重新加入。
  - period (seconds): 设置每次尝试加入网络的时间间隔(以秒为单位)。
  - maximum number of attempts: 设置最大尝试次数。如果超过这个次数设备仍未能加入网络，将停止尝试

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_join_stop.svg">

```python
lora915.join(0)
```

- 停止设备尝试加入 LoRaWAN 网络的过程。这个块在不再需要加入网络时使用

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_receive_data.svg">

```python
lora915.receive_data()
```

- 从缓冲区接收下行数据。LoRaWAN 网络可以通过下行链路发送数据到设备，这个块用于读取这些数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_send_data.svg">

```python
lora915.send_data('')
```

- 发送数据负载到 LoRaWAN 网络。
  - unconfirm/confirm: 选择发送的数据包是否需要确认(confirm)或不需要确认(unconfirm)。选择确认会增加通信的可靠性，但也可能增加延迟

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_set_join_mode.svg">

```python
lora915.set_join_mode(0)
```

- 设置设备的加入模式为 OTAA(Over The Air Activation)，即通过空中激活方式加入 LoRaWAN 网络。OTAA 是 LoRaWAN 标准推荐的安全加入方式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lorawan_915/uiflow_block_lorawan915_set_uplink_app_port.svg">

```python
lora915.set_uplink_app_port(1)
```

- 设置 LoRaWAN 上行数据的应用端口。此端口用于标识数据包发送到网络服务器上的哪个应用程序。
  - 范围： 端口号的范围是1到233。每个端口号对应于特定的应用程序或服务，选择正确的端口可以确保数据被正确处理

