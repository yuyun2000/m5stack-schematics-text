# Easy I/O

## 案例程序

读取数字引脚和模拟引脚的数值并显示在屏幕上

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/easyio/uiflow_block_easyio_demo1.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
from easyIO import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

label0 = M5Label('label0', x=130, y=60, color=0x000, font=FONT_MONT_14, parent=None)
label1 = M5Label('label1', x=130, y=102, color=0x000, font=FONT_MONT_14, parent=None)

label0.set_text(str(analogRead(39)))
label1.set_text(str(digitalRead(0)))
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/easyio/uiflow_block_easyio_analog_read_pin.svg"> 

```python
str(analogRead(39))
```

- 设置 ADC 引脚，并读取模拟值
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/easyio/uiflow_block_easyio_set_analog_read_pin.svg"> 

```python
str(analogRead(39))
```
 
- 设置 ADC 引脚，并读取模拟值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/easyio/uiflow_block_easyio_digital_read_pin.svg"> 

```python
str(digitalRead(0))
```

- 设置数字引脚，并读取电平值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/easyio/uiflow_block_easyio_map.svg"> 

```python
str(map_value(0, 0, 1023, 0, 4))
```

- map 映射函数
  - "0":需要映射的变量
  - "0":变量的最小值
  - "1023":变量的最大值
  - "0":映射输出的最小值
  - "4":映射输出的最大值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/easyio/uiflow_block_easyio_analog_write_pin_duty.svg"> 

```python
analogWrite(26, 0)
```

- 设置模拟引脚的输出占空比

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/easyio/uiflow_block_easyio_digital_write_pin_vale.svg"> 

```python
digitalWrite(26, 0)
```

- 设置数字引脚的输出电平值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/easyio/uiflow_block_easyio_toggle_pin.svg"> 

```python
toggleIO(26)
```

- 切换引脚电平值