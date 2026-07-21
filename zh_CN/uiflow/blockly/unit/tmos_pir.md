# [Unit TMOS PIR](/zh_CN/unit/UNIT-TMOS%20PIR)

## 案例程序

> 在主循环中不断更新并打印 TMOS PIR 传感器检测到的数据，包括运动状态、存在状态、环境温度变化以及物体温度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/uiflow_block_unit_tmos_pir_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

tmos_0 = unit.get(unit.TMOS, unit.PORTA)

while True:
  tmos_0.tick_callback()
  print(tmos_0.get_data_ready())
  print(tmos_0.get_motion_state())
  print(tmos_0.get_motion_value())
  print(tmos_0.get_presence_state())
  print(tmos_0.get_presence_value())
  print(tmos_0.get_tamb_shock_state())
  print(tmos_0.get_tambient_raw_value())
  print(tmos_0.get_temperature_data())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/1_uiflow_block_unit_tmos_get_data_ready.svg">

```python
tmos_0.get_data_ready()
```

- 检查传感器数据是否已更新。如果最新的传感器读数已经可用，则返回 True；否则返回 False。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/2_uiflow_block_unit_tmos_get_motion_state.svg">

```python
tmos_0.get_motion_state()
```

- 检查是否检测到运动。如果传感器检测到运动，则返回 True；否则返回 False。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/3_uiflow_block_unit_tmos_get_motion_value.svg">

```python
tmos_0.get_motion_value()
```

- 获取运动检测的数值。这可能表示检测到的运动强度或范围，通常以整数形式返回。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/4_uiflow_block_unit_tmos_get_presence_state.svg">

```python
tmos_0.get_presence_state()
```

- 检查是否检测到存在(即场内是否有人)。如果检测到人的存在，则返回 True；否则返回 False。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/5_uiflow_block_unit_tmos_get_presence_value.svg">

```python
tmos_0.get_presence_value()
```

- 获取存在检测的数值，类似于运动检测值，但用于确定是否有人在传感器范围内。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/6_uiflow_block_unit_tmos_get_tamb_shock_state.svg">

```python
tmos_0.get_tamb_shock_state()
```

- 检查是否检测到环境温度的急剧变化。如果有显著的温度变化，返回 True；否则返回 False。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/7_uiflow_block_unit_tmos_get_tambient_raw_value.svg">

```python
tmos_0.get_tambient_raw_value()
```

- 读取当前环境温度，通常以整数形式返回。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/8_uiflow_block_unit_tmos_get_temperature_data.svg">

```python
tmos_0.get_temperature_data()
```

- 读取传感器前方物体的温度，以浮点数形式返回。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/9_uiflow_block_unit_tmos_callback.svg">

```python
def tmos_0_ambient_temperature_shock_detect_event(arg):
  # global params
  pass
tmos_0.set_callback(tmos_0_ambient_temperature_shock_detect_event, tmos_0.AMBIENT_TEMPERATURE_SHOCK_DETECT)
```

- 当传感器检测到环境温度时触发的事件。这个块可以设置为在某些条件下执行操作，如温度变化。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/10_uiflow_block_unit_tmos_tick.svg">

```python
tmos_0.tick_callback()
```

- 在程序的主循环中反复执行的操作。这可以用来定期检查传感器的状态或读取值。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/11_uiflow_block_unit_tmos_get_gain_mode.svg">

```python
tmos_0.get_gain_mode()
```

- 获取传感器的增益模式。增益模式决定了传感器处理信号的方式，通常以整数形式表示不同的模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/12_uiflow_block_unit_tmos_get_tmos_sensitivity.svg">

```python
tmos_0.get_tmos_sensitivity()
```

- 获取传感器的灵敏度。这是一个浮点数，高值表示更高的灵敏度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/13_uiflow_block_unit_tmos_get_motion_threshold.svg">

```python
tmos_0.get_motion_threshold()
```

- 获取触发运动检测的阈值。这是一个整数值，低值可能意味着即使是小的移动也会被检测到。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/14_uiflow_block_unit_tmos_get_motion_hysteresis.svg">

```python
tmos_0.get_motion_hysteresis()
```

- 获取运动检测的滞后值，用于定义传感器停止报告运动前必须达到的稳定状态。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/15_uiflow_block_unit_tmos_get_presence_threshold.svg">

```python
tmos_0.get_presence_threshold()
```

- 获取存在检测的阈值。设置这个值可以调整何时认为有人存在。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/16_uiflow_block_unit_tmos_get_presence_hysteresis.svg">

```python
tmos_0.get_presence_hysteresis()
```

- 获取存在检测的滞后值，这决定了在停止报告存在之前的稳定时间。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/17_uiflow_block_unit_tmos_get_tambient_shock_threshold.svg">

```python
tmos_0.get_tambient_shock_threshold()

```

- 获取环境温度变化检测的阈值。这个阈值用于触发温度快速变化的事件。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/18_uiflow_block_unit_tmos_get_tambient_shock_hysteresis.svg">

```python
tmos_0.get_tambient_shock_hysteresis()

```

- 获取环境温度变化检测的滞后值。这决定了温度变化报告停止前的稳定期。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/19_uiflow_block_unit_tmos_set_gain_mode.svg">

```python
tmos_0.set_gain_mode(0)
```
- 设置传感器的增益模式为宽增益模式。这种模式可能提供更广的检测范围或更大的信号放大。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/20_uiflow_block_unit_tmos_set_tmos_sensitivity.svg">

```python
tmos_0.set_tmos_sensitivity(0)
```

- 设置传感器的灵敏度。这个值可以从0到4080调整，数值越高，传感器越敏感。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/21_uiflow_block_unit_tmos_set_motion_threshold.svg">

```python
tmos_0.set_motion_threshold(200)
```

- 设置触发运动检测的阈值。这个值决定了多少级别的移动被识别为有效运动，可调范围从0到32767。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/22_uiflow_block_unit_tmos_set_motion_hysteresis.svg">

```python
tmos_0.set_motion_hysteresis(0)
```

- 设置运动检测的滞后值。这个值帮助防止传感器在边界条件下频繁切换状态，可调范围从0到255。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/23_uiflow_block_unit_tmos_set_presence_threshold.svg">

```python
tmos_0.set_presence_threshold(200)
```

- 设置触发存在检测的阈值。类似于运动阈值，这个设置决定了何种级别的“存在”会被认为是有效的，可调范围同样为0到32767。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/24_uiflow_block_unit_tmos_set_presence_hysteresis.svg">

```python
tmos_0.set_presence_hysteresis(0)
```

- 设置存在检测的滞后值。这个值用于稳定传感器的输出，防止因微小变化而频繁更改状态。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/25_uiflow_block_unit_tmos_set_tambient_shock_threshold.svg">

```python
tmos_0.set_tambient_shock_threshold(200)
```

- 设置环境温度快速变化的检测阈值。此值决定什么样的温度变化速度被认为是显著的。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/toms_pir/26_uiflow_block_unit_tmos_set_tambient_shock_hysteresis.svg">

```python
tmos_0.set_tambient_shock_hysteresis(0)
```

- 设置环境温度快速变化检测的滞后值。此设置有助于防止因小幅温度波动而误报。





