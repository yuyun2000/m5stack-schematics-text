# StickC-Plus2 固件烧录与程序推送

## 1. 准备工作

- 参考[UIFlow Web IDE 教程](/zh_CN/uiflow/uiflow_web)，了解使用 UiFlow 的基本流程， 并完成 M5Burner 固件烧录工具的安装。
- 在 M5Burner 中下载适配`StickC-Plus2`的固件， 如下图所示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/burner_m5stickc_plus2_01.jpg" width="70%">

## 2.USB 驱动安装

\#> 点击下方链接下载匹配操作系统的驱动程序。CP34X (适用于`CH9102`) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 3. 端口选择

1\. 将设备通过 USB 线连接至电脑，在 M5Burner 中选择对应固件的 Burn 按钮，填写 WiFi 信息，选择对应设备端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/burner_m5stickc_plus2_02.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/burner_m5stickc_plus2_03.jpg" width="70%">

## 4. 固件烧录

1\. 点击 Start 按键开始烧录。 注：若中途出现烧录失败或连接超时等情况，请检查是否存在端口占用，或尝试更新 USB 线，降低波特率。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/burner_m5stickc_plus2_04.jpg" width="70%">

## 5.API KEY

1\. 完成固件烧录后，设备将重新启动，保持连接 USB 连接。使用 M5Burner 点击`Configure`选项，选择对应端口，点击`Load`加载当前设备配置。获取成功后将弹窗显示当前设备的`API KEY`, `Start Mode`等信息， 此时我们可以复制保存设备的 API KEY 信息用于后续步骤使用。 注：在本示例中，我们将使用 UIFlow Web IDE (网络版) 进行编程，因此`Start Mode`需要确保配置为`Internet Mode`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/burner_m5stickc_plus2_05.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/burner_m5stickc_plus2_06.png" width="70%">

2\. 将设备配置为在线编程模式后， 我们需要通过 API KEY 让设备与 UiFlow 建立起连接， 使其能够为指定的设备推送程序。用户需在电脑端浏览器访问[flow.m5stack.com](http://flow.m5stack.com/)进入 UiFlow 编程页面

3\. 点击页面右上角的菜单栏中的设置按钮， 输入我们在上一步骤获取的 API KEY, 点击 OK 保存， 等待提示连接成功。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/uiflow_m5stickc_plus2_01.png" width="70%">

## 6.RUN

1\. 完成以上步骤，就可以开始使用 UiFlow 进行编程了。下面将向你演示一个简单的程序，驱动 StickC-Plus2 点亮 LED 指示灯。(1. 拖动 LED 点亮程序块 2. 拼接至 Setup 初始化程序 .3 点击右上角运行按钮)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/uiflow_m5stickc_plus2_example_01.gif" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5stickc_plus2/uiflow_m5stickc_plus2_example_02.png" width="70%">

## 7.USB 编程模式

- 参考[UIFlow Desktop IDE 教程](/zh_CN/uiflow/uiflow_desktop)，安装 UIFlow Desktop 的基本流程， 并了解基本的使用流程。参考以下操作将设备设置为 USB 编程模式， 或通过 M5Burner 的 Configure 选项将`Start Mode`设置为`USB Mode`后，即可通过 UIFlow Desktop IDE 编程。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5core/burner_m5core_07.jpg" width="70%">
