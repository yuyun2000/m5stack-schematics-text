# [Unit LoRaWAN470](/zh_CN/unit/lorawan470)

## 案例程序

配置 LoRaWAN470 并连接网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_example.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
LoRaWAN470_0 = unit.get(unit.LoRaWAN, unit.PORTC)

flag = None

LoRaWAN470_0.set_join_mode(0)
LoRaWAN470_0.config_OTAA('', '', '')
LoRaWAN470_0.set_frequency_band_mask('0400')
LoRaWAN470_0.set_rx_window_param(0, 0, 505300000)
LoRaWAN470_0.set_class_mode(2)
LoRaWAN470_0.set_uplink_downlink_mode(1)
LoRaWAN470_0.join(1, 1, 8, 8)
flag = False
while True:
  if not flag and LoRaWAN470_0.check_join_status():
    flag = True
    print('Joined')
  if flag:
    LoRaWAN470_0.send_data('M5STACK', 1, 5)
    print(LoRaWAN470_0.check_downlink_data())
  wait(10)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_uart_init.svg">

```python
LoRaWAN470_0.uart_port_id(1)
```

- 设置核心 UART ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_check_downlink_data.svg">

```python
print((str('ckeck downlink data:') + str(LoRaWAN470_0.check_downlink_data())))
```

- 检查并接收下行链路数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_check_join_status.svg">

```python
print((str('status:') + str(LoRaWAN470_0.check_join_status())))
```

- 检查加入状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_check_sent_status.svg">

```python
print((str('uplink data status:') + str(LoRaWAN470_0.check_uplink_status())))
```

- 检查上行链路数据状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_config.svg">

```python
LoRaWAN470_0.set_frequency_band_mask('')
LoRaWAN470_0.set_rx_window_param(0, 0, 869525000)
LoRaWAN470_0.set_class_mode(0)
LoRaWAN470_0.set_uplink_downlink_mode(1)
```

- 配置 Config 参数
  - frequency band mask：频段掩码
  - RX window param：接收窗口参数
  - RX1 offset：RX1窗口偏移
  - RX2 datarate SF12 BW125：RX2窗口的数据速率（扩频因子12，带宽125kHz）
  - RX2 freq(H1)：RX2窗口频率
  - class mode classA：设备模式（Class A）
  - uplink downlin same frequency mode： 上行下行同频模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_config_mode.svg">

```python
LoRaWAN470_0.config_OTAA('afeafe53453453adsfsdf423', 'gffgfds-546fgdg-ggfd', '33453453-4564-54')
```

- Config OTAA mode
  - device eui
  - app key
  - app eui

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_get_abp_config.svg">

```python
print((str('ABP Config:') + str(LoRaWAN470_0.get_ABP_config())))
```

- 获取 ABP 配置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_get_otaa_config.svg">

```python
print((str('OTAA Config:') + str(LoRaWAN470_0.get_OTAA_config())))
```

- 获取 OTTA 配置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_join_start.svg">

```python
LoRaWAN470_0.join(1, 1, 8, 1)
```

- 加入 LoRaWAN 网络配置
  - open auto jion
  - period (seconds)
  - maximum number of attempts

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_join_stop.svg">

```python
LoRaWAN470_0.join(0)
```

- 停止加入 LoRaWAN 网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_receive_data.svg">

```python
print((str('downlink data:') + str((LoRaWAN470_0.receive_data()))))
```

- 从缓冲区接收下行链路数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_send_data.svg">

```python
LoRaWAN470_0.send_data('')
```

- 发送数据负载

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_set_join_mode.svg">

```python
LoRaWAN470_0.set_join_mode(0)
```

- 设置加入模式
  - OTTA
  - ABP

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lorawan_470/uiflow_block_unit_lorawan470_set_uplink_app_port.svg">

```python
LoRaWAN470_0.set_uplink_app_port(1)
```

- 设置上行链路应用端口（1~233）