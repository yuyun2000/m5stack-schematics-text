# AtomS3U Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5AtomS3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/quickstart_arduino_atoms3u_select_board.png" width="70%" />

## 2. 下载模式

按住复位按键（大约2秒）直到内部绿色 LED 灯亮起, 便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/AtomS3U.gif" width="40%"/>

## 3. 端口选择

将设备通过 USB 接口连接至电脑，在设备进入下载模式后，Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/quickstart_arduino_atoms3u_selectport.png" width="70%" />

## 4. 程序编译 & 烧录

?>注意：|请设置 Arduino IDE 中 `Tools` -> `USB-CDC On Boot` 选项为 `Enabled`，否则无法使用串口，选项位置如下图。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/quickstart_arduino_atoms3u_USB_CDC.png" width="70%" />

打开 Arduino 粘贴下方所示代码，点击上传按钮，程序将编译并上传至 AtomS3U。

```cpp line-num
#include <M5Unified.h>

void setup() {
    M5.begin();
    Serial.begin(115200);    
}

void loop() {
    Serial.println("hello world!");
    delay(2000);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/quickstart_arduino_atoms3u_select_demoupload.png" width="70%" />

烧录成功后，打开串口监视器，将波特率设置为 115200，即可看到每隔 2 秒输出一次的 "hello world!"。

## 5. 相关资源

- **Arduino Library**
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- **Arduino API & Examples**
  - [Button](/zh_CN/arduino/m5atoms3u/button)
  - [IR NEC](/zh_CN/arduino/m5atoms3u/ir_nec)
  - [RGB LED](/zh_CN/arduino/m5atoms3u/rgb_led)
  - [MIC](/zh_CN/arduino/m5atoms3u/mic)