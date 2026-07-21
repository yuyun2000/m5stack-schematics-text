# Unit UWB Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit_UWB](https://github.com/m5stack/M5Unit-UWB)

- 使用到的硬件产品：
  - [AtomS3](https://shop.m5stack.com/products/atoms3-dev-kit-w-0-85-inch-screen)
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit UWB](https://shop.m5stack.com/products/ultra-wideband-uwb-unit-indoor-positioning-module-dw1000)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/3.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_02.webp" width="20%"/>

## 2. 注意事项

?> 注意 | 该设备需要 2 个及以上才能实现测距或定位，如一个设备作 Tag 多个设备作 Anchor （想了解详细原理的可自行搜索）。

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/unit/uwb)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U100" type="UNIT"></ProductCompatible> 

## 3. 案例程序

- 本教程中使用的主控设备为一款 CoreS3 和两款 AtomS3 ，搭配三个 Unit UWB。本 Unit UWB 模块采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，CoreS3 和 AtomS3 与模块连接后对应的串口 IO 均为 `G1 (RX)`，`G2 (TX)`。

- 本 Unit UWB 模块例程在 Anchor 的设置部分提供了基站编号设置的枚举 `UWB_Anchor_num` ，用户根据实际需要修改函数 `setupmode()` 中的值即可（ Tag 模式下任意编号均可）。

- Tag 部分程序：

```cpp line-num
/*
 * SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 *
 *
 * @Hardwares: M5CoreS3 + Unit UWB
 * @Dependent Library:
 * M5Unified: https://github.com/m5stack/M5Unified
 * M5Unit_UWB: https://github.com/m5stack/M5Unit-UWB
 */
#include <M5Unified.h>
#include "M5_UWB.h"

M5_UWB Unit_UWB;
UWB_Mode        Unit_UWB_Mode   = UWB_Mode_Tag;
UWB_Anchor_num  Unit_UWB_Tag    = UWB_Anchor_0; // Select the anchor

bool Uwb_Init = 0;
uint8_t Tag_num       = 0;
uint8_t UI_Init_flag = 0;
void UWB_UI_display();

void setup(){
    M5.begin();
    Serial.begin(115200);
    Unit_UWB.begin(&Serial2, 22, 21, 115200);
    Uwb_Init = Unit_UWB.setupmode(Unit_UWB_Mode, Unit_UWB_Tag, (char *)"5"); // Set the UWB mode and distance value
    if(Uwb_Init){
        Serial.println("UWB Init Success");
    } else {
        Serial.println("UWB Init Failed");
    }
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    delay(100);
}

void loop(){
    Tag_num = Unit_UWB.readstring();
    UWB_UI_display();
    delay(100);
}

void UWB_UI_display(){
    if(UI_Init_flag == 0){
      M5.Display.fillScreen(WHITE);
      M5.Display.setCursor(0, 0);
      M5.Display.println("UWB Test");
      M5.Display.println("Tag Model, Distance: \r\n(uint: m)\r\n");
      UI_Init_flag = 1;
    }
    M5.Display.fillRect(0, 60, 340, 240, WHITE);
    M5.Display.setCursor(0, 60);
    M5.Display.print(Unit_UWB.DATA);
    Serial.println(Unit_UWB.DATA);
}
```

- Anchor 部分程序：

```cpp line-num
/*
 * SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 *
 *
 * @Hardwares: AtomS3 + Unit UWB
 * @Platform Version: Arduino M5Stack Board Manager v2.1.3
 * @Dependent Library:
 * M5Unified: https://github.com/m5stack/M5Unified
 * M5Unit_UWB: https://github.com/m5stack/M5Unit-UWB
 */
#include <M5Unified.h>
#include "M5_UWB.h"

M5_UWB Unit_UWB;
UWB_Mode Unit_UWB_Mode = UWB_Mode_Base;
UWB_Anchor_num Unit_UWB_Anchor = UWB_Anchor_1; // Select the anchor point

bool Uwb_Init = 0;
uint8_t Tag_num       = 0;
uint8_t UI_Init_flag = 0;
void UWB_UI_display();

const char* getAnchornNum(UWB_Anchor_num Num) {
    switch (Num) {
        case UWB_Anchor_0:      return "Base_0";
        case UWB_Anchor_1:      return "Base_1";
        case UWB_Anchor_2:      return "Base_2";
        case UWB_Anchor_3:      return "Base_3";
        case UWB_Anchor_4:      return "Base_4";
        default:                return "Unknown";
    }
}

void setup(){
    M5.begin();
    Serial.begin(115200);
    Unit_UWB.begin(&Serial2, 1, 2, 115200);
    Uwb_Init = Unit_UWB.setupmode(Unit_UWB_Mode, Unit_UWB_Anchor, (char *)"5"); // Set the UWB mode and distance value
    if(Uwb_Init){
        Serial.println("UWB Init Success");
    } else {
        Serial.println("UWB Init Failed");
    }
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    delay(100);
}

void loop(){
    Tag_num = Unit_UWB.readstring();
    UWB_UI_display();
    delay(100);
}

void UWB_UI_display(){
    if(UI_Init_flag == 0){
      M5.Display.fillScreen(WHITE);
      M5.Display.setCursor(0, 0);
      M5.Display.println("UWB Test");
      M5.Display.println("Base Model");
      const char * current_num = getAnchornNum(Unit_UWB_Anchor);
      M5.Display.printf("Anchor: %s", current_num);
      UI_Init_flag = 1;
    }
    M5.Display.setCursor(0, 80);
    M5.Display.print(Unit_UWB.DATA);
    Serial.println(Unit_UWB.DATA);
}
```

## 3. 编译上传

- 下载模式：不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考 [Arduino IDE上手教程](/zh_CN/arduino/arduino_ide) 页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3，AtomS3 的烧录方式一致：长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/download%20mode1.gif" width="30%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/module/module_gps_v2.0/module_gps_v2.0_example_02.jpg" width="70%">

## 4. 室内测距

- 这里分别将两个 AtomS3 连接 Unit UWB 模块作为 Anchor，一个 CoreS3 连接 Unit UWB 模块作为 Tag（需要注意的是 Anchor 和 Tag 之间的距离最好在 5 - 50m 左右）

- Tag 运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/845/Unit_UWB_Test_1.jpg" width="40%">

- Anchor 运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/845/Unit_UWB_Test_2.jpg" width="40%"/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/845/Unit_UWB_Test_3.jpg" width="40%"/>
