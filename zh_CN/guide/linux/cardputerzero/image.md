# CardputerZero 镜像烧录指南

## 1. 准备工作

访问 [M5 Imager - Github Releases](https://github.com/CardputerZero/m5stack-imager)，根据操作系统下载对应版本的 M5 Imager 烧录工具。

## 2. 烧录与配置

1. 打开 M5 Imager 烧录工具。在设备列表中选择 `CardputerZero`，然后点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_01.png" width="60%">

2. 将 microSD 卡插入读卡器并连接至电脑，等待系统识别存储设备, 选择需要烧录的镜像版本。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_02.png" width="60%">

3. 选择目标存储设备。请确认所选设备正确，避免误擦除其他存储介质的数据。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_03.png" width="60%">

4. 根据需要配置用户名、密码以及 Wi-Fi 连接信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_04.png" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_05.png" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_06.png" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_07.png" width="60%">

5. 如需远程登录设备，可启用 SSH 连接功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_08.png" width="60%">

6. 确认配置无误后，开始烧录并等待流程完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_09.png" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_10.png" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_11.png" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_m5_imager_12.png" width="60%">

### USB 接口烧录 (不推荐)

?> 烧录速率 | 通过 USB 接口烧录的速度相对较慢，且 usbboot 在部分电脑可能存在兼容问题。如需提升烧录效率，强烈建议使用读卡器连接电脑进行烧录。

#### Rpiboot

安装 Rpiboot。该工具用于将 CardputerZero 模拟为磁盘，以便进行后续镜像烧录。由于部分版本存在兼容性问题，请参考下方提供的版本与 `commit` 信息，下载合适的 usbboot 版本。

#### For Windows

- 下载并安装 [rpiboot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)程序。

#### For Linux / MacOS

- Linux 系统，需要使用源码编译[rpiboot](https://github.com/raspberrypi/usbboot)工具。

```bash
# For Linux
# sudo apt install git libusb-1.0-0-dev pkg-config
# For MacOS
brew install libusb
brew install pkg-config
git clone https://github.com/raspberrypi/usbboot
cd usbboot
git checkout 61c482663c9b2a61ee86ba491f131ba4ca90e4ea
make
sudo ./rpiboot
```

1. 将 microSD 卡插入设备, 将 USB 接口切换开关拨至左侧，以启用机身右侧的 USB Type-C 接口。
2. 机身右侧的 USB Type-C 接口将设备连接至电脑，并打开 `rpiboot` 程序，进入识别等待。
3. 长按设备的 Boot 按键。
4. 保持按住 Boot 按键的同时，将电源开关拨至 `ON`，并在持续按住超过 5 秒后松开。
5. 等待 `rpiboot` 连接识别成功后，电脑端将识别到对应的存储设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_usb_download_01.png" width="80%">
