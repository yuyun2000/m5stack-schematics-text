# EEPROM

## 案例程序

写入变量进入 EEPROM，并显示在屏幕

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/eeprom/uiflow_block_eeprom_demo.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import nvs

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

label0 = M5Label('label0', x=137, y=88, color=0x000, font=FONT_MONT_14, parent=None)

nvs.write(str('q'), '1')
while True:
  label0.set_text(str(nvs.read_str('q')))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/eeprom/uiflow_block_eeprom_write_str.svg"> 

```python
nvs.write(str(''), '')
```

- 初始化 EEPROM,设置变量，并赋值
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/eeprom/uiflow_block_eeprom_read_str.svg"> 

```python
str(nvs.read_str('q'))
```
 
- 读取 EEPROM 的变量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/eeprom/uiflow_block_eeprom_read_int.svg"> 

```python
str(nvs.read_int('q'))
```

- 将 EEPREOM 的变量转化为整型输出

