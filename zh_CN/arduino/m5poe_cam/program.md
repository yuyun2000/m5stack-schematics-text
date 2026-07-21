# Unit PoE CAM Arduino示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5PoECAM`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_select_board_01.jpg" width="70%">


- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5PoECAM`驱动库安装。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_lib_01.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_lib_02.jpg" width="70%">

- 4.使用到的硬件产品:
  - [ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)
  - [Unit PoE CAM-W v1.1](https://shop.m5stack.com/products/m5stack-poe-camera-with-wi-fi-ov3660)

>本教程适用于 Unit PoE CAM / Unit PoE CAM-W / Unit PoE CAM-W v1.1 设备。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_cover_01.webp" width="20%">


## 2.烧录工具

使用[ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)配套的转接板连接Unit PoE CAM-W v1.1预留的程序下载接口，参考下方步骤烧录固件程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_download_board_01.png" width="80%" />

## 3.端口选择

- 将设备通过USB线连接至电脑，Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_select_port_01.jpg" width="70%">

## 4.程序编译&烧录

- 打开驱动库中的案例程序"web_cam - eth", 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_eth_example_01.jpg" width="70%">

#>静态IP|如需设置静态IP，可参考注释内容进行配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_static_ip_01.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_static_ip_02.jpg" width="70%">

#>摄像头配置|由于不同的摄像头型号区分，摄像头成像的方向和支持的最大图像尺寸可能会有所不同。参考以下代码，在执行PoECAM.Camera.begin()后，根据需求配置图像旋转和镜像显示。

```cpp line-num
// for CAMERA_OV2640 ( Unit PoE CAM / Unit PoE CAM-W )
PoECAM.Camera.sensor->set_vflip(PoECAM.Camera.sensor, 0);
PoECAM.Camera.sensor->set_hmirror(PoECAM.Camera.sensor, 0);
PoECAM.Camera.sensor->set_framesize(PoECAM.Camera.sensor, FRAMESIZE_UXGA); //1600x1200
// for CAMERA_OV3660 ( Unit PoE CAM-W v1.1 )
PoECAM.Camera.sensor->set_vflip(PoECAM.Camera.sensor, 0);
PoECAM.Camera.sensor->set_hmirror(PoECAM.Camera.sensor, 1);
PoECAM.Camera.sensor->set_framesize(PoECAM.Camera.sensor, FRAMESIZE_QXGA); //2048x1536
```

连接串口工具后复位设备或重新上电，查看设备IP。通过浏览器访问IP实时预览图像。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_eth_example_02.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_arduino_eth_example_03.png" width="50%">


## 5.相关资源

- **Github**
  - [M5PoECAM Library](https://github.com/m5stack/M5PoECAM)

