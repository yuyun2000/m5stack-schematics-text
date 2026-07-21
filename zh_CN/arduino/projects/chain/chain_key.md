# Chain Key 使用教程

## 1.准备工作

- 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide) 完成 IDE 安装，并根据实际使用的开发板安装对应的板管理与需要的驱动库。
- 使用到的驱动库：
  - [M5Chain](https://github.com/m5stack/M5Chain)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_library.png" width="70%">

- 使用到的硬件产品：
  - [Chain DualKey](https://shop.m5stack.com/products/chain-dual-key-with-esp32-s3)
  - Chain 系列连接器，如 [Chain Bridge](https://shop.m5stack.com/products/chain-bridge-connector-for-chain-series) 或 [Chain Return](https://shop.m5stack.com/products/chain-return-connector-for-chain-series)
  - [Chain Key](https://shop.m5stack.com/products/chain-mechanical-key-button-stm32g031)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_02.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1154/5.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-02.webp" width="20%">

## 2.示例程序

#> 编译要求 | M5Stack 板管理版本 >= 3.2.4<br>M5Chain 库版本 >= 1.0.0

```cpp line-num
#include "M5Chain.h"

#define RXD_PIN GPIO_NUM_5  // 47 for the other side of Chain DualKey
#define TXD_PIN GPIO_NUM_6  // 48 for the other side of Chain DualKey

Chain M5Chain;

device_list_t *device_list = NULL;
uint16_t device_count = 0;
uint8_t opr_status = 0;

uint8_t button_status;
chain_button_press_type_t button_press_type;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("===========================");
  Serial.println("M5Stack Chain Key Test");

  M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);
  while (!M5Chain.isDeviceConnected()) {
    Serial.println("No device connected");
    delay(1000);
  }

  M5Chain.getDeviceNum(&device_count);
  device_list = (device_list_t *)malloc(sizeof(device_list_t));
  device_list->count = device_count;
  device_list->devices = (device_info_t *)malloc(sizeof(device_info_t) * device_count);
  M5Chain.getDeviceList(device_list);

  if (device_list->devices[0].device_type == CHAIN_KEY_TYPE_CODE) {
    Serial.println("ID[1] is Chain Key");
  } else {
    Serial.println("ID[1] is NOT Chain Key");
    return;
  }

  // Device ID, double click interval (100MS/200MS/.../900MS/1000MS), long press interval (3S/4S/.../9S/10S), operation status
  M5Chain.setKeyButtonTriggerInterval(1, BUTTON_DOUBLE_CLICK_TIME_500MS, BUTTON_LONG_PRESS_TIME_5S, &opr_status);
  Serial.println("Set double and long press intervals\n");
  delay(1000);
}

void loop() {
  M5Chain.getKeyButtonStatus(1, &button_status);  // Device ID
  // Serial.print("button_status: ");
  // Serial.println(button_status);

  while (M5Chain.getKeyButtonPressStatus(1, &button_press_type)) {  // Device ID
    switch (button_press_type) {
      case CHAIN_BUTTON_PRESS_SINGLE:
        Serial.println("Single pressed");
        break;
      case CHAIN_BUTTON_PRESS_DOUBLE:
        Serial.println("Double pressed");
        break;
      case CHAIN_BUTTON_PRESS_LONG:
        Serial.println("Long pressed");
        break;
    }
  }
}
```

用 Chain Bridge 连接器连接主控 Chain DualKey 和 Chain Key。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/key_connect.jpg" width="50%">

将以上程序编译并上传至设备，打开串口监视器，程序会检测按键的按下事件（单击、双击、长按）并输出消息：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/Arduino_key.png" width="90%">

你还可以修改程序中的 `BUTTON_DOUBLE_CLICK_TIME_500MS`、`BUTTON_LONG_PRESS_TIME_5S` 为双击、长按事件设置不同的触发间隔时间。

## 3.参考链接

- [M5Chain Lib - GitHub](https://github.com/m5stack/M5Chain)
- [Chain 系列设备 Bus 通信](/zh_CN/arduino/projects/chain/chain_bus)