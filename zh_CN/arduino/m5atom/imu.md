# Atom-Matrix IMU 六轴姿态传感器

Atom-Matrix 六轴姿态传感器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5Atom
- M5Unified 库版本 >= 0.2.13

```cpp line-num
#include <M5Unified.h>

m5::imu_data_t imuData;

void setup() {
  M5.begin();
  Serial.begin(115200);
}

void loop() {
  M5.Imu.update();
  imuData = M5.Imu.getImuData();

  Serial.printf("\n Acc X = %6.2f  \n", imuData.accel.x);
  Serial.printf(" Acc Y = %6.2f  \n", imuData.accel.y);
  Serial.printf(" Acc Z = %6.2f  \n\n", imuData.accel.z);

  Serial.printf(" Gyr X = %6.2f  \n", imuData.gyro.x);
  Serial.printf(" Gyr Y = %6.2f  \n", imuData.gyro.y);
  Serial.printf(" Gyr Z = %6.2f  \n", imuData.gyro.z);

  delay(1000);
} 
```

该程序会通过串口反馈实时的加速度计、陀螺仪读数，每秒钟刷新一次。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/Atom_Matrix_V1_1_Arduino_IMU.png" width="50%">

## API

Atom-Matrix 姿态传感器部分使用了 `M5Unified` 库中的 `Imu_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - IMU Class](/zh_CN/arduino/m5unified/imu_class)

## IMU 三轴方向示意图

- Atom-Matrix
  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/674/IMU-Atom-Matrix.jpg" width="50%">

- Atom-Matrix v1.1
  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/IMU-Atom-Matrix-v1.1.jpg" width="50%">
