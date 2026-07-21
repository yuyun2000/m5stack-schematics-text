# CM4Stack Raspberry Pi OS

## 1.CM4Stack镜像

| Image Version                                                  | Download Link                                                                                                                                              |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2023-03-08-CM4StackOS-canary-2023-02-21-raspios-bullseye-armhf | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/cm4stack/cm4stack_images/canary/2023-03-08-CM4StackOS-canary-2023-02-21-raspios-bullseye-armhf.gz) |
| 2023-02-21-CM4StackOS-raspberry-bullseye-arm64                 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/cm4stack/cm4stack_images/canary/2023-02-21-CM4StackOS-raspberry-bullseye-arm64.7z)                 |

## 2.烧录工具

访问[Raspberrypi官网](https://www.raspberrypi.org/software/)下载对应系统版本的Raspberry Pi Imager烧录工具，并根据操作系统的类型进行安装。 

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/CM4STACK/Raspberry%20image.webp" width="60%">

## 3.Rpiboot

该工具用于将CM4模拟为磁盘, 用于后续的镜像烧录。

### For Windows

- 下载并安装 [rpiboot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)程序。
  
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CM4Stack/7304aa21caaabf125aae42b96851ea7.png" width="30%">

### For Linux

- Linux系统，需要使用源码编译[rpiboot](https://github.com/raspberrypi/usbboot)工具。

```bash
sudo apt install git libusb-1.0-0-dev pkg-config
git clone --depth=1 https://github.com/raspberrypi/usbboot
cd usbboot
make
sudo ./rpiboot
```


## 4.镜像烧录

### For Windows

- 1.保持长按设备上的BOOT按钮, 然后使用USB线将设备连接至电脑。
- 2.在电脑端找到已经安装好的 `rpiboot.exe` 程序双击运行, 等待电脑提示新磁盘设备。
- 3.打开烧录软件 `Raspberry Pi Imager`，在系统选择中点击自定义系统，选中上面获取到的镜像，然后选中磁盘，进行烧录。耐心等待烧录完成即可。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/CM4STACK/s2.webp" width="60%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/CM4STACK/s3.webp" width="60%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/CM4STACK/s4.webp" width="60%">

- 4.重新上电，等待进入系统。

### For Linux

- 1.保持长按设备上的BOOT按钮, 然后使用USB线将设备连接至电脑。
- 2.使用命令`sudo ./rpiboot`运行先前编译好的rpiboot工具, 等待电脑提示新磁盘设备。
- 3.打开烧录软件 `Raspberry Pi Imager`，在系统选择中点击自定义系统，选中上面获取到的镜像，然后选中磁盘，进行烧录。耐心等待烧录完成即可。
- 4.重新上电，等待进入系统。
 

## 5.初始化设置

启动CM4Stack后，首次登录系统需要进行初始化设置。可以通过SSH或高分辨率多媒体信号接口连接进行操作。根据页面提示依次设置用户名、密码、网络连接、语言等参数。完成初始化后，即可开始使用CM4Stack。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/CM4STACK/Raspberry1.webp" width="60%">

