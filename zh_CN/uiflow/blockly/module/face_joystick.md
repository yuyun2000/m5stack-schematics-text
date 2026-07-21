# [Faces Joystick](/zh_CN/module/joystick)

## 案例程序

实时监控操纵杆的反向 X、Y 值和当前 X、Y 值，同时检测按键的按下状态，并设置 LED 灯的颜色为红色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_joystick/uiflow_block_face_joystick_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import face

setScreenColor(0x222222)

faces_joystick = face.get(face.JOYSTICK)

while True:
  print((str('reverse X value：') + str((faces_joystick.InvertX))))
  print((str('reverse Y value：') + str((faces_joystick.InvertY))))
  print((str('Status：') + str((faces_joystick.Press))))
  faces_joystick.setLed(0, 0xff0000)
  print((str('X value：') + str((faces_joystick.X))))
  print((str('Y value:') + str((faces_joystick.Y))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_joystick/uiflow_block_faces_joystick_invert_x.svg">

```python
faces_joystick.InvertX
```

- 获取 X 轴的反向值。这个函数返回 X 轴的反向数值，通常用于获取操纵杆或传感器的反向输出

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_joystick/uiflow_block_faces_joystick_invert_y.svg">

```python
faces_joystick.InvertY
```

- 获取 Y 轴的反向值。类似于 X 轴的反向值，这个函数返回 Y 轴的反向数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_joystick/uiflow_block_faces_joystick_press.svg">

```python
faces_joystick.Press
```

- 检测按压状态。这个块返回一个布尔值，用于判断按钮是否被按下

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_joystick/uiflow_block_faces_joystick_setLed.svg">

```python
faces_joystick.setLed(0, 0xff0000)
```

- 设置 LED 的颜色。这个块允许你设置特定位置 LED 的颜色，有两种选择：使用 RGB 颜色(红、绿、蓝)值或直接从调色板中选择颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_joystick/uiflow_block_faces_joystick_setLed_input.svg">

```python
faces_joystick.setLed(0, 0xff0000)
```

- 设置指定位置 LED 的颜色。这一语句使用调色板中的颜色选择

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_joystick/uiflow_block_faces_joystick_x.svg">

```python
faces_joystick.X
```

- 获取 X 轴的值。返回操纵杆或传感器在 X 轴上的当前输出

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_joystick/uiflow_block_faces_joystick_y.svg">

```python
faces_joystick.Y
```

- 获取 Y 轴的值。返回操纵杆或传感器在 Y 轴上的当前输出
