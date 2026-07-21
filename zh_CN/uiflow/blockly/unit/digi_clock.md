# [Unit DigiClock](/zh_CN/unit/digi_clock)

## 案例程序

> 数码管显示字符 A

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
digi_clock_0 = unit.get(unit.DIGI_CLOCK, unit.PORTA)

digi_clock_0.init_i2c_address(0x30)
digi_clock_0.write_brightness(4)
while True:
  digi_clock_0.write_char('A',0)
  wait(1)
  digi_clock_0.clear()
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_unit_digiclock_init_i2c_address.svg">

```python
igi_clock_0.init_i2c_address(0x30)
```

- 初始化 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_unit_digiclock_clear.svg">

```python
digi_clock_0.clear()
```

- 清除数码屏幕显示数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_unit_digiclock_read_version.svg">

```python
print(digi_clock_0.read_version())
```

- 获取 Unit 版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_unit_digiclock_write_brightness.svg">

```python
digi_clock_0.write_brightness(0)
```

- 设置屏幕亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_unit_digiclock_write_char.svg">

```python
digi_clock_0.write_char('',0)
```

- 对指定 index 数码管显示字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_unit_digiclock_write_char_list.svg">

```python
digi_clock_0.write_char_list('')
```

- 对指定 index 数码管显示字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_unit_digiclock_write_match_string.svg">

```python
digi_clock_0.write_match_string('')
```

- 数码管显示数值字符串。如"12356"

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/digi_clock/uiflow_block_unit_digiclock_write_raw.svg">

```python
digi_clock_0.write_raw(0,0)
```

- 对指定数码管写入原始数据

