# [Hat Mini Encoderc](/zh_CN/hat/MiniEncoderC%20Hat)

## 案例程序

设置 mini encoder 通讯地址，设置灯的颜色为白色，串口实时打印编码器的数值和按键的状态值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/joystick/uiflow_block_hat_joystick_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_mini_encoderc_0 = hat.get(hat.MINI_ENCODERC)

hat_mini_encoderc_0.init_i2c_address(0x42)
hat_mini_encoderc_0.set_LED_RGB24(50, 50, 50)
while True:
  print(hat_mini_encoderc_0.get_counter_value())
  print(hat_mini_encoderc_0.get_button_status())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_init.svg">

```python
hat_mini_encoderc_0.init_i2c_address(0x42)
```

- 初始化Mini EncoderC设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_get_button_status.svg">

```python
print((str('status:') + str((hat_mini_encoderc_0.get_button_status()))))
```

- 获取编码器按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_get_counter_value.svg">

```python
print((str('counter:') + str((hat_mini_encoderc_0.get_counter_value()))))
```

- 获取编码器计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_get_device_status.svg">

```python
print((str('status:') + str((hat_mini_encoderc_0.read_status(0xFE)))))
```

- 获取设备状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_get_increment_value.svg">

```python
print((str('increment:') + str((hat_mini_encoderc_0.get_increment_value()))))
```

- 获取编码器增量值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_reset_counter_value.svg">

```python
hat_mini_encoderc_0.reset_counter_value()
```

- 重置编码器计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_set_counter_value.svg">

```python
hat_mini_encoderc_0.set_counter_value(1000)
```

- 设置编码器计数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_set_i2c_address.svg">

```python
hat_mini_encoderc_0.set_i2c_address(0x42)
```

- 设置I2C通信地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/mini_encoderc/uiflow_block_hat_miniencoderc_set_led_rgb.svg">

```python
hat_mini_encoderc_0.set_LED_RGB24(50, 50, 50)
```

- 设置RGB LED颜色

