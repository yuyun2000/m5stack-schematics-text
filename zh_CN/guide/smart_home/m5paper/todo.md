# M5Paper Todo 使用教程

本教程将为 M5Paper 烧录 Todo List 应用固件。可同步 Microsoft Todo APP 的任务列表。

## 驱动安装

\#> 点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本 (CP210X/CH9102), 请根据你所使用的版本下载对应的驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。`CH9102_VCP_SER_MacOS v1.7`在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。)

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 烧录工具

> 请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具。解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 固件烧录

1\. 双击打开 Burner 烧录工具，①在左侧菜单中选择对应的设备类型`M5Paper`, 选择`TODO`固件，点击下载按钮进行下载。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/smart_home/m5paper/todo/todo_01.jpg" width="70%">

2\. 然后将 M5 设备通过 Type-C 数据线连接到电脑，选择对应的 COM 口，波特率可使用 M5Burner 中的默认配置，点击 "Burn" 开始烧录。当烧录日志提示`Burn Successfully`时，则表示固件已经烧录完成。

3\. 烧录完成后，设备将自动重启。首次启动，将会显示介绍页面，其中包含的注意事项。 点击屏幕进入下一步语言配置，除了英文以外的两种语言均需要从 TF 卡加载字体文件 (字体文件命名必须为`Font.ttf`)。 [示例ttf文件下载地址](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/example/Font.ttf). 时区配置。点击左上角`Exit`进入下一页。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/smart_home/m5paper/todo/paper_todo_01.png" width="30%">

4\. 选择将要连接的 WiFi 网络，输入密码进行连接。连接成功后，将会自动生成`设备码`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/smart_home/m5paper/todo/paper_todo_02.png" width="30%"><img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/smart_home/m5paper/todo/paper_todo_03.png" width="30%">

5\. 扫码 M5Paper 屏幕上显示的二维码，进入设备绑定页面，`填入设备码`并`绑定个人microsoft账号`, 等待绑定完成。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/smart_home/m5paper/todo/todo_02.png" width="70%">

6\. 绑定成功后，就可以通过 microsoft 官方 todo 应用添加任务，并同步到 M5Paper 上显示了。(M5Paper 进入列表后，按下拨轮中心按钮，可刷新列表。) [下载Microsoft ToDo App](https://to-do.microsoft.com/tasks/)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/smart_home/m5paper/todo/paper_todo_app_01.jpg" width="30%"><img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/smart_home/m5paper/todo/paper_todo_04.png" width="30%">

## 程序源码

- [M5EPD_Todo](https://github.com/m5stack/M5EPD_Todo)
- [M5EPD Library](https://github.com/m5stack/M5EPD)
