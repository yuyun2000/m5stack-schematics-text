# StickC-Plus IMU 姿态传感器

## 案例程序

```cpp line-num
#include <M5StickCPlus.h>

float accX = 0.0F;
float accY = 0.0F;
float accZ = 0.0F;

float gyroX = 0.0F;
float gyroY = 0.0F;
float gyroZ = 0.0F;

float pitch = 0.0F;
float roll  = 0.0F;
float yaw   = 0.0F;

void setup() {
    M5.begin();             // Init M5StickC Plus.  初始化 M5StickC Plus
    M5.Imu.Init();          // Init IMU.  初始化IMU
    M5.Lcd.setRotation(3);  // Rotate the screen. 将屏幕旋转
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setTextSize(1);
    M5.Lcd.setCursor(80, 15);  // set the cursor location.  设置光标位置
    M5.Lcd.println("IMU TEST");
    M5.Lcd.setCursor(30, 30);
    M5.Lcd.println("  X       Y       Z");
    M5.Lcd.setCursor(30, 70);
    M5.Lcd.println("  Pitch   Roll    Yaw");
}


void loop() {
    static float temp = 0;
    M5.IMU.getGyroData(&gyroX, &gyroY, &gyroZ);
    M5.IMU.getAccelData(&accX, &accY, &accZ);
    M5.IMU.getAhrsData(&pitch, &roll, &yaw);
    M5.IMU.getTempData(&temp);
    M5.Lcd.setCursor(30, 40);
    M5.Lcd.printf("%6.2f  %6.2f  %6.2f      ", gyroX, gyroY, gyroZ);
    M5.Lcd.setCursor(170, 40);
    M5.Lcd.print("o/s");
    M5.Lcd.setCursor(30, 50);
    M5.Lcd.printf(" %5.2f   %5.2f   %5.2f   ", accX, accY, accZ);
    M5.Lcd.setCursor(170, 50);
    M5.Lcd.print("G");
    M5.Lcd.setCursor(30, 80);
    M5.Lcd.printf(" %5.2f   %5.2f   %5.2f   ", pitch, roll, yaw);

    M5.Lcd.setCursor(30, 95);
    M5.Lcd.printf("Temperature : %.2f C", temp);
    delay(100);
}
```

## IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/IMU-StickC-Plus.jpg" width="70%">