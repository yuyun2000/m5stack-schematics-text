# [Hat Yun](/zh_CN/hat/hat-yun)

## 案例程序

设置灯的颜色为红色，并获取传感器的温湿度和大气压力数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/yun/uiflow_block_hat_yun_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_yun_0 = hat.get(hat.YUN)

hat_yun_0.SetRGBAll(0xff0000)
while True:
  print(hat_yun_0.temperature)
  print(hat_yun_0.humidity)
  print(hat_yun_0.pressure)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/yun/uiflow_block_get_hat_yun_brightness.svg">

```python
print((str('brightness:') + str((hat_yun_0.getLight()))))
```

- 获取亮度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/yun/uiflow_block_get_hat_yun_humidity.svg">

```python
print((str('humidity:') + str((hat_yun_0.humidity))))
```

- 获取湿度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/yun/uiflow_block_get_hat_yun_pressure.svg">

```python
print((str('pressure:') + str((hat_yun_0.pressure))))
```

- 获取气压数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/yun/uiflow_block_get_hat_yun_temperature.svg">

```python
print((str('temperature:') + str((hat_yun_0.temperature))))
```

- 获取温度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/yun/uiflow_block_yun_hat_set_color.svg">

```python
hat_yun_0.SetRGB(1, 0xff0000)
```

- 设置颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/yun/uiflow_block_yun_hat_set_color_all.svg">

```python
hat_yun_0.SetRGBAll(0xff0000)
```

- 所有LED灯设置颜色

