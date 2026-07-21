# [Unit Pbhub](/zh_CN/unit/pbhub)

## 案例程序

> 控制电机旋转

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
pbhub_0 = unit.get(unit.PBHUB, unit.PORTA)

while True:
  pbhub_0.setServoAngle(0, 0, 11)
  wait(1)
  pbhub_0.setServoAngle(0, 0, 180)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_init_i2c_address.svg">

```python
pbhub_0.init_i2c_address(0x61)
```

- 初始化 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_analogRead.svg">

```python
print(pbhub_0.analogRead(0))
```

- 读取模拟值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_digital_read_value.svg">

```python
print(pbhub_0.digitalRead(0, 0))
```

- 读取引脚数字值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_digital_write_value.svg">

```python
pbhub_0.digitalWrite(0, 0, 0)
```

- 向引脚写入数字值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_pwm_read.svg">

```python
print(pbhub_0.pwmRead(0, 0))
```

- 读取对应引脚对应脉冲

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_pwm_write.svg">

```python
pbhub_0.pwmWrite(0, 0, 0)
```

- 向对应引脚下对应 IO 口写入脉冲

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_read_status.svg">

```python
print(pbhub_0.read_status(0xFE))
```

- 读取 unit 状态/版本号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_setBrightness_value.svg">

```python
pbhub_0.setBrightness(0, 50)
```

- 设置指定引脚 RGB 灯珠亮度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_setColorPos_value.svg">

```python
pbhub_0.setColorPos(0, 0, 0xff0000)
```

- 设置指定引脚对应指定序号 RGB 灯珠的颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_setColorPos_value_input.svg">

```python
pbhub_0.setColorPos(0, 0, 0xff0000)
```

- 设置指定引脚对应指定范围 RGB 灯珠的颜色(可选择 RGB 方式 palette/Rgb/Hex)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_setColor_value.svg">

```python
pbhub_0.setColor(0, 0, 0, 0xff0000)
```

- 设置指定引脚对应指定范围 RGB 灯珠的颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_setColor_value_input.svg">

```python
pbhub_0.setColor(0, 0, 0, 0xff0000)
```

- 设置指定范围内 RGB 灯珠颜色(可选择 RGB 方式 palette/Rgb/Hex)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_setRgbNum_value.svg">

```python
pbhub_0.setRgbNum(0, 1)
```

- 设置指定引脚 IO 口的 LED 灯

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_set_i2c_address.svg">

```python
pbhub_0.init_i2c_address(0x61)
```

- 设置固件版本/I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_set_servo_angle.svg">

```python
pbhub_0.setServoAngle(0, 0, 90)
```

- 设置舵机旋转的角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pbhub/uiflow_block_pbhub_set_servo_pulse.svg">

```python
pbhub_0.setServoPulse(0, 0, 1000)
```

- 向引脚写入数字值

