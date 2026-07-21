# [Hat Thermal](/zh_CN/hat/hat-thermal)

## 案例程序

获取传感器获取的物体中心位置温度和最高，最低温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/thermal/uiflow_block_hat_thermal_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_thermal_0 = hat.get(hat.MLX90640)

while True:
  print(hat_thermal_0.getCenterTmp())
  print(hat_thermal_0.getMaxTmp())
  print(hat_thermal_0.getMinTmp())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/thermal/uiflow_block_hat_thermal_get_center_temperature.svg">

```python
hat_thermal_0.getCenterTmp()
```

- 获取传感器视场中心点的温度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/thermal/uiflow_block_hat_thermal_get_max_temperature.svg">

```python
hat_thermal_0.getMaxTmp()
```

- 获取传感器检测到的最高温度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/thermal/uiflow_block_hat_thermal_get_min_temperature.svg">

```python
hat_thermal_0.getMinTmp()
```

- 获取传感器检测到的最低温度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/thermal/uiflow_block_hat_thermal_get_temperature.svg">

```python
hat_thermal_0.getTmp(0, 0)
```

- 获取指定像素位置的温度值（示例中为0,0坐标点）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/thermal/uiflow_block_hat_thermal_set_max_visible_temperature.svg">

```python
hat_thermal_0.setColorMaxTmp(35)
```

- 设置色温映射显示的最高温度值（例如设置为35°C）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/thermal/uiflow_block_hat_thermal_set_min_visible_temperature.svg">

```python
hat_thermal_0.setColorMinTmp(24)
```

- 设置色温映射显示的最低温度值（例如设置为24°C）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/thermal/uiflow_block_hat_thermal_update.svg">

```python
hat_thermal_0.update(x=0, y=0, show=True, showCenter=True)
```

- 更新传感器显示，可选设置是否显示中心点和坐标位置