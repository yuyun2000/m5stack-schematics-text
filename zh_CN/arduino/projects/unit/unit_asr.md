# Unit ASR Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-ASR](https://github.com/m5stack/M5Unit-ASR)

- 1.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit ASR](https://shop.m5stack.com/products/asr-unit-with-offline-voice-module-ci-03t)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U914_04.webp" width="20%">


## 2.案例程序

#>案例说明 | Unit ASR 支持语音唤醒与语音命令输入，并通过串口返回当前的语音指令信息。Unit ASR 默认固件中预置了一些命令词, 具体如下表所示。通过使用M5Unit-ASR我们能够非常方便的注册对应命令的回调函数，实现一些简单的语音命令控制。


### Turn On/Off

基于M5Unified和M5GFX添加基本的命令显示功能, 并添加`turn on`，`turn off`指令回调函数，模拟开关灯控制场景。


```cpp line-num
#include <M5Unified.h>
#include <unit_asr.hpp>

ASRUnit asr;

void turnOnHandler()
{
    Serial.println("turn on command received!");
    M5.Display.setCursor(0, 0);
    M5.Display.fillRect(0, 0, 320, 60, BLACK);
    M5.Display.println("turn on!");
}

void turnOffHandler()
{
    Serial.println("turn off command received!");
    M5.Display.setCursor(0, 0);
    M5.Display.fillRect(0, 0, 320, 60, BLACK);
    M5.Display.println("turn off!");
}

void wakeupHandler()
{
    Serial.println("Hi,M Five command received!");
    M5.Display.setCursor(0, 0);
    M5.Display.fillRect(0, 0, 320, 60, BLACK);
    M5.Display.println("wakeup!");
}

void setup()
{
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    Serial.begin(115200);
    asr.begin(&Serial1, 115200, 18, 17);
    asr.addCommandWord(0x14, "turn on", turnOnHandler);
    asr.addCommandWord(0x15, "turn off", turnOffHandler);
    asr.addCommandWord(0xFF, "Hi,M Five", wakeupHandler);
    M5.Display.setCursor(0, 0);
    M5.Display.fillRect(0, 0, 320, 60, BLACK);
    M5.Display.println("Say \"Hi,M Five\"\nto wakeup!");
}

void loop()
{
    M5.update();
    if (asr.update()) {
        Serial.println(asr.getCurrentCommandWord());
        Serial.println(asr.getCurrentCommandNum());
        Serial.println(asr.getCurrentRawMessage());
        Serial.println((asr.checkCurrentCommandHandler()));
    }
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/unit_asr_arduino_upload_01.jpg" width="70%">


## 4.命令交互

1. 使用 `Hi M Five`命令唤醒。
2. 回应 `I'm here`。
3. 使用 `Turn on` 命令，回应 `OK`。
4. 使用 `Turn off` 命令，回应 `OK`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/unit_asr_arduino_example_01.jpg" width="70%">


## 5.自定义命令

1. Unit ASR 支持通过重新生成固件来修改或添加新的交互命令，参考下方教程进行自定义指令固件生成与烧录。

- [Unit ASR 自定义固件生成与烧录](/zh_CN/guide/offline_voice/unit_asr/firmware)

2. 使用 Unit ASR 配置模板定义的自定义指令可通过M5Unit-ASR库进行添加和使用。例如在命令词汇中定义的参数指令为`AA 55 46 55 AA`, 其中指令码为 `0x46`。可参考下方案例程序进行指令添加与注册回调函数。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_08.jpg" width="80%">


```cpp line-num
#include <M5Unified.h>
#include <unit_asr.hpp>

ASRUnit asr;

void JustHandler()
{
    Serial.println("Just command received!");
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    asr.begin(&Serial1, 115200, 22, 21);
    asr.addCommandWord(0x46, "Just", JustHandler);
}


void loop()
{
    M5.update();
    if (asr.checkMessage()) {
        Serial.println(asr.getCurrentCommandWord());
        Serial.println(asr.getCurrentCommandNum());
        Serial.println(asr.getCurrentRawMessage());
        Serial.println((asr.checkCurrentCommandHandler()));
    }
}
```


1. Unit ASR 供电
2. 使用 `Hi M Five`命令唤醒，回应 `I'm here`。
3. 使用 `Just` 命令，回应 `Do it`。
4. `JustHandler`函数正常调用


```bash
Just command received!
Just
0x46
0xAA 0x55 0x46 0x55 0xAA 
1
```