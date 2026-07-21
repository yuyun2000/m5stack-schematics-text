# [Atomic Stepmotor Base](/zh_CN/atom/Atomic%20Stepmotor%20Base)

## 案例程序

该程序控制 PWM 信号和方向切换。通过按钮 A 的单击和双击，切换运行状态和方向标志位。运行标志`run_flag`为1时，PWM 信号恢复并驱动设备；方向标志`dir_flag`为0或1时，分别控制引脚23的输出高低以改变方向。ADC 读取值用于监测输入信号，RGB 灯颜色指示运行状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_atomic_base_stepmotor_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from easyIO import *
import machine

dir_flag = None
run_flag = None
adc_val = None

def buttonA_wasDoublePress():
  global dir_flag, run_flag, adc_val, adc0, PWM0
  if dir_flag == 0:
    dir_flag = 1
  else:
    dir_flag = 0
  pass
btnA.wasDoublePress(buttonA_wasDoublePress)

def buttonA_wasPressed():
  global dir_flag, run_flag, adc_val, adc0, PWM0
  if run_flag == 0:
    rgb.setColorAll(0x33ff33)
    run_flag = 1
  else:
    rgb.setColorAll(0x000000)
    run_flag = 0
  pass
btnA.wasPressed(buttonA_wasPressed)

digitalWrite(21, 1)
digitalWrite(22, 0)
dir_flag = 0
run_flag = 0
adc0 = machine.ADC(33)
adc0.width(machine.ADC.WIDTH_12BIT)
adc0.atten(machine.ADC.ATTN_11DB)
adc_val = 0
rgb.setColorAll(0x000000)
PWM0 = machine.PWM(19, freq=12000, duty=0, timer=0)
PWM0.pause()
PWM0.duty(50)
while True:
  adc_val = adc0.read()
  if run_flag == 1:
    PWM0.resume()
  else:
    PWM0.pause()
  if dir_flag == 1:
    digitalWrite(23, 1)
  else:
    digitalWrite(23, 0)
  print(adc_val)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_base_stepmotor_init.svg">

```python
stepmotor = Stepmotor('Full')
```

- 初始化步进电机，并设置步进模式为全步进(Full step)，这会影响电机的步进方式和精度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_base_stepmotor_disbale.svg">

```python
stepmotor.disbale()
```

- 禁用步进电机，停止电机的操作，电机将不会再接收到任何运动命令。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_base_stepmotor_enable.svg">

```python
stepmotor.enable()
```

- 启用步进电机，允许电机开始执行命令并响应控制信号。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_base_stepmotor_get_status.svg">

```python
stepmotor.get_status()
```

- 获取步进电机的状态，通常用于检测电机是否处于启用状态或是否运行正常。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_base_stepmotor_get_voltage.svg">

```python
stepmotor.get_voltage()
```

- 获取步进电机的电压值，可能用于监控电源情况，以确保电机在正常电压下运行。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_base_stepmotor_move_circles.svg">

```python
stepmotor.move_circles(0, 0)
```

- 设置电机按顺时针方向旋转指定的圈数，该语句用于控制电机的转动角度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_base_stepmotor_move_steps.svg">

```python
stepmotor.move_steps(0, 0)
```

- 设置电机按顺时针方向移动指定的步数，用户可以通过步数精确控制电机的转动角度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/stepmotor/uiflow_block_base_stepmotor_reset.svg">

```python
stepmotor.reset()
```

- 将步进电机或者某个设备重置为初始状态。

