# [Unit ENV/ENV-II/ENV-III/ENV-IV](/zh_CN/unit/env)

## 案例程序

> 获取 ENV 采集的温度，湿度，大气压强数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
env_0 = unit.get(unit.ENV, unit.PORTA)

while True:
  print(env_0.temperature)
  print(env_0.humidity)
  print(env_0.pressure)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env/uiflow_block_dht12_get_temperature.svg">

```python
print(env_0.temperature)
```

- 此方法允许读取 ENV 采集的温度值并返回一个浮点型数值。计量单位为 °C。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env/uiflow_block_dht12_get_humidity.svg">

```python
print(env_0.humidity)
```

- 此方法允许读取 ENV 采集的相对湿度值并返回一个浮点型数值。计量单位为%RH。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env/uiflow_block_dht12_pressure.svg">

```python
print(env_0.pressure)
```

- 此方法允许读取 ENV 采集的大气压并返回一个浮点型数值。计量单位为 Pa。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env/enviv/uiflow_block_unit_env4_get_mode.svg">

```python
env4_0.set_mode(0xFD)
```

- 设置设备运行模式。此功能函数只适用于 ENV IV

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env/enviv/uiflow_block_unit_env4_set_mode.svg">

```python
print(env4_0.get_mode)
```

- 获取当前设备运行模式。此功能函数只适用于 ENV IV
  - NOHEAT_HIGHPRECISION：不加热，保持高精度测量或控制
  - NOHEAT_MEDPRECISION：不加热，精度中等
  - NOHEAT_LOWPRECISION：不加热，精度最低
  - HIGHHEAT_1S：高加热模式，加热周期1秒
  - HIGHHEAT_100MS：高加热模式，加热周期100毫秒
  - MEDHEAT_1S：中加热模式，加热周期1秒
  - MEDHEAT_100MS：中加热模式，加热周期100毫秒
  - LOWHEAT_1S：低加热模式，加热周期1秒
  - LOWHEAT_100MS：低加热模式，加热周期100毫秒
