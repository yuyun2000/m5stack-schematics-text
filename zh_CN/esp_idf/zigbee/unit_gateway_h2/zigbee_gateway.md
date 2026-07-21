# ESP Zigbee Gateway

本教程将介绍如何使用 Unit Gateway H2 搭配 CoreS3 主控运行 ESP Zigbee Gateway 案例程序。ESP Zigbee Gateway 是一个基于 ESP32 系列 Wi-Fi SoC 和 ESP32-H2 802.15.4 SoC 的网关设备。它可以将 Zigbee 网络与 Wi-Fi 网络连接起来，实现智能家居设备的互联互通。

## 1. 准备工作

- 1\. 环境配置： 参考[ESP-IDF - ESP32S3上手教程](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/index.html)完成基本编译环境。

\#>ESP-IDF 版本 | 该案例编译推荐使用 ESP-IDF 版本`v5.3.1`

```bash
git clone -b v5.3.1 --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh
. ./export.sh
```

- 2\. 使用 Git 指令`clone recursive`递归克隆 ESP-Zigbee-SDK 仓库

```bash
git clone --recursive https://github.com/espressif/esp-zigbee-sdk.git
cd esp-zigbee-sdk
```

- 3\. 使用到的硬件产品:
  - [Unit Gateway H2](https://shop.m5stack.com/products/esp32-h2-thread-zigbee-gateway-unit)
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_10.webp" width="20%">

- 4\. 后续教程使用到的 idf.py 指令均依赖 ESP-IDF, 运行指令前需要执行 ESP-IDF 中`. ./export.sh`用于激活相关的环境变量。详细说明请参考[ESP-IDF - ESP32S3上手教程](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/index.html)。

## 2. 编译 RCP 固件

- 1\. 在编译 Gateway 固件之前，需要先生成 RCP 固件。参考下方指令进入对应的 rcp 固件目录，设置编译 target 为`esp32h2`。

```bash
cd $IDF_PATH/examples/openthread/ot_rcp
idf.py set-target esp32h2
idf.py menuconfig
```

- 2\. 使用`idf.py menuconfig`进入配置页面。在 menuconfig 中配置：`Component config` -> `OpenThread RCP Example` - `Enable OPENTHREAD_NCP_VENDOR_HOOK`

\#> 波特率修改 | 由于芯片的引脚驱动能力等因素，使用长的连接线连接 Unit 时串口有可能无法正常工作，如遇到这种情况则需适当降速处理，此处将默认波特率 460800 降速为 230400。

- 3\. 修改波特率，打开 `main/esp_ot_config.h` ，将 43 行 `.baud_rate = 460800;` 修改为 `.baud_rate = 230400;`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_rcp_baudrate_change_01.png" width="50%">

- 4\. 完成配置后，执行以下指令进行 RCP 固件编译。

```bash
idf.py build
```

- 5\. 打开 Unit Gateway H2 外壳，按住设备 boot 按键，然后连接 USB 供电使其进入下载模式。并执行以下指令进行烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_download_mode1.gif" width="50%">

```bash
idf.py flash
```

## 3. 编译 Gateway 固件

- 1\. 进入`esp_zigbee_gateway`案例程序路径，设置编译对象。

```bash
cd esp-zigbee-sdk/examples/esp_zigbee_gateway
idf.py set-target esp32s3
idf.py menuconfig
```

- 2\. 并在 menuconfig 中配置正确的通信引脚，该引脚配置针对 CoreS3 主控，若使用其他的主控设备可根据实际情况进行修改。

```bash
- Board Configuration
  - Pin to RCP reset: -1
  - Pin to RCP boot: -1
  - Pin to RCP TX: 18
  - Pin to RCP RX: 17
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_zigbee_gateway_config_01.jpg" width="40%">

- 3.Gateway WiFi 连接配置

```bash
- Example Connection Configuration
  - WiFi SSID
  - WiFi Password
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_config_01.png" width="50%">

添加以下函数与头文件，并添加到 app_main 中开头进行调用初始化，打开 CoreS3 的 Grove 供电输出能力。

```cpp
#include "driver/i2c.h"

void fix_aw9523_p0_pull_up(void)
{
    /* AW9523 P0 is in push-pull mode */
    const i2c_config_t i2c_conf = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = GPIO_NUM_12,
        .sda_pullup_en = GPIO_PULLUP_DISABLE,
        .scl_io_num = GPIO_NUM_11,
        .scl_pullup_en = GPIO_PULLUP_DISABLE,
        .master.clk_speed = 400000
    };
    i2c_param_config(I2C_NUM_1, &i2c_conf);
    i2c_driver_install(I2C_NUM_1, i2c_conf.mode, 0, 0, 0);

    uint8_t data[2];
    data[0] = 0x11;
    data[1] = 0x10;
    i2c_master_write_to_device(I2C_NUM_1, 0x58, data, sizeof(data), 1000 / portTICK_PERIOD_MS);
    i2c_driver_delete(I2C_NUM_1);
}
```

### 4. 编译和烧录

```bash
idf.py build
idf.py erase_flash
idf.py flash
```

## 5. 开始运行

- 将 CoreS3 与 Unit Gateway H2 连接。
- 将 CoreS3 连接至电脑
- 通过`idf.py monitor`或其他的串口调试工具在 115200bps 配置下查看运行日志。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_unit_connect_01.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_zigbee_gateway_monitor_01.png" width="100%">

正常运行日志内容：

- RCP 固件版本检查
- Wi-Fi 连接成功
- Zigbee 网络创建成功
- 网络开放允许设备加入
