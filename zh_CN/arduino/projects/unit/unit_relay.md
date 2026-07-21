# Unit Relay Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Relay](https://shop.m5stack.com/products/mini-3a-relay-unit)


<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/relay/relay_cover_01.webp" width="20%">


## 2.案例程序

#>案例说明|Unit Relay是一款机械式继电器，提供了 `NC` ，`NO` ，`COM` 三个接口，能够帮助我们控制 `AC 220V@3A` / `DC 30V@3A` 线路的通断。使用时仅需配置 IO 高/低电平即可控制通断。当控制引脚输出低电平时 NO 与 COM 断开，NC 与 COM 导通。 控制引脚输出高电平时 NO 与 COM 导通，NC 与 COM 断开。


```cpp line-num
#include <M5Unified.h>

#define RELAY_PIN 9

bool relay_no_status = false;

void setup()
{
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, LOW);
    M5.Display.setCursor(10, 40);
    M5.Display.println("Relay NO & COM Open");
}

void loop(void)
{
    M5.update();
    auto t = M5.Touch.getDetail();

    if (t.wasClicked() || M5.BtnA.wasClicked()) {
        relay_no_status = !relay_no_status;
        if (relay_no_status) {
            M5.Display.clear();
            M5.Display.setCursor(10, 40);
            M5.Display.println("Relay NO & COM Closed");
            digitalWrite(RELAY_PIN, HIGH);
        } else {
            M5.Display.clear();
            M5.Display.setCursor(10, 40);
            M5.Display.println("Relay NO & COM Open");
            digitalWrite(RELAY_PIN, LOW);
        }
    }
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">


- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/784/unit_relay_example_01.jpg" width="70%">


## 4.开关控制

通过触屏可控制 Unit Relay 线路通断，进而实现负载供电控制。


<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/784/unit_relay_example_02.jpg" width="70%">
