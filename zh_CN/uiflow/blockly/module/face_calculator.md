# [Faces Calculator](/zh_CN/module/faces_calculator)

## 案例程序

读取并打印按键状态和输入字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_calculator/uiflow_block_faces_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import face

setScreenColor(0x222222)
faces_calc = face.get(face.CALC)

def buttonA_wasPressed():
  # global params
  faces_calc.clearStr()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  faces_calc.deleteStrLast()
  pass
btnB.wasPressed(buttonB_wasPressed)


while True:
  if faces_calc.isNewKeyPress():
    print((str('Button Value:') + str((faces_calc.readKey()))))
    print((str('Input string:') + str((faces_calc.readStr()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_calculator/uiflow_block_faces_isNewKeyPress.svg">

```python
faces_calc.isNewKeyPress()
```

- 检测是否有新的按键按下：
  - True:新的按键按下
  - False:无新的按键按下

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_calculator/uiflow_block_faces_readKey.svg">

```python
faces_calc.readKey()
```

- 读取输入按键 key 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_calculator/uiflow_block_faces_readStr.svg">

```python
faces_calc.readStr()
```

- 读取输入字符串。将会积累连续输入的内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_calculator/uiflow_block_faces_deleteStrLast.svg">

```python
faces_calc.deleteStrLast()
```

- 删除输入的最后一个字符


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_calculator/uiflow_block_faces_clearStr.svg">

```python
faces_calc.clearStr()
```

- 清空输入的字符


