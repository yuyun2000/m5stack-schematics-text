# [Unit NCIR2](/zh_CN/unit/NCIR2)

## 案例程序

> 测量红外检测的温度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
ncir2_0 = unit.get(unit.NCIR2, unit.PORTA)

ncir2_0.init_i2c_address(0x5A)
while True:
  print((str('temperature:') + str((ncir2_0.temperature_measure()))))
  print((str('emissivity:') + str((ncir2_0.emissivity_measure()))))
  print((str('threshold value:') + str((ncir2_0.temperature_threshold(0x20)))))
  print((str('buzzer frequency:') + str((ncir2_0.temp_buzzer_freq(0x40)))))
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_init.svg">

```python
ncir2_0.init_i2c_address(0x5A)
```

- 初始化 I2C 通讯地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_button_status.svg">

```python
print(ncir2_0.button_status())
```

- 获取按键状态 (按下或者放开)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_buzzer_control.svg">

```python
print(ncir2_0.buzzer_control())
```

- 获取蜂鸣器使能状态 (打开或者关闭)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_buzzer_duty.svg">

```python
print(ncir2_0.buzzer_duty())
```

- 获取蜂鸣器占空比 (占空比数值 0-255，数值越大，响度越大)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_buzzer_freq.svg">

```python
print(ncir2_0.buzzer_freq())
```

- 获取蜂鸣器频率值 (默认 4000)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_device_status.svg">

```python
print(ncir2_0.read_device_status(0xFE))
```

- 获取设备固件版本或 I2C 地址 (I2C 默认地址为 0x5A)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_device_temp.svg">

```python
print(ncir2_0.chip_temperature_measure())
```

- 获取设备温度值 (℃)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_emissivity.svg">

```python
print(ncir2_0.emissivity_measure())
```

- 获取物体表面的反射率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_rgb_led.svg">

```python
print(ncir2_0.rgb_led())
```

- 获取 RGB LED 颜色 (RGB 值为 0-255)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_temperature.svg">

```python
print(ncir2_0.temperature_measure())
```

- 获取温度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_temp_buzzer_duty.svg">

```python
print(ncir2_0.temp_buzzer_duty(0x44))
```

- 设定最高最低温度下蜂鸣器的占空比 (占空比数值为 0-255，占空比越大响度越大)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_temp_buzzer_freq.svg">

```python
print(ncir2_0.temp_buzzer_freq(0x40))
```

- 获取最高或最低温度时蜂鸣器频率 (默认为 4000，数值越高响度越尖锐)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_temp_buzzer_interval.svg">

```python
print(ncir2_0.temp_alarm_interval(0x42))
```

- 获取最高或最低温度时蜂鸣器高低电平间隔 (默认最低为 100，最高为 204)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_temp_led_color.svg">

```python
print(ncir2_0.temp_alarm_led(0x30))
```

- 获取最高或最低温度时 LED 的颜色 (RGB 值为 0-255)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_get_temp_threshold.svg">

```python
print(ncir2_0.temperature_threshold(0x20))
```

- 获取最高或最低温度阈值 (默认设置为最低 10°C，最高 37°C)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_save_setting.svg">

```python
ncir2_0.save_config_setting()
```

- 保存当前配置设定

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_buzzer_duty.svg">

```python
ncir2_0.buzzer_duty(80)
```

- 获取蜂鸣器占空比 (占空比数值 0-255，数值越大，响度越大)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_buzzer_freq.svg">

```python
ncir2_0.buzzer_freq(4000)
```

- 设定蜂鸣器的频率 (默认蜂鸣器频率为 4000，数值越大响度越大)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_control.svg">

```python
ncir2_0.buzzer_control(0x01)
```

- 设定蜂鸣器的使能状态 (打开或者关闭)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_emissivity.svg">

```python
ncir2_0.emissivity_measure(0.95)
```

- 设定反射率 (皮肤反射率为 0.95)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_i2c_address.svg">

```python
ncir2_0.write_i2c_address(0x5A)
```

- 设置设备的 I2C 地址 (默认为 0x5A)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_rgb_led.svg">

```python
ncir2_0.rgb_led(50, 50, 50)
```

- 设定 RGB LED 的颜色值 (RGB 值范围 0-255)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_temp_buzzer_duty.svg">

```python
ncir2_0.temp_buzzer_duty(0x44, 80)
```

- 设定最高最低温度下蜂鸣器的占空比 (占空比数值为 0-255，占空比越大响度越大)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_temp_buzzer_freq.svg">

```python
ncir2_0.temp_buzzer_freq(0x40, 4000)
```

- 设定最高或最低温度下蜂鸣器的间隔 (数值设置越高响得越快)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_temp_buzzer_interval.svg">

```python
ncir2_0.temp_alarm_interval(0x42, 100)
```

- 设定最高或最低温度下蜂鸣器的间隔 (数值设置越高响得越快)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_temp_led_color.svg">

```python
ncir2_0.temp_alarm_led(0x30, 50, 50, 50)
```

- 设定最高或最低温时蜂鸣器频率 (这里默认设置为 4000，频率越大，响声越尖锐)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir2/uiflow_block_unit_ncir2_set_temp_threshold.svg">

```python
ncir2_0.temperature_threshold(0x20, 25)
```

- 设定最高或最低温时 LED RGB 颜色值 (RGB 值在 0-255 之间)
