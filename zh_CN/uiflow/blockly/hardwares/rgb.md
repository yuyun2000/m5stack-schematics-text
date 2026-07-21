# RGB

## 案例程序

驱动 RGB 灯带闪烁

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_RGB_demo.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x111111)

R = None
G = None
B = None
i = None

circle0 = M5Circle(95, 90, 15, 0xFFFFFF, 0xFFFFFF)
circle1 = M5Circle(220, 90, 15, 0xFFFFFF, 0xFFFFFF)

import random

while True:
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)
  for i in range(0, 256, 10):
    rgb.setColorFrom(6, 10, (R << 16) | (G << 8) | B)
    rgb.setColorFrom(1, 5, (G << 16) | (R << 8) | B)
    rgb.setBrightness(i)
  for i in range(255, -1, -10):
    rgb.setColorFrom(6, 10, (R << 16) | (G << 8) | B)
    rgb.setColorFrom(1, 5, (G << 16) | (R << 8) | B)
    rgb.setBrightness(i)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_color.svg"> 

```python
rgb.setColorAll(0xff0000)
```

- 设置所有灯的颜色
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_color_value.svg"> 

```python
rgb.setColorAll(0x000000)
```
 
- 设置所有灯珠的颜色 RGB 值
  - (R:0-255  G:0-255 B:0-255)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_color_option.svg"> 

```python
rgb.setColorAll(0x000000)
```

- 设置颜色数据类型
  - `Palette`: 直接选择颜色面板进行切换灯带颜色
  - `RGB`: 输入 RGB 数值进行切换灯带颜色
  - `HEX`: 输入颜色转化而成的16进制数值进行灯珠颜色切换


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_side_color.svg"> 

```python
rgb.setColorFrom(6, 10, 0xff0000)
```

- 数值
  - "6"：第六个灯珠
  - "10"：第十个灯珠
  - "0xff0000"：RGB 值

#>说明|右边灯珠是第一至第五个灯珠，左边是代表第六到第十个灯珠

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_side_color_value.svg"> 

```python
rgb.setColorFrom(6, 10, 0xff0000)
```

- 选择不同侧的灯珠，并通过 RGB 值进行切换颜色


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_side_color_option.svg"> 

```python
rgb.setColorFrom(6, 10, 0xff0000)
```

- 设置颜色数据类型
  - `Palette`: 直接选择颜色面板进行切换灯带颜色
  - `RGB`: 输入 RGB 数值进行切换灯带颜色
  - `HEX`: 输入颜色转化而成的16进制数值进行灯珠颜色切换


#>说明|选择不同侧的灯带，并切换调节模式进行切换颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_index_color.svg"> 

```python
rgb.setColor(1, 0xff0000)
```

- 数值
  - "1"：设置单个具体灯珠进行颜色切换(1-10)
  - "0xff0000"：颜色数值


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_index_color_value.svg"> 

```python
rgb.setColor(1, 0xff0000)
```

- 设置具体某个灯珠的颜色 RGB 值
  - (R:0-255  G:0-255 B:0-255)


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_side_color_option.svg"> 

```python
rgb.setColor(1, 0xff0000)
```

- 设置单颗灯珠颜色数据类型
  - `Palette`: 直接选择颜色面板进行切换灯带颜色
  - `RGB`: 输入 RGB 数值进行切换灯带颜色
  - `HEX`: 输入颜色转化而成的16进制数值进行灯珠颜色切换

#>说明|选择单颗灯珠，并切换调节模式进行切换颜色


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rgb/uiflow_block_rgb_bar_brightness.svg"> 

```python
rgb.setBrightness(10)
```

- 设置灯珠亮度(0-255)
  - 数值越大灯珠越亮