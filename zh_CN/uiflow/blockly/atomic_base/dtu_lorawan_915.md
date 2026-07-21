# [Atom DTU LoRaWAN 915](/zh_CN/atom/atom_dtu_lorawan915)

## 案例程序

该程序使用 LoRaWAN 915 DTU 模块在 OTAA 模式下连接网络，连接过程中 RGB 灯的亮度变化显示状态。连接成功后，设备每5秒发送一次数据“012345678”，并检查是否有下行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_atomic_base_lorawan_915_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.DTU_LoRaWAN import DTU_LoRaWAN
import time

j = None

rgb.setColorAll(0xcc6600)
dtu_lora915 = DTU_LoRaWAN()
dtu_lora915.set_join_mode(0)
dtu_lora915.config_OTAA('d896e0ff00000241', '0000000000000001', '98929b92f09e2daf676d646d0f61d251')
dtu_lora915.set_frequency_band_mask('0001')
dtu_lora915.set_rx_window_param(0, 0, 923300000)
dtu_lora915.set_class_mode(2)
dtu_lora915.set_uplink_downlink_mode(1)
dtu_lora915.join(1, 1, 8, 15)
rgb.setColorAll(0xff6666)
while not dtu_lora915.check_join_status():
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
  dtu_lora915.send_data('012345678', 1, 15)
  print(dtu_lora915.check_downlink_data())
  wait(5)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_init.svg">

```python
dtu_lora915 = DTU_LoRaWAN()
```

- 初始化 LoRaWAN 915 DTU 模块。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_any.svg">

```python
dtu_lora915.any()
```

- 保持缓存。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_check_downlink_data.svg">

```python
dtu_lora915.check_downlink_data()
```

- 检查并接收下行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_check_join_status.svg">

```python
dtu_lora915.check_join_status()
```

- 检查加入 LoRaWAN 网络的状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_check_sent_status.svg">

```python
dtu_lora915.check_uplink_status()
```

- 检查上行数据状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_config.svg">

```python
dtu_lora915.set_frequency_band_mask('0001')
dtu_lora915.set_rx_window_param(0, 0, 923300000)
dtu_lora915.set_class_mode(0)
dtu_lora915.set_uplink_downlink_mode(1)
```

- 配置 LoRaWAN 的参数，包含频率掩码、接收窗口参数、RX1偏移量、RX2数据速率、RX2频率、工作模式和下行链路的模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_config_mode.svg">

```python
dtu_lora915.config_OTAA('', '', '')
```

- 配置 OTAA 模式，设置设备 EUI、应用密钥(App Key)和应用 EUI。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_get_abp_config.svg">

```python
dtu_lora915.get_ABP_config()
```

- 获取 ABP(Activation By Personalization)配置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_get_otaa_config.svg">

```python
dtu_lora915.get_OTAA_config()
```

- 获取 OTAA(Over-The-Air Activation)配置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_join_start.svg">

```python
dtu_lora915.join(1, 1, 8, 1)
```

- 开始加入 LoRaWAN 网络，设置自动加入模式、间隔时间(秒)和最大尝试次数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_join_stop.svg">

```python
dtu_lora915.join(0)
```

- 停止加入 LoRaWAN 网络的过程。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_read.svg">

```python
dtu_lora915.read()
```

- 读取所有数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_readline.svg">

```python
dtu_lora915.readline()
```

- 逐行读取数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_read_characters.svg">

```python
dtu_lora915.read(10)
```

- 读取10个字符。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_read_coils.svg">

```python
dtu_lora915.read_coils(1, 1, 0)
```

- 读取线圈寄存器，从指定从站地址、起始地址和线圈数量开始。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_read_discrete_inputs.svg">

```python
dtu_lora915.read_discrete_inputs(1, 1, 0)
```

- 读取离散输入寄存器，从指定从站地址、起始地址和输入数量开始。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_read_holding_registers.svg">

```python
dtu_lora915.read_holding_registers(1, 1, 0, True)
```

- 读取保持寄存器，从指定从站地址、起始地址和寄存器数量开始，可选择数据是否为有符号。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_read_input_registers.svg">

```python
dtu_lora915.read_input_registers(1, 1, 0, True)
```

- 读取输入寄存器，从指定从站地址、起始地址和寄存器数量开始，可选择数据是否为有符号。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_receive_data.svg">

```python
dtu_lora915.receive_data()
```

- 从缓存中接收下行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_send_data.svg">

```python
dtu_lora915.send_data('')
```

- 发送数据负载，可以选择确认或非确认方式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_set_join_mode.svg">

```python
dtu_lora915.set_join_mode(0)
```

- 设置入网模式，这里设置为 OTAA(Over-the-Air Activation，空中激活)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_set_uplink_app_port.svg">

```python
dtu_lora915.set_uplink_app_port(1)
```

- 设置上行应用程序端口，范围为 1 到 233。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_write.svg">

```python
dtu_lora915.write('')
```

- 通过 UART 写入数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_write_line.svg">

```python
dtu_lora915.write(''+"\r\n")
```

- 通过 UART 写入一行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_write_multiple_coils.svg">

```python
dtu_lora915.write_multiple_coils(1, 1, 0)
```

- 写入多个线圈到指定的从地址，起始地址和输出值可以自定义。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_write_multiple_registers.svg">

```python
dtu_lora915.write_multiple_registers(1, 1, 0, True)
```

- 写入多个寄存器到从设备地址，起始地址和寄存器值可以自定义。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_write_raw_data.svg">

```python
dtu_lora915.write(bytes([0, 0, 0]))
```

- 通过 UART 写入原始数据，数据以列表形式输入。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_write_single_coil.svg">

```python
dtu_lora915.write_single_coil(1, 1, 0)
```

- 写入单个线圈到指定的从设备地址，起始地址和输出值可以自定义。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_lorawan_915/uiflow_block_base_lorawan915_write_single_register.svg">

```python
dtu_lora915.write_single_register(1, 1, 0, True)
```

- 写入单个寄存器到从设备地址，起始地址和寄存器值可以自定义，并可以选择数据是否为有符号。

