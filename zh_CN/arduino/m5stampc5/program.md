# Stamp-C5 Arduino 示例程序编译与烧录

## 1. 准备工作

- 1\.Arduino IDE 安装：参考[Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。

- 2\.板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装，并选择开发板 `M5StampC5`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/quickstart_arduino_stamp-c5_select_board.png" width="70%" />

## 2. 端口选择

将 Stamp-C5 通过 USB 线连接至电脑，在 Arduino IDE 中选择对应设备端口。若端口未显示，请检查 USB 线是否支持数据传输，并确认系统已识别 USB CDC 串口设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/quickstart_arduino_stamp-c5_select_port.png" width="70%"/>

## 3. 程序编译 & 烧录

在 Arduino IDE 工作区输入下方代码，点击上传按钮，将自动进行程序编译与烧录。

```cpp line-num
void setup() {
    Serial.begin(115200);    
}

void loop() {
    Serial.println("hello world!");
    delay(2000);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/quickstart_arduino_stamp-c5_select_demoupload.png" width="70%" />

烧录成功后，打开串口监视器，将波特率设置为 115200，即可看到设备每隔 2 秒输出一次 "hello world!"。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/quickstart_arduino_stamp-c5_example.png" width="40%" />
