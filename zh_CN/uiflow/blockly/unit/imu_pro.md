# [Unit Mini IMU-Pro](/zh_CN/unit/IMU%20Pro%20Mini%20Unit)

## 案例程序

获取陀螺仪状态，已经当前大气温度和压强

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_imupro_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import libs.bmi270 as bmi270
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
imu_pro_0 = unit.get(unit.IMU_PRO, unit.PORTA)

imu_pro_0.imu_instance.set_gyr_odr(bmi270.GYR_ODR_200)
while True:
  print((str('temperature:') + str((imu_pro_0.temperature))))
  print((str('pressure:') + str((imu_pro_0.pressure))))
  print((str('acceleratuin:') + str((imu_pro_0.acceleration))))
  print((str('gyro:') + str((imu_pro_0.gyro))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_bmi_set_acc_odr.svg">

```python
imu_pro_0.imu_instance.set_acc_odr(bmi270.ACC_ODR_200)
```

- 设置加速度计的输出数据率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_bmi_set_acc_range.svg">

```python
imu_pro_0.imu_instance.set_acc_range(bmi270.ACC_RANGE_2G)
```

- 设置加速度计的测量范围

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_bmi_set_gyro_odr.svg">

```python
imu_pro_0.imu_instance.set_gyr_odr(bmi270.GYR_ODR_200)
```

- 设置陀螺仪的输出数据率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_bmi_set_gyro_range.svg">

```python
imu_pro_0.imu_instance.set_acc_range(bmi270.GYR_RANGE_250)
```

- 设置陀螺仪的测量范围

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_get_acc.svg">

```python
print((str('acceleration:') + str((imu_pro_0.acceleration))))
```

- 获取加速度计数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_get_attitude.svg">

```python
print((str('attitude angles:') + str((imu_pro_0.attitude))))
```

- 获取姿态角数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_get_compass.svg">

```python
print((str('compass angle:') + str((imu_pro_0.compass))))
```

- 获取电子罗盘数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_get_gyro.svg">

```python
print((str('gyro:') + str((imu_pro_0.gyro))))
```

- 获取陀螺仪数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_get_mag.svg">

```python
print((str('magnetometer value:') + str((imu_pro_0.magnetometer))))
```

- 获取磁力计数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_get_pressure.svg">

```python
print((str('pressure:') + str((imu_pro_0.pressure))))
```

- 获取气压计数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_get_temp.svg">

```python
print((str('termperature:') + str((imu_pro_0.temperature))))
```

- 获取温度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/imu_pro/uiflow_block_unit_imupro_set_gyro_offset.svg">

```python
imu_pro_0.setGyroOffsets(0, 0, 0)
```

- 设置陀螺仪零偏校准值

