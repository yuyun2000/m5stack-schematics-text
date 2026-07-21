# [Unit RTC](/zh_CN/unit/UNIT%20RTC)

## 案例程序

设置时钟

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_rtc_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
rtc_0 = unit.get(unit.RTC8563, unit.PORTA)

rtc_0.set_date_time(37, 1, 1, 1, 0, 0, 0)
while True:
  print((str('hours') + str((rtc_0.get_date_time(2)))))
  print((str('minutes:') + str((rtc_0.get_date_time(1)))))
  print((str('seconds:') + str((rtc_0.get_date_time(0)))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_check_alarm_flag.svg">

```python
print((str('alarm flag:') + str((rtc_0.check_alarm_flag()))))
```

- 检查闹钟标志位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_check_timer_flag.svg">

```python
print((str('flag:') + str((rtc_0.check_timer_flag()))))
```

- 检查定时器标志位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_clear_alarm.svg">

```python
rtc_0.clear_alarm_flag()
```

- 清除闹钟

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_clear_timer_flag.svg">

```python
rtc_0.clear_timer_flag()
```

- 清除定时器标志位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_disable_alarm.svg">

```python
rtc_0.disable_alarm()
```

- 禁用闹钟

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_disable_timer.svg">

```python
rtc_0.disable_timer()
```

- 禁用定时器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_get_date_time.svg">

```python
print((str('rtc:') + str((rtc_0.get_date_time(0)))))
```

- 获取日期时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_get_timer_value.svg">

```python
print((str('value:') + str((rtc_0.get_timer_value()))))
```

- 获取定时器当前值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_pause_timer.svg">

```python
rtc_0.pause_timer()
```

- 暂停定时器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_resume_timer.svg">

```python
rtc_0.resume_timer()
```

- 恢复定时器运行

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_set_alarm.svg">

```python
rtc_0.set_alarm_clock(1, 0, 0)
```

- 设置闹钟

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_set_date_time.svg">

```python
rtc_0.set_date_time(0, 1, 1, 1, 0, 0, 0)
```

- 设置日期时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/rtc/uiflow_block_unit_rtc_set_timer_mode.svg">

```python
rtc_0.set_timer_mode(0, 0)
```

- 设置定时器工作模式

