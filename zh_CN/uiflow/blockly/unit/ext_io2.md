# [Unit EXT.IO2](/zh_CN/unit/extio2)

## 案例程序

控制舵机转动和控制RGB LED 发光

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
ext_io2_0 = unit.get(unit.EXT_IO2, unit.PORTA)

ext_io2_0.init_i2c_address(0x45)
ext_io2_0.set_config_mode(2, 3)
ext_io2_0.set_config_mode(1, 4)
ext_io2_0.write_rgb_led(1, 78, 74, 96)
while True:
  ext_io2_0.write_servo_angle(2, 65)
  print((str('servo angle:') + str((ext_io2_0.read_servo_angle(2)))))
  wait(1)
  ext_io2_0.write_servo_angle(2, 176)
  print((str('servo angle:') + str((ext_io2_0.read_servo_angle(2)))))
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_init_i2c_address.svg">

```python
ext_io2_0.init_i2c_address(0x45)
```

- 初始化 EXTIO2 Unit 并获取通信地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_get_config_mode.svg">

```python
print((str('config mode:') + str((ext_io2_0.get_config_mode(0)))))
```

- 获取指定频道的当前配置模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_read_adc12_pin.svg">

```python
print((str('ADC 12bit:') + str((ext_io2_0.read_adc12_pin(0)))))
```

- 读取引脚的 12 位 ADC 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_read_adc8_pin.svg">

```python
print((str('ADC 8bit:') + str((ext_io2_0.read_adc8_pin(0)))))
```

- 读取引脚的 8 位 ADC 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_read_digital_input_pin.svg">

```python
print((str('digital input:') + str((ext_io2_0.read_input_pin(0)))))
```

- 读取 input pin 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_read_rgb_led_pin.svg">

```python
print((str('RGB LED:') + str((ext_io2_0.read_rgb_led(0)))))
```

- 读取指定通道 RGB LED 值 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_read_servo_angle_pin.svg">

```python
print((str('servo angle:') + str((ext_io2_0.read_servo_angle(0)))))
```

- 读取指定通道的舵机旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_read_servo_pulse_pin.svg">

```python
print((str('servo pulse:') + str((ext_io2_0.read_servo_pulse(0)))))
```

- 读取指定通道的脉冲宽度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_read_status.svg">

```python
print((str('version:') + str((ext_io2_0.read_status(0XFE)))))
```

- 获取当前设备固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_set_config_mode.svg">

```python
ext_io2_0.set_config_mode(0, 0)
```

- 设置特定频道的配置模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_set_i2c_address.svg">

```python
ext_io2_0.set_i2c_address(0x45)
```

- 重新设置 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_write_digital_output_pin.svg">

```python
ext_io2_0.write_output_pin(0, 0)
```

- 设置数字输出引脚电平

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_write_rgb_led_pin.svg">

```python
ext_io2_0.write_rgb_led(0, 0, 0, 0)
```

- 写入 RGB 颜色值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_write_servo_angle.svg">

```python
ext_io2_0.write_servo_angle(0, 0)
```

- 写入角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io2/uiflow_block_extio2_write_servo_pulse.svg">

```python
ext_io2_0.write_servo_pulse(0, 500)
```

- 写入脉冲宽度

