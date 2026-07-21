# Hat RS485 Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库:

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 使用到的硬件产品:
  - [StickC-Plus2](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit)
  - [Hat RS485](https://shop.m5stack.com/products/m5stickc-rs485-hat-aoz1282ci)
  - [Shielded Twisted Pair Cable](https://shop.m5stack.com/products/24awg-4-core-shielded-twisted-pair-cable)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5StickC%20PLUS2/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-rs485/hat-rs485_cover_01.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/cable/24awg_cable/24awg_cable_cover_01.webp" width="20%">

## 2. 案例程序

\#> 案例说明 | Hat RS485 是一款兼容 M5StickC 的 RS485 转换器，内部集成 SP485EEN 芯片，主要由一个 RS485 自动收发电路和一个 DC-DC 降压电路组成（可将输入电压降压至 5V）。该产品用于将 TTL 信号转换为 RS485 信号，从而实现不同设备之间的通信。本案例将使用两个 StickC-Plus2、一对屏蔽双绞线以及两个 Hat RS485 模块进行连接。两个 Hat RS485 模块通过 TX 与 RX 接口相互发送数据，接收到的数据将在 StickC-Plus2 屏幕及电脑串口监视器上显示。

### 完整程序

```cpp line-num
#include <M5Unified.h>

void setup() {
  // Initializatization
  auto cfg = M5.config();
  M5.begin(cfg);
  // Serial2.begin(unsigned long baud, uint32_t config, int8_t rxPin, int8_t txPin, bool invert)
  Serial2.begin(9600, SERIAL_8N1, 26, 0);   // (RX: G26, TX: G0)
  Serial.begin(115200);

  // setup display
  M5.Display.setRotation(1);
  M5.Display.fillScreen(BLACK);
  M5.Display.setTextColor(ORANGE);
  M5.Display.setTextSize(2);
  M5.Display.setCursor(0, 10);
  M5.Display.println("RS485 message:");
}

void loop() {
  M5.update();
  if (M5.BtnA.wasClicked()) {     // Click StickC-Plus2 Button A to send data
    Serial.println("RST485 sent: Hello M5Stack!");
    Serial2.println("Hello M5Stack!");
  }
  if (Serial2.available()) {      // Received data and display on StickC-Plus2's screen
    char ch = Serial2.read();
    M5.Display.setTextColor(CYAN);
    M5.Display.setTextSize(2);
    M5.Display.print(ch);
  }
  delay(10);
}
```

## 3. 编译上传

1. 进入下载模式：不同的 Stick 设备进行程序烧录前需要安装对应的驱动程序，不同的主控设备使用的驱动与安装步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体设备对应的操作方式。

2. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/864/arduino_hat_rs485_example_01.png" width="70%">

3. 程序完成编译并上传至第一个 StickC 设备后，第二个 StickC 设备也需要上传同样的程序。

## 4.Hat RS485 互相发送数据显示

该程序将通过 Hat RS485 的 TX 和 RX 接口来互相发送数据（点按 StickC-Plus2 的 ButtonA 按键来发送数据），并在 StickC-Plus2 的屏幕和电脑的串口监视器打印数据：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/864/arduino_hat_rs485_example_02.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/864/arduino_hat_rs485_example_serial_03.png" width="70%">
