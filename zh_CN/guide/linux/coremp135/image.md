# CoreMP135 镜像烧录

CoreMP135 套件目前提供了一些适配好的系统镜像，用户根据自己的需求选择自己的镜像进行下载，并解压获得 \*.img 文件。本教程将以烧录 buildroot 镜像为例，演示烧录，以及如何连接设备。

\#> 烧录镜像需要做的一些准备 |- CoreMP135<br/>- 镜像文件.img<br/>- microSD 卡<br/>- SD 卡读卡器<br/>- 镜像烧录工具[balenaEtcher](https://www.balena.io/etcher/)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/prepare_01.jpg" width="70%">

## 1. 下载镜像文件

| 镜像版本                        | 内核版本 | 下载链接                                                                                                             |
| ------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| M5_CoreMP135_buildroot_20240515 | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_buildroot_20240515.7z) |
| M5_CoreMP135_buildroot_20240628 | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_buildroot_20240628.7z) |
| M5_CoreMP135_debian12_20240515  | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_debian12_20240515.7z)  |
| M5_CoreMP135_debian12_20240628  | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_debian12_20240628.7z)  |
| M5_CoreMP135_debian12_20240919  | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_debian12_20240919.7z)  |

## 2. 烧录镜像

### Windows 环境下烧录

1\. 下载，并打开[balenaEtcher镜像烧录工具](https://www.balena.io/etcher/), 点击`Flash from file`选项载入镜像。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/balenaetcher_01.jpg" width="70%">

2\. 选择要上一步下载下来的 \*.img 镜像文件。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/balenaetcher_02.jpg" width="70%">

3\. 点击`Select target`，选择对应的 microSD 存储卡作为目标存储设备

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/balenaetcher_03.jpg" width="70%">

4\. 点击`Flash`按钮开始烧录

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/balenaetcher_04.jpg" width="70%">

5\. 工具提示 Flash Complete 时，表示镜像烧录完成，可以关闭烧录软件并取出 microSD 卡

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/balenaetcher_05.jpg" width="70%">

### linux 环境烧录

1.Linux 环境下可以直接通过 dd 指令进行写入，参考以下命令将`M5_CoreMP135_xxx.img`替换为实际镜像文件路径，将`/dev/sdbx`替换为实际设备

```shell
sudo dd if=M5_CoreMP135_xxx.img of=/dev/sdbx bs=1M status=progress oflag=dsync sync
```

## 3. 启动系统

1\. 将烧录了镜像的 microSD 插入开发板，然后通过`USB`或`12V DC`电源为整机供电。(注：电源供电能力建议`>2A`), 系统首次启动时会进行默认环境配置，也可能出现重启的现象，整个过程持续 45 秒左右，可以连接串口终端，观察启动 log。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/sd_card_01.jpg" width="50%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/boot_01.jpg" width="50%">

\#> 注意事项：上电时网口灯有微弱的亮光，启动到网卡驱动后，网口灯量度增加。可用判断是否启动到内核。上电时屏幕不亮，启动到屏幕时，屏幕背光亮起。可用来判断是否启动到内核。

## 4. 操作视频

<video width="600" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/coremp135_image.mp4" type="video/mp4">
</video>
