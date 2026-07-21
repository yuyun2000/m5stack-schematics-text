# [Unit Gesture](/zh_CN/unit/Gesture)

## 案例程序

> Unit Gesture 读取手势

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gesture/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
gesture_0 = unit.get(unit.GESTURE, unit.PORTA)

gesture_0.begin()
gesture_0.set_gesture_highrate(True)
while True:
  print(gesture_0.get_gesture())
  print(gesture_0.gesture_description((gesture_0.get_gesture())))
  if gesture_0.GestureUp:
    print('up')
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gesture/uiflow_block_gesture_begin.svg">

```python
gesture_0.begin()
```

- 初始化 Unit

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gesture/uiflow_block_gesture_get.svg">

```python
print(gesture_0.get_gesture())
```

- 获取手势

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gesture/uiflow_block_gesture_get_desc.svg">

```python
print(gesture_0.gesture_description((gesture_0.get_gesture())))
```

- 获取说明 (获取手势的值)，配合获取到的手势值使用

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gesture/uiflow_block_gesture_set_highrate.svg">

```python
gesture_0.set_gesture_highrate(True)
```

- 设置高速率 (真或假)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gesture/uiflow_block_gesture_status.svg">

```python
print(gesture_0.GestureNone)
```

- 手势值 返回所选手势的值。主要用于逻辑运算。
- 如果设置为 UP，Unit 检索到用户做出的手势为 up，返回 true
