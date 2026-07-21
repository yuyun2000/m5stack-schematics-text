# IMU

## 案例程序

读取显示当前 IMU 姿态数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
import imu

setScreenColor(0x222222)
imu0 = imu.IMU()

while True:
  print((str('X: ') + str((imu0.ypr[1]))))
  print((str('Y: ') + str((imu0.ypr[2]))))
  print((str('X ACC: ') + str((imu0.acceleration[0]))))
  print((str('Y ACC: ') + str((imu0.acceleration[1]))))
  print((str('Z ACC: ') + str((imu0.acceleration[2]))))
  print((str('X Gyr: ') + str((imu0.gyro[0]))))
  print((str('Y Gyr: ') + str((imu0.gyro[1]))))
  print((str('Z Gyr: ') + str((imu0.gyro[2]))))
  wait_ms(2)
```


## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_get_x.svg"> 

```python
imu0.ypr[1]
```

- 获取横滚数据


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_get_y.svg"> 

```python
imu0.ypr[2]
```

- 获取俯仰数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_get_x_acc.svg"> 

```python
imu0.acceleration[0]
```

- 获取 X 轴加速度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_get_y_acc.svg"> 

```python
imu0.acceleration[1]
```

- 获取 Y 轴加速度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_get_z_acc.svg"> 

```python
imu0.acceleration[2]
```

- 获取 Z 轴加速度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_get_x_gyr.svg"> 

```python
imu0.gyro[0]
```

- 获取 X 方向角速度


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_get_y_gyr.svg"> 

```python
imu0.gyro[1]
```

- 获取 Y 方向角速度


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/imu/uiflow_block_imu_get_z_gyr.svg"> 

```python
imu0.gyro[2]
```

- 获取 Z 方向角速度
