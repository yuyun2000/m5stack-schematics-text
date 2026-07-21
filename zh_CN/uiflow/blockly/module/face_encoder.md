# [Faces Encoder](/zh_CN/module/encoder)

## Example

重置编码器的值，设置第一个 LED 为红色，并在循环中不断打印编码器的旋转方向、按键状态以及当前的编码值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_encoder/uiflow_block_face_encoder_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import face

setScreenColor(0x222222)

faces_encode = face.get(face.ENCODE)

faces_encode.clearValue()
faces_encode.setLed(0, 0xff0000)
while True:
  print((str('direction：') + str((faces_encode.getDir()))))
  print((str('press status：') + str((faces_encode.getPress()))))
  print((str('value：') + str((faces_encode.getValue()))))
  wait_ms(2)
```

## API

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_encoder/uiflow_block_faces_encode_clearValue.svg">

```python
faces_encode.clearValue()
```

- 将编码器的当前值清零。复位编码器的值为零

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_encoder/uiflow_block_faces_encode_getDir.svg">

```python
faces_encode.getDir()
```

- 获取编码器的旋转方向。返回的值表示当前编码器的旋转方向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_encoder/uiflow_block_faces_encode_getPress.svg">

```python
faces_encode.getPress()
```

- 检查编码器的按键是否被按下。返回一个布尔值(True/False)来表示按键的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_encoder/uiflow_block_faces_encode_getValue.svg">

```python
faces_encode.getValue()
```

- 获取编码器的当前编码值。返回的值是编码器的当前位置值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_encoder/uiflow_block_faces_encode_setLed.svg">

```python
faces_encode.setLed(0, 0xff0000)
```

- 设置特定位置的 LED 颜色。你可以选择 LED 的位置和颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_encoder/uiflow_block_faces_encode_setLed_input.svg">

```python
faces_encode.setLed(0, 0xff0000)
```

- 设置指定位置的 LED 颜色。你可以从调色板中选择颜色，并将其应用到指定的 LED 位置(例如位置0)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_encoder/uiflow_block_faces_encode_setLed_rgb.svg">

```python
faces_encode.setLed(0, 0x000000)
```

- 设置指定位置的 LED 颜色，通过手动输入红、绿、蓝(RGB)三个颜色值来决定 LED 的最终颜色。这允许你更加精确地控制 LED 的颜色输出

