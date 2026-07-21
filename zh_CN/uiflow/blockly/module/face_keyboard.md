# [Faces Keyboard](/zh_CN/module/faces_keyboard)

## 案例程序

读取并打印按键值和输入字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_keyboard/uiflow_block_faces_keyboard_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import face

setScreenColor(0x222222)

faces_keyboard = face.get(face.KEYBOARD)

def buttonA_wasPressed():
  # global params
  faces_keyboard.clearStr()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  faces_keyboard.deleteStrLast()
  pass
btnB.wasPressed(buttonB_wasPressed)


while True:
  if faces_keyboard.isNewKeyPress():
    print((str('Button value:') + str((faces_keyboard.readKey()))))
    print((str('Input string:') + str((faces_keyboard.readStr()))))
  wait_ms(2)
```

## 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_keyboard/uiflow_block_faces_keyboard_isNewKeyPress.svg">

```python
faces_keyboard.isNewKeyPress()
```

- 检测是否有新的按键按下：
  - True:新的按键按下
  - False:无新的按键按下

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_keyboard/uiflow_block_faces_keyboard_readKey.svg">

```python
faces_keyboard.readKey()
```

- 读取输入按键 key 值


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_keyboard/uiflow_block_faces_keyboard_readStr.svg">

```python
faces_keyboard.readStr()
```

- 读取输入字符串。将会积累连续输入的内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_keyboard/uiflow_block_faces_keyboard_deleteStrLast.svg">

```python
faces_keyboard.deleteStrLast()
```

- 删除输入的最后一个字符


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_keyboard/uiflow_block_faces_keyboard_clearStr.svg">

```python
faces_keyboard.clearStr()
```

- 清空输入的字符


