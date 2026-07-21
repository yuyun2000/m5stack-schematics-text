# [Unit Thermal2](/zh_CN/unit/Thermal2)

## 案例程序

热成像温度采集

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_tjermal2_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x000000)
thermal2_0 = unit.get(unit.THERMAL2, unit.PORTA)

rgb = None
freq = None
high_temp_thres = None
update = None
low_temp = None
high_temp = None

title0 = M5Title(title="UNIT THERMAL-2", x=105, fgcolor=0xffffff, bgcolor=0x990000)
label0 = M5TextBox(12, 35, "DEVICE ID:", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label1 = M5TextBox(159, 35, "label1", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label2 = M5TextBox(12, 60, "MEDIAN TEMP:", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label3 = M5TextBox(168, 60, "label3", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label4 = M5TextBox(12, 84, "AVERAGE TEMP:", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label5 = M5TextBox(12, 109, "LOW TEMP:", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label6 = M5TextBox(12, 136, "HIGH TEMP:", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label8 = M5TextBox(178, 84, "label8", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label9 = M5TextBox(144, 109, "label9", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label10 = M5TextBox(144, 136, "label10", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
rectangle0 = M5Rect(278, 60, 10, 20, 0xff0000, 0xff0000)
rectangle1 = M5Rect(250, 60, 10, 20, 0x0000ff, 0x0000ff)
rectangle2 = M5Rect(306, 60, 10, 20, 0x00ff00, 0x00ff00)
label7 = M5TextBox(250, 35, "L  H  D", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label11 = M5TextBox(50, 224, "A-ON", lcd.FONT_Default, 0xff9200, rotate=0)
label12 = M5TextBox(137, 224, "A-OFF", lcd.FONT_Default, 0xff9200, rotate=0)
label13 = M5TextBox(11, 163, "HIGH TEMP THRES:", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label14 = M5TextBox(218, 163, "label14", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label15 = M5TextBox(12, 190, "HIGH TEMP FREQ:", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label16 = M5TextBox(213, 190, "label16", lcd.FONT_DejaVu18, 0xff9200, rotate=0)
label17 = M5TextBox(232, 224, "RGB", lcd.FONT_Default, 0xff9200, rotate=0)

from numbers import Number

# Describe this function...
def button_status():
  global rgb, freq, high_temp_thres, update, low_temp, high_temp
  if thermal2_0.button_status(0x08):
    freq = (freq if isinstance(freq, Number) else 0) + 50
    if freq > 4000:
      freq = 1500
    label16.setText(str(freq))
  elif thermal2_0.button_status(0x10):
    thermal2_0.alarm_buzzer_freq(0x32, freq)

def buttonC_wasPressed():
  global rgb, freq, high_temp_thres, update, low_temp, high_temp
  rgb = (rgb if isinstance(rgb, Number) else 0) + 1
  if rgb == 1:
    thermal2_0.rgb_led(50, 0, 0)
  elif rgb == 2:
    thermal2_0.rgb_led(0, 50, 0)
  elif rgb == 3:
    thermal2_0.rgb_led(0, 0, 50)
    rgb = 0
  pass
btnC.wasPressed(buttonC_wasPressed)

def buttonA_wasPressed():
  global rgb, freq, high_temp_thres, update, low_temp, high_temp
  thermal2_0.temp_alarm_ctrl(0x80, True)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global rgb, freq, high_temp_thres, update, low_temp, high_temp
  thermal2_0.temp_alarm_ctrl(0x80, False)
  pass
btnB.wasPressed(buttonB_wasPressed)

label0.setText('DEVICE ID:')
label1.setText(str(thermal2_0.device_info(0x00)))
wait(1.5)
label0.setText('DEVICE VER:')
label1.setText(str(thermal2_0.device_info(0x02)))
wait(1.5)
label0.setText('DEVICE I2C:')
label1.setText(str(thermal2_0.i2c_addr(0x00)))
high_temp_thres = 33
label14.setText(str(high_temp_thres))
thermal2_0.func_ctrl(0x02, True)
thermal2_0.temp_threshold(0x30, high_temp_thres)
thermal2_0.temp_alarm_led(0x35, 200, 0, 0)
freq = 1500
rgb = 0
while True:
  update = thermal2_0.data_refresh_ctrl()
  label3.setText(str(thermal2_0.temp_measure(0x00, False)))
  label8.setText(str(thermal2_0.temp_measure(0x02, False)))
  low_temp = thermal2_0.temp_measure(0x08, False)
  label9.setText(str(low_temp))
  high_temp = thermal2_0.temp_measure(0x0c, False)
  label10.setText(str(high_temp))
  rectangle1.setSize(height=(2 * int(low_temp)))
  rectangle0.setSize(height=(2 * int(high_temp)))
  rectangle2.setSize(height=(5 * (int(high_temp) - int(low_temp))))
  button_status()
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_alarm_buzzer_freq.svg">

```python
 print((str('frequency:') + str((thermal2_0.alarm_buzzer_freq(0x22)))))
```

- 获取报警蜂鸣器频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_alarm_buzzer_interval.svg">

```python
print((str('buzzer interval:') + str((thermal2_0.temp_alarm_interval(0x24)))))
```

- 获取报警蜂鸣器间隔

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_button_status.svg">

```python
print((str('status:') + str((thermal2_0.button_status(0x01)))))
```

- 获取按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_buzzer_duty.svg">

```python
print(thermal2_0.buzzer_duty())
```

- 获取蜂鸣器占空比

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_buzzer_freq.svg">

```python
print(thermal2_0.buzzer_freq())
```

- 获取蜂鸣器频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_data_refresh_ctrl.svg">

```python
print(thermal2_0.data_refresh_ctrl())
```

- 获取数据刷新控制状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_device_info.svg">

```python
print((str('device info:') + str((thermal2_0.device_info(0x00)))))
```

- 获取设备信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_func_ctrl.svg">

```python
print((str('control:') + str((thermal2_0.func_ctrl()))))
```

- 获取功能控制状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_i2c_address.svg">

```python
print((str('i2c address:') + str((thermal2_0.i2c_addr(0x00)))))
```

- 获取I2C地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_noise_filter.svg">

```python
print(thermal2_0.noise_filter())
```

- 获取噪声滤波器状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_refresh_rate.svg">

```python
print(thermal2_0.refresh_rate())
```

- 获取刷新率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_subpage_info.svg">

```python
print(thermal2_0.subpage_info())
```

- 获取子页面信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_temp_alarm_led.svg">

```python
print((str('color:') + str((thermal2_0.temp_alarm_led(0x25)))))
```

- 获取温度报警LED状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_temp_alarm_status.svg">

```python
print((str('alarm status:') + str((thermal2_0.temp_alarm_status()))))
```

- 获取温度报警状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_temp_data_buffer.svg">

```python
print((str('buffer:') + str((thermal2_0.temp_data_buffer()))))
```

- 获取温度数据缓冲区

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_temp_differential.svg">

```python
print((str('position:') + str((thermal2_0.temp_differential(0x00, 0)))))
```

- 获取温差值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_temp_measure.svg">

```python
print((str('value:') + str((thermal2_0.temp_measure(0x00, True)))))
```

- 获取温度测量值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_temp_monitor.svg">

```python
print((str('size:') + str((thermal2_0.get_temp_monitor(1)))))
```

- 获取温度监控状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_get_temp_threshold.svg">

```python
print((str('temperature threshold:') + str((thermal2_0.temp_threshold(0x20)))))
```

- 获取温度阈值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_buzzer_duty.svg">

```python
thermal2_0.buzzer_duty(50)
```

- 设置蜂鸣器占空比

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_buzzer_freq.svg">

```python
thermal2_0.buzzer_freq(2000)
```

- 设置蜂鸣器频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_func_ctrl.svg">

```python
thermal2_0.func_ctrl(0x01, True)
```

- 设置功能控制

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_led_color.svg">

```python
thermal2_0.rgb_led(50, 50, 50)
```

- 设置LED颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_noise_filter.svg">

```python
thermal2_0.noise_filter(0)
```

- 设置噪声滤波器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_refresh_rate.svg">

```python
thermal2_0.refresh_rate(0)
```

- 设置刷新率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_temp_alarm_ctrl.svg">

```python
thermal2_0.temp_alarm_ctrl(0x80, True)
```

- 设置温度报警控制

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_temp_alarm_interval.svg">

```python
thermal2_0.temp_alarm_interval(0x24, 5)
```

- 设置温度报警间隔

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_temp_alarm_led.svg">

```python
thermal2_0.temp_alarm_led(0x25, 50, 50, 50)
```

- 设置温度报警LED

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_temp_freq.svg">

```python
thermal2_0.alarm_buzzer_freq(0x22, 1000)
```

- 设置温度采样频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_temp_monitor.svg">

```python
thermal2_0.temp_monitor(15, 11)
```

- 设置温度监控

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal2/uiflow_block_unit_thermal2_set_temp_threshold.svg">

```python
thermal2_0.temp_threshold(0x20, 25)
```

- 设置温度阈值

