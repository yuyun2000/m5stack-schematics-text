# [Unit RGB](/zh_CN/unit/rgb)

## 案例程序

RGB 灯闪烁

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_rgb_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
rgb_0 = unit.get(unit.RGB, unit.PORTB)

while True:
  rgb_0.setColor(1, 0xff0000)
  rgb_0.setColor(2, 0x33ff33)
  rgb_0.setColor(3, 0x3366ff)
  wait(0.1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_block_rgb_unit_set_brightness.svg">

```python
rgb_0.setBrightness(20)
```

- 设置亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_block_rgb_unit_set_color.svg">

```python
rgb_0.setColor(1, 0xff0000)
```

- 设置指定 LED 灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_block_rgb_unit_set_color_all.svg">

```python
rgb_0.setColorAll(0xff0000)
```

- 设置所有 LED 灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_block_rgb_unit_set_color_all_input.svg">

```python
rgb_0.setColorAll(0xff0000)
```

- 设置所有 LED 灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_block_rgb_unit_set_color_from.svg">

```python
rgb_0.setColorFrom(1, 3, 0xff0000)
```

- 设置指定范围 LED 灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_block_rgb_unit_set_color_from_input.svg">

```python
rgb_0.setColorFrom(1, 3, 0xff0000)
```

- 设置指定范围 LED 灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_block_rgb_unit_set_color_input.svg">

```python
rgb_0.setColor(1, 0xff0000)
```

- 设置指定 LED 灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb/uiflow_block_rgb_unit_set_color_rgb.svg">

```python
rgb_0.setColor(1, 0x000000)
```

- 设置指定 LED 灯颜色（RGB）

