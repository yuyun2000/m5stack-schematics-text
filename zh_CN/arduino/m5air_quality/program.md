# Air Quality Arduino 示例程序编译与烧录 

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5StampS3`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stamp_s3/quickstart_arduino_stamps3_select_board.png" width="70%" />

- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`，`M5GFX`，`Sensirion I2C SEN5X`，`Sensirion I2C SCD4x`驱动库安装。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/quickstart_arduino_air_quality_download_library05.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/coreink_arduino_lib_02.jpg" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/quickstart_arduino_air_quality_download_library03.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/quickstart_arduino_air_quality_download_library04.png" width="70%" />


## 2.下载模式

- 上电前按住 Air Quality 模组上的 G0 按键, 然后连接USB线供电将进入下载模式。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/airq%20(2).gif" width="50%" />


## 3.端口选择 & 配置

- 将设备通过USB线连接至电脑，在完成驱动安装后， Arduino IDE中可选中对应的控制板和设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/quickstart_arduino_air_quality_select_port.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/quickstart_arduino_air_quality_select_board_config.png" width="70%">


## 4.程序编译&烧录

### Hello World

在Arduino IDE中新建程序，并粘贴下方Hello World案例代码，编译并烧录至设备，显示屏和串口监视器将显示"HelloWorld"!

```cpp line-num
#include <M5Unified.h>

void setup() {

  auto cfg = M5.config();
  M5.begin(cfg);
  M5.Display.setTextSize(3);
  M5.Display.println("HelloWorld!");
  Serial.println("Hello World!!!"); 
}

void loop() {
}
```

2.上传完成就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_display.jpg" width="30%">

## 5.相关资源

-  **Github**
   - [M5Unified](https://github.com/m5stack/M5Unified)
   - [M5GFX](https://github.com/m5stack/M5GFX)
   - [Sensirion I2C SEN5X](https://github.com/Sensirion/arduino-i2c-sen5x)
   - [Sensirion I2C SCD4x](https://github.com/Sensirion/arduino-i2c-scd4x)

-  **Arduino API & Examples**

    - [Sensor-SEN55](/zh_CN/arduino/m5air_quality/sen55)
    - [Sensor-SCD40](/zh_CN/arduino/m5air_quality/scd40)
    - [RTC](/zh_CN/arduino/m5air_quality/rtc)
    - [Display](/zh_CN/arduino/m5air_quality/display)
    - [Button](/zh_CN/arduino/m5air_quality/button)
    - [Battery](/zh_CN/arduino/m5air_quality/battery)
    - [Wi-Fi](/zh_CN/arduino/m5air_quality/wifi)
    - [Buzzer](/zh_CN/arduino/m5air_quality/buzzer)
    - [Wakeup](/zh_CN/arduino/m5air_quality/wakeup)