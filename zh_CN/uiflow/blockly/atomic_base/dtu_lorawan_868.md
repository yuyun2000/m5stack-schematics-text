# [Atom DTU LoRaWAN 868](/zh_CN/atom/atom_dtu_lorawan868)

## 案例程序

该程序使用 LoRaWAN 868 DTU 模块在 OTAA 模式下连接网络，RGB 灯在连接期间通过亮度变化指示状态。连接成功后，设备每5秒发送一次数据“012345678”并检查下行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_atomic_base_lorawan_868_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.DTU_LoRaWAN import DTU_LoRaWAN
import time

j = None

rgb.setColorAll(0xcc6600)
dtu_lora868 = DTU_LoRaWAN()
dtu_lora868.set_join_mode(0)
dtu_lora868.config_OTAA('00bb9da5b97addf8', '00000000000000000000000000000000', '27dfe264ca33ac1957c005eb48ba4728')
dtu_lora868.set_frequency_band_mask('0001')
dtu_lora868.set_rx_window_param(0, 0, 869525000)
dtu_lora868.set_class_mode(2)
dtu_lora868.set_uplink_downlink_mode(1)
dtu_lora868.join(1, 1, 8, 10)
rgb.setColorAll(0xff6666)
while not dtu_lora868.check_join_status():
  print('waiting join....')
  for j in range(101):
    rgb.setBrightness(j)
    wait_ms(10)
  for j in range(100, -1, -1):
    rgb.setBrightness(j)
    wait_ms(10)
print('connected!')
rgb.setBrightness(100)
rgb.setColorAll(0x33ff33)
while True:
  dtu_lora868.send_data('012345678', 1, 15)
  print(dtu_lora868.check_downlink_data())
  wait(5)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_init.svg">

```python
dtu_lora868 = DTU_LoRaWAN()
```

- 初始化 LoRaWAN 868 DTU 模块，用于 LoRaWAN 通信。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_any.svg">

```python
dtu_lora868.any()
```

- 保留缓存数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_check_downlink_data.svg">

```python
dtu_lora868.check_downlink_data()
```

- 检查并接收下行数据(从服务器发送到设备的数据)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_check_join_status.svg">

```python
dtu_lora868.check_join_status()
```

- 检查设备加入 LoRaWAN 网络的状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_check_sent_status.svg">

```python
dtu_lora868.check_uplink_status()
```

- 检查上行数据的状态(从设备发送到服务器的数据)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_config.svg">

```python
dtu_lora868.set_frequency_band_mask('')
dtu_lora868.set_rx_window_param(0, 0, 869525000)
dtu_lora868.set_class_mode(0)
dtu_lora868.set_uplink_downlink_mode(1)
```

- 用于配置 LoRaWAN 的频率、窗口参数、数据速率、模式等。
    - frequency band mask：用于选择频率段的掩码。
    - RX1 offset 和 RX2 freq (Hz)：设置接收窗口和频率。
    - class mode：选择 LoRaWAN 类别(如 Class A)。
    - uplink downlink：设置上下行频率模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_config_mode.svg">

```python
dtu_lora868.config_OTAA('', '', '')
```

- 用于配置 OTAA 模式的必要参数：
    - device eui：设备标识。
    - app key 和 app eui：用于 OTAA 认证的应用密钥和应用标识符。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_get_abp_config.svg">

```python
dtu_lora868.get_ABP_config()
```

- 用于获取 ABP 模式的配置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_get_otaa_config.svg">

```python
dtu_lora868.get_OTAA_config()
```

- 用于获取 OTAA 模式的配置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_join_start.svg">

```python
dtu_lora868.join(1, 1, 8, 1)
```

- 启动加入 LoRaWAN 网络的过程。
    - open：设置是否自动加入网络。
    - period (seconds)：指定每次尝试加入网络的时间间隔。
    - maximum number of attempts：最大尝试次数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_join_stop.svg">

```python
dtu_lora868.join(0)
```

- 停止当前的网络加入操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_read.svg">

```python
dtu_lora868.read()
```

- Read all：读取所有内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_readline.svg">

```python
dtu_lora868.readline()
```

- Read line：按行读取数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_read_characters.svg">

```python
dtu_lora868.read(10)
```

- 读取指定数量的字符，例如读取 10 个字符。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_read_coils.svg">

```python
dtu_lora868.read_coils(1, 1, 0)
```

- 从指定的从设备地址读取线圈状态，设置起始地址和线圈数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_read_discrete_inputs.svg">

```python
dtu_lora868.read_discrete_inputs(1, 1, 0)
```

- 从指定的从设备地址读取离散输入状态，设置起始地址和输入数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_read_holding_registers.svg">

```python
dtu_lora868.read_holding_registers(1, 1, 0, True)
```

- 从指定的从设备地址读取保持寄存器，设置起始地址和寄存器数量，支持有符号数或无符号数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_read_input_registers.svg">

```python
dtu_lora868.read_input_registers(1, 1, 0, True)
```

- 从指定的从设备地址读取输入寄存器，设置起始地址和寄存器数量，支持有符号数或无符号数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_receive_data.svg">

```python
dtu_lora868.receive_data()
```

- 从缓冲区接收下行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_send_data.svg">

```python
dtu_lora868.send_data('')
```

- 发送数据负载，设置数据和确认模式(确认或不确认)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_set_join_mode.svg">

```python
dtu_lora868.set_join_mode(0)
```

- 设置加入模式，支持 OTAA(Over-the-Air Activation)模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_set_uplink_app_port.svg">

```python
dtu_lora868.set_uplink_app_port(1)
```

- 设置上行应用端口，端口号范围是1到233。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_write.svg">

```python
dtu_lora868.write('')
```

- 通过 UART 发送数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_write_line.svg">

```python
dtu_lora868.write(''+"\r\n")
```

- 通过 UART 发送一行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_write_multiple_coils.svg">

```python
dtu_lora868.write_multiple_coils(1, 1, 0)
```

- 写入多个线圈，从属地址为1，起始地址和输出值都为1。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_write_multiple_registers.svg">

```python
dtu_lora868.write_multiple_registers(1, 1, 0, True)
```

- 写入多个寄存器，从属地址为1，起始地址为1，寄存器值为0，并且签名为 True(即使用有符号数据)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_write_raw_data.svg">

```python
dtu_lora868.write(bytes([0, 0, 0]))
```

- 通过 UART 写入原始数据，使用创建的列表(数据为0，0，0)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_write_single_coil.svg">

```python
dtu_lora868.write_single_coil(1, 1, 0)
```

- 写入单个线圈，从属地址为1，输出地址和输出值都为1。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_868/uiflow_block_base_lorawan868_write_single_register.svg">

```python
dtu_lora868.write_single_register(1, 1, 0, True)
```

- 写入单个寄存器，从属地址为1，寄存器地址为1，寄存器值为0，并且签名为 True(即使用有符号数据)。

