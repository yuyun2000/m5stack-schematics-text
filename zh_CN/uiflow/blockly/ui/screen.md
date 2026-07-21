# Screen

## 案例程序

调节屏幕亮度，并切换屏幕颜色。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ui/screen/uiflow_block_screen_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0x222222)
lcd.setBrightness(30)

while True:
  setScreenColor(0xff0000)
  wait(1)
  setScreenColor(0x3366ff)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ui/screen/uiflow_block_screen_set_backgroundcolor.svg"> 

```python
setScreenColor(0xff0000)
```

- 设置屏幕颜色
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ui/screen/uiflow_block_screen_set_backgroundcolor_rgb_value.svg"> 

```python
setScreenColor(0xff0000)
```
 
- 设置屏幕颜色，通过修改 RGB 数值进行颜色修改
  - (R:0-255  G:0-255 B:0-255)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ui/screen/uiflow_block_screen_set_backgroundcolor_option.svg"> 

```python
setScreenColor(0xff0000)
```

- 设置颜色数据类型
  - `Palette`: 直接选择颜色面板进行切换屏幕颜色
  - `RGB`: 输入 RGB 数值进行切换颜色面板颜色
  - `HEX`: 输入颜色转化而成的16进制数值进行切换数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ui/screen/uiflow_block_screen_set_rotate_mode.svg"> 

```python
lcd.setRotation(0)
```

- 旋转屏幕
  - "0"：逆时针旋转270°
  - "1"：逆时针旋转180°
  - "2"：逆时针旋转90°
  - "3"：旋转0°，水平显示

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ui/screen/uiflow_block_screen_set_brightness.svg"> 

```python
lcd.setBrightness(30)
```

- 设置屏幕亮度，数值范围0-255，整数型，数值越大，亮度越大。
