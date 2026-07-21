# [Hat Mini Joyc](/zh_CN/hat/MiniJoyC)

## 案例程序

设置通讯地址，获取电位器的 X,Y 原始数值和按键的初始状态值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_mini_joyc_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_mini_joyc_0 = hat.get(hat.MINI_JOYC)

hat_mini_joyc_0.init_i2c_address(0x54)
while True:
  print(hat_mini_joyc_0.get_adc12_raw(0))
  print(hat_mini_joyc_0.get_adc12_raw(1))
  print(hat_mini_joyc_0.get_button_status())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_init.svg">

```python
hat_mini_joyc_0.init_i2c_address(0x54)
```

- 初始化 Mini JoyC 的 I2C 地址，此处设置为 0x54

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_get_10bit_value.svg">

```python
hat_mini_joyc_0.get_10bit_value()
```

- 从 Mini JoyC 获取 10 位分辨率的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_get_8bit_value.svg">

```python
hat_mini_joyc_0.get_8bit_value()
```

- 从 Mini JoyC 获取 8 位分辨率的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_get_button_status.svg">

```python
hat_mini_joyc_0.get_button_status()
```

- 获取 Mini JoyC 上按钮的当前状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_get_device_status.svg">

```python
hat_mini_joyc_0.get_device_status()
```

- 检查 Mini JoyC 设备的当前状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_get_offset_value.svg">

```python
hat_mini_joyc_0.get_offset_value()
```

- 获取 Mini JoyC 的偏移值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_get_raw_value.svg">

```python
hat_mini_joyc_0.get_raw_value()
```

- 从 Mini JoyC 获取原始 ADC（模数转换）值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_set_i2c_address.svg">

```python
hat_mini_joyc_0.set_i2c_address(new_address)
```

- 将 Mini JoyC 的 I2C 地址更改为 new_address。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_set_led_rgb.svg">

```python
hat_mini_joyc_0.set_led_rgb(red, green, blue)
```

- 通过指定红、绿、蓝值来设置 Mini JoyC 上的 RGB LED 颜色。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_joyc/uiflow_block_hat_minijoyc_set_offset_value.svg">

```python
hat_mini_joyc_0.set_offset_value(offset)
```

- 为 Mini JoyC 设置偏移值。

