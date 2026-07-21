# [Unit Roller485](/zh_CN/unit/Unit-Roller485)

## 案例程序

启动电机旋转

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_roller485_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
roller485_0 = unit.get(unit.ROLLER485, unit.PORTA)

roller485_0.init_device(0, 0x64)
roller485_0.set_motor_mode(1)
roller485_0.set_motor_output_state(1)
while True:
  roller485_0.set_motor_speed_current_setting(1000, 400)
  roller485_0.set_motor_speed_pid(15, 0.0001, 400)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_init.svg">

```python
roller485_0.init_device(0, 0x64)
```

- 初始化Roller通信模式为I2C

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_device_spec.svg">

```python
print((str('spec:') + str((roller485_0.get_device_spec(0xFE)))))
```

- 获取设备信息（返回整数）
  - FIRMWARE：规格固件信息
  - I2C ADDRESS：I2C 地址信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_encoder_value.svg">

```python
print((str('count value:') + str((roller485_0.get_encoder_value()))))
```

- 获取电机编码器计数值（返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_baudrate.svg">

```python
print((str('485 baudrate:') + str((roller485_0.get_485_baudrate()))))
```

- 获取电机485波特率（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_current_mode.svg">

```python
print((str('current mode:') + str((roller485_0.get_motor_mode()))))
```

- 获取电机当前工作模式（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_current_readback.svg">

```python
print((str('readback value:') + str((roller485_0.get_motor_current_readback()))))
```

- 获取电机电流反馈值（返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_error_code.svg">

```python
print((str('error code:') + str((roller485_0.get_motor_error_code()))))
```

-  获取电机错误代码（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_id.svg">

```python
print((str('485 id:') + str((roller485_0.get_motor_id()))))
```

-  获取电机485设备ID（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_max_current.svg">

```python
print((str('speed max current setting value:') + str((roller485_0.get_motor_speed_max_current()))))
```

- 获取电机最大电流设置值（单位：mA，返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_output_status.svg">

```python
print((str('output status:') + str((roller485_0.get_motor_output_status()))))
```

- 获取电机输出状态（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_position_max_current.svg">

```python
print((str('position max current setting value:') + str((roller485_0.get_motor_position_max_current()))))
```

- 获取位置模式最大电流设置值（单位：mA，返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_position_pid.svg">

```python
print((str('position pid:') + str((roller485_0.get_motor_position_pid()))))
```

- 获取位置环PID参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_position_readback.svg">

```python
print((str('readback value:') + str((roller485_0.get_motor_position_readback()))))
```

- 获取位置反馈值（返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_position_setting.svg">

```python
print((str('position setting value:') + str((roller485_0.get_motor_position_setting()))))
```

- 获取位置设定值（返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_speed_max_current.svg">

```python
print((str('speed max current setting value:') + str((roller485_0.get_motor_speed_max_current()))))
```

- 获取速度模式最大电流设置值（单位：mA，返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_speed_pid.svg">

```python
print((str('speed id:') + str((roller485_0.get_motor_speed_pid()))))
```

- 获取速度环PID参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_speed_readback.svg">

```python
print((str('readback value:') + str((roller485_0.get_motor_speed_readback()))))
```

-  获取速度反馈值（单位：RPM，返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_motor_speed_setting.svg">

```python
print((str('setting value:') + str((roller485_0.get_motor_speed_setting()))))
```

- 获取速度设定值（单位：RPM，返回浮点数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_rgb_brightness.svg">

```python
print((str('brightness:') + str((roller485_0.get_rgb_brightness()))))
```

- 获取RGB颜色亮度（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_rgb_color.svg">

```python
print((str('RGB color:') + str((roller485_0.get_rgb_color()))))
```

-  获取RGB颜色值（返回元组：R,G,B）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_rgb_mode.svg">

```python
print((str('RGB mode:') + str((roller485_0.get_rgb_mode()))))
```

-  获取RGB工作模式（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_temperature.svg">

```python
print((str('temperature:') + str((roller485_0.get_temperature_value()))))
```

- 获取设备温度（返回整数，单位：℃）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_get_vin_value.svg">

```python
print((str('voltage:') + str((roller485_0.get_vin_value()))))
```

-  获取设备输入电压（单位：mV，返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_button_change_mode.svg">

```python
roller485_0.set_button_change_mode(0)
```

- 通过按钮切换电机模式(禁用/开启)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_data_save_in_flash.svg">

```python
roller485_0.set_data_save_in_flash()
```

- 将电流设置保存到Flash

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_encoder_value.svg">

```python
roller485_0.set_encoder_value(1000)
```

- 设置电机编码器计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_i2c_address.svg">

```python
roller485_0.set_i2c_address(0x64)
```

-  设置电机485波特率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_baudrate.svg">

```python
roller485_0.set_485_baudrate(0)
```

- 获取电机485设备ID（返回整数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_id.svg">

```python
roller485_0.set_motor_id(0x01)
```

- 设置电机485设备ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_max_current.svg">

```python
roller485_0.set_motor_max_current(400)
```

- 设置电机最大电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_mode.svg">

```python
roller485_0.set_motor_mode(1)
```

- 设置电机模式
  - Speed
  - Position
  - Current
  - Encoder

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_output_control.svg">

```python
roller485_0.set_motor_output_state(1)
```

- 开启/关闭 电机输出控制

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_position_current_setting.svg">

```python
roller485_0.set_motor_position_current_setting(1000, 400)
```

- 设置位置模式目标位置脉冲，最大电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_position_pid.svg">

```python
roller485_0.set_motor_position_pid(15, 0.0001, 400)
```

- 设置位置环PID参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_speed_current.svg">

```python
roller485_0.set_motor_speed_current_setting(1000, 400)
```

- 设置速度模式目标转速，最大电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_motor_speed_pid.svg">

```python
roller485_0.set_motor_speed_pid(15, 0.0001, 400)
```

- 设置速度环PID参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_moto_over_range_protect.svg">

```python
roller485_0.set_motor_over_range_protect(0)
```

- 禁用/开启 电机超范围保护

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_remove_protect.svg">

```python
roller485_0.set_remove_protect()
```

- 启用解除卡死保护

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_rgb_brightness.svg">

```python
roller485_0.set_rgb_brightness(50)
```

- 设置RGB亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_rgb_color.svg">

```python
roller485_0.set_rgb_color((0xff0000))
```

- 设置RGB颜色调色板

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_rgb_mode.svg">

```python
roller485_0.set_rgb_mode(0)
```

- 设置RGB工作模式
  - disable
  - enable

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/roller_485/uiflow_block_unit_roller485_set_stall_protect.svg">

```python
roller485_0.set_motor_stall_protect(0)
```

-  开启/禁用 电机堵转保护



