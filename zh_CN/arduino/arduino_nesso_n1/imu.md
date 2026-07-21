# Arduino Nesso N1 IMU 姿态传感器

Arduino Nesso N1 IMU 姿态传感器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = ArduinoNessoN1
- M5GFX 库版本 >= 0.2.17
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

void setup() {
  auto cfg = M5.config();
  M5.begin(cfg);
  M5.Display.setRotation(1);
  M5.Display.setTextColor(GREEN);
  M5.Display.setTextDatum(middle_center);
  M5.Display.setFont(&fonts::FreeSansBold9pt7b);
  M5.Display.setTextSize(1);
}

void loop(void) {
  auto imu_update = M5.Imu.update();
  if (imu_update) {
    M5.Display.setCursor(0, 40);
    M5.Display.clear();  // Delay 100ms 延迟100ms

    auto data = M5.Imu.getImuData();

    // The data obtained by getImuData can be used as follows.
    // data.accel.x;      // accel x-axis value.
    // data.accel.y;      // accel y-axis value.
    // data.accel.z;      // accel z-axis value.
    // data.accel.value;  // accel 3values array [0]=x / [1]=y / [2]=z.

    // data.gyro.x;      // gyro x-axis value.
    // data.gyro.y;      // gyro y-axis value.
    // data.gyro.z;      // gyro z-axis value.
    // data.gyro.value;  // gyro 3values array [0]=x / [1]=y / [2]=z.

    // data.value;  // all sensor 9values array [0~2]=accel / [3~5]=gyro /
    //              // [6~8]=mag

    Serial.printf("ax:%f  ay:%f  az:%f\r\n", data.accel.x, data.accel.y,
                  data.accel.z);
    Serial.printf("gx:%f  gy:%f  gz:%f\r\n", data.gyro.x, data.gyro.y,
                  data.gyro.z);

    M5.Display.printf("IMU:\r\n");
    M5.Display.printf("ax:%0.2f ay:%0.2f az:%0.2f\r\n", data.accel.x,
                      data.accel.y, data.accel.z);
    M5.Display.printf("gx:%0.2f gy:%0.2f gz:%0.2f\r\n", data.gyro.x,
                      data.gyro.y, data.gyro.z);
  }
  delay(100);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_imu_example_01.jpg" width="50%" />

## API

Arduino Nesso N1 的 IMU 驱动部分使用了 M5Unified 库中的`IMU_Class`, 更多按键相关的 API 可以参考下方文档：

- [M5Unified - IMU Class](/zh_CN/arduino/m5unified/imu_class)
