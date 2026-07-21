# [Unit BLDC Driver](/zh_CN/unit/Unit-BLDC%20Driver)

## 案例程序

> 电机匀速旋转

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
bldc_driver_0 = unit.get(unit.BLDC_DRIVER, unit.PORTA)

bldc_driver_0.init_i2c_address(0x65)
bldc_driver_0.set_motor_model(1)
bldc_driver_0.set_mode(0)
while True:
  bldc_driver_0.set_open_loop_pwm(500)
  bldc_driver_0.set_rpm_float(500)
  print((str('rpm value:') + str((bldc_driver_0.get_read_back_rpm_str))))
  print((str('pwm value:') + str((bldc_driver_0.get_open_loop_pwm))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_init.svg">

```python
bldc_driver_0.init_i2c_address(0x65)
```

- 初始化 BLDC Driver 并设置 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_device_spec.svg">

```python
print((str('Version:') + str((bldc_driver_0.get_device_spec(0xFE)))))
```

- 获取设备的当前版本
  - FIRMWARE_VERSION
  - I2C_ADDRESS 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_direction.svg">

```python
print((str('Current direction:') + str((bldc_driver_0.get_motor_current_direction))))
```

- 获取电机当前转动方向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_mode.svg">

```python
print((str('Current mode:') + str((bldc_driver_0.get_current_mode))))
```

- 获取当前模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_motor_model.svg">

```python
print((str('Mofot Current mode:') + str((bldc_driver_0.get_motor_current_model))))
```

- 获取电机当前的工作模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_motor_pole_pairs.svg">

```python
print((str('pole pairs:') + str((bldc_driver_0.get_motor_pole_pairs))))
```

- 获取电机的极对数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_pid.svg">

```python
print((str('PID value:') + str((bldc_driver_0.get_pid_value))))
```

- 获取 PID 控制器的参数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_pwm.svg">

```python
print((str('dutycycle value:') + str((bldc_driver_0.get_open_loop_pwm))))
```

- 获取开环模式下 PWM 的占空比值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_read_back_freq_float.svg">

```python
print((str('freq value') + str((bldc_driver_0.get_read_back_freq_float))))
```

- 获取反馈的频率值（浮点数格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_read_back_freq_int.svg">

```python
print((str('freq value:') + str((bldc_driver_0.get_read_back_freq_int))))
```

- 获取反馈的频率值（整数格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_read_back_freq_str.svg">

```python
print((str('freq value:') + str((bldc_driver_0.get_read_back_freq_str))))
```

- 获取反馈的频率值（字符串格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_read_back_rpm_float.svg">

```python
print((str('freq value:') + str((bldc_driver_0.get_read_back_freq_float))))
```

- 获取反馈的转速值（RPM，浮点数格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_read_back_rpm_int.svg">

```python
print((str('rpm value:') + str((bldc_driver_0.get_read_back_rpm_int))))
```

- 获取反馈的转速值（RPM，整数格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_read_back_rpm_str.svg">

```python
print((str('rpm value:') + str((bldc_driver_0.get_read_back_rpm_str))))
```

- 获取反馈的转速值（RPM，字符串格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_rpm_float.svg">

```python
print((str('rpm value:') + str((bldc_driver_0.get_read_back_rpm_float))))
```

- 获取设定的转速值（RPM，浮点数格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_rpm_int.svg">

```python
print((str('rpm value:') + str((bldc_driver_0.get_rpm_int))))
```

- 获取设定的转速值（RPM，整数格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_get_status.svg">

```python
print((str('motor status:') + str((bldc_driver_0.get_motor_status))))
```

- 获取电机的当前状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_save.svg">

```python
bldc_driver_0.save_data_in_flash()
```

- 将当前电机数据保存到闪存中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_direction.svg">

```python
bldc_driver_0.set_direction(0)
```

- 设置电机转动方向为正向
  - FORWARD
  - BACKWARD

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_i2c_address.svg">

```python
bldc_driver_0.set_i2c_address(0x65)
```

- 设置设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_mode.svg">

```python
bldc_driver_0.set_mode(0)
```

- 设置电机模式
  - OPEN_LOOP:开环
  - COLSE_LOOP:闭环

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_motor_model.svg">

```python
bldc_driver_0.set_motor_model(0)
```

- 设置电机速度模式
  - LOW_SPEED
  - HIGH_SPEED

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_open_loop_pwm.svg">

```python
bldc_driver_0.set_open_loop_pwm(500)
```

- 设置开环模式下 PWM 的占空比

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_pid.svg">

```python
bldc_driver_0.set_pid_value(14200, 5536, 1580)
```

- 设置 PID 控制器的参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_pole_pairs.svg">

```python
bldc_driver_0.set_pole_pairs(7)
```

- 设置电机的极对数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_rpm_float.svg">

```python
bldc_driver_0.set_rpm_float(500)
```

- 设置电机转速（浮点数格式）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bldc_driver/uiflow_block_unit_bldcdriver_set_rpm_int.svg">

```python
bldc_driver_0.set_rpm_int(500)
```

- 设置电机转速（整数格式）

