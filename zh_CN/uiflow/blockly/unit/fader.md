# [Unit Fader](/zh_CN/unit/fader)

## 案例程序

读取滑动电位器活动位置 12 位的原始数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_fader_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
fader_0 = unit.get(unit.FADER, unit.PORTB)

fader_0.setColor(1, 0xff0000)
while True:
  print((str('darw:') + str((fader_0.readraw12()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_multi_set_color.svg">

```python
fader_0.setColor(1, 0xff0000)
```

- 设置指定灯珠索引颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_multi_set_color_all.svg">

```python
fader_0.setColorAll(0xff0000)
```

- 设置所有灯珠颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_multi_set_color_all_input.svg">

```python
fader_0.setColorAll(0xff0000)
```

- 设置所有灯珠颜色
  - Palette
  - RGB
  - Hex 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_multi_set_color_from.svg">

```python
fader_0.setColorFrom(1, 5, 0xff0000)
```

- 设置部分灯珠颜色（from to）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_multi_set_color_from_input.svg">

```python
fader_0.setColorFrom(1, 5, 0x000000)
```

- 设置部分灯珠颜色（from to）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_multi_set_color_from_rgb.svg">

```python
fader_0.setColorFrom(1, 5, 0x000000)
```

- 设置指定灯珠索引颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_multi_set_color_input.svg">

```python
fader_0.setColor(1, 0xff0000)
```

- 设置指定灯珠索引颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_readraw12.svg">

```python
print((str('rew(12) data:') + str((fader_0.readraw12()))))
```

- 传感器中读取 12 位的原始数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_readraw16.svg">

```python
print((str('rew(16) data:') + str((fader_0.readraw16()))))
```

- 传感器中读取 16 位的原始数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_set_brightness.svg">

```python
fader_0.setBrightness(0)
```

- 设置所有灯珠亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_set_bright_pot.svg">

```python
fader_0.setBrightPOT()
```

- 设置调节亮度电位器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fader/uiflow_block_fader_set_color_pot.svg">

```python
fader_0.setColorPOT(1)
```

- 设置调节亮度电位器可调节 led 数量

