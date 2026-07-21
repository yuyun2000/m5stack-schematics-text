# [Unit Puzzle](/zh_CN/unit/Unit-Puzzle)

## 案例程序

> 设置 puzzle_0 的亮度为 20，并持续显示设置矩阵颜色图案。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/uiflow_block_unit_puzzle_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

puzzle_0 = unit.get(unit.PUZZLE, unit.PORTA, 64)
puzzle_0.setBrightness(20)
while True:
  puzzle_0.setColor(20, 0xff0000)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/1_uiflow_block_unit_puzzle_set_color.svg">

```python
puzzle_0.setColor(1, 0xff0000)
```

- 设置某个特定灯(编号 1 至 64)的 RGB 颜色，颜色可以从调色板(Palette)中选择。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/2_uiflow_block_unit_puzzle_set_color_from.svg">

```python
puzzle_0.setColorFrom(1, 5, 0xff0000)
```

- 设置一组灯(从编号 1 到 5)的 RGB 颜色，颜色同样可以从调色板中选择。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/3_uiflow_block_unit_puzzle_set_color_all.svg">

```python
puzzle_0.setColorAll(0xff0000)
```

- 设置所有灯的 RGB 颜色。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/4_uiflow_block_unit_puzzle_set_brightness.svg">

```python
puzzle_0.setBrightness(20)
```

- 设置灯的整体亮度，范围是 0 至 100。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/5_uiflow_block_unit_puzzle_set_show_lock.svg">

```python
puzzle_0.setShowLock(True)
```

- 设置是否显示锁定状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/6_uiflow_block_unit_puzzle_show.svg">

```python
puzzle_0.show()
```

- 使当前设置的 RGB LED 显示。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/7_uiflow_block_unit_puzzle_set_hexagon_matrix.svg">

```python
puzzle_0.setColor(20, 0xff0000)
```

- 可通过 RGB 颜色选择器分别设置红、绿、蓝的值，进而控制灯阵的颜色，序号代表 RGB 位置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/puzzle/8_uiflow_block_unit_puzzle_set_hexagon_matrix_rgb.svg">

```python
puzzle_0.setColor(20, 0xff0000)
```

- 可通过 RGB 数值分别设置红、绿、蓝的值，进而控制灯阵的颜色。