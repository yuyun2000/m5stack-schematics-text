# CM4Stack HA 镜像烧录教程

本教程将演示如何为 CM4Stack 烧录 Home Assistant 镜像，搭建智能家居控制中心。

## 1. 下载镜像文件

| 镜像版本                                | 下载链接                                                                                                                         |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 2024-03-06-CM4StackOS-haos_rpi4-64-12.1 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/cm4stack/cm4stack_images/hos/2024-03-06-CM4StackOS-haos_rpi4-64-12.1.7z) |

## 2. 烧录镜像

### Windows 环境下烧录

1\. 下载[Raspberry Pi Imager镜像烧录工具](https://www.raspberrypi.org/software/), 并完成安装。

2\. 下载[rpiboot.exe](https://raw.githubusercontent.com/raspberrypi/usbboot/master/win32/rpiboot_setup.exe)引导加载程序，并完成安装。

?> 文件下载注意事项 | rpiboot.exe 下载时可能会提示文件存在安全性问题，点击文件报告为安全后即可正常下载。

3\. 长按 CM4Stack 机身侧面的 BOOT 按钮，然后使用 USB 线将设备连接至电脑。注意：先按住 BOOT 按钮，再连接电脑供电。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_01.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_02.png" width="70%">

4\. 运行已经安装好的[rpiboot.exe](https://raw.githubusercontent.com/raspberrypi/usbboot/master/win32/rpiboot_setup.exe)引导程序。此时电脑将识别到新的磁盘设备。如果点击 rpiboot_setup.exe 文件未检查到 CM4Stack，可尝试更换数据线或重新操作上电流程。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_03.jpg" width="40%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_04.png" width="70%">

5\. 打开官⽅烧录软件 Raspberry Pi Imager，在系统选择中点击⾃定义系统，选择已经下载好的镜像文件，然后选中磁盘点击 NEXT，配置设备信息，开始进行烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_05.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_06.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_07.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_08.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_09.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_10.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_11.jpg" width="70%">

### linux 环境烧录

1.linux 环境需要手动编译 rpiboot 工具，你可以在其[rpiboot Github](https://github.com/raspberrypi/usbboot)获取源码。

```bash
sudo apt install git pkg-config make gcc libusb-1.0-0-dev

git clone --depth=1 https://github.com/raspberrypi/usbboot
cd usbboot
make
```

2\. 长按 CM4Stack 机身侧面的 BOOT 按钮，然后使用 USB 线将设备连接至电脑。注意：先按住 BOOT 按钮，再连接电脑供电。然后执行 rpiboot 程序。

```bash
sudo ./rpiboot
```

3\. 烧录系统可使⽤官⽅烧录软件[Raspberry Pi Imager Ubuntu](https://www.raspberrypi.com/software/)进⾏烧录，步骤和 Windows 下烧录操作⼀样。 也可以直接使⽤ dd 命令进⾏烧录镜像文件解压出来的.img。下⾯烧录命令仅供参考，请替换磁盘对象后进⾏使⽤。

```bash
sudo dd if=./2024-03-06-CM4StackOS-haos_rpi4-64-12.1.img of=/dev/sda bs=1M status=progress oflag=dsync
```

## 3. 启动系统

为 CM4Stack 连接供电和以太网，待启动后，设备屏幕将显示当前 IP, 同一局域网的其他设备可通过 IP:8123 访问 Home Assistant Dashboard 页面。
Home Assistant OS 首次启动需要通过网络获取资源文件，该步骤可能持续数十分钟，若出现长时间无法正常初始化的情况，可尝试更换配置了代理的网络环境。

```bash
http://xxx.xxx.xxx.xxx:8123/
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_12.png" width="30%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/cm4stack/cm4_ha_13.jpg" width="70%">

## video

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115489204342004&bvid=BV1TK16B6EHx&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/5sShI3w7YSQ?si=LoPv6bstZ7YnZBuq" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
