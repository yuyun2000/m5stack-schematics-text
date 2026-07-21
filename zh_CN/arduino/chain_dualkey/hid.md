# Chain DualKey USB HID

Chain DualKey USB HID 相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.4
- 开发板选项 = M5ChainDualKey
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include "USB.h"
#include "USBHIDKeyboard.h"
#include "USBHIDMouse.h"
#include "M5Unified.h"

#define pin_Key1 0
#define pin_Key2 17

m5::Button_Class Key1;
m5::Button_Class Key2;
USBHIDKeyboard Keyboard;
USBHIDMouse Mouse;

void setup() {
  pinMode(pin_Key1, INPUT);
  pinMode(pin_Key2, INPUT);

  Keyboard.begin();
  Mouse.begin();
  USB.begin();
}

void loop() {
  uint32_t ms = millis();
  Key1.setRawState(ms, !digitalRead(pin_Key1));
  Key2.setRawState(ms, !digitalRead(pin_Key2));

  if (Key1.wasPressed()) {
    // Keyboard.print("123 ABC def ,?#");
  }
  if (Key1.wasReleased()) {
    // Keyboard.write(KEY_RETURN);
  }
  if (Key1.wasHold()) {
    // Keyboard.press(KEY_LEFT_GUI);  // Command key in macOS, Windows key in Windows
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.press('c');
    delay(500);
    Keyboard.releaseAll();
  }

  if (Key2.wasPressed()) {
    Mouse.move(50, 50);  // x, y
  }
  if (Key2.wasHold()) {
    Mouse.click(MOUSE_RIGHT);
  }

  delay(10);
}
```

将以上代码复制到 Arduino IDE，编译并上传至 Chain DualKey。上传完成后，按住 Key1 将触发 `Ctrl + C` 组合键在 Windows 上复制（macOS 的 Command 键请看代码注释），按下 Key2 鼠标光标将向右下移动一段距离，按住 Key2 将触发鼠标右键单击。你也可以将代码中注释掉的部分取消注释，探索更多 USB HID 键盘功能（请注意不同按键触发条件与 USB HID 事件之间的逻辑冲突）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Keys.jpg" width="30%">

程序上传后若按键无反应，可以重启设备，操作方法是：将开关拨至中间位置，断开 USB-C 数据线并重新连接（不要按住 Key1）。

如果 Chain DualKey 已经被编程为 USB HID 设备，则上传新程序时需要让设备重新进入下载模式，操作方法是：断开 USB-C 数据线，将开关拨到中间位置，按住 Key1 重新连接 USB-C 数据线，然后松开 Key1。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Download_mode.gif" width="50%">

## API

Chain DualKey USB HID 部分使用了`arduino-esp32`自带的`USB`库，更多相关的 API 可以参考下方文档：

- [arduino-esp32 USB Lib - GitHub](https://github.com/espressif/arduino-esp32/tree/master/libraries/USB)
- [USB HID Keyboard functions & enums](https://github.com/espressif/arduino-esp32/blob/master/libraries/USB/src/USBHIDKeyboard.h)
- [USB HID Mouse functions & enums](https://github.com/espressif/arduino-esp32/blob/master/libraries/USB/src/USBHIDMouse.h)
- [USB - Espressif Docs](https://docs.espressif.com/projects/arduino-esp32/zh-cn/latest/api/usb.html)
