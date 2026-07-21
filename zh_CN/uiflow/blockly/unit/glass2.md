# [Unit Glass2](/zh_CN/unit/Glass2%20Unit)

## 案例程序

> 绘制文本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

glass2_0 = unit.get(unit.GLASS2_OLED, unit.PORTA)

font_size = None
from numbers import Number

font_size = 0
glass2_0.fill(0x000000)
for count in range(4):
  font_size = (font_size if isinstance(font_size, Number) else 0) + 1
  if font_size == 1:
    glass2_0.print('M5STACK', 0, 0, 1, 0xffffff)
  elif font_size == 2:
    glass2_0.print('M5STACK', 10, 0, 2, 0xffffff)
  elif font_size == 3:
    glass2_0.print('M5STACK', 25, 0, 3, 0xffffff)
  elif font_size == 4:
    glass2_0.print('M5STACK', 40, 0, 4, 0xffffff)
    font_size = 0
  glass2_0.show()
  wait_ms(500)
glass2_0.fill(0x000000)
glass2_0.show()
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_init.svg">

```python
glass2_0.init_device_address(0x3C)
```

- 设置 I2C 地址(0x3C~0x3D)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_display_brightness.svg">

```python
glass2_0.contrast(0)
```

- 设置屏幕亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_display_invert.svg">

```python
glass2_0.invert(1)
```

- 设置屏幕颜色(正常显示还是反转颜色)
  - 0:NORMAL(正常)
  - 1:REVERSE(反转)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_display_power.svg">

```python
glass2_0.power_ctrl(0x00)
```

- 屏幕电源开启和关闭(ON/OFF)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_display_scroll.svg">

```python
glass2_0.scroll(0, 0)
```

- 从新复制一份以上运行代码屏幕显示的内容，并定义初始位置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_display_show.svg">

```python
glass2_0.show()
```

- 打开屏幕显示开关


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_fill.svg">

```python
glass2_0.fill(0xffffff)
```

- 设置全屏颜色
  - White：白
  - Black：黑

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_fill_rect.svg">

```python
glass2_0.fill_rect(0, 0, 0, 0, 0xffffff)
```

- 绘制方形

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_hline.svg">

```python
glass2_0.hline(0, 0, 0, 0xffffff)
```

- 绘制水平线

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_image.svg">

```python
glass2_0.image(0, 0, "/flash/img/m5stack.pbm")
```

- 填充外部资源图片

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_line.svg">

```python
glass2_0.line(0, 0, 0, 0, 0xffffff)
```

- 绘制线条，输入点到点坐标

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_pixel.svg">

```python
glass2_0.pixel(0, 0, 0xffffff)
```

- 输入显示像素点

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_rect.svg">

```python
glass2_0.rect(0, 0, 0, 0, 0xffffff)
```

- 绘制矩形

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_text.svg">

```python
glass2_0.print('M5Stack', 0, 0, 1, 0xffffff)
```

- 绘制文本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass2/uiflow_block_unit_glass2_vline.svg">

```python
glass2_0.vline(0, 0, 0, 0xffffff)
```

- 绘制垂直线

