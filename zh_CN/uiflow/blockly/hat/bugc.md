# [Hat BugC](/zh_CN/hat/hat-bugc)

## 案例程序

前进后退不断交替，并且灯切换颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc/uiflow_block_hat_bugc_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_bugc_0 = hat.get(hat.BUGC)

while True:
  hat_bugc_0.SetAllRGB(0xff0000)
  hat_bugc_0.SetPulse(0, 255)
  hat_bugc_0.SetPulse(1, -255)
  hat_bugc_0.SetPulse(2, 255)
  hat_bugc_0.SetPulse(3, -255)
  wait(5)
  hat_bugc_0.SetAllRGB(0x00ff00)
  hat_bugc_0.SetAllPulse(-255, 255, -255, 255)
  wait(5)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc/uiflow_block_hat_bugc_rgb_set_all.svg">

```python
hat.get(hat.BUGC)
```

- 设置 RGB 灯条的颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc/uiflow_block_hat_bugc_rgb_set_all2.svg">

```python
hat_bugc_0.SetRGB(0, 0xff0000)
```

- 分别通过 RGB 数值来设置 RGB 灯条的颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc/uiflow_block_hat_bugc_rgb_set_all_rgb.svg">

```python
hat_bugc_0.SetRGB(0, 0x000000)
```

- 通过指定 R(红色)、G(绿色)和 B(蓝色)值来设置 RGB 灯条的颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc/uiflow_block_hat_bugc_set_all_pulse.svg">

```python
hat_bugc_0.SetAllRGB(0x000000)
```

- 设置所有通道的脉冲宽度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc/uiflow_block_hat_bugc_set_pulse.svg">

```python
hat_bugc_0.SetAllPulse(0, 0, 0, 0)
```

- 设置特定通道的脉冲宽度

