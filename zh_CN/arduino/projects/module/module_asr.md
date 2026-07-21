# Module ASR Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-ASR](https://github.com/m5stack/M5Unit-ASR)

- 3.使用到的硬件产品:
  - [CoreS3-SE](https://shop.m5stack.com/products/m5stack-cores3-se-iot-controller-w-o-battery-bottom?variant=45170957451521)
  - [Module ASR](https://shop.m5stack.com/products/m5stack-asr-module-ci1302)
  - [Unit Dual Button](https://shop.m5stack.com/products/mini-dual-button-unit)
  - [Grove to 4P](https://shop.m5stack.com/products/connector-grove-to-4-pin-10pcs)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CORES3%20SE/3.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_02.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dual_button/dual_button_cover_01.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/converter/grove_to_4p/grove_to_4p_cover_01.webp" width="20%">

## 2.注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/module/Module_ASR)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="M147" type="MODULE"></ProductCompatible>

## 3.案例程序

- 本教程中使用的主控设备为 CoreS3-SE ，搭配 Module ASR 实现语音交互。使用前请参考下图，将引脚拨码开关，切换到指定位置。

### 3.1 引脚拨码开关

Module ASR 采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口 IO 为 `G18 (RX)`，`G17 (TX)`，实物引脚拨码开关位置如下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_dip_switch.png" width="50%">

### 3.2 IO 端口

- Module ASR 具有 5 路 IO 端口，可通过语音命令控制对应 IO 输出高低电平或通过 IO 输入触发特定语音回应，IO 端口如下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_GPIO_output.jpg" width="50%">

### 3.3 程序代码

Module ASR 支持语音、串口唤醒与命令输入，并通过语音及串口返回当前的相关指令信息。Module ASR 默认固件中预置了一些命令词, 不局限于下方的 `turn off` 等命令，具体请见 [Module ASR 出厂预设命令](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_Command.pdf)。

```cpp line-num
#include <M5Unified.h>
#include <unit_asr.hpp>

ASRUnit asr;

void turnOnHandler()
{
    Serial.println("turn on command received!");
    M5.Display.clear();
    M5.Display.drawCenterString("turn off!", 160, 110);
}

void turnOffHandler()
{
    Serial.println("turn off command received!");
    M5.Display.clear();
    M5.Display.drawCenterString("turn off!", 160, 110);
}

void wakeupHandler()
{
    Serial.println("wakeup command received!");
    M5.Display.clear();
    M5.Display.drawCenterString("wakeup!", 160, 110);
}

void PA2_HighHandler()
{
    Serial.println("set PA2 level to high");
    M5.Display.clear(TFT_GREEN);
    M5.Display.drawCenterString("PA2 level: high", 160, 110);
}

void PA2_LowHandler()
{
    Serial.println("set PA2 level to low");
    M5.Display.clear(TFT_YELLOW);
    M5.Display.drawCenterString("PA2 level: low", 160, 110);
}

void AddHandler()
{
    Serial.println("Add command received!");
    M5.Display.clear();
    M5.Display.drawCenterString("Add", 160, 110);
}

void PA4_InputHandler()
{
    Serial.println("PA4 key pressed");
    M5.Display.clear();
    M5.Display.drawCenterString("PA4 key pressed", 160, 110);
}

void setup()
{
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    Serial.begin(115200);
    asr.begin(&Serial1, 115200, 18, 17);
    asr.addCommandWord(0x14, "turn on", turnOnHandler);
    asr.addCommandWord(0x15, "turn off", turnOffHandler);
    asr.addCommandWord(0x31, "Hi,ASR", wakeupHandler);
    asr.addCommandWord(0x32, "hello", wakeupHandler);
    asr.addCommandWord(0x50, "PA2 high level", PA2_HighHandler);
    asr.addCommandWord(0x51, "PA2 low level", PA2_LowHandler);
    asr.addCommandWord(0xFF, "Hi,M Five", wakeupHandler);
    asr.addCommandWord(0x33, "Add", AddHandler);
    asr.addCommandWord(0x5B, "PA4 input", PA4_InputHandler);
    asr.printCommandList();
    M5.Display.clear();
    M5.Display.drawCenterString("Say", 160, 60);
    M5.Display.drawCenterString("\"Hi,M Five\"", 160, 80);
    M5.Display.drawCenterString("\"Hello\"", 160, 100);
    M5.Display.drawCenterString("\"Hi,ASR\"", 160, 120);
    M5.Display.drawCenterString("to wakeup!", 160, 140);
}

void loop()
{
    M5.update();
    if (asr.update()) {
        Serial.println(asr.getCurrentCommandWord());
        Serial.printf("0x%X\n", asr.getCurrentCommandNum());
        Serial.println(asr.getCurrentRawMessage());
        Serial.println((asr.checkCurrentCommandHandler()));
    }
}
```

### 3.4 自定义命令设置

- **Module ASR 仅能通过重新生成固件来修改或添加新的交互命令**，请参考教程 [Module ASR 自定义固件生成与烧录](/zh_CN/guide/offline_voice/module_asr/firmware) 进行自定义指令固件生成与烧录。

- 上方例程中在自定义语音命令词汇 `Add` 的参数指令为`AA 55 33 55 AA`，其中指令码为 `0x33`，固件配置信息如下图所示，例程中使用 `addCommandWord` 函数将指令加入指令表中与注册回调函数。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_7.png" width="80%">

- 上方例程中 `PA4 input` 为自定义命令，参数指令为 `AA 55 5B 55 AA`，其中指令码为 `0x5B`，固件配置需要在 `Pin脚配置` 中设置 `GPIO_A4` 为 `输入模式`，详细信息如下图所示，例程中使用 `addCommandWord` 函数将指令加入指令表中与注册回调函数。 

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_io_input_1.png" width="80%">  
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_io_input_2.png" width="80%">  
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_io_input_3.png" width="80%">

## 4.编译上传

- 1\. 进入下载模式：CoreS3-SE 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

#> 说明| 不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128_SE_Download_Mode.gif" width="30%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_example.png" width="70%">

## 5.命令交互

- 唤醒操作  
上电后，主控屏幕显示如下方左图所示，语音使用 `Hi M Five`命令唤醒，模块回应 `I'm here`，主控屏幕显示如下方右图所示。  

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_wakeup_prompt.jpg" width="30%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_wakeup.jpg" width="30%">  

串口监视器反馈如下所示：

```
wakeup command received!
Hi,M Five
0xFF
0xAA 0x55 0xFF 0x55 0xAA 
1
```

- 预设命令交互  
1\. 语音使用 `Turn on` 命令，模块回应 `OK`，主控屏幕显示 `turn on!`。  
2\. 语音使用 `Turn off` 命令，模块回应 `OK`，主控屏幕显示 `turn off!`。  

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_turn_on.jpg" width="30%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_turn_off.jpg" width="30%">  

串口监视器反馈如下所示：  

```
turn on command received!
turn on
0x46
0xAA 0x55 0x14 0x55 0xAA 
1
turn on command received!
turn on
0x46
0xAA 0x55 0x15 0x55 0xAA 
1
```

- IO 控制命令交互  
1\. 语音使用 `PA2 high level` 命令，模块回应 `PA2 high level`，主控屏幕显示 `PA2 level: high` 并且背景色变为绿色，PA2 输出高电平，LED 灯亮。  
2\. 语音使用 `PA2 low level` 命令，模块回应 `PA2 low level`，主控屏幕显示 `PA2 level: low` 并且背景色变为黄色， PA2 输出低电平，LED 灯灭。  
3\. 按动 Unit Dual Button 的 B 键(红色按键)，模块回应 `PA4 key pressed`，主控屏幕显示 `PA4 key pressed`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_high.jpg" width="30%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_low.jpg" width="30%">  
<video style="width:40vw;max-width:30%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_pa4_input.mp4" type="video/mp4"></video>

串口监视器反馈如下所示：  

```
set PA2 level to high
PA2 high level
0x50
0xAA 0x55 0x50 0x55 0xAA 
1
set PA2 level to low
PA2 low level
0x51
0xAA 0x55 0x51 0x55 0xAA 
1
PA4 key pressed
PA4 input
0x5B
0xAA 0x55 0x5B 0x55 0xAA 
1
```

- 自定义命令交互  
语音使用 `Add` 命令，模块回应 `Add successfully`，主控屏幕显示 `Add successfully!`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_arduino_add.jpg" width="30%">  

串口监视器反馈如下所示：  

```
Add command received!
Add
0x33
0xAA 0x55 0x33 0x55 0xAA 
1
```

