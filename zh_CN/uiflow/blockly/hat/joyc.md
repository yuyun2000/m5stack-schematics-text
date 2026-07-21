# [Hat Joyc](/zh_CN/hat/hat-joyc)

## 案例程序

设置灯的颜色为红色，串口实时打印电位器的 X,Y 的数值和旋转的角度和按键的状态值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joyc/uiflow_block_hat_joyc_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_joyc_0 = hat.get(hat.JOYC)

hat_joyc_0.SetLedColor(0xff0000)
while True:
  print(hat_joyc_0.GetX(0))
  print(hat_joyc_0.GetY(0))
  print(hat_joyc_0.GetAngle(0))
  print(hat_joyc_0.GetPress(0))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joyc/uiflow_block_hat_joyc_get_angle.svg">

```python
hat_joyc_0.GetAngle(0)
```

- 获取操纵杆的角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joyc/uiflow_block_hat_joyc_get_distance.svg">

```python
hat_joyc_0.GetDistance(0)
```

- 获取操纵杆的距离值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joyc/uiflow_block_hat_joyc_get_press.svg">

```python
hat_joyc_0.GetPress(0)
```

- 获取操纵杆的按压状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joyc/uiflow_block_hat_joyc_get_x.svg">

```python
hat_joyc_0.GetX(0)
```

- 获取操纵杆在 X 轴上的数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joyc/uiflow_block_hat_joyc_get_y.svg">

```python
hat_joyc_0.GetY(0)
```

- 获取操纵杆在 Y 轴上的数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joyc/uiflow_block_hat_joyc_set_led_color.svg">

```python
hat_joyc_0.SetLedColor(0x0)
```

- 设置 LED 灯的颜色(红、绿、蓝三色)

