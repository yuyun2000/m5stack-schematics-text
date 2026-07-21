# Atomic QRCode2 Base Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：          

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5UnitQRCode](https://github.com/m5stack/M5Unit-QRCode/blob/main)

- 使用到的硬件产品：
  - [AtomS3R](https://shop.m5stack.com/products/atoms3r-ai-chatbot-kit-8mb-psram)
  - [Atomic QRCode2 Base](https://shop.m5stack.com/products/atomic-barcode-qr-code-scanner-2-base)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20QRCode2%20Base/img-a5bef961-6af5-4b7a-b7fa-92338c4fd305.webp" width="20%">

## 2. 案例程序

- 本教程中使用的主控设备为 AtomS3R ，搭配 Atomic QRCode2 Base。本扫码模块采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口 IO 为 `G5 (TX)`、`G6 (RX)`。

#>说明 | 1\. 本模块沿用同类产品驱动库，但`仅能通过串口控制`，不可使用 M5UnitQRCode 库中的 I2C 接口相关内容。  
2\. 下方例程默认为手动扫码模式，用户可通过按压主控设备屏幕来控制扫码解码`一次`；若使用自动扫码模式，可将程序中 `#define UART_AUTO_SCAN_MODE` 宏定义取消注释。  
3\. `setDecodeTrigger` 函数仅在手动扫码模式下有效，自动扫码模式下调用此函数无法控制扫码解码。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include "M5UnitQRCode.h"

M5Canvas canvas(&M5.Display);

M5UnitQRCodeUART qrcode;

// #define UART_AUTO_SCAN_MODE //Enabling this macro definition will automatically scan and decode the code.
#define UART_TX 5
#define UART_RX 6

void setup() {
    M5.begin();
    Serial.begin(115200);

    canvas.setColorDepth(16); 
    canvas.createSprite(M5.Display.width(), M5.Display.height());
    canvas.setFont(&fonts::efontCN_16);
    canvas.setTextScroll(true);

    while (!qrcode.begin(&Serial1, 115200, UART_TX, UART_RX)) {
        canvas.println("Init Fail");
        Serial.println("QRCode2 Init Fail");
        canvas.pushSprite(0, 0);
        delay(1000);
    }
    canvas.println("Init Success");
    Serial.println("QRCode2 Init Success");
#ifdef UART_AUTO_SCAN_MODE
    canvas.println("Auto Scan Mode");
    qrcode.setTriggerMode(AUTO_SCAN_MODE);
#else
    canvas.println("Manual Scan Mode");
    qrcode.setTriggerMode(MANUAL_SCAN_MODE);
#endif
    canvas.setTextColor(TFT_YELLOW);
    canvas.println("Press screen to\nstop/start scan");
    canvas.setTextColor(TFT_WHITE);
    canvas.pushSprite(0, 0);
}

void loop() {
    if (qrcode.available()) {
        String data     = qrcode.getDecodeData();
        uint16_t length = data.length();
        Serial.printf("len:%d\n", length);
        Serial.printf("decode data:");
        Serial.println(data);
        canvas.println("Decode data:");
        canvas.println(data);
        canvas.pushSprite(0, 0);
    }
    M5.update();
#ifndef UART_AUTO_SCAN_MODE
    if (M5.BtnA.wasPressed()) {
        qrcode.setDecodeTrigger(true); //Trigger scanning and decoding process once
    }
#endif
}
```

## 3. 编译上传

- 1\. 下载模式：不同设备进行程序烧录前需要下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- AtomS3R 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/536/Atomic_QRCode2_Base_arduino_example.png" width="70%">

## 4. 扫码效果展示

- 通过按压主控设备屏幕，可以控制扫码解码一次；扫描下方左边二维码，检测结果如下方右图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/M5Stack_QRCode.png" width="30%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/536/Atomic_QRCode2_Base_example.jpg" width="30%">

