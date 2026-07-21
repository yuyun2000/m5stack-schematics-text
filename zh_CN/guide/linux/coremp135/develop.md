# CoreMP135开发

本教程将基于M5Stack Linux应用开发框架编程控制CoreMP135上的外设硬件

## 1.准备工作

- CoreMP135设备(完成buildroot/debian镜像烧录, 该步骤可参考[CoreMP135镜像烧录教程](/zh_CN/guide/linux/coremp135/image))
- CoreMP135供电电源(DC 12V电源或Type-C 5V输入)
- CoreMP135通过网线连接至与开发环境电脑同一网段下的网络

## 2.环境搭建

### Windows环境搭建

1.访问[https://www.python.org/](https://www.python.org/), 安装[python3](https://www.python.org/), 并在安装过程中, 勾选`Add Path`选项使其添加到环境变量中。


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/python_add_path_01.jpg" width="50%">


2.打开命令行, 输入以下指令, 通过pip管理工具安装编译构建工具以及相关依赖

```bash
pip install parse scons pexpect paramiko scp
```

3.获取访问[M5Stack_Linux_Libs Github](https://github.com/m5stack/M5Stack_Linux_Libs)获取开发框架和案例源码, 可通过下载zip压缩包的形式或通过`git clone`方式获取。

```bash
git clone https://github.com/m5stack/M5Stack_Linux_Libs
```

4.点击下方链接下载适用于windows平台的`gcc-linaro-7.5.0-2019.12-i686-mingw32_arm-linux-gnueabihf`交叉编译工具链, 并将其保存到自定义工作目录中，并解压。(注意: 路径中不允许存在特殊字符)

- [gcc-linaro-7.5.0-2019.12-i686-mingw32_arm-linux-gnueabihf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linaro/gcc-linaro-7.5.0-2019.12-i686-mingw32_arm-linux-gnueabihf.zip)


### Linux环境搭建

1.执行以下指令安装相关依赖

```bash
sudo apt install make cmake
pip install parse scons pexpect paramiko scp
```

2.获取访问[M5Stack_Linux_Libs Github](https://github.com/m5stack/M5Stack_Linux_Libs)获取开发框架和案例源码, 可通过下载zip压缩包的形式或通过`git clone`方式获取。

```bash
git clone https://github.com/m5stack/M5Stack_Linux_Libs
```

3.点击下方链接下载适用于Linux平台的`gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf`交叉编译工具链, 并将其保存到自定义工作目录中，并解压。(注意: 路径中不允许存在特殊字符)

- [gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linaro/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz)

## 4.编译案例程序

1.打开案例程序的目录, 并打开命令行界面, 输入`scons menuconfig`指令进行编译配置。(注：windows用户若cmd终端打开配置界面无法正常移动光标, 请使用powershell访问)

```bash
cd M5Stack_Linux_Libs/examples/lcd_hello_world
scons menuconfig
```

2.回车键进入Toolchain Configuration

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/scons_menuconfig_01.jpg" width="70%">

3.回车键打开配置, 填写交叉编译工具链的绝对路径以及工具链的前缀, Esc键退出保存。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/scons_menuconfig_02.jpg" width="70%">

4.当前案例工程下, 输入以下指令进行编译, 编译完成后将会输出可执行文件到当前路径的dist目录。

```bash
scons -j4
```


## 5.推送案例程序

1.通过开发框架中的程序推送脚本，可将编译好的程序推送至CoreMP135的用户目录中，方便调试运行，这样避免每次手动复制文件到SD卡中的繁琐操作。在此之前, 我们需要将CoreMP135连接至与当前电脑同一网段, 然后通过路由器后台查看设备IP或串口连接登录后使用`ifconfig`指令，获取当前设备的IP地址。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/local_network.png" width="50%">

## 6.串口连接

1.CoreMP135的USB将默认启用为系统log端口, 用户可使用该接口连接至电脑, 使用putty或MobaXterm之类的终端工具进行访问, 默认波特率为`115200bps`, 以下操作基于putty进行操作, 请点击下方链接下载putty安装包，并根据操作指引实现登录。默认用户名为`root`, 密码为`root`。

- [putty - download](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/uart_01.jpg" width="30%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/uart_com_01.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/uart_log_01.png" width="70%">


## 7.SSH访问

1.将设备通过网线连接至与当前电脑同一网段下。电脑可通过命令行ssh指令实现远程访问。默认用户名为`root`, 密码为`root`。

```shell
ssh root@192.168.2.212
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/local_network.png" width="50%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/eth_01.jpg" width="30%">


?>注意事项|新版本debian镜像中, 默认对root登录权限进行了关闭。 若使用的是debian镜像，请在使用前通过串口登录访问设备, 使用`useradd`指令创建新的用户，或参考下图使用`core-config`指令启用root用户的ssh访问权限。用于推送程序配置的配置文件`setup.ini`, 也请根据实际用户信息入。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_coreconfig_root_ssh_01.png" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_coreconfig_root_ssh_02.png" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_coreconfig_root_ssh_03.png" width="50%">


3.案例工程目录下的`setup.ini`配置文件，可用于配置远程推送的设备IP地址，以及推送的目录， 将其修改为实际设备的IP地址和用户信息。 (部分案例若未包含该文件，则需手动创建，并添加以下配置内容)

```bash
[ssh]
local_file_path = dist
remote_file_path = /root
remote_host = 192.168.2.212
remote_port = 22
username = root
password = root
```


```bash
ifconfig
```


4.并执行以下`scons push`指令进行推送。

```bash
scons push

#log
#scons: Reading SConscript files ...
#...
#push dist\lcd_hello_world /root/lcd_hello_world success!
```

3.回到CoreMP135的命令行终端，进入我们刚刚推送程序的目录，可找到发送过来的可执行文件，赋予文件执行权限, 然后运行。

```bash
chmod +x lcd_hello_world
./lcd_hello_world
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/lcd_hello_world_01.gif" width="60%">

4.由于该案例调用到了屏幕驱动, 若你使用的是CoreMP135的默认出厂固件, 你需要手动关闭GUI进程，防止冲突.

```bash
ps | grep "start_ui"

#239 root     /usr/local/m5stack/dist/core135_start_ui
#312 root     grep start_ui

kill 239
```


## 8.配置开机自启

编辑`/etc/rc.local`启动脚本文件, 在文件尾部添加我们编译完成的程序的启动指令

```bash
vi /etc/rc.local
```

```bash
sleep 2
/root/lcd_hello_world &
```


## 9.操作视频

<video width="600" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/coremp135_develop.mp4" type="video/mp4">
</video>

