# [Unit 8Encoder](/zh_CN/unit/8Encoder)

## 案例程序

> 编辑程序，开启 1/2/3 旋转编码器，并监听编码器统计值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
encoder8_0 = unit.get(unit.ENCODER8, unit.PORTA)

encoder8_0.init_i2c_address(0x41)
encoder8_0.set_LED_RGB24(2, 50, 50, 50)
while True:
  print((str('counter 1 value:') + str((encoder8_0.get_counter_value(1)))))
  print((str('counter 2 value:') + str((encoder8_0.get_counter_value(2)))))
  print((str('counter 3 value:') + str((encoder8_0.get_counter_value(3)))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_init.svg">

```python
encoder8_0.init_i2c_address(0x41)
```

- 使用指定的 I2C 接口和地址初始化 Encoder8 单元

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_get_button_status.svg">

```python
print((str('button status:') + str((encoder8_0.get_button_status(0)))))
```

- 获取指定频道的按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_get_counter_value.svg">

```python
print((str('counter value:') + str((encoder8_0.get_counter_value(0)))))
```

- 获取指定通道的计数器值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_get_device_status.svg">

```python
print((str('device status:') + str((encoder8_0.read_status(0xFE)))))
```

- 获取设备的状态以及版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_get_increment_value.svg">

```python
print((str('increment value:') + str((encoder8_0.get_increment_value(0)))))
```

- 获取指定频道的增量值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_get_switch_status.svg">

```python
print((str('switch status:') + str((encoder8_0.get_switch_status()))))
```

- 获取全局开关的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_reset_counter_value.svg">

```python
encoder8_0.reset_counter_value(0)
```

- 重设指定通道的计数器值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_set_counter_value.svg">

```python
encoder8_0.reset_counter_value(0)
```

- 设置指定通道的计数器值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_set_i2c_address.svg">

```python
encoder8_0.set_i2c_address(0x41)
```

- 为器件设置新的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_set_led_rgb.svg">

```python
encoder8_0.set_LED_RGB24(0, 50, 50, 50)
```

- 设置指定通道的 RGB 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8encoder/uiflow_block_encoder8_set_led_rgb_from.svg">

```python
encoder8_0.set_LED_RGB24_From(0, 0, 50, 50, 50)
```

- 设置一系列通道的 RGB 颜色

