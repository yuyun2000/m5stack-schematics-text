# CM4Stack UiFlow本地模式使用指南

## 注意事项

（截至2023年最新说明）
- 仅支持UiFlow 1.x版本（2023年起UIFlow.local基于1.x版本开发，不兼容UiFlow2）
- 截至2023年6月，该功能仍处于开发阶段，后续可能调整
- 本文以Windows系统为例进行说明

### 兼容设备列表

![支持设备图示](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_01.webp)

- Core系列 
- Fire
- StickC/StickC-Plus
- Atom-Lite/Atom-Matrix/AtomU
- Core2
- CoreInk
- Paper
- Stamp-Pico
- Tough
- Atom Display
- M5Station

### 不兼容设备

- CoreS3
- AtomS3/AtomS3-Lite/AtomS3U
- Stamp-S3

## 系统架构

CM4Stack作为广域网端服务器，通过有线网口连接无线路由器，运行UiFlow的客户端PC和M5Stack设备则接入该无线网络。

![系统架构图](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_02.webp)

## 硬件准备

需要以下设备搭建运行环境：
- CM4Stack（作为UIFlow.local服务器）
- 带有线网口的无线路由器（需设置为路由模式，WAN口连接CM4Stack）
- 网线（用于连接CM4Stack与路由器）

## 软件需求

### 镜像烧录电脑（Windows/Linux）

MacOS用户需自行编译RPIBOOT工具

必备软件：
- [RPIBOOT](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)（用于识别CM4Stack的eMMC存储）
- [Raspberry Pi 镜像工具](https://www.raspberrypi.com/software/)（用于写入UIFlow.local镜像）

### 客户端电脑

- M5Burner（用于给M5Stack设备刷写UiFlow固件）

## 软件安装指南

### RPIBOOT

按默认设置完成安装即可。

### Raspberry Pi 镜像工具

保持默认设置安装。

## 镜像烧录步骤

### ① 下载解压镜像文件

解压下载的ZIP压缩包，获取.img格式的镜像文件。

### ② 启动RPIBOOT

在开始菜单搜索运行RPIBOOT，启动后会出现以下提示：

![RPIBOOT启动界面](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_21.webp)

### ③ 连接CM4Stack

在设备断电状态下，长按左侧BOOT键的同时通过USB连接电脑，此时会识别出bootfs驱动器：
![设备连接示意图](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_22_cn.webp)

### ④ 使用Raspberry Pi 工具

#### 1. 选择系统镜像

- 主界面点击`Choose OS`。

![系统选择入口](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_23_cn.webp)

- 在弹出的对话框选择`Use custom image`。

![自定义镜像选项](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_24_cn.webp)

- 选择已下载的UIFlow.local镜像文件

![镜像选择界面](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_25_cn.webp)

#### 2. 选择存储设备

选择名为RPI-MSD-0001的存储设备（注意实际名称可能有所不同）：

![存储设备选择](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_26_cn.webp)

#### 3. 系统设置

点击右下角齿轮图标进行高级设置：

![设置入口](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_27.webp)

- 主机名：设置CM4Stack的设备名称
- SSH功能：启用远程管理（可设置密码或公钥认证）

![SSH设置](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_32_cn.webp)

- 账户密码：设置系统登录凭证（可选）

![账户设置](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_35_cn.webp)

- Wi-Fi配置：设置互联网接入Wi-Fi（注意：这是用于外网连接的Wi-Fi，若仅本地使用可不配置，但部分网络功能将受限）

![网络设置](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_31_cn.webp)

- 区域设置：配置时区和键盘布局

![区域设置](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_36_cn.webp)

#### 4. 开始烧录

完成设置后点击`Write`，确认对话框点击`Yes`开始写入：

![烧录过程](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_37_cn.webp)

![确认提示](https://static-cdn.m5stack.com/resource/docs/quick_start/cm4stack/uiflow_local_33_cn.webp)

## 路由器连接配置

用网线将CM4Stack的有线网口与无线路由器的WAN口相连。

### 路由器设置要点

（具体操作请参考路由器说明书）
- 必须设置为路由模式（桥接模式不可用）
- WAN口需启用DHCP自动获取（CM4Stack将作为上级DHCP服务器）
- 确保启用DHCP服务（M5Stack设备依赖DHCP获取IP）

## 客户端连接

- 运行UiFlow的电脑：接入同一无线路由器
- M5Stack设备：使用M5Burner刷写UiFlow固件后，配置连接该路由器

## 启动UiFlow

将M5Stack设备设为Wi-Fi模式并获取APIKey后，在客户端电脑访问``http://flow.m5stack.com``（注意是http协议），忽略安全警告即可进入UiFlow操作界面。