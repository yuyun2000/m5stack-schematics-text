# Unit PoE CAM-W v1.1 使用教程

>本教程将演示如何为 Unit PoE CAM-W v1.1 烧录 Web Camera 固件, 并实现局域网网页实时图像预览。本教程适用于 Unit PoE CAM / Unit PoE CAM-W / Unit PoE CAM-W v1.1 设备。

## 1.准备工作

- 1.使用到的硬件产品:
  - [ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)
  - [Unit PoE CAM-W v1.1](https://shop.m5stack.com/products/m5stack-poe-camera-with-wi-fi-ov3660)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_cover_01.webp" width="20%">

- 2.[参考M5Burner教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具下载, 并参考下图, 下载对应的固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_firmware_01.jpg" width="80%" />

## 2.固件烧录

使用[ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)配套的转接板连接 Unit PoE CAM-W v1.1 预留的程序下载接口，参考下方步骤烧录固件程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_download_board_01.png" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_firmware_02.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_firmware_03.jpg" width="80%" />

## 3.获取设备 IP

#>设备供电| Unit PoE CAM-W v1.1 可通过 Grove 接口 5V 供电或通过 PoE 交换机网线直接供电。当设备网络指示灯闪烁则代表网络工作正常。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_network_led_01.png" width="50%" />

通过 M5Burner 或其他串口工具，复位设备并查看设备 IP。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_serial_monitor_01.jpg" width="80%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_serial_monitor_02.jpg" width="80%" />

## 4.实时预览图片

同一局域网下，通过以下 URL 实时获取设备图像。

- Capture URL: `192.168.xxx.xxx`
- Stream URL: `192.168.xxx.xxx/stream`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_web_preview_01.png" width="50%" />

按下机身侧边按键，可切换图像分辨率。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_change_img_size_01.png" width="50%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_serial_monitor_03.png" width="80%" />
