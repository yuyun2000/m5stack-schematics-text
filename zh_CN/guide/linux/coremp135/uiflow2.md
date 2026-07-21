# CoreMP135 UiFlow2 快速上手

## 1. 准备工作

- CoreMP135 供电电源 (DC 12V 电源或 Type-C 5V 输入)
- CoreMP135 通过网线接入网络
- CoreMP135 需完成最新版本**debian**镜像烧录，该步骤可参考[CoreMP135镜像烧录教程](/zh_CN/guide/linux/coremp135/image)
- 使用[putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)工具通过串口访问设备终端，并开启 debian root ssh 访问权限，该步骤可参考[CoreMP135开发教程](/zh_CN/guide/linux/coremp135/develop#6.串口连接)
- 为 CoreMP135 设备的 microSD 卡重新分区扩容，该步骤可[CoreMP135分区扩容教程](/zh_CN/guide/linux/coremp135/fdisk)

## 2. 下载系统依赖包

- 通过串口或 ssh 连接设备进入终端，执行以下指令下载系统依赖包（该步骤需依赖网络）。

```bash
apt update
apt install -y python3-pip libportaudio2
```

## 3. 安装 UiFlow2 Python library

\#>CoreMP135-UiFlow2 软件包 | CoreMP135-UiFlow2 软件包是一个为 CoreMP135 UiFlow2 准备的 Python 3.11 第三方库，用于运行由 UiFlow2 生成的代码。该库包含一个可直接执行的 UiFlow2 命令行工具，用于启动 / 停止后台服务。后台服务将连接到 UiFlow2 的服务器以接收命令。

- 通过 pip 包管理器下载[UiFlow2](https://pypi.org/project/uiflow2/)软件包，由于 Debian 12 系统中的 pip 启用了系统保护功能，参考以下指令，添加`--break-system-packages` 标志来安装软件包（该步骤需依赖网络）。

```bash
pip install uiflow2 --break-system-packages
```

- 测试是否安装成功，可以看到 pip 安装包列表中已经存在 uiflow2。

```bash
pip list
```

```bash
Package            Version
------------------ ---------
certifi            2025.1.31
charset-normalizer 3.4.1
distro             1.8.0
evdev              1.9.1
idna               3.10
paho-mqtt          2.1.0
pip                23.0.1
PyAudio            0.2.14
pyserial           3.5
requests           2.32.3
setuptools         66.1.1
smbus2             0.5.0
uiflow2            0.0.1
urllib3            2.3.0
wheel              0.38.4
```

- 如果网络异常，下载缓慢等情况，可尝试更换以下镜像源。参考以下指令备份原有软件源信息，然后重新写入镜像源信息。

```bash
mv /etc/apt/sources.list /etc/apt/sources.list.backup
```

```bash
vim /etc/apt/sources.list
```

```bash
deb https://mirrors.ustc.edu.cn/debian/ bookworm main non-free non-free-firmware contrib
deb-src https://mirrors.ustc.edu.cn/debian/ bookworm main non-free non-free-firmware contrib
deb https://mirrors.ustc.edu.cn/debian-security/ bookworm-security main
deb-src https://mirrors.ustc.edu.cn/debian-security/ bookworm-security main
deb https://mirrors.ustc.edu.cn/debian/ bookworm-updates main non-free non-free-firmware contrib
deb-src https://mirrors.ustc.edu.cn/debian/ bookworm-updates main non-free non-free-firmware contrib
deb https://mirrors.ustc.edu.cn/debian/ bookworm-backports main non-free non-free-firmware contrib
deb-src https://mirrors.ustc.edu.cn/debian/ bookworm-backports main non-free non-free-firmware contrib
```

- 完成保存后，执行以下指令更新软件包信息

```bash
apt update
```

## 4. 绑定设备账户

参考以下指令，输入你的 M5Stack 账户的邮件地址和密码，将设备绑定到你的账户。如果你没有账户，可以[点击此处注册一个新账户](https://forum.m5stack.com/register)。

```bash
uiflow2 register
Please input your email: XXXXXXXXX@XXXX.com
Please input your password:
```

## 5. 启动 UiFlow2 服务

```bash
# 启用UiFlow2服务
uiflow2
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_uiflow2_start_01.jpg" width="70%">

- 其他常用指令

```bash
# 运行默认UiFlow 菜单程序，并启用UiFlow2服务
uiflow2 ui

# 停止UiFlow2服务
uiflow2 stop
```

- Linux 系统服务指令

```bash
# enable uiflow2 systemd service, uiflow2 will start automatically when the system starts
uiflow2 enable

# restart uiflow2 systemd service
systemctl restart uiflow2.service

# check uiflow2 systemd service status
systemctl status uiflow2.service

# stop uiflow2 systemd service
systemctl stop uiflow2.service

# remove uiflow2 systemd service
uiflow2 disable
```

## 6. 程序推送

- 访问[UiFlow2 Web IDE](https://uiflow2.m5stack.com/)并登录 M5Stack 账户。在设备列表中，能够查看当前在线的设备。选中设备后，即可开始编程。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_uiflow2_program_01.png" width="70%">

- 拖拽 UI 模拟器左侧组件至屏幕并编辑，点击右下角运行按钮（RUN）即可完成程序推送。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_uiflow2_program_02.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_uiflow2_program_03.jpg" width="70%">

## 7. 操作视频

- CoreMP135 UiFlow2 快速上手

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/cmp135UIFlow2quickstart.mp4" type="video/mp4"></video>
