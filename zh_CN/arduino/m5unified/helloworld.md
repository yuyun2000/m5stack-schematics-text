# M5Unified 快速上手

#>简介|M5Unified是一个M5Stack主控设备驱动库, 该库中适配了大多数M5Stack主控的内置硬件驱动, 如LCD、Touch、按键、扬声器、麦克风等。 M5Unified提供了一套统一的API, 同一套程序能够非常方便的运行在不同的M5Stack设备上。M5Unified支持在Arduino或ESP-IDF开发平台中使用, 能够有效提供你的开发效率。

## 准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择你实际使用的开发板选项。
- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`驱动库安装。(根据提示安装依赖库`M5GFX`)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unified/m5unified_install_01.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unified/m5unified_install_02.jpg" width="70%">

## Hello World

在Arduino IDE中新建程序, 并粘贴下方Hello World案例代码, 编译并烧录至设备, 显示屏和串口监视器将显示"HelloWorld!"，并每秒计数一次。

```cpp line-num
#include <M5Unified.h>  // Make the M5Unified library available to your program.

// global variables (define variables to be used throughout the program)
uint32_t count;

// setup function is executed only once at startup.
// This function mainly describes the initialization process.
void setup()
{
    auto cfg = M5.config();  // Assign a structure for initializing M5Stack
    // If config is to be set, set it here
    // Example.
    // cfg.external_spk = true;

    M5.begin(cfg);  // initialize M5 device

    M5.Display.setTextSize(3);           // change text size
    M5.Display.print("Hello World!!!");  // display Hello World! and one line is displayed on the screen
    Serial.println("Hello World!!!");    // display Hello World! and one line on the serial monitor
    count = 0;                           // initialize count
}

// loop function is executed repeatedly for as long as it is running.
// loop function acquires values from sensors, rewrites the screen, etc.
void loop()
{
    M5.Display.setCursor(0, 20);              // set character drawing coordinates (cursor position)
    M5.Display.printf("COUNT: %d\n", count);  // display count on screen
    Serial.printf("COUNT: %d\n", count);      // display count serially
    count++;                                  // increase count by 1
    delay(1000);                              // wait 1 second(1,000msec)
}
```


## 案例程序

M5Unified驱动库中提供了一系列的案例程序, 可用于参考不同的硬件外设API的使用方式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unified/m5unified_install_02.jpg" width="70%">


## M5Unified API

- [Button Class](/zh_CN/arduino/m5unified/button_class)
- [IMU Class](/zh_CN/arduino/m5unified/imu_class)
- [Mic Class](/zh_CN/arduino/m5unified/mic_class)
- [Power Class](/zh_CN/arduino/m5unified/button_class)
- [RTC8563 Class](/zh_CN/arduino/m5unified/power_class)
- [Speaker Class](/zh_CN/arduino/m5unified/speaker_class)
- [Touch Class](/zh_CN/arduino/m5unified/touch_class)


## 迁移说明

参考下方教程, 学习如何从其他M5Stack主控驱动库, 迁移使用M5Unified作为驱动。

- [M5Unified Migration](/zh_CN/arduino/m5unified/migration)

