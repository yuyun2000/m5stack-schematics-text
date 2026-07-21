# [Unit ToF4M](/zh_CN/unit/Unit-ToF4M)

## 案例程序

> 获取设备测量的距离数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tof4m/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
tof4m_0 = unit.get(unit.TOF4M, unit.PORTA)

tof4m_0.set_distance_mode('SHORT')
tof4m_0.set_measurement_timing_budget(200)
while True:
  print(tof4m_0.get_single_distance_value)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tof4m/uiflow_block_unit_tof4m_get_single_distance.svg">

```python
print(tof4m_0.get_single_distance_value)
```

- 获取 Unit ToF4M 测量的单独距离(返回 int)。单位毫米 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tof4m/uiflow_block_unit_tof4m_set_distance_mode.svg">

```python
tof4m_0.set_distance_mode('SHORT')
```

- 设置 Unit ToF4M 测量的模式 
  - SHORT:短距离
  - MEDIUM:中距离
  - LONG:长距离
 
<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tof4m/uiflow_block_unit_tof4m_set_measurement_budget.svg">

```python
tof4m_0.set_measurement_timing_budget(200)
```

- 设置 Unit ToF4M 时间预算 (ms)


