# Tab5 ESP32-C6 Wi-Fi 模组恢复出厂固件

\#>Wi-Fi 模组出厂固件 | Tab5 内置的 ESP32-C6 模组在出厂时默认烧录了 Wi-Fi SDIO 固件。若 Wi-Fi 出现工作异常或烧录了其他程序，可通过以下方式重新烧录还原 Wi-Fi 固件。

## 1. 准备工作

- [参考M5Burner教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具下载，并参考下图，下载对应的固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Restore_Factory_WiFi_Firmware_01.jpg" width="80%" />

## 2. 烧录工具

Tab5 的 PCB 板上预留了 ESP32-C6 模组的下载烧录接口，用户可以通过 USB-TTL 转接板进行固件烧录。本教程中使用到的 USB-TTL 转接板为 M5Stack 官方[ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)，与下载接口线序一致，可以非常方便的连接和烧录， 连接方式如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Restore_Factory_WiFi_Firmware_02.jpg" width="80%" />

## 3. 端口选择

将设备通过 USB 线连接至电脑，在设备进入下载模式后， M5Burner 中可选中对应设备的端口。 <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Restore_Factory_WiFi_Firmware_03.jpg" width="80%" />

## 4. 固件烧录

点击 Burn 开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Restore_Factory_WiFi_Firmware_04.jpg" width="80%" />
