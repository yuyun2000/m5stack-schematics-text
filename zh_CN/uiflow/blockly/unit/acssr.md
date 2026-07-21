# [Unit ACSSR](/zh_CN/unit/acssr)

## 案例程序

> 点击按键，控制继电器的输人输出状态以及 RGB 的灯亮灭

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
acssr_0 = unit.get(unit.AC_SSR, unit.PORTA)

def buttonA_wasPressed():
  # global params
  acssr_0.set_i2c_ssr_state(1)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  acssr_0.set_i2c_ssr_state(0)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  # global params
  acssr_0.set_i2c_rgb_led(50, 50, 50)
  pass
btnC.wasPressed(buttonC_wasPressed)

acssr_0.init_mode(1)
print((str('FW version:') + str((acssr_0.get_i2c_status(0xFE)))))
while True:
  if acssr_0.get_i2c_ssr_status():
    print('ON')
  else:
    print('OFF')
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_init_i2c_address.svg">

```python
acssr_0.init_i2c_address(0x50)
```

- 初始化设置 ACSSR Unit 的 I2C 通讯地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_init_modbus.svg">

```python
acssr_0.init_modbus(4, 1, 115200, 8, 1, None)
```

- 初始化 Modbus 通讯格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_get_i2c_led.svg">

```python
print(acssr_0.get_i2c_rgb_led())
```

- 通过 i2c 获取 RGB 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_get_i2c_ssr_status.svg">

```python
print(acssr_0.get_i2c_ssr_status())
```

- 通过 I2C 获取 SSR 的开关状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_get_i2c_status.svg">

```python
print(acssr_0.get_i2c_status(0xFE))
```

- 通过 I2C 模式获取固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_get_modbus_led.svg">

```python
print(acssr_0.get_modbus_rgb_led())
```

- 通过 Modbus 通讯方式获取 RGB 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_get_modbus_ssr_status.svg">

```python
print(acssr_0.get_modbus_ssr_status())
```

- 通过 Modbus 获取 SSR 的开关状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_get_modbus_status.svg">

```python
print(acssr_0.get_modbus_status(0x0001))
```

- 通过 Modbus 模式获取固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_select_mode.svg">

```python
acssr_0.init_mode(1)
```

- 设置 ACSSR Unit 的通讯模式，I2C 或者是 Modbus

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_set_i2c_address.svg">

```python
acssr_0.set_i2c_address(0x50)
```

- 设置 ACSSR 的 i2c 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_set_i2c_rgb_led.svg">

```python
acssr_0.set_i2c_rgb_led(50, 50, 50)
```

- 通过 i2c 设置 RGB 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_set_i2c_ssr_state.svg">

```python
acssr_0.set_i2c_ssr_state(1)
```

- 设置 SSR 设备的开关状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_set_modbus_address.svg">

```python
acssr_0.set_modbus_address(0x50)
```

- 设置 ACSSR 的 i2c 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_set_modbus_rgb_led.svg">

```python
acssr_0.set_modbus_rgb_led(50, 50, 50)
```

- Modbus 设置 LED 的 RGB 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/acssr/uiflow_block_unit_acssr_set_modbus_ssr_state.svg">

```python
acssr_0.set_modbus_ssr_state(1)
```

- Modbus 设置 SSR 的状态开关
