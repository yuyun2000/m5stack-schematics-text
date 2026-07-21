# [Module 4Encoder Motor](/zh_CN/module/Module-4EncoderMotor)

## 案例程序

4个编码点击分别设置不同的 pwm 值，控制不同转速和方向，以及打印输出输入电压值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_4encoder_demo2.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import module

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

encoder4_motor = module.get(module.ENCODER4MOTOR)

encoder4_motor.init_i2c_address(0x24)
encoder4_motor.set_all_motors_mode(0x00)
while True:
  encoder4_motor.set_motor_pwm_dutycycle(0x00, (-127))
  encoder4_motor.set_motor_pwm_dutycycle(0x01, 50)
  encoder4_motor.set_motor_pwm_dutycycle(0x02, 95)
  encoder4_motor.set_motor_pwm_dutycycle(0x03, 127)
  print((str('Vin value:') + str((encoder4_motor.get_vin_current_int_value()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_device_spec.svg">

```python
encoder4_motor.get_device_spec(0xFE)
```

- 获取设备的固件版本信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_encoder_mode_direction.svg">

```python
encoder4_motor.get_encoder_mode()
```

- 获取编码器模式的方向信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_motor_encoder_value.svg">

```python
encoder4_motor.get_motor_encoder_value(0x00)
```

- 获取指定电机的编码器值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_motor_pos_pid_value.svg">

```python
encoder4_motor.get_position_PID_value(0x00)
```

- 获取指定电机的位置控制 PID 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_motor_speed_pid_value.svg">

```python
encoder4_motor.get_speed_PID_value(0x00)
```

- 获取指定电机的速度控制 PID 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_motor_speed_value.svg">

```python
encoder4_motor.get_motor_speed_value(0x00)
```

- 获取指定电机的当前速度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_vin_adc_raw12_value.svg">

```python
encoder4_motor.get_vin_adc_raw12_value()
```

- 获取输入电压的12位 ADC(模数转换)原始值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_vin_adc_raw8_value.svg">

```python
encoder4_motor.get_vin_adc_raw8_value()
```

- 获取输入电压的8位 ADC(模数转换)原始值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_vin_current_float_value.svg">

```python
encoder4_motor.get_vin_current_float_value()
```

- 获取输入电压的电流值(单位为安培)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_vin_current_value.svg">

```python
encoder4_motor.get_vin_current_int_value()
```

- 获取输入电压的电流值(单位为毫安)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_get_vin_voltage_value.svg">

```python
encoder4_motor.get_vin_voltage()
```

- 获取输入电压的电压值，返回一个整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_init.svg">

```python
encoder4_motor.init_i2c_address(0x24)
```

- 初始化设备的 I2C 地址，范围是0x01到0x7F

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_encoder_mode_direction.svg">

```python
encoder4_motor.set_encoder_mode(0x00)
```

- 设置编码器模式的方向，图中选择的是 "AB" 或 “BA” 模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_i2c_address.svg">

```python
encoder4_motor.set_i2c_address(0x24)
```

- 设置设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_mode.svg">

```python
encoder4_motor.set_motor_mode(0x00, 0x00)
```

- 设置电机1的运行模式。在下拉菜单中，有三个选项：
    - NORMAL: 正常模式，电机按默认设置运行。
    - POSITION: 位置控制模式，通过指定的位置控制电机的运动。
    - SPEED: 速度控制模式，通过指定的速度控制电机的转动。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_mode_all.svg">

```python
encoder4_motor.set_all_motors_mode(0x00)
```

- 设置所有电机的模式
  - NORMAL: 正常模式，电机按默认设置运行。
  - POSITION: 位置控制模式，通过指定的位置控制电机的运动。
  - SPEED: 速度控制模式，通过指定的速度控制电机的转动。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_motor_encoder_value.svg">

```python
encoder4_motor.set_motor_encoder_value(0x00, 1000)
```

- 设置电机的编码器值，这个值通常表示电机的当前位置或累计转动量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_pos_encoder_value.svg">

```python
encoder4_motor.set_position_encoder_value(0x00, 1000)
```

- 设置电机的位置编码器值。这个值用于指定电机的目标位置或位置控制中的当前位置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_pos_max_speed_value.svg">

```python
encoder4_motor.set_position_max_speed_value(0x00, 100)
```

- 设置电机在位置控制模式下的最大速度值，范围是-127到127

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_pos_pid_value.svg">

```python
encoder4_motor.set_position_PID_value(0x00, 3, 1, 15)
```

- 设置电机的位置控制 PID 参数，P(比例)、I(积分)、D(微分),这些参数用于调整电机的响应特性。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_pwm_dutycycle.svg">

```python
encoder4_motor.set_motor_pwm_dutycycle(0x00, 50)
```

- 设置电机1的 PWM 占空比，范围是-127到127。占空比控制电机的转速和方向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_speed_pid_value.svg">

```python
encoder4_motor.set_speed_PID_value(0x00, 10, 1, 15)
```

- 设置电机的速度控制 PID 参数，P(比例)、I(积分)、D(微分)。用于速度控制时的调整

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4encoder_motor/uiflow_block_module_4encodermotor_set_speed_point_value.svg">

```python
encoder4_motor.set_speed_point_value(0x00, 50)
```

- 设置电机1的速度设定值，范围是-127到127。这个值表示目标速度

