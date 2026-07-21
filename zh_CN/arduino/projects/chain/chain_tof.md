# Chain ToF 使用教程

## 1.准备工作

- 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide) 完成 IDE 安装，并根据实际使用的开发板安装对应的板管理与需要的驱动库。
- 使用到的驱动库：
  - [M5Chain](https://github.com/m5stack/M5Chain)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_library.png" width="70%">

- 使用到的硬件产品：
  - [Chain DualKey](https://shop.m5stack.com/products/chain-dual-key-with-esp32-s3)
  - Chain 系列连接器，如 [Chain Bridge](https://shop.m5stack.com/products/chain-bridge-connector-for-chain-series) 或 [Chain Return](https://shop.m5stack.com/products/chain-return-connector-for-chain-series)
  - [Chain ToF](https://shop.m5stack.com/products/chain-tof-vl53l0)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_02.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1154/5.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_02.webp" width="20%">

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

uint16_t tof_distance;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("===========================");
  Serial.println("M5Stack Chain ToF Test");

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

  if (device_list->devices[0].device_type == CHAIN_TOF_TYPE_CODE) {
    Serial.println("ID[1] is Chain ToF\n");
    delay(1000);
  } else {
    Serial.println("ID[1] is NOT Chain ToF\n");
    return;
  }

  // Device ID, ToF measure mode (CONTINUOUS/SINGLE/STOP), operation status pointer
  M5Chain.setToFMeasureMode(1, CHAIN_TOF_MODE_SINGLE, &opr_status);
  // Device ID, ToF measure time (20-200 ms), operation status pointer
  M5Chain.setToFMeasureTime(1, 50, &opr_status);
}

void loop() {
  M5Chain.getToFDistance(1, &tof_distance);  // Device ID
  Serial.printf("tof_distance: %4d mm\n", tof_distance);  // 30 - 2000
  delay(200);
}
```

用 Chain Bridge 连接器连接主控 Chain DualKey 和 Chain ToF。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/tof_connect.jpg" width="50%">

将以上程序编译并上传至设备，点击 Arduino IDE 右上角的按钮打开串口监视器（Serial Monitor）。可以看到 Chain ToF 到遮挡物的距离（有效范围为 30 - 2000 mm）：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/Arduino_tof.png" width="90%">

## 3.参考链接

- [M5Chain Lib - GitHub](https://github.com/m5stack/M5Chain)
- [Chain 系列设备 Bus 通信](/zh_CN/arduino/projects/chain/chain_bus)