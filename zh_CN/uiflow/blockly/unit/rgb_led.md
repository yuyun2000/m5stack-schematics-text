# [Unit RGB LED](/zh_CN/unit/neopixel)

## 案例程序

矩阵流水灯

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_rgbled_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
neopixel_0 = unit.get(unit.NEOPIXEL, unit.PORTB, 10)

R = None
G = None
B = None
i = None

import random

while True:
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)
  for i in range(1, 31):
    neopixel_0.setColorFrom(1,i,(R << 16) | (G << 8) | B)
  wait_ms(500)
  for i in range(1, 31):
    neopixel_0.setColorFrom(1, i, 0x000000)
  wait_ms(500)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_brightness.svg">

```python
neopixel_0.setBrightness(20)
```

- 设置亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_color.svg">

```python
neopixel_0.setColor(1, 0xff0000)
```

- 设置颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_color_all.svg">

```python
neopixel_0.setColorAll(0xff0000)
```

- 设置指定单个 LED 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_color_all_input.svg">

```python
neopixel_0.setColorAll(0xff0000)
```

- 设置所有 LED 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_color_from.svg">

```python
neopixel_0.setColorFrom(1, 5, 0xff0000)
```

- 设置指定范围 RGB LED 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_color_from_input.svg">

```python
neopixel_0.setColorFrom(1, 5, 0xff0000)
```

- 设置指定范围 RGB LED 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_color_from_rgb.svg">

```python
neopixel_0.setColorFrom(1, 5, 0x000000)
```

- 设置指定范围 RGB LED 颜色 （RGB）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_color_input.svg">

```python
neopixel_0.setColor(1, 0xff0000)
```

- 设置指定 RGB LED 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_hexagon_matrix.svg">

```python
neopixel_0.setShowLock(True)
```

- 设置六边形矩阵

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_hexagon_matrix_rgb.svg">

```python
neopixel_0.setShowLock(True)
```

- 设置六边形矩阵RGB 灯

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_set_show_lock.svg">

```python
neopixel_0.setShowLock(True)
```

- 设置显示锁定状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rgb_led/uiflow_block_rgb_multi_show.svg">

```python
neopixel_0.show()
```

- 显示 RGB LED

