# Stamp-P4 Arduino 示例程序编译与烧录

## 1. 准备工作

- 1\.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2\.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5StampP4`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/quickstart_arduino_stamp-p4_select_board.png" width="70%" />

## 2. 端口选择

将设备通过 USB 线连接至电脑, Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/quickstart_arduino_stamp-p4_select_port.png" width="70%"/>

## 3. 程序编译 & 烧录

在 Arduino IDE 工作区输入下方代码, 点击上传按钮，将自动进行程序编译与烧录。

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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/quickstart_arduino_stamp-p4_select_demoupload.png" width="70%" />

烧录成功后，打开串口监视器，将波特率设置为 115200，即可看到每隔 2 秒输出一次的 "hello world!"。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/quickstart_arduino_stamp-p4_example.png" width="40%" />

 