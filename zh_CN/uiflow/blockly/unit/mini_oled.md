# [Unit Mini Oled](/zh_CN/unit/MiniOLED%20Unit)

## 案例程序

> 点击按钮 A，滚动显示 “ WELCOME M5 MINI OLED"

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x272727)
mini_oled_0 = unit.get(unit.MINI_OLED, unit.PORTA)

i = None

# Describe this function...
def text_scroll():
  global i
  mini_oled_0.fill(0)
  mini_oled_0.text('WELCOME', 8, 4, 1)
  mini_oled_0.text('M5', 30, 18, 1)
  mini_oled_0.text('MINI OLED', 0, 32, 1)
  mini_oled_0.show()
  for count in range(5):
    mini_oled_0.invert(1)
    mini_oled_0.show()
    wait_ms(250)
    mini_oled_0.invert(0)
    mini_oled_0.show()
    wait_ms(250)
  for i in range(11):
    mini_oled_0.scroll(i, i)
    mini_oled_0.show()
    wait_ms(250)

def buttonA_wasPressed():
  global i
  text_scroll()
  pass
btnA.wasPressed(buttonA_wasPressed)

text_scroll()
wait_ms(200)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_display_brightness.svg">

```python
mini_oled_0.contrast(150)
```

- 设置显示亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_display_color.svg">

```python
mini_oled_0.invert(1)
```

- 设置显示颜色(正反转)
  - 0 :INVERT
  - 1 :NORMAL

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_display_power.svg">

```python
mini_oled_0.power_ctrl(0x00)
```

- 设置显示开关(NO/OFF)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_display_scroll.svg">

```python
mini_oled_0.scroll(0, 0)
```

- 设置屏幕滚动(X\Y)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_display_show.svg">

```python
mini_oled_0.show()
```

- 显示使能

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_fill.svg">

```python
mini_oled_0.fill(1)
```

- 填充颜色
  - 1: White
  - 0: Black

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_fill_rect.svg">

```python
mini_oled_0.fill_rect(0, 0, 0, 0, 1)
```

- 填充规定区域颜色
  - Color(1): White
  - Color(0): Black

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_hline.svg">

```python
mini_oled_0.hline(0, 0, 0, 1)
```

- 画横线
  - Color(1): White
  - Color(0): Black

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_line.svg">

```python
mini_oled_0.line(0, 0, 0, 0, 1)
```

- 画两点之间的直线
  - Color(1): White
  - Color(0): Black

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_pixel.svg">

```python
mini_oled_0.pixel(0, 0, 1)
```

- 画像素
  - Color(1): White
  - Color(0): Black

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_rect.svg">

```python
mini_oled_0.rect(0, 0, 0, 0, 1)
```

- 画正方形
  - Color(1): White
  - Color(0): Black

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_text.svg">

```python
mini_oled_0.text('', 0, 0, 1)
```

- 显示文字
  - Color(1): White
  - Color(0): Black

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_oled/uiflow_block_unit_minioled_vline.svg">

```python
mini_oled_0.vline(0, 0, 0, 1)
```

- 画垂直线
  - Color(1): White
  - Color(0): Black