# Tough 固件烧录与程序推送

## 1. 准备工作

- 参考[UIFlow Web IDE 教程](/zh_CN/uiflow/uiflow_web)，了解使用 UiFlow 的基本流程， 并完成 M5Burner 固件烧录工具的安装。
- 在 M5Burner 中下载适配`Tough`的固件， 如下图所示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5tough/burner_m5tough_01.jpg" width="70%">

## 2.USB 驱动安装

\#> 点击下方链接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP210X (适用于`CP2104`版本)/CP34X (适用于`CH9102`版本) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片， 可同时安装两种驱动。`CH9102_VCP_SER_MacOS v1.7`在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。)

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 3. 端口选择

1\. 将设备通过 USB 线连接至电脑，在 M5Burner 中选择对应固件的 Burn 按钮，填写 WiFi 信息，选择对应设备端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5tough/burner_m5tough_02.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5tough/burner_m5tough_03.jpg" width="70%">

## 4. 固件烧录

1\. 点击 Start 按键开始烧录。 注：若中途出现烧录失败或连接超时等情况，请检查是否存在端口占用，或尝试更新 USB 线，降低波特率。

当提示`Burn successfully, click here to return`时，表示烧录成功。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5tough/burner_m5tough_04.jpg" width="70%">

## 5.API KEY

1\. 完成固件烧录后，设备将重新启动，保持连接 USB 连接。使用 M5Burner 点击`Configure`选项，选择对应端口，点击`Load`加载当前设备配置。获取成功后将弹窗显示当前设备的`API KEY`, `Start Mode`等信息， 此时我们可以复制保存设备的 API KEY 信息用于后续步骤使用。 注：在本示例中，我们将使用 UIFlow Web IDE (网络版) 进行编程，因此`Start Mode`需要确保配置为`Internet Mode`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5tough/burner_m5tough_05.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5tough/burner_m5tough_06.jpg" width="70%">

## 6.RUN

完成上述配置后， 任意拖动程序块到工作区。 点击右下角的三角形运行按钮，执行程序。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5tough/uiflow_m5tough_example_01.gif" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5tough/uiflow_m5tough_example_02.png" width="70%">

## 7.USB 编程模式

- 参考[UIFlow Desktop IDE 教程](/zh_CN/uiflow/uiflow_desktop)，安装 UIFlow Desktop 的基本流程， 并了解基本的使用流程。参考以下操作将设备设置为 USB 编程模式， 或通过 M5Burner 的 Configure 选项将`Start Mode`设置为`USB Mode`后，即可通过 UIFlow Desktop IDE 编程。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5core/burner_m5core_07.jpg" width="70%">
