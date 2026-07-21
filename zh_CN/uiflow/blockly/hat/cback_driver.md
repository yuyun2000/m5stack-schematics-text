# [Hat CBack Driver](/zh_CN/hat/c_back_driver)

## 案例程序

控制两个舵机通道来回转动0-180度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_driver/uiflow_block_hat_cback_driver_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_cback_0 = hat.get(hat.CBACK)

while True:
  hat_cback_0.set_servo_angle(0x00, 0)
  hat_cback_0.set_servo_angle(0x01, 0)
  wait(1)
  hat_cback_0.set_servo_angle(0x00, 90)
  hat_cback_0.set_servo_angle(0x01, 90)
  wait(1)
  hat_cback_0.set_servo_angle(0x00, 180)
  hat_cback_0.set_servo_angle(0x01, 180)
  wait(1)
  hat_cback_0.set_servo_angle(0x00, 90)
  hat_cback_0.set_servo_angle(0x01, 90)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_driver/uiflow_block_hat_cback_get_input.svg">

```python
hat_cback_0.set_output(0)
```

- 检查输入端口 B 的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_driver/uiflow_block_hat_cback_raw_adc.svg">

```python
hat_cback_0.get_adc16_raw()
```

- 读取原始的 ADC 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_driver/uiflow_block_hat_set_output.svg">

```python
hat_cback_0.set_output(0)
```

- 设置输出端口 B 的状态，输出的值可以是 0 或 1

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_driver/uiflow_block_hat_set_servo_angle.svg">

```python
hat_cback_0.set_servo_angle(0x00, 0)
```

- 设置伺服电机的角度，指定伺服电机通道(此处为 Channel1)，角度设置为 0 度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_driver/uiflow_block_hat_set_servo_pulse.svg">

```python
hat_cback_0.set_servo_pulse(0x10, 500)
```

- 设置伺服电机的脉冲宽度，指定伺服电机通道(此处为 Channel1)，脉冲宽度为 500

