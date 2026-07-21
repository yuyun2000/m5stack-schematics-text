# [Unit LCD](/zh_CN/unit/lcd)

## 案例程序

> 绘制基础图形和文字

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
lcd_0 = unit.get(unit.LCD, unit.PORTA)

lcd_0.fill(0x999999)
lcd_0.text('M5Stack', 0, 0, 0xff0000)
lcd_0.line(0, 10, 50, 10, 0xff0000)
lcd_0.rect(10, 10, 20, 20, 0xff0000)
lcd_0.brightness(0)
lcd_0.show_on()
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_init_display.svg">

```python
lcd_0.init_display(135, 240, 1)
```

- 初始化定义 Unit 屏幕大小

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_brightness.svg">

```python
lcd_0.brightness(0)
```

- 设置显示亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_fill.svg">

```python
lcd_0.fill(0xff0000)
```

- 设置屏幕颜色填充

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_fill_input.svg">

```python
lcd_0.fill(0xff0000)
```

- 设置屏幕颜色填充以及填充模式
  - plette
  - RGB
  - Hex

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_fill_rect.svg">

```python
lcd_0.fill_rect(0, 0, 0, 0, 0xff0000)
```

- 填充规定区域颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_fill_rect_input.svg">

```python
lcd_0.fill_rect(0, 0, 0, 0, 0xff0000)
```

- 填充规定区域颜色
  - plette
  - RGB
  - Hex

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_flip.svg">

```python
lcd_0.rotate(4)
```

- 设置屏幕翻转
  - Flip(1~6)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_hline.svg">

```python
lcd_0.hline(0, 0, 0, 0xff0000)
```

- 画横线

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_hline_input.svg">

```python
lcd_0.hline(0, 0, 0, 0xff0000)
```

- 画横线
  - plette
  - RGB
  - Hex

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_line.svg">

```python
lcd_0.line(0, 0, 0, 0, 0xff0000)
```

- 绘制点到点的直线

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_line_input.svg">

```python
lcd_0.line(0, 0, 0, 0, 0xff0000)
```

- 绘制点到点的直线
  - plette
  - RGB
  - Hex

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_pixel.svg">

```python
lcd_0.pixel(0, 0, 0xff0000)
```

- 绘制像素

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_pixel_input.svg">

```python
lcd_0.pixel(0, 0, 0xff0000)
```

- 绘制像素
  - plette
  - RGB
  - Hex

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_rect.svg">

```python
lcd_0.rect(0, 0, 0, 0, 0xff0000)
```

- 画正方形

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_rect_input.svg">

```python
lcd_0.rect(0, 0, 0, 0, 0xff0000)
```

- 画正方形
  - plette
  - RGB
  - Hex

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_rotate.svg">

```python
lcd_0.rotate(0)
```

- 设置转动角度(0,90,180,270)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_show_on.svg">

```python
lcd_0.show_on()
```

- 开启设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_sleep.svg">

```python
lcd_0.sleep(0)
```

- 设置睡眠时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_text.svg">

```python
lcd_0.text('', 0, 0, 0xff0000)
```

- 绘制文本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_text_input.svg">

```python
lcd_0.text('', 0, 0, 0xff0000)
```

- 绘制文本
  - plette
  - RGB
  - Hex

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_vline.svg">

```python
lcd_0.vline(0, 0, 0, 0xff0000)
```

- 画垂直线

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/lcd/uiflow_block_unit_lcd_vline_input.svg">

```python
lcd_0.vline(0, 0, 0, 0xff0000)
```

- 画垂直线
  - plette
  - RGB
  - Hex
