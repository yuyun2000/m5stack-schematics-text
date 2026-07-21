# POWER

## 案例程序

等待 5 秒后开机，灯带一秒后关机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_demo.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

screen.set_screen_brightness(30)
screen.set_screen_bg_color(0xff0000)
power.setPowerLED(True)
wait(1)
power.restart_after_seconds(2)
screen.set_screen_bg_color(0xff0000)
screen.set_screen_brightness(30)
power.setPowerLED(True)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_get_charge_state.svg">

```python
str(power.getChargeState())
```

- 返回充电状态，并以字符串的形式输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_get_bat_voltage.svg">

```python
str(power.getChargeState())
```

- 返回的电池电压值转换为字符串并输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_get_bat_voltage_percent.svg">

```python
str(power.getBatPercent())
```

- 返回的电池电量百分比转换为字符串并输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_get_bat_current.svg">

```python
str(power.getBatCurrent())
```

- 返回的电池电流值转换为字符串并输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_get_bat_current.svg">

```python
str(power.getBatCurrent())
```

- 返回的电池输出电流值转换为字符串并输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_get_vbus_voltage.svg">

```python
str(power.getVBusVoltage())
```

- 返回的 VBus 电压值转换为字符串并输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_get_temperature.svg">

```python
str(power.getPmuInTemp())
```

- 返回的 PMU 内部温度值转换为字符串并输出。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_power_off.svg">

```python
power.powerOff()
```

- 关机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_set_charge_current.svg">

```python
power.setChargeCurrent(power.CURRENT_100MA)
```

- 设置充电电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_set_screen_brightness.svg">

```python
screen.set_screen_brightness(30)
```

- 设置屏幕亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_set_led.svg">

```python
power.setPowerLED(True)
```

- 设置电源指示灯的亮灭

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_set_bus_mode.svg">

```python
power.setBusPowerMode(1)
```

- 设置 M5-Bus 总线电源是否输出

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_set_restart.svg">

```python
power.restart_after_seconds(0)
```

- 设置多少秒之后重启

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/power/uiflow_block_power_restart_on.svg">

```python
power.restart_on(minutes=0, hours=0, date=1, weekday=0)
```

- 设置特定时间进行重启
