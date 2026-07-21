# [Unit ExtEncoder](/zh_CN/unit/ExtEncoder%20Unit)

## 案例程序

> 采集外接编码器和仪表计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
extencoder_0 = unit.get(unit.EXT_ENCODER, unit.PORTA)

extencoder_0.init_i2c_address(0x59)
while True:
  print((str('encoder:') + str((extencoder_0.get_encoder_value()))))
  print((str('meter:') + str((extencoder_0.get_meter_value()))))
  print((str('string meter') + str((extencoder_0.get_str_meter_value()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_init.svg">

```python
extencoder_0.init_i2c_address(0x59)
```

- 初始化 ExtEncoderUnit I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_set_i2c_address.svg">

```python
extencoder_0.set_i2c_address(0x59)
```

- 重置设备 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_reset_encoder.svg">

```python
extencoder_0.reset_encoder()
```

- 重置编码器和仪表计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_set_perimeter_value.svg">

```python
extencoder_0.set_perimeter_value(1000)
```

- 设置一周脉冲值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_set_pulse_value.svg">

```python
extencoder_0.set_pulse_value(1000)
```

- 设置每周(360°)接收脉冲值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_set_zero_counter_value.svg">

```python
extencoder_0.set_zero_counter_value(0)
```

- 设置零脉冲总值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_set_z_trigger_mode.svg">

```python
extencoder_0.set_z_trigger_mode(0)
```

- 设置清除 Z 触发模式
  - NOT CLEAR
  - Z-RISING EDGE
  - Z-FALLING EDGE

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_get_device_firmware.svg">

```python
print(extencoder_0.get_firmware_status())
```

- 获取 ExtEncoderUnit 对象的固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_get_encoder_value.svg">

```python
print(extencoder_0.get_encoder_value())
```

- 获取编码器脉冲计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_get_meter_value.svg">

```python
print(extencoder_0.get_meter_value())
```

- 获取 ExtEncoderUnit 对象的仪表值。单位为毫米

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_get_perimeter_value.svg">

```python
print(extencoder_0.get_perimeter_value())
```

- 获取 ExtEncoderUnit 对象的周长。单位为毫米

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_get_pulse_value.svg">

```python
print(extencoder_0.get_pulse_value())
```

- 获取每周期脉冲值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_get_str_meter_value.svg">

```python
print(extencoder_0.get_str_meter_value())
```

- 获取字符串仪表脉冲计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_get_zero_counter_value.svg">

```python
print(extencoder_0.get_zero_counter_value())
```

- 获取 ExtEncoderUnit 对象的零模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_encoder/uiflow_block_unit_extencoder_get_z_trigger_mode.svg">

```python
print(extencoder_0.get_z_trigger_mode())
```

- 到 Z 触发器模型
