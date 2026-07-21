# [Hat Joystick](/zh_CN/hat/hat-joystick)

## 案例程序

串口实时打印电位器的 X,Y 轴和按键值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joystick/uiflow_block_hat_joystick_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_Joystick_0 = hat.get(hat.JOYSTICK)

while True:
  print(hat_Joystick_0.X)
  print(hat_Joystick_0.Y)
  print(hat_Joystick_0.Press)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joystick/uiflow_block_hat_joystick_press.svg">

```python
hat_Joystick_0.Press
```

- 检查操纵杆是否被按下

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joystick/uiflow_block_hat_joystick_reversal_x.svg">

```python
hat_Joystick_0.InvertX
```

- 获取操纵杆 X 轴的反转值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joystick/uiflow_block_hat_joystick_reversal_y.svg">

```python
hat_Joystick_0.InvertY
```

- 获取操纵杆 Y 轴的反转值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joystick/uiflow_block_hat_joystick_x.svg">

```python
hat_Joystick_0.X
```

- 获取操纵杆的 X 轴位置值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joystick/uiflow_block_hat_joystick_y.svg">

```python
hat_Joystick_0.Y
```

- 获取操纵杆的 Y 轴位置值

