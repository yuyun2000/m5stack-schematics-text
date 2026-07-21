# DinMeter Arduino 示例程序编译与烧录 

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5DinMeter`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/quickstart_arduino_dinmeter_select_board.png" width="70%" />

- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`，`M5GFX`，`M5DinMeter`驱动库安装。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/quickstart_arduino_dinmeter_install_library_dinmeter.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/quickstart_arduino_dinmeter_install_library_GFX_and_Unified.png" width="70%" />

## 2.操作说明

#>开关机操作|开机：可通过按"WAKE"按钮，以及 RTC 定时触发的 IRQ 信号进行唤醒启动，在完成触发唤醒信号后，在程序初始化中需要设置 hold(G46)引脚为高电平(1)对电源进行维持，否则设备将重新进入休眠状态。<br/>关机：在无 USB 外部供电时，按 RST 按键实现，或者无 USB 外部供电时，在程序运行中设置 HOLD(GPIO46)=0，即实现断电关机。

#>下载模式|如果要进入下载模式，请在开机前按住 StampS3 上的 G0 按键，通电之后再松开。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5DinMeter/dinmeter%20(2).gif" width="30%" />

## 3.端口选择 & 配置

- 将设备通过USB线连接至电脑，在完成驱动安装后， Arduino IDE中可选中对应的控制板和设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/quickstart_arduino_dinmeter_select_port.png" width="70%">

## 4.程序编译&烧录

### Hello World

在Arduino IDE中新建程序，并粘贴下方Hello World案例代码，编译并烧录至设备，显示屏和串口监视器将显示"HelloWorld"!

```cpp line-num
#include <M5Unified.h>

//––– Adjust these to position your text –––
static const int16_t X_POS = 0;  // horizontal pixel offset
static const int16_t Y_POS = 60;  // vertical pixel offset

void setup() {
  auto cfg = M5.config();
  M5.begin(cfg);

  M5.Display.setTextSize(2);
  M5.Display.setCursor(X_POS, Y_POS);
  M5.Display.println("Hello World!");

  Serial.begin(115200);
  Serial.println("Hello World!!!");
}

void loop() {
  // nothing here
}

```

2.上传完成就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/K134_display.jpg" width="30%">


## 5.M5DinMeter 示例

- 在 Arduino IDE 中打开 M5DinMeter 库示例并进行烧录

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/quickstart_arduino_dinmeter_install_library_demo.png" width="70%">

## 6.相关资源

-  **Github**

   - [M5DinMeter](https://github.com/m5stack/M5DinMeter)
   - [M5Unified](https://github.com/m5stack/M5Unified)
   - [M5GFX](https://github.com/m5stack/M5GFX)
   

-  **Arduino API & Examples**

    - [Display](/zh_CN/arduino/m5dinmeter/display)
    - [Encoder](/zh_CN/arduino/m5dinmeter/encoder)
    - [Wakeup](/zh_CN/arduino/m5dinmeter/wakeup)
    - [Battery](/zh_CN/arduino/m5dinmeter/battery)
    - [RTC](/zh_CN/arduino/m5dinmeter/rtc)
    - [Buzzer](/zh_CN/arduino/m5dinmeter/buzzer)
    - [Wi-Fi](/zh_CN/arduino/m5dinmeter/wifi)
    - [Button](/zh_CN/arduino/m5dinmeter/button)