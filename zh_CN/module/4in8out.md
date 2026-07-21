# Module13.2 4In8Out

<span class="product-sku">SKU:M122</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4in8out/4in8out_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4in8out/4in8out_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/969/M122-package-zheng.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/969/M122-package-fan.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4in8out/4in8out_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4in8out/4in8out_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4in8out/4in8out_06.webp">
</PictureViewer>

## 描述

**Module13.2 4In8Out** 是一款可堆叠的 **8 路 MOS 驱动输出 + 4 路无源接点输入** IO 扩展控制模块。它采用 STM32F030 作为 IO 扩展芯片，通过 I2C 协议通信，独立端口支持 9 ~ 24V DC 电源输入，集成 MP1584 DC-DC 电路可为主控设备提供 5V/3A 供电。8 路输出采用 AO3400A MOS 管，共电源阳极，能直接驱动负载，每路最大通断电流 1A；4 路输入为共地无源接点输入，**禁止接入有源信号或大于 5V 的信号**。模块通过 M5-Bus 接口与主控设备连接，支持堆叠扩展，适用于多通道负载驱动和限位开关、按键检测等应用场景。

## 产品特性

- STM32F030F4P6 主控芯片
- 8 路共电源正极 MOS 管驱动输出端口（AO3400A），能直接驱动负载，每路最大通断电流 1A
- 4 路共地无源输入端口，禁止接入**有源信号**或**大于5V**的信号
- 内置 MP1584 DC-DC 电路，可为主控设备提供 5V/3A 供电
- I2C 通信接口

## 包装内容

- 1 x Module13.2 4In8Out
- 13 x KF2EDGK-2.54-2P 接线端子

## 应用场景

- 多通道负载驱动 (继电器、气阀、单向电机、信号指示灯等)
- 限位开关
- 按键检测

## 规格参数

| 规格         | 参数                       |
| ------------ | -------------------------- |
| MCU          | STM32F030F4P6              |
| 通信接口     | I2C 通信 @ 0x45（可修改）  |
| 供电电压     | 9 ~ 24V                    |
| 输出通道     | 8 路                       |
| 输出电流     | 每路 ≤ 1A, 总电流不大于 8A |
| 输入通道     | 4 路                       |
| 通道接口规格 | KF2EDGR-2.54-2P            |
| 产品尺寸     | 54.0 x 54.0 x 19.7mm       |
| 产品重量     | 21.9g                      |
| 包装尺寸     | 80.0 x 55.0 x 28.0mm       |
| 毛重         | 52.5g                      |

## 操作说明

\#> 板载拨动开关的作用 | 下图红色框内是 boot0 的控制拨动开关，拨到 1 端拉高是刷写固件模式。拨到 0 端拉低是从闪存开始读取用户程序，即正常使用模式

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/4in8out/M5PPT%20(2).png" width="40%">

## 原理图

- [Module13.2 4In8Out 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/549/Sch_4IN8OUT.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/549/Sch_4IN8OUT_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN |
| ---- | ---- | ----- | --- |
| GND  | 1    | 2     |     |
| GND  | 3    | 4     |     |
| GND  | 5    | 6     |     |
|      | 7    | 8     |     |
|      | 9    | 10    |     |
|      | 11   | 12    | 3V3 |
|      | 13   | 14    |     |
|      | 15   | 16    |     |
| SDA  | 17   | 18    | SCL |
|      | 19   | 20    |     |
|      | 21   | 22    |     |
|      | 23   | 24    |     |
| HPWR | 25   | 26    |     |
| HPWR | 27   | 28    | 5V  |
| HPWR | 29   | 30    |     |
::

## 尺寸图

- [Module13.2 4In8Out 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/969/4in8out.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/969/4in8out_page_01.png" width="100%">

## 软件开发

### Arduino

- [Module13.2 4In8Out Arduino 库文件](https://github.com/m5stack/M5Module-4IN8OUT)

```cpp
#include <M5Unified.h>
#include "MODULE_4IN8OUT.h"

MODULE_4IN8OUT module;

void setup() {
    M5.begin(); 

    while (!module.begin(&M5.In_I2C, MODULE_4IN8OUT_ADDR)) {
        Serial.println("4IN8OUT INIT ERROR");
        M5.Lcd.println("4IN8OUT INIT ERROR");
        delay(1000);
    };
    Serial.println("4IN8OUT INIT SUCCESS");
    M5.Lcd.println("4IN8OUT INIT SUCCESS");
}

long interval = 0;
bool level    = false;

void loop() {
    for (uint8_t i = 0; i < 4; i++) {
        if (module.getInput(i) == 1) {
            M5.Lcd.fillRect(60 + 60 * i, 0, 25, 25, TFT_BLACK);
            M5.Lcd.fillRect(60 + 60 * i, 0, 25, 25, TFT_BLUE);
        } else {
            M5.Lcd.fillRect(60 + 60 * i, 0, 25, 25, TFT_BLACK);
            M5.Lcd.drawRect(60 + 60 * i, 0, 25, 25, TFT_BLUE);
        }
        M5.Lcd.drawString("IN" + String(i), 40 + 60 * i, 5);
    }
    M5.Lcd.drawString("4IN8OUT MODULE", 60, 80, 4);
    M5.Lcd.drawString("FW VERSION:" + String(module.getVersion()), 70, 120, 4);
    if (millis() - interval > 1000) {
        interval = millis();
        level    = !level;
        for (uint8_t i = 0; i < 8; i++) {
            module.setOutput(i, level);
            if (level) {
                M5.Lcd.fillRect(20 + 35 * i, 200, 25, 25, TFT_BLACK);
                M5.Lcd.fillRect(20 + 35 * i, 200, 25, 25, TFT_GREEN);
            } else {
                M5.Lcd.fillRect(20 + 35 * i, 200, 25, 25, TFT_BLACK);
                M5.Lcd.drawRect(20 + 35 * i, 200, 25, 25, TFT_GREEN);
            }
            M5.Lcd.drawString("OUT" + String(i), 18 + 35 * i, 180);
            delay(50);
        }
    }
    // if (M5.BtnB.wasPressed() || M5.Touch.getDetail().wasClicked()) {
    //     if (module.setDeviceAddr(0x66)) {
    //         Serial.println("Update Addr: 0x66");
    //     }
    // }
    // M5.update();
}
```

### UiFlow1

- [Module13.2 4In8Out UiFlow1 文档](/zh_CN/uiflow/blockly/module/4in8out)

### UiFlow2

- [Module13.2 4In8Out UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/4in8out.html)

### 通信协议

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4in8out/4in8out_sch_02.webp" width="100%">

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113580544361157&bvid=BV1yA6PYZEZQ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/g28O_zxvCm0?si=UlJ9RH5BKMrTwTe6" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
