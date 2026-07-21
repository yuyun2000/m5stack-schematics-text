# StackChan IMU 姿态传感器

StackChan IMU 姿态传感器输入相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5CoreS3
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include <M5Unified.h>

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
}

void loop(void) {
    auto imu_update = M5.Imu.update();
    if (imu_update) {
        M5.Display.setCursor(0, 20);
        M5.Display.clear();  // Delay 100ms

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

        data.mag.x;      // mag x-axis value.
        data.mag.y;      // mag y-axis value.
        data.mag.z;      // mag z-axis value.
        data.mag.value;  // mag 3values array [0]=x / [1]=y / [2]=z.

        data.value;  // all sensor 9values array [0~2]=accel / [3~5]=gyro / [6~8]=mag

        Serial.printf("ax:%f  ay:%f  az:%f\r\n", data.accel.x, data.accel.y, data.accel.z);
        Serial.printf("gx:%f  gy:%f  gz:%f\r\n", data.gyro.x, data.gyro.y, data.gyro.z);
        Serial.printf("mx:%f  my:%f  mz:%f", data.mag.x, data.mag.y, data.mag.z);
        M5.Display.printf("IMU:\r\n");
        M5.Display.printf("ax:%f\nay:%f\naz:%f\r\n", data.accel.x, data.accel.y, data.accel.z);
        M5.Display.printf("gx:%f\ngy:%f\ngz:%f\r\n", data.gyro.x, data.gyro.y, data.gyro.z);
        M5.Display.printf("mx:%f\nmy:%f\nmz:%f\r\n", data.mag.x, data.mag.y, data.mag.z);
    }
    delay(100);
}
```

烧录成功后，您可以在串口监视器和屏幕上看到 IMU 传感器的加速度、陀螺仪和磁力计数据。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/StackChan_IMU.jpg" width="40%">

## API

StackChan IMU 部分使用了 M5Unified 库中的`IMU_Class`, 更多 IMU 相关的API可以参考下方文档:

- [M5Unified - IMU Class](/zh_CN/arduino/m5unified/imu_class)

