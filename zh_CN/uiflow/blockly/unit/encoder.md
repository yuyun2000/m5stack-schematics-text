# [Unit Encoder](/zh_CN/unit/encoder)

## 案例程序

旋转编码器计数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_encoder_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
encoder_0 = unit.get(unit.ENCODER_LED, unit.PORTA)

while True:
  if encoder_0.get_button_status():
    print((str('count:') + str((encoder_0.get_encoder_count()))))
  encoder_0.set_LED_RGB(3, 0xff0000)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_block_unit_encoder_btn_status.svg">

```python
print((str('button:') + str((encoder_0.get_button_status()))))
```

- 获取按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_block_unit_encoder_count.svg">

```python
print((str('count:') + str((encoder_0.get_encoder_count()))))
```

- 获取旋转编码器计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_block_unit_encoder_reset_count.svg">

```python
encoder_0.reset_count()
```

- 将编码器计数值归零

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_block_unit_encoder_set_color.svg">

```python
encoder_0.set_LED_RGB(3, 0xff0000)
```

- 配置编码器LED指示灯的颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_block_unit_encoder_set_color_input.svg">

```python
encoder_0.set_LED_RGB(3, 0xff0000)
```

- 设置指定 LED 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_block_unit_encoder_set_count.svg">

```python
encoder_0.set_encoder_count(1000)
```

- 初始化编码器计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_block_unit_encoder_set_mode.svg">

```python
encoder_0.set_encoder_mode(0)
```

- 切换编码器工作模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/encoder/uiflow_block_unit_encoder_set_rgb.svg">

```python
encoder_0.set_LED_RGB(3, 0x000000)
```

- 通过RGB分量值精确配置LED颜色

