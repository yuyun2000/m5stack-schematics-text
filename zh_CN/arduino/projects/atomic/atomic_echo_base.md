# Atomic Voice Base Arduino 使用教程

## 1. 准备工作

- 1\. 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 2\. 使用到的驱动库:

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Atomic-EchoBase](https://github.com/m5stack/M5Atomic-EchoBase)

- 3\. 使用到的硬件产品:
  - [AtomS3R](https://shop.m5stack.com/products/atoms3r-dev-kit)
  - [Atomic Voice Base](https://shop.m5stack.com/products/atomic-echo-base-with-microphone-and-speaker?variant=45913005228289)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20Echo%20Base/3.webp" width="20%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/atomic/atomic_echo_base/atomic_echo_base_lib_01.png" width="70%">

## 2. 案例程序

参考[M5Atomic-EchoBase](https://github.com/m5stack/M5Atomic-EchoBase)中的`RecordPlay`案例程序。根据实际连接的设备，在程序中修改实际使用的 IO 信息。本教程中使用的主控设备为 AtomS3R, 使用的 IO 配置与 AtomS3 一致。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/atomic/atomic_echo_base/atomic_echo_base_example_01.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/atomic/atomic_echo_base/atomic_echo_base_example_02.jpg" width="70%">

?> 注意事项 | Atomic Voice Base 麦克风支持的采样率范围为 16KHz-64KHz, 初始化时需要配置有效的范围内。

### 初始化

```cpp line-num
// Initialize the EchoBase with ATOMS3 pinmap.
echobase.init(16000 /*Sample Rate*/, 38 /*I2C SDA*/, 39 /*I2C SCL*/, 7 /*I2S DIN*/, 6 /*I2S WS*/, 5 /*I2S DOUT*/,
              8 /*I2S BCK*/, Wire);

echobase.setSpeakerVolume(50);             // Set speaker volume to 50%.
echobase.setMicGain(ES8311_MIC_GAIN_6DB);  // Set microphone gain to 6dB.
```

### 录制与播放

```cpp line-num
// Recording
echobase.setMute(true);
delay(10);
echobase.record(buffer, RECORD_SIZE);  // Record audio into buffer.
delay(100);

// Playing
echobase.setMute(false);
delay(10);
echobase.play(buffer, RECORD_SIZE);  // Play audio from buffer.
delay(100);
```

### 完整程序

基于 M5Unified 和 M5GFX 添加基本的显示，和按键操作，实现按下按键，开始录制，完成后自动播放录音。

```cpp line-num
/*
 * SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 */

#include "M5Unified.h"
#include <Arduino.h>
#include <M5EchoBase.h>

#define RECORD_SIZE (1024 * 96)  // Define the size of the record buffer to 96KB.

M5EchoBase echobase(I2S_NUM_0);    // Create an instance of the M5EchoBase class.
static uint8_t *buffer = nullptr;  // Pointer to hold the audio buffer.

void setup()
{
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    Serial.begin(115200);

    // Initialize the EchoBase with ATOMS3 pinmap.
    echobase.init(16000 /*Sample Rate*/, 38 /*I2C SDA*/, 39 /*I2C SCL*/, 7 /*I2S DIN*/, 6 /*I2S WS*/, 5 /*I2S DOUT*/,
                  8 /*I2S BCK*/, Wire);

    // Initialize the EchoBase with ATOM pinmap.
    // echobase.init(16000 /*Sample Rate*/, 25 /*I2C SDA*/, 21 /*I2C SCL*/, 23 /*I2S DIN*/, 19 /*I2S WS*/, 22 /*I2S
    // DOUT*/, 33 /*I2S BCK*/, Wire);

    echobase.setSpeakerVolume(50);             // Set speaker volume to 50%.
    echobase.setMicGain(ES8311_MIC_GAIN_6DB);  // Set microphone gain to 6dB.

    buffer = (uint8_t *)malloc(RECORD_SIZE);  // Allocate memory for the record buffer.
    // Check if memory allocation was successful.
    if (buffer == nullptr) {
        // If memory allocation fails, enter an infinite loop.
        while (true) {
            M5.Display.println("Failed to allocate memory :(");
            Serial.println("Failed to allocate memory :(");
            delay(1000);
        }
    }

    Serial.println("EchoBase ready, start recording and playing!");
    M5.Display.println("Click! For Record and Play");
}

void loop()
{
    M5.update();
    if (M5.BtnA.wasClicked()) {
        M5.Display.fillScreen(BLACK);
        M5.Display.setCursor(0, 0);
        M5.Display.println("Recording");
        // Recording
        echobase.setMute(true);
        delay(10);
        echobase.record(buffer, RECORD_SIZE);  // Record audio into buffer.
        delay(100);

        M5.Display.println("Playing");
        // Playing
        echobase.setMute(false);
        delay(10);
        echobase.play(buffer, RECORD_SIZE);  // Play audio from buffer.
        delay(100);
        M5.Display.println("Done");
    }
}
```

## 3. 编译上传

- 1\. 下载模式：不同设备进行程序烧录前需要下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- AtomS3R 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/atomic/atomic_echo_base/atomic_echo_base_example_03.jpg" width="70%">

## 4. 录制与播放

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/atomic/atomic_echo_base/atomic_echo_base_record_01.jpg" width="40%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/atomic/atomic_echo_base/atomic_echo_base_record_02.png" width="40%">
