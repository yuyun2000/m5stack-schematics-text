# Tab5 ESP-IDF 出厂固件编译

本教程将介绍如何编译 Tab5 的默认出厂固件程序，用户可基于该固件进行二次开发。

## 1. 准备工作

1. 环境配置： 本教程基于 Ubuntu 操作系统搭建 ESP-IDF 开发环境，其他平台的编译环境搭建方式，具体请参考[ESP-IDF - ESP32-P4上手教程](https://docs.espressif.com/projects/esp-idf/en/v5.4.2/esp32p4/get-started/linux-macos-setup.html)。

\#>ESP-IDF 版本 | 本教程推荐使用 ESP-IDF 版本`v5.4.2`

2. 使用 git 版本管理工具拉取 esp-idf 项目，切换至指定分支并执行脚本安装相关工具链。

?> 注意事项 |`. ./export.sh`指令的`"."`与脚本之间有一个空格，该指令等同于`source ./export.sh`

```bash
git clone -b v5.4.2 --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh
. ./export.sh
```

3. 后续教程使用到的 idf.py 指令均依赖 ESP-IDF, 运行指令前需要在项目工程路径下调用 ESP-IDF 中`. ./export.sh`用于激活相关的环境变量。详细说明请参考[ESP-IDF - ESP32-P4上手教程](https://docs.espressif.com/projects/esp-idf/en/v5.4.2/esp32p4/get-started/linux-macos-setup.html)。

## 2.User Demo

1. 拉取 Tab5 出厂固件项目源码，放置到与 esp-idf 项目同级目录下。

```bash
git clone https://github.com/m5stack/M5Tab5-UserDemo.git
```

2. 进入 M5Tab5-UserDemo 项目文件夹，并通过 python 脚本拉取依赖库组件。执行该命令前请确保 PC 端已安装 python 开发环境。

```bash
cd M5Tab5-UserDemo
python ./fetch_repos.py
```

3. 在项目路径`M5Tab5-UserDemo`->`platforms`->`tab5`中，调用 esp-idf 项目中`export.sh`用于激活相关的环境变量。以下指令适用于 M5Tab5-UserDemo 项目文件夹与 esp-idf 处于同级目录，其他路径则需根据实际情况修改指令。

```bash
cd platforms/tab5
. ../../../esp-idf/export.sh
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_userdemo_01.jpg" width="70%">

## 3. 程序编译与烧录

Tab5 通过数据线连接至电脑，长按复位按键直至绿色指示灯开始快速闪烁，松开按键后，设备即进入下载模式，等待固件烧录。此时执行以下指令进行程序编译与烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/download_mode2.gif" width="40%">

```bash
idf.py flash
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_userdemo_02.jpg" width="70%">

## 4. 开始使用

完成烧录后，可点击屏幕各个区域，进行功能单元测试。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_userdemo_03.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_userdemo_04.png" width="70%">
