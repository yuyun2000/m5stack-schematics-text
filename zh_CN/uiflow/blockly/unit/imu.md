# [Unit Mini IMU](/zh_CN/unit/imu)

## 案例程序

> 获取陀螺仪当前状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
unit_imu_0 = unit.get(unit.IMU6886, unit.PORTA)

unit_imu_0.setAccUnit(0)
unit_imu_0.gyroFullScaleRange(0x00)
while True:
  print((str('ACC Z:') + str((unit_imu_0.acceleration[0]))))
  print((str('ACC Y:') + str((unit_imu_0.acceleration[1]))))
  print((str('ACC Y:') + str((unit_imu_0.acceleration[2]))))
  print((str('Gyro X:') + str((unit_imu_0.gyro[0]))))
  print((str('Gyro Y:') + str((unit_imu_0.gyro[1]))))
  print((str('Gyro Z:') + str((unit_imu_0.gyro[2]))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_acc_fullscale_range.svg">

```python
unit_imu_0.accFullScaleRange(0x00)
```

- 设置所有加速度刻度范围

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_get_acc_x.svg">

```python
print(unit_imu_0.acceleration[0])
```

- 获取加速度计 X 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_get_acc_y.svg">

```python
print(unit_imu_0.acceleration[1])
```

- 获取加速度计 Y 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_get_acc_z.svg">

```python
print(unit_imu_0.acceleration[2])
```

- 获取加速度计 Z 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_get_gyr_x.svg">

```python
print(unit_imu_0.gyro[0])
```

- 获取陀螺仪 X 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_get_gyr_y.svg">

```python
print(unit_imu_0.gyro[1])
```

- 获取陀螺仪 Y 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_get_gyr_z.svg">

```python
print(unit_imu_0.gyro[2])
```

- 获取陀螺仪 Z 的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_get_x.svg">

```python
print(unit_imu_0.ypr[1])
```

- 获取 X 轴姿态角

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_get_y.svg">

```python
print(unit_imu_0.ypr[2])
```

- 获取 Y 轴姿态角

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_gyro_calibrate.svg">

```python
unit_imu_0.gyroCalibrate(250, 5)
```

- 使用采样数和每个采样的延迟设置陀螺仪校准

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_gyro_fullscale_range.svg">

```python
unit_imu_0.gyroFullScaleRange(0x00)
```

- 设置陀螺仪刻度范围

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_set_acc_unit.svg">

```python
unit_imu_0.setAccUnit(0)
```

- 设置加速度计单位 g 或 m/s^2

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu/uiflow_block_unit_imu_set_gyro_offset.svg">

```python
unit_imu_0.setGyroOffsets(0, 0, 0)
```

- 设置手动陀螺仪校准偏移值

