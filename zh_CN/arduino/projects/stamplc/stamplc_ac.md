# StamPLC AC Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5StamPLC](https://github.com/m5stack/M5StamPLC)

- 使用到的硬件产品：
  - [StamPLC](https://shop.m5stack.com/products/m5stamp-plc-controller-with-m5stamps3)
  - [StamPLC AC](https://shop.m5stack.com/products/ac-dc-power-supply-module-for-stamplc-12v-1a)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_04.webp" width="20%"/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_02.webp" width="20%"/>

## 2. 案例程序

- 本教程中使用的主控设备为 StamPLC，搭配 StamPLC AC。StamPLC AC 通过 I2C 的方式与主机通讯，集成的 RGB LED 和继电器开关由 IO 扩展芯片控制，请根据实际的电路连接修改程序中的引脚定义，设备连接后对应的 I2C IO 为 `G15 (SCL)`、`G13 (SDA)`，RGB LED IO 为 `P5 (SYS_LEDR)`、`P6 (SYS_LEDG)`、`P7 (SYS_LEDB)`，继电器开关 IO 为 `P2 (REL_EN)`。

实物连接组装如下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/stamplc_ac_connect.png" width="70%">

```cpp line-num
#include "M5StamPLC.h"

M5StamPLC_AC stamplc_ac;

void setup()
{
    /* Init M5StamPLC */
    M5StamPLC.begin();
    M5StamPLC.Display.setFont(&fonts::FreeMonoBold12pt7b);
    M5StamPLC.Display.drawCenterString("StamPLC AC", 120, 60);
    /* Init M5StamPLC-AC */
    while (!stamplc_ac.begin()) {
        printf("M5StamPLC-AC init failed, retry in 1s...\n");
        delay(1000);
    }
}

void loop()
{
    static bool relay_state = false;

    /* Toggle M5StamPLC-AC relay state */
    relay_state = !relay_state;
    stamplc_ac.writeRelay(relay_state);
    printf("Write M5StamPLC-AC Relay to %s\n", stamplc_ac.readRelay() ? "ON" : "OFF");
    if (relay_state)
    {
        stamplc_ac.setStatusLight(0, 1, 0);
        printf("Set M5StamPLC-AC status light to green\n");
    }
    else
    {
        stamplc_ac.setStatusLight(1, 0, 0);
        printf("Set M5StamPLC-AC status light to red\n");
    }
    delay(1000);
}
```

## 3.编译上传

- 长按 StamPLC 上的 Boot 按键, 等待红灯亮起后释放，此时设备进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_download_mode.gif" width="40%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/StamPLC_AC__arduino_example.png" width="70%">

## 4.继电器开关控制

- 上电后，StamPLC 会自动初始化 StamPLC AC 模块，并将继电器开关设置为断开状态，状态指示灯显示红色。随后每隔 1 秒钟，继电器开关会切换一次状态，同时状态指示灯颜色也会随之变化：当继电器闭合时，状态指示灯显示绿色，灯泡亮起；当继电器断开时，状态指示灯显示红色，灯泡熄灭。  

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/StamPLC_AC_example.mp4" type="video/mp4"></video>

串口监视器反馈如下所示：

```
Write M5StamPLC-AC Relay to ON
Set M5StamPLC-AC status light to green
Write M5StamPLC-AC Relay to OFF
Set M5StamPLC-AC status light to red
...
```