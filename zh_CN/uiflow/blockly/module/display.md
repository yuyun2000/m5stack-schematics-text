# [Module13.2 Display](/zh_CN/module/Display%20Module%2013.2)

## 案例程序

Display 屏幕显示 “M5Stack”

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/display/uiflow_display_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

display = module.get(module.M5DISPLAY)
hdmi = display.display_init()

setScreenColor(0x222222)
setResolution(1280, 720, type=hdmi)
setScreenColor(0x000000, type=hdmi)

display_module_title0 = M5Title(title="Title", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF, type=hdmi)
display_module_label0 = M5TextBox(91, 185, "M5Stack", lcd.FONT_DejaVu56, 0xFFFFFF, rotate=0, type=hdmi)


setScreenColor(0xff0000, type=hdmi)
setScreenColor(0x14b6c6, type=hdmi)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/display/uiflow_block_display_screen_set_bgcolor.svg">

```python
setScreenColor(0xff0000, type=hdmi)
```

- 设置屏幕的背景颜色为红色
  - Red: 表示选择的颜色是红色。系统使用默认的颜色编码来填充屏幕背景。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/display/uiflow_block_display_screen_set_bgcolor_input.svg">

```python
setScreenColor(0xff0000, type=hdmi)
```

- 通过使用调色板选择背景颜色，然后设置屏幕的背景颜色为所选颜色
  - Palette: 提供一个颜色选择工具或预定义颜色供你选择。当前选择的是红色 (Red)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/display/uiflow_block_display_screen_set_bgcolor_rgb.svg">

```python
setScreenColor(0x000000, type=hdmi)
```

- 使用 RGB(红色、绿色、蓝色)值精确设置屏幕背景颜色
    - R: 红色通道的值，范围是0到255。值为 0 时，表示没有红色。
    - G: 绿色通道的值，范围是0到255。值为 0 时，表示没有绿色。
    - B: 蓝色通道的值，范围是0到255。值为 0 时，表示没有蓝色。
    - 在这个例子中，RGB 三个通道的值都为 0，这表示屏幕背景将设置为黑色。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/display/uiflow_block_display_screen_set_rotate.svg">

```python
hdmi.setRotation(0)
```

- 设置屏幕的旋转模式
  - 0: 旋转模式参数，当前值为 0 表示默认模式，不旋转屏幕。如果设置为其他值，如 1, 2, 3，屏幕将会分别旋转90度、180度或270度。

