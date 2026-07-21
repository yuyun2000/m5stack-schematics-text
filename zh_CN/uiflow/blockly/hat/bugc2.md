# [Hat BugC2](/zh_CN/app/BUGC2)

## 案例程序

向前和向后交替运动

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_bugc2_0 = hat.get(hat.BUGC2)

hat_bugc2_0.InitDeviceAddr(0x38)
while True:
  hat_bugc2_0.SetMotorSpeed(0x00, 100)
  hat_bugc2_0.SetMotorSpeed(0x02, 100)
  hat_bugc2_0.SetMotorSpeed(0x01, -100)
  hat_bugc2_0.SetMotorSpeed(0x01, -100)
  wait(5)
  hat_bugc2_0.SetMotorSpeed(0x00, -100)
  hat_bugc2_0.SetMotorSpeed(0x02, -100)
  hat_bugc2_0.SetMotorSpeed(0x01, 100)
  hat_bugc2_0.SetMotorSpeed(0x03, 100)
  wait(5)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_init.svg">

```python
hat_bugc2_0.InitDeviceAddr(0x38)
```

- 初始化设备的 I2C 地址，设置为 0x38

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_get_adc_raw_value.svg">

```python
hat_bugc2_0.GetAdcValue(8)
```

- 获取 8位 ADC 原始值(返回整数)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_get_bat_voltage.svg">

```python
hat_bugc2_0.GetBatVoltage
```

- 获取电池电压(单位为毫伏，返回整数)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_get_device_spec.svg">

```python
hat_bugc2_0.GetDeviceSpec(0xFE)
```

- 获取设备固件版本的详细信息(返回整数)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_rx_cb.svg">

```python
hat_bugc2_0.SetRxCb(hat_bugc2_0_rx_cb)
```

- 红外 NEC 接收回调函数，用于处理接收到的数据和地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_set_i2c_address.svg">

```python
hat_bugc2_0.SetI2cAddress(0x38)
```

- 设置前左电机的速度，当前速度值为 50，范围是 -100 到 100

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_set_motor_speed.svg">

```python
hat_bugc2_0.SetMotorSpeed(0x00, 50)
```

- 设置前左电机的速度，当前速度设置为 50，速度范围是 -100 到 100

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/bugc2/uiflow_block_hat_bugc2_set_rgb_color.svg">

```python
hat_bugc2_0.SetRGBColor(0x00, 0xff0000)
```

- 设置轮子 RGB 颜色，当前颜色设置为红色

