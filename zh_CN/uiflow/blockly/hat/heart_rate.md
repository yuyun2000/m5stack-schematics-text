# [Hat Heart Rate](/zh_CN/hat/hat_heart_rate)

## 案例程序

获取心率和血氧的数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/heart_rate/uiflow_block_hat_heart_rate_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_heartrate_0 = hat.get(hat.HEART_RATE)

hat_heartrate_0.setMode(0x03)
while True:
  print(hat_heartrate_0.getHeartRate())
  print(hat_heartrate_0.getSpO2())
  wait(0.4)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/heart_rate/uiflow_block_hat_heartrate_get_heartrate.svg">

```python
hat_heartrate_0.getHeartRate()
```

- 获取心率数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/heart_rate/uiflow_block_hat_heartrate_get_ir.svg">

```python
hat_heartrate_0.getIr()
```

- 获取红外原始 ADC 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/heart_rate/uiflow_block_hat_heartrate_get_red.svg">

```python
hat_heartrate_0.getRed()
```

- 获取红光原始 ADC 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/heart_rate/uiflow_block_hat_heartrate_get_spo2.svg">

```python
hat_heartrate_0.getSpO2()
```

- 获取血氧饱和度(SpO2)数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/heart_rate/uiflow_block_hat_heartrate_set_led_current.svg">

```python
hat_heartrate_0.setLedCurrent(0x00, 0x00)
```

- 设置红光和红外 LED 的电流值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/heart_rate/uiflow_block_hat_heartrate_set_mode.svg">

```python
hat_heartrate_0.setMode(0x02)
```

- 设置心率或其他模式

