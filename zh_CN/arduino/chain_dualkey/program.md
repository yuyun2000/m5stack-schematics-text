# Chain DualKey Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE 安装：参考 [Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2.板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5ChainDualKey`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_board.png" width="70%">

- 3.驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`驱动库安装，并根据提示安装全部依赖库。

## 2.端口选择

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Download_mode.gif" width="50%">

将设备的开关拨到中间位置，按住 Key1（远离挂绳的按键）通过 USB-C 数据线连接至电脑，然后松开 Key1，设备进入下载模式，可在 Arduino IDE 中选择对应的主控和设备端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_port.png" width="70%">

## 3.程序编译&烧录

```cpp line-num
#include <M5Unified.h>
m5::Button_Class Key1;

void setup() {
  pinMode(0, INPUT);
  Serial.begin(115200);
}

void loop() {
  uint32_t ms = millis();
  Key1.setRawState(ms, !digitalRead(0));
  if (Key1.wasPressed()) {
    Serial.println("Key1 was pressed");
  }
  delay(10);
}
```

将以上程序复制到 Arduino IDE，点击上传按钮，待程序编译上传完成后，打开串口监视器。按下 Key1 时，设备会向串口发送一行文字：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_program.png" width="70%">

Chain DualKey 没有 reset 按键。上传程序之后若程序未运行，可以将开关拨至中间位置，断开 USB-C 数据线并重新连接（不要按住 Key1），让设备重启。

?> 注意事项 | 请勿将引脚 `SWITCH_1 (G8)`、`SWITCH_2 (G7)` 配置为输出高电平，否则将导致设备无法正常关断电源。

## 4.相关资源

- Arduino API & Examples
  - [BLE HID](/zh_CN/arduino/chain_dualkey/ble)
  - [Button](/zh_CN/arduino/chain_dualkey/button)
  - [Power](/zh_CN/arduino/chain_dualkey/power)
  - [RGB LED](/zh_CN/arduino/chain_dualkey/led)
  - [Switch](/zh_CN/arduino/chain_dualkey/switch)
  - [USB HID](/zh_CN/arduino/chain_dualkey/hid)