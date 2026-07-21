# [Hat ENV](/zh_CN/hat/hat-env)

## 案例程序

输出温湿度和大气压力数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/env/uiflow_block_hat_env_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat
import hat

setScreenColor(0x111111)

hat_env_0 = hat.get(hat.ENV)

while True:
  print(hat_env_0.pressure)
  print(hat_env_0.temperature)
  print(hat_env_0.humidity)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/env/uiflow_block_hat_env_get_humidity.svg">

```python
hat_env_0.humidity
```

- 用于获取环境湿度，返回值为浮点型百分比

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/env/uiflow_block_hat_env_get_temperature.svg">

```python
hat_env_0.temperature
```

- 用于获取环境温度，返回值为摄氏度的浮点型数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/env/uiflow_block_hat_env_pressure.svg">

```python
hat_env_0.pressure
```

- 用于获取环境气压，返回值为 hPa(百帕)单位的浮点型数据

