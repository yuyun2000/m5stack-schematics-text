# Unit CAM Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5UnitCAM`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_select_board.png" width="70%" />

## 2.USB 驱动安装

\#> 点击下方连接下载匹配操作系统的驱动程序。CP34X (适用于`CH9102`) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 3. 端口选择

将设备通过 USB 线连接至电脑，在完成驱动安装后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unitcam/quickstart_arduino_unitcam_select_port.png" width="70%" />

## 4. 程序编译 & 烧录

1\. 打开案例程序 “CameraWebServer”

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unitcam/quickstart_arduino_unitcam_select_demo.png" width="70%" />

2\. 选择摄像头模块**CAMERA_MODEL_M5STACK_UNITCAM**

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unitcam/quickstart_arduino_unitcam_select_model.png" width="70%" />

3\. 修改 Partition Scheme 为 Huge APP

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unitcam/quickstart_arduino_unitcam_select_hugeapp.png" width="70%" />

4\. 在代码中填入 WiFi 名称和密码

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unitcam/quickstart_arduino_unitcam_select_wifi.png" width="70%" />

5\. 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unitcam/quickstart_arduino_unitcam_upload.png" width="70%" />

## 5. 程序效果如下

1\. 打开串口，波特率调节至 115200，重新连接数据线进行复位，显示 WiFi 已连接，并将 IP 地址复制至浏览器，点击 Start Stream

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5unitcam/quickstart_arduino_unitcam_select_buad_and_ip.png" width="70%" />

2\. 效果如下

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/effect.png" width="70%" />
