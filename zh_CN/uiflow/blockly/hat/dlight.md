# [Hat DLight](/zh_CN/hat/hat_dlight)

## 案例程序

串口输出光照值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dlight/uiflow_block_hat_dlight_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_dlight_0 = hat.get(hat.DLIGHT)

hat_dlight_0.set_mode(0x10)
while True:
  print(hat_dlight_0.get_lux())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dlight/uiflow_block_hat_dlight_get_lux.svg">

```python
hat_dlight_0.get_lux()
```

- 读取光照强度的数值(lux)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dlight/uiflow_block_hat_dlight_set_continous_mode.svg">

```python
hat_dlight_0.set_mode(0x10)
```

- 设置为连续模式，当前选择为 H-Res1，用于连续读取光照强度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dlight/uiflow_block_hat_dlight_set_one_shot_mode.svg">

```python
hat_dlight_0.set_mode(0x20)
```

- 设置为单次模式，当前选择为 H-Res1，用于单次读取光照强度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dlight/uiflow_block_hat_dlight_set_state_mode.svg">

```python
hat_dlight_0.set_mode(0x00)
```

- 控制模块状态，当前选择为 Power Down，用于关闭设备或进入低功耗模式

