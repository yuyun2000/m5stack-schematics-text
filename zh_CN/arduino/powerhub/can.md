# PowerHub CAN

PowerHub CAN 通信相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5PowerHub

```cpp line-num
#include <Arduino.h>
#include "driver/twai.h"

const gpio_num_t MCU_CAN_TXD = GPIO_NUM_39;
const gpio_num_t MCU_CAN_RXD = GPIO_NUM_40;

void setup() {
  Serial.begin(115200);

  twai_general_config_t g_config = TWAI_GENERAL_CONFIG_DEFAULT(MCU_CAN_TXD, MCU_CAN_RXD, TWAI_MODE_NORMAL);
  twai_timing_config_t t_config = TWAI_TIMING_CONFIG_500KBITS();
  twai_filter_config_t f_config = TWAI_FILTER_CONFIG_ACCEPT_ALL();

  if (twai_driver_install(&g_config, &t_config, &f_config) == ESP_OK && twai_start() == ESP_OK) {
    Serial.println("\nCAN ready. ");
  } else {
    Serial.println("\nCAN init failed. ");
    while (1) delay(1000);
  }
}

void loop() {
  // transmit
  twai_message_t tx_msg = {};
  tx_msg.extd = 0;            // 0 = standard frame, 1 = extended frame
  tx_msg.identifier = 0x123;  // 11-bit standard ID, change it on another device
  tx_msg.data_length_code = 2;
  tx_msg.data[0] = 0xAA;  // change it on another device
  tx_msg.data[1] = 0xBB;  // change it on another device

  if (twai_transmit(&tx_msg, pdMS_TO_TICKS(100)) == ESP_OK) {
    Serial.println("TX OK");
  } else {
    Serial.println("TX failed");
  }

  // receive (non-blocking)
  twai_message_t rx_msg;
  if (twai_receive(&rx_msg, pdMS_TO_TICKS(10)) == ESP_OK) {
    Serial.print("RX: ");
    for (int i = 0; i < rx_msg.data_length_code; i++) Serial.printf("%02X ", rx_msg.data[i]);
    Serial.printf("(ext=%d, id=0x%X, dlc=%d)", rx_msg.extd, rx_msg.identifier, rx_msg.data_length_code);
    Serial.println();
  }

  delay(2000);
}
```

准备两个 PowerHub，刷入以上代码（可修改消息 ID、内容以作区分），将两者的 120 Ω 终端匹配电阻开关置于 ON，然后用 XT30(2+2)-F 接口的连接线（比如 [PwrCAN Cable](/zh_CN/accessory/PwrCAN%20Cable)）连接两个设备的 CAN 接口：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_CAN.jpeg" width="50%">

连接后，两个 PowerHub 将互相通过 CAN 发送消息。将其中一个连接到电脑，观察串口输出：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_CAN_output.png" width="90%">

## API

PowerHub CAN 通信部分驱动使用了`ESP-IDF`中的`TWAI`，更多相关的 API 可以参考下方文档：

- [TWAI - Espressif Docs English](https://docs.espressif.com/projects/esp-idf/en/v5.4.3/esp32s3/api-reference/peripherals/twai.html)
- [TWAI - Espressif Docs 中文](https://docs.espressif.com/projects/esp-idf/zh_CN/v5.4.3/esp32s3/api-reference/peripherals/twai.html)