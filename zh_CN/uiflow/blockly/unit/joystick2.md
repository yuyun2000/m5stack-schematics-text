# [Unit Joystick2](/zh_CN/unit/Unit-JoyStick2)

## 案例程序

> 初始化操纵杆模块的 I2C 地址和 LED 亮度，并在循环中连续获取操纵杆的当前位置、ADC 值、按键状态和固件版本，并将这些信息打印出来。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/uiflow_block_unit_joystick2_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

joystick2_0 = unit.get(unit.JOYSTICKV2, unit.PORTA)

joystick2_0.init_i2c_address(0x63)
joystick2_0.set_led_brightness(50)
while True:
  print(joystick2_0.get_axis_position())
  print(joystick2_0.get_x_position())
  print(joystick2_0.get_y_position())
  print(joystick2_0.get_adc_value())
  print(joystick2_0.get_x_raw())
  print(joystick2_0.get_y_raw())
  print(joystick2_0.get_button_status())
  print(joystick2_0.get_firmware_version())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/1_uiflow_block_unit_joystick2_init.svg">

```python
joystick2_0.init_i2c_address(0x63)
```

- 设置操纵杆模块的 I2C 地址。地址范围为 0x08 到 0x77，默认值为 0x63。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/2_uiflow_block_unit_joystick2_get_axis_position.svg">

```python
joystick2_0.get_axis_position()
```

- 获取操纵杆的当前位置(X 和 Y 坐标)，返回一个元组。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/3_uiflow_block_unit_joystick2_get_x_position.svg">

```python
joystick2_0.get_x_position()
```

- 获取操纵杆的 X 轴位置值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/4_uiflow_block_unit_joystick2_get_y_position.svg">

```python
joystick2_0.get_y_position()
```

- 获取操纵杆的 Y 轴位置值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/5_uiflow_block_unit_joystick2_get_adc_value.svg">

```python
joystick2_0.get_adc_value()
```

- 获取操纵杆的 X 和 Y 轴的 ADC 值(模拟值)，返回一个元组。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/6_uiflow_block_unit_joystick2_get_x_raw.svg">

```python
joystick2_0.get_x_raw()
```

- 获取操纵杆的 X 轴 ADC 值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/7_uiflow_block_unit_joystick2_get_y_raw.svg">

```python
joystick2_0.get_y_raw()
```

- 获取操纵杆的 Y 轴 ADC 值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/8_uiflow_block_unit_joystick2_get_button_status.svg">

```python
joystick2_0.get_button_status()
```

- 获取操纵杆按键的状态。如果按下，返回 True；否则返回 False。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/9_uiflow_block_unit_joystick2_get_firmware_version.svg">

```python
joystick2_0.get_firmware_version()
```

- 获取操纵杆模块的固件版本，返回一个整数值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/10_uiflow_block_unit_joystick2_set_axis_x_invert.svg">

```python
joystick2_0.set_axis_x_invert(True)
```

- 反转 X 轴方向。设置为 True 时，X 轴输出值将被反转。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/11_uiflow_block_unit_joystick2_set_axis_y_invert.svg">

```python
joystick2_0.set_axis_y_invert(True)
```

- 反转 Y 轴方向。设置为 True 时，Y 轴输出值将被反转。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/12_uiflow_block_unit_joystick2_set_axis_swap.svg">

```python
joystick2_0.set_axis_swap(True)
```

- 交换 X 轴和 Y 轴的输出值。设置为 True 时，X 和 Y 轴数据将互换。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/13_uiflow_block_unit_joystick2_set_deadzone_position.svg">

```python
joystick2_0.set_deadzone_position(0, 0)
```

- 设置操纵杆位置的死区范围。死区内的值会被视为中心位置，避免噪声干扰。参数范围为 0 到 4096。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/14_uiflow_block_unit_joystick2_set_deadzone_adc.svg">

```python
joystick2_0.set_deadzone_adc(0, 0)
```

- 设置操纵杆 ADC 值的死区范围。参数范围为 0 到 32768。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/15_uiflow_block_unit_joystick2_fill_color.svg">

```python
joystick2_0.fill_color(0xff0000)
```

- 设置操纵杆 LED 的填充颜色(如模块上的指示灯颜色)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/16_uiflow_block_unit_joystick2_set_led_brightness.svg">

```python
joystick2_0.set_led_brightness(50)
```

- 设置操纵杆 LED 的亮度，范围为 0% 到 100%。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/17_uiflow_block_unit_joystick2_set_address.svg">

```python
joystick2_0.set_i2c_address(0x63)
```

- 改变操纵杆模块的 I2C 地址。用于在多模块环境下避免地址冲突。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/18_uiflow_block_unit_joystick2_set_axis_x_mapping.svg">

```python
joystick2_0.set_axis_x_mapping(0, 0, 0, 0)
```

- 设置 X 轴的映射参数：
  - Min negative ADC value: X 轴负向最小 ADC 值(最左或最下)。
  - Max negative ADC value: X 轴负向最大 ADC 值。
  - Min positive ADC value: X 轴正向最小 ADC 值(最右或最上)。
  - Max positive ADC value: X 轴正向最大 ADC 值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick2/19_uiflow_block_unit_joystick2_set_axis_y_mapping.svg">

```python
joystick2_0.set_axis_y_mapping(0, 0, 0, 0)
```

- 设置 Y 轴的映射参数：
  - Min negative ADC value: Y 轴负向最小 ADC 值(最左或最下)。
  - Max negative ADC value: Y 轴负向最大 ADC 值。
  - Min positive ADC value: Y 轴正向最小 ADC 值(最右或最上)。
  - Max positive ADC value: Y 轴正向最大 ADC 值。


