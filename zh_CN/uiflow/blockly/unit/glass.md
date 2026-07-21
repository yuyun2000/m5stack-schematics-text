# [Unit Glass](/zh_CN/unit/Glass%20Unit)

## 案例程序

> 绘制文本，直线，圆并唤醒蜂鸣器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
glass_0 = unit.get(unit.GLASS_OLED, unit.PORTA)

glass_0.draw_text('M5Stack', 0, 0, 8, 1)
glass_0.draw_line(0, 10, 50, 10, 1)
glass_0.draw_circle(30, 30, 8, 1)
glass_0.disp_show()
glass_0.buzzer_freq(1000, 50)
glass_0.buzzer_ctrl(1)
wait(1)
glass_0.buzzer_ctrl(0)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_buzzer_ctrl.svg">

```python
glass_0.disp_ctrl(1)
```

- 设置屏幕显示开关
  - 1:ON
  - 0:OFF

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_buzzer_freq.svg">

```python
glass_0.buzzer_freq(1000, 50)
```

- 设置蜂鸣器的频率和占空比

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_colour_reverse.svg">

```python
glass_0.colour_reverse(0)
```

- 设置屏幕颜色(正常显示还是反转颜色)
  - 1:NORMAL(正常)
  - 0:REVERSE(反转)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_disp_clear.svg">

```python
glass_0.disp_clear()
```

- 清除屏幕显示

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_disp_ctrl.svg">

```python
glass_0.disp_ctrl(1)
```

- 设置屏幕显示开关
  - 1:ON
  - 0:OFF

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_disp_invert.svg">

```python
glass_0.disp_invert(0, 0)
```

- 设置显示模式，正常显示或者反转
  - 1:NORMAL(正常)
  - 0:REVERSE(反转)
  - filp:(0°/180°)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_disp_show.svg">

```python
glass_0.disp_show()
```

- 打开屏幕显示开关

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_draw_circle.svg">

```python
glass_0.draw_circle(0, 0, 5, 1)
```

- 画圆，输入半径和坐标

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_draw_line.svg">

```python
glass_0.draw_line(0, 0, 10, 10, 1)
```

- 画线，输入点到点的坐标

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_draw_pixel.svg">

```python
glass_0.draw_pixel(0, 0, 1)
```

- 输入显示像素点

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_draw_text.svg">

```python
glass_0.draw_text('', 0, 0, 8, 1)
```

- 输入显示文字，输入坐标和字号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_get_button_status.svg">

```python
print(glass_0.get_button_status(0))
```

- 获取按键的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/glass/uiflow_block_unit_glass_get_fw_version.svg">

```python
print(glass_0.get_firmware_version())
```

- 获取固件的版本

