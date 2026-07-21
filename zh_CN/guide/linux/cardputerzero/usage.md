
# CardputerZero 快速上手

## 开关机

设备充电需要将电源开关拨至 ON 

## 键盘使用

### 功能键

- ESC/HOME:
- NEXT:

### 快捷键

- 屏幕亮度调整:
- 音量调整:

## 内置应用

出厂镜像预置的应用列表

### Wi-Fi 连接配置

### 摄像头

## 串口连接调试

## SSH 远程访问

## 网络配置

## 文件系统扩容

```bash
sudo raspi-config
# 选择 Advanced Options -> Expand Filesystem -> 重启
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_resize_fs_01.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_resize_fs_02.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_resize_fs_03.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_resize_fs_04.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_resize_fs_05.png" width="70%">

## USB 接口

### USB 2.0

CardputerZero 将 CM0 内部的 USB 接口资源，通过 USB Hub 集线器的方式进行了拓展。实现了多路 USB 接口，以太网接口功能。

机身左侧提供了一个 Host / Slave 物理切换开关。使用 Slave 模式时候将断开 USB Hub 芯片连接， 此时，左侧的 USB-A , USB Type-C 接口，以及顶部 EXT 2.54-14P 拓展总线的 HAT-P0/P1 USB 接口，以太网接口将无法使用。

- Slave 模式：
  - CM0 USB 连接至机身右侧 USB Type-C 接口
- Host 模式：
  - CM0 USB 连接至内部 USB Hub, 经过 USB Hub 进一步拓展出 4 路 USB 接口。
  - USB Hub 拓展出的 USB1 经过 USB-ETH 芯片拓展出以太网接口功能。
  - USB Hub 拓展出的 USB2 ~ 4 分别用于，USB-A , USB Type-C 接口，以及顶部 EXT 2.54-14P 拓展总线的 HAT-P0/P1 USB 接口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_usb_sch_01.png" width="70%">

## I2C/UART 接口

## EXT.CAP 接口
