# [PM2.5](/zh_CN/base/pm2.5)

## 案例程序

#> 获取 pm2.5各个颗粒的数值以及 sht20获取的温湿度值


## SHT20

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_sht20_Demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

pm25_sht20 = module.get(module.PM25)

while True:
  print((str('SPM PM1.0:') + str((pm25_sht20.get_pm1_0_factory()))))
  print((str('SPM PM2.5:') + str((pm25_sht20.get_pm2_5_factory()))))
  print((str('SPM PM10:') + str((pm25_sht20.get_pm10_factory()))))
  print((str('ATE PM1.0:') + str((pm25_sht20.get_pm1_0_air()))))
  print((str('ATE PM1.0:') + str((pm25_sht20.get_pm2_5_air()))))
  print((str('ATE PM1.0:') + str((pm25_sht20.get_pm10_air()))))
  print((str('>3.0um Particles:') + str((pm25_sht20.get_num_above_0_3()))))
  print((str('TEM:') + str((pm25_sht20.get_sht20_temperature))))
  print((str('HUM:') + str((pm25_sht20.get_sht20_humidity))))
  wait_ms(2)
```


## SHT30

#> 获取 pm2.5各个颗粒的数值以及 sht30获取的温湿度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_sht30_Demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

pm25_sht30 = module.get(module.PM25_SHT30)

while True:
  print((str('SPM PM1.0:') + str((pm25_sht30.get_pm1_0_factory()))))
  print((str('SPM PM2.5:') + str((pm25_sht30.get_pm2_5_factory()))))
  print((str('SPM PM10:') + str((pm25_sht30.get_pm10_factory()))))
  print((str('ATE PM1.0:') + str((pm25_sht30.get_pm1_0_air()))))
  print((str('ATE PM1.0:') + str((pm25_sht30.get_pm2_5_air()))))
  print((str('ATE PM1.0:') + str((pm25_sht30.get_pm10_air()))))
  print((str('>3.0um Particles:') + str((pm25_sht30.get_num_above_0_3()))))
  print((str('TEM:') + str((pm25_sht30.get_sht30_temperature))))
  print((str('HUM:') + str((pm25_sht30.get_sht30_humidity))))
  wait_ms(2)
```


## 功能说明

### SHT20

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_get_num_above.svg">

```python
pm25_sht20.get_num_above_0_3()
```

- 获取空气中直径大于0.3(2.5/10)微米的颗粒物数量，单位是0.1升空气中的颗粒数，返回一个整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_get_pm_factory.svg">

```python
pm25_sht20.get_pm1_0_factory()
```

- 获取 PM2.5 传感器(SHT20)的 PM1.0(PM2.5,PM10) 浓度值
    - PM: 代表微粒物质的浓度，通常以微克每立方米(µg/m³)为单位。
    - ATE: 这个选项通常代表空气质量指数(AQI)或其他特定的测量标准，不过具体含义可能依赖于设备或应用的定义。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_pm25_sht20_get_humidity.svg">

```python
pm25_sht20.get_sht20_humidity
```

- 获取相对湿度值，单位是百分比相对湿度(%RH)，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_pm25_sht20_get_temperature.svg">

```python
pm25_sht20.get_sht20_temperature
```

- 获取温度值，单位是摄氏度(°C)，返回一个浮点数


### SHT30

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_pm25_sht30_get_humidity.svg">

```python
pm25_sht30.get_sht30_humidity
```

- 获取相对湿度值，单位是百分比相对湿度(%RH)，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_pm25_sht30_get_num_above.svg">

```python
pm25_sht30.get_num_above_0_3()
```

- 获取空气中直径大于0.3(2.5/10)微米的颗粒物数量，单位是0.1升空气中的颗粒数，返回一个整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_pm25_sht30_get_pm_factory.svg">

```python
pm25_sht30.get_pm1_0_factory()
```

- 获取 PM2.5 传感器(SHT30)的 PM1.0(PM2.5,PM10) 浓度值
    - PM: 代表微粒物质的浓度，通常以微克每立方米(µg/m³)为单位。
    - ATE: 这个选项通常代表空气质量指数(AQI)或其他特定的测量标准，不过具体含义可能依赖于设备或应用的定义。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pm2.5/uiflow_block_pm25_sht30_get_temperature.svg">

```python
pm25_sht30.get_sht30_temperature()
```

- 获取温度值，单位是摄氏度(°C)，返回一个浮点数

