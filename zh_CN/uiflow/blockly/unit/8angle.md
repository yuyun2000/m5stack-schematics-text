# [Unit 8Angle](/zh_CN/unit/8Angle)

## 案例程序

> 获取设备按钮已经指定通道按钮状态，并设置指示灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
angle8_0 = unit.get(unit.ANGLE8, unit.PORTA)

while True:
  print(angle8_0.get_button_status())
  print(angle8_0.get_adc12_raw(0))
  print(angle8_0.read_status(0xFE))
  angle8_0.set_LED_RGB24(0, 50, 50, 50, 50)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_angle8_adc_12raw.svg">

```python
print(angle8_0.get_adc12_raw(0))
```

- 从某通道(0-7)获取12为 ADC 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_angle8_adc_8raw.svg">

```python
print(angle8_0.get_adc8_raw(0))
```

- 从某通道获取8位的 ADC 数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_angle8_button_status.svg">

```python
print(angle8_0.get_button_status())
```

- 获取开关的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_angle8_init.svg">

```python
angle8_0.init_i2c_address(0x43)
```

- 初始化设备的 I2C 通讯地址(默认0x43)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_angle8_read_status.svg">

```python
print(angle8_0.read_status(0xFE))
```

- 获取固件的版本


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_angle8_set_i2c_address.svg">

```python
angle8_0.set_i2c_address(0x43)
```

- 设置 I2C 地址


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_angle8_set_led_rgb.svg">

```python
angle8_0.set_LED_RGB24(0, 50, 50, 50, 50)
```

- 设置某通道(0-7)的 RGB 值和亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8angle/uiflow_block_angle8_set_led_rgb_from.svg">

```python
angle8_0.set_LED_RGB24_From(0, 8, 50, 50, 50, 50)
```

- 批量设置多通道(0-7)的 RGB 值和亮度