# AtomS3R IMU 姿态传感器

AtomS3R IMU 姿态传感器输入相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5AtomS3R
- M5Unified 库版本 >= 0.2.17
- M5GFX 库版本 >= 0.2.22

```cpp line-num
#include <M5Unified.h>

void setup(void) {
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    Serial.begin(115200);
}

void loop(void) {
    auto imu_update = M5.Imu.update();
    if (imu_update) {
        auto data = M5.Imu.getImuData();

        // The data obtained by getImuData can be used as follows.
        data.accel.x;      // accel x-axis value.
        data.accel.y;      // accel y-axis value.
        data.accel.z;      // accel z-axis value.
        data.accel.value;  // accel 3values array [0]=x / [1]=y / [2]=z.

        data.gyro.x;      // gyro x-axis value.
        data.gyro.y;      // gyro y-axis value.
        data.gyro.z;      // gyro z-axis value.
        data.gyro.value;  // gyro 3values array [0]=x / [1]=y / [2]=z.

        data.value;  // all sensor 9values array [0~2]=accel / [3~5]=gyro / [6~8]=mag

        Serial.printf("ax:%f  ay:%f  az:%f\r\n", data.accel.x, data.accel.y, data.accel.z);
        Serial.printf("gx:%f  gy:%f  gz:%f\r\n", data.gyro.x, data.gyro.y, data.gyro.z);
        M5.Display.clear();
        M5.Display.setCursor(0, 0);          
        M5.Display.printf("ax:%.3f\nay:%.3f\naz:%.3f\r\n", data.accel.x, data.accel.y, data.accel.z);
        M5.Display.printf("gx:%.3f\ngy:%.3f\ngz:%.3f\r\n", data.gyro.x, data.gyro.y, data.gyro.z);
    }
    delay(100);
}
```

烧录上述程序到 AtomS3R 后，可以看到 IMU 传感器的加速度和陀螺仪数据会实时输出在串口监视器和屏幕上。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/C126_AtomS3R_Arduino_pictures_03.jpg" width="30%">

## API

AtomS3R IMU 部分使用了 M5Unified 库中的 `IMU_Class`, 更多按键相关的 API 可以参考下方文档:

- [M5Unified - IMU Class](/zh_CN/arduino/m5unified/imu_class)

## IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/IMU-AtomS3R.jpg" width="70%">