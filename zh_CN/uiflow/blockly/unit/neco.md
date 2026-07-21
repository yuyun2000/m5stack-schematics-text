# [Unit Neco](/zh_CN/uiflow/blockly/unit/neco)

## 案例程序

设置 Unit Neco LED 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_neco_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
neco_0 = unit.get(unit.NECO, unit.PORTB, 70)

def neco_0_button_wasPressed_cb():
  # global params
  neco_0.setRamdomColor(6)
  pass
neco_0.button.wasPressed(neco_0_button_wasPressed_cb)

print((str('status:') + str((neco_0.button.wasPressed()))))
neco_0.setBrightness(20)
while True:
  neco_0.setColorFrom(1, 5, 0xff0000)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_button_callback.svg">

```python
def neco_0_button_wasPressed_cb():
  # global params
  pass
neco_0.button.wasPressed(neco_0_button_wasPressed_cb)
```

- 按钮回调函数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_button_state.svg">

```python
print((str('status:') + str((neco_0.button.wasPressed()))))
```

- 获取按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_brightness.svg">

```python
neco_0.setBrightness(20)
```

- 设置LED灯亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_color.svg">

```python
neco_0.setColor(1, 0xff0000)
```

- 设置LED灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_color_all.svg">

```python
neco_0.setColorAll(0xff0000)
```

- 设置LED灯全部颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_color_all_input.svg">

```python
neco_0.setColorAll(0xff0000)
```

- 设置LED灯全部颜色
  - Palette
  - RGB
  - HEX

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_color_from.svg">

```python
neco_0.setColorFrom(1, 5, 0xff0000)
```

- 设置部分LED灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_color_from_input.svg">

```python
neco_0.setColorFrom(1, 5, 0xff0000)
```

- 设置部分LED灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_color_input.svg">

```python
neco_0.setColorFrom(1, 5, 0xff0000)
```

- 自定义任意LED灯颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_one_random_color_all.svg">

```python
neco_0.setRandomColorAll()
```

- 指定所有LED灯位为一种随机颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_one_random_color_from.svg">

```python
neco_0.setRandomColorFrom(1, 5)
```

- 指定一定范围内LED颜色随机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_random_color.svg">

```python
neco_0.setRamdomColor(1)
```

- 指定一定范围内LED为一种随机颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_random_color_all.svg">

```python
neco_0.setRandomColorRandomLed()
```

- 指定所有LED颜色随机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/neco/uiflow_block_unit_neco_set_random_color_from.svg">

```python
neco_0.setRandomColorRandomLedFrom(1, 5)
```

- 指定一定范围内LED颜色随机

