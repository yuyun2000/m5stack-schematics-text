# [Atom DTU LoRaWAN 470](/zh_CN/atom/atom_dtu_lorawan470)

## 案例程序

这个程序通过 LoRaWAN 协议进行设备入网、数据发送和接收。初始化后，设备在 OTAA 模式下自动尝试入网，RGB 灯亮度变化显示连接状态。成功连接后，设备每5秒发送一次数据，并检查是否有下行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_atomic_base_lorawan_470_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.DTU_LoRaWAN import DTU_LoRaWAN
import time

j = None

rgb.setColorAll(0xcc6600)
dtu_lora470 = DTU_LoRaWAN()
dtu_lora470.set_join_mode(0)
dtu_lora470.config_OTAA('2fd1549588a2f196', '00000000000000000000000000000000', '059d230cf60aaf212783b4b7e801a389')
dtu_lora470.set_frequency_band_mask('0400')
dtu_lora470.set_rx_window_param(0, 0, 505300000)
dtu_lora470.set_class_mode(2)
dtu_lora470.set_uplink_downlink_mode(1)
dtu_lora470.join(1, 1, 8, 10)
rgb.setColorAll(0xff6666)
while not dtu_lora470.check_join_status():
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
  dtu_lora470.send_data('012345678', 1, 15)
  print(dtu_lora470.check_downlink_data())
  wait(5)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_init.svg">

```python
dtu_lora470 = DTU_LoRaWAN()
```

- 初始化 LoRaWAN 470 DTU 模块，准备设备以便进行 LoRa 通信。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_any.svg">

```python
modbus._mdbus_uart.any()
```

- 检查是否有未处理的缓存数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_check_downlink_data.svg">

```python
dtu_lora470.check_downlink_data()
```

- 检查并接收来自网关的下行数据，通常用于设备接收网络指令或信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_check_join_status.svg">

```python
dtu_lora470.check_join_status()
```

- 检查设备是否成功加入 LoRaWAN 网络。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_check_sent_status.svg">

```python
dtu_lora470.check_uplink_status()
```

- 检查设备发送的上行数据的状态，确认数据是否成功发送。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_config.svg">

```python
dtu_lora470.set_frequency_band_mask('0001')
dtu_lora470.set_rx_window_param(0, 0, 505300000)
dtu_lora470.set_class_mode(0)
dtu_lora470.set_uplink_downlink_mode(1)
```

- 设置频段掩码、接收窗口参数、接收频率和数据速率(例如 RX1 和 RX2 参数)。
- 设置设备的工作模式(Class A)，以及上下行通信的频率模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_config_mode.svg">

```python
dtu_lora470.config_OTAA('', '', '')
```

- 通过 OTAA(Over-The-Air Activation)模式配置设备，输入设备 EUI、应用密钥(app key)和应用 EUI。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_get_abp_config.svg">

```python
dtu_lora470.get_ABP_config()
```

- 获取设备的 ABP(Activation By Personalization)模式配置信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_get_otaa_config.svg">

```python
dtu_lora470.get_OTAA_config()
```

- 获取设备的 OTAA 模式配置信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_join_start.svg">

```python
dtu_lora470.join(1, 1, 8, 1)
```

- 启动加入 LoRaWAN 网络的过程。可以选择自动加入模式，设定尝试加入的间隔时间(秒)和最大尝试次数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_join_stop.svg">

```python
dtu_lora470.join(0)
```

- 停止加入 LoRaWAN 网络的过程。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_read.svg">

```python
dtu_lora470.read()
```

- 读取所有可用的数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_readline.svg">

```python
dtu_lora470.readline()
```

- 按行读取数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_read_characters.svg">

```python
dtu_lora470.read(10)
```

- 读取指定数量的字符。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_read_coils.svg">

```python
dtu_lora470.read_coils(1, 1, 0)
```

- 读取线圈状态，使用 Modbus 协议，指定从机地址、起始地址和线圈数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_read_discrete_inputs.svg">

```python
dtu_lora470.read_discrete_inputs(1, 1, 0)
```

- 读取离散输入状态，指定从机地址、起始地址和输入数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_read_holding_registers.svg">

```python
dtu_lora470.read_holding_registers(1, 1, 0, True)
```

- 读取保持寄存器，指定从机地址、起始地址和寄存器数量。可以选择读取有符号或无符号的值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_read_input_registers.svg">

```python
dtu_lora470.read_input_registers(1, 1, 0, True)
```

- 读取输入寄存器，指定从机地址、起始地址和寄存器数量。可以选择读取有符号或无符号的值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_receive_data.svg">

```python
dtu_lora470.receive_data()
```

- 从缓冲区接收下行数据，通常用于处理 LoRaWAN 网络发送的消息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_send_data.svg">

```python
dtu_lora470.send_data('')
```

- 发送数据负载，可以选择是否使用确认模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_set_join_mode.svg">

```python
dtu_lora470.set_join_mode(0)
```

- 设置加入网络的模式，如 OTAA(Over-The-Air Activation，空中激活)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_set_uplink_app_port.svg">

```python
dtu_lora470.set_uplink_app_port(1)
```

- 设置上行应用端口，范围是 1 到 233。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_write.svg">

```python
dtu_lora470.write('')
```

- 在 UART 串口中写入数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_write_line.svg">

```python
dtu_lora470.write(''+"\r\n")
```

- 在 UART 串口中写入一行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_write_multiple_coils.svg">

```python
dtu_lora470.write_multiple_coils(1, 1, 0)
```

- 向 Modbus 设备写入多个线圈的状态，指定起始地址和输出值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_write_multiple_registers.svg">

```python
dtu_lora470.write_multiple_registers(1, 1, 0, True)
```

- 向 Modbus 设备写入多个寄存器的值，指定起始地址、寄存器值，并支持带符号数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_write_raw_data.svg">

```python
dtu_lora470.write(bytes([0, 0, 0]))
```

- 在 UART 串口中写入原始数据，数据以列表的形式传递。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_write_single_coil.svg">

```python
dtu_lora470.write_single_coil(1, 1, 0)
```

- 向 Modbus 设备的单个线圈写入状态，指定输出地址和输出值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_470/uiflow_block_base_lorawan470_write_single_register.svg">

```python
dtu_lora470.write_single_register(1, 1, 0, True)
```

- 向 Modbus 设备的单个寄存器写入值，指定寄存器地址和寄存器值，并支持带符号的数据。

