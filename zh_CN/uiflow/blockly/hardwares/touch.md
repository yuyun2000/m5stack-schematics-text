# Touch

## 案例程序

将触摸坐标和触摸状态显示在屏幕上

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/touch/uiflow_block_touch_demo.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
from m5stack import touch

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

label0 = M5Label('label0', x=123, y=59, color=0x000, font=FONT_MONT_14, parent=None)
label1 = M5Label('label1', x=121, y=93, color=0x000, font=FONT_MONT_14, parent=None)

while True:
  label0.set_text(str(touch.read()))
  label1.set_text(str(touch.status()))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/touch/uiflow_block_touch_get_touch_coordinate.svg"> 

```python
str(touch.read())
```

- 获取屏幕触摸点坐标 x 和 y 轴(x：0-320,y：0-240)
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/touch/uiflow_block_touch_get_touch_coordinate_x.svg"> 

```python
str(touch.read()[0])
```
 
- 获取屏幕触摸点的 x 轴坐标(返回0-320)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/touch/uiflow_block_touch_get_touch_coordinate_y.svg"> 

```python
str(touch.read()[1])
```

- 获取屏幕触摸点的 y 轴坐标(返回0-240)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/touch/uiflow_block_touch_get_touch_press_status.svg"> 

```python
str(touch.status())
```

- 返回 true 或者 false，触摸屏幕返回 ture，没有触摸屏幕返回 false


