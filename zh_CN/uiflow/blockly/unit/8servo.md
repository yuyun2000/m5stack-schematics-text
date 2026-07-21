# [Unit 8Servos](/zh_CN/unit/8Servos%20Unit)

## 案例程序

> 设置通道 1 设置连接的 RGB LED 为红色，设置连接的 Servo 每一秒调整旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
servos8_0 = unit.get(unit.SERVOS8, unit.PORTA)

servos8_0.init_i2c_address(0x25)
servos8_0.set_config_mode(1, 4)
servos8_0.set_config_mode(2, 3)
while True:
  servos8_0.write_rgb_led(1, 0xff0000)
  wait(1)
  servos8_0.write_servo_angle(2, 61)
  print((str('servo angle:') + str((servos8_0.read_servo_angle(2)))))
  wait(1)
  servos8_0.write_servo_angle(2, 150)
  print((str('servo angle:') + str((servos8_0.read_servo_angle(2)))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_init_i2c_address.svg">

```python
servos8_0.init_i2c_address(0x25)
```

- 初始化 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_get_config_mode.svg">

```python
print((str('config mode:') + str((servos8_0.get_config_mode(0)))))
```

- 获取指定通道配置模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_read_adc12_pin.svg">

```python
print((str('ADC 12bit:') + str((servos8_0.read_adc12_pin(0)))))
```

- 获取指定通道的12位 ADC（模数转换）值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_read_adc8_pin.svg">

```python
print((str('ADC 8bit:') + str((servos8_0.read_adc8_pin(0)))))
```

- 获取指定通道的8位 ADC（模数转换）值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_read_digital_input_pin.svg">

```python
print((str('rgb led color:') + str((servos8_0.read_input_pin(0)))))
```

- 获取指定通道的数字输入状态（返回 true 或 false）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_read_rgb_led_pin.svg">

```python
print((str('rgb led color:') + str((servos8_0.read_rgb_led(0)))))
```

- 获取指定通道的 RGB LED 颜色（返回颜色列表）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_read_servo_angle_pin.svg">

```python
print((str('servo angle:') + str((servos8_0.read_servo_angle(0)))))
```

- 获取指定通道的旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_read_servo_current.svg">

```python
print((str('servo current:') + str((servos8_0.read_servo_current()))))
```

- 获取舵机电流（返回 float）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_read_servo_pulse_pin.svg">

```python
print((str('servo pulse:') + str((servos8_0.read_servo_pulse(0)))))
```

- 获取指定通道的舵机脉冲宽度（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_read_status.svg">

```python
print((str('firmware version:') + str((servos8_0.read_status(0XFE)))))
```

- 获取固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_set_config_mode.svg">

```python
servos8_0.set_config_mode(0, 0)
```

- 设置指定通道的配置模式
  - Digital Input:数字输入模式
  - Digital Output:数字输出模式
  - ADC Input:模拟输入模式
  - Servo CTRL:舵机控制模式
  - RGB LED:RGB LED 控制模式
  - PWM Duty:PWM 占空比控制模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_set_i2c_address.svg">

```python
servos8_0.set_i2c_address(0x0x25)
```

- 设置 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_write_digital_output_pin.svg">

```python
servos8_0.write_output_pin(0, 0)
```

- 设置指定通道数字输出电平

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_write_pwm_duty.svg">

```python
servos8_0.write_pwm_duty(0, 50)
```

- 设置指定通道的 PWM 占空比

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_write_rgb_led_pin.svg">

```python
servos8_0.write_rgb_led(0, 0xff0000)
```

- 设置指定通道的 RGB LED 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_write_servo_angle.svg">

```python
servos8_0.write_servo_angle(0, 0)
```

- 设置指定通道的舵机旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/8servo/uiflow_block_unit_servos8_write_servo_pulse.svg">

```python
servos8_0.write_servo_pulse(0, 500)
```

- 设置指定通道的舵机脉冲宽度

