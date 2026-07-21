# [Unit TimerPWR](/zh_CN/unit/Unit-TimerPWR)

## 案例程序

> 通过 TimerPWR 模块获取电池、USB 和 Grove 端口的状态信息，设置模块的各种功能(如按钮、Grove 输出、OLED 背光等)，并处理与设备睡眠和唤醒相关的事件。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/uiflow_block_unit_timerpwr_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

timerpwr_1 = unit.get(unit.TIMERPWR, unit.PORTA)

timerpwr_1.init_i2c_address(0x56)

timerpwr_1.set_oled_backlight_status(True)
timerpwr_1.set_wakeup_trigger(timerpwr_1.TRIG_ALL)
while True:
  timerpwr_1.sleep_cycle(0, 0, 5, 0, 0, 5)
  print(timerpwr_1.get_battery_voltage())
  print(timerpwr_1.get_battery_current())
  print(timerpwr_1.get_usb_voltage())
  print(timerpwr_1.get_usb_current())
  print(timerpwr_1.get_grove_voltage())
  print(timerpwr_1.get_grove_current())
  print(timerpwr_1.get_firmware_version())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/1_uiflow_block_unit_timerpwr_init.svg">

```python
timerpwr_1.init_i2c_address(0x56)
```

- 初始化 TimerPWR 模块的 I2C 地址为 0x56。该地址用于通过 I2C 总线与模块通信。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/2_uiflow_block_unit_timerpwr_get_battery_voltage.svg">

```python
timerpwr_1.get_battery_voltage()
```

- 获取当前电池的电压值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/3_uiflow_block_unit_timerpwr_get_battery_current.svg">

```python
timerpwr_1.get_battery_current()
```

- 获取当前电池的电流值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/4_uiflow_block_unit_timerpwr_get_usb_voltage.svg">

```python
timerpwr_1.get_usb_voltage()
```

- 获取当前 USB 端口的电压。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/5_uiflow_block_unit_timerpwr_get_usb_current.svg">

```python
timerpwr_1.get_usb_current()
```

- 获取当前 USB 端口的电流。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/6_uiflow_block_unit_timerpwr_get_grove_voltage.svg">

```python
timerpwr_1.get_grove_voltage()
```

- 获取与 Grove 端口连接的外设的电压。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/7_uiflow_block_unit_timerpwr_get_grove_current.svg">

```python
timerpwr_1.get_grove_current()
```

- 获取 Grove 接口的电流信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/8_uiflow_block_unit_timerpwr_get_button_status.svg">

```python
timerpwr_1.get_button_status(0)
```

- 0 是按钮的编号，返回值为按钮是否被按下的状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/9_uiflow_block_unit_timerpwr_get_grove_output_status.svg">

```python
timerpwr_1.get_grove_output_status()
```

- 获返回当前 Grove 输出端口的启用或禁用状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/10_uiflow_block_unit_timerpwr_get_oled_backlight_status.svg">

```python
timerpwr_1.get_oled_backlight_status()
```

- 返回当前 OLED 显示屏背光是否打开。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/11_uiflow_block_unit_timerpwr_get_firmware_version.svg">

```python
timerpwr_1.get_firmware_version()
```

- 获取 TimerPWR 模块当前固件的版本号。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/12_uiflow_block_unit_timerpwr_save_data_to_flash.svg">

```python
timerpwr_1.save_data_to_flash()
```

- 将数据保存到闪存中。此块将模块中的数据(如电池、电流等)保存到持久存储中，以便以后使用。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/13_uiflow_block_unit_timerpwr_set_grove_output_status.svg">

```python
timerpwr_1.set_grove_output_status(True)
```

- 设置 Grove 输出端口状态为启用(True)。这个块启用 Grove 端口的输出功能。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/14_uiflow_block_unit_timerpwr_set_oled_backlight_status.svg">

```python
timerpwr_1.set_oled_backlight_status(True)
```

- 设置 OLED 背光为启用(True)。这个块打开 OLED 屏幕的背光。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/15_uiflow_block_unit_timerpwr_set_wakeup_trigger.svg">

```python
timerpwr_1.set_wakeup_trigger(timerpwr_1.TRIG_ALL)
```

- 设置唤醒触发条件为所有事件触发(TRIG_ALL)。这个块配置模块在任何事件(如按钮按下、USB 插入等)发生时触发唤醒。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/16_uiflow_block_unit_timerpwr_set_sleep_trigger.svg">

```python
timerpwr_1.set_sleep_trigger(timerpwr_1.TRIG_ALL)
```

- 设置睡眠触发条件为所有事件触发(TRIG_ALL)。这个块配置模块在任何事件发生时会进入睡眠状态，节省电力。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/17_uiflow_block_unit_timerpwr_sleep_once.svg">

```python
timerpwr_1.sleep_once(0, 0, 5, 0, 0, 5)

```

- 设置一次性睡眠模式，参数是定时睡眠的配置(例如每隔5秒进入睡眠状态)。这将使设备进入睡眠模式，并在指定的时间后唤醒。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/18_uiflow_block_unit_timerpwr_sleep_cycle.svg">

```python
timerpwr_1.sleep_cycle(0, 0, 5, 0, 0, 5)

```

- 设置循环睡眠模式，这个块会使设备周期性地进入睡眠并唤醒。例如，每过 5 秒进入睡眠模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/19_uiflow_block_unit_timerpwr_usb_callback.svg">

```python
def timerpwr_1_btna_released_event(args):
  # global params
  pass
timerpwr_1.set_callback(timerpwr_1.EVENT_BUTTONA_RELEASED, timerpwr_1_btna_released_event)

```
- 为 EVENT_BUTTONA_RELEASED 事件设置回调函数。当按下按钮 A 后释放时，会触发 timerpwr_1_btna_released_event 函数。args 参数包含触发事件时的相关数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/20_uiflow_block_unit_timerpwr_charging_callback.svg">

```python
def timerpwr_1_charging_event(args):
  # global params
  pass
timerpwr_1.set_callback(timerpwr_1.EVENT_CHARGING, timerpwr_1_charging_event)
```

- 为 EVENT_CHARGING 事件设置回调函数。这个事件在充电状态发生变化时触发，回调函数是 timerpwr_1_charging_event。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/21_uiflow_block_unit_timerpwr_button_callback.svg">

```python
def timerpwr_1_usb_inserted_event(args):
  # global params
  pass
timerpwr_1.set_callback(timerpwr_1.EVENT_USB_INSERTED, timerpwr_1_usb_inserted_event)
```

- 为 EVENT_USB_INSERTED 事件设置回调函数。这个事件在 USB 插入时触发，回调函数是 timerpwr_1_usb_inserted_event。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timerpwr/22_uiflow_block_unit_timerpwr_tick.svg">

```python
timerpwr_1.tick()
```

- 更新并处理 TimerPWR 模块的内部状态。通常在循环中调用，确保模块的工作状态和事件的处理。




