# CoreInk 固件烧录与程序推送

## 1. USB 驱动安装

烧录 CoreInk 固件前，请先安装 FTDI 驱动，使电脑正常识别设备并生成虚拟串口，保证烧录工具与设备正常通信。具体操作如下：

将设备连接至 PC，打开设备管理器为设备安装 [FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 Windows 10 环境为例，下载匹配操作系统的驱动文件并解压，通过设备管理器进行安装。某些系统环境下，需要安装两次驱动才会生效，未识别的设备名通常为 `M5Stack` 或 `USB Serial`。Windows 推荐使用驱动文件在设备管理器直接进行安装（自定义更新），可执行文件安装方式可能无法正常工作。

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

对于 MacOS 用户，安装前请勾选 `系统偏好设置` -> `安全性与隐私` -> `通用` -> `允许以下位置下载的 App` -> `App Store 和认可的开发者` 选项。

## 2. UiFlow2 固件烧录

1. 参考 [UiFlow2 Web IDE 教程](/zh_CN/uiflow2/uiflow_web)，了解使用 UiFlow2 的基本流程，并完成 M5Burner 固件烧录工具的安装。
2. 在 M5Burner 中下载适配 `CoreInk` 的固件，如下图所示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5coreink/burner_m5coreink_01.png" width="70%"/>

3. 将设备通过 USB 线连接至电脑。设备开机后插入 USB 接口，连接后，M5Burner 弹出 `Found New Device` 时，表示连接成功，进入编程模式。此时屏幕不显示内容。


4. 在 M5Burner 中点击对应固件的 `Burn` 按钮，选择对应设备端口后，单击 `Start`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5coreink/burner_m5coreink_02.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5coreink/burner_m5coreink_03.png" width="70%"/>

5. 填写该设备需要连接的 Wi-Fi 配置，包括 Wi-Fi SSID 和 Wi-Fi Password，以及其他需要添加或修改的设备配置后，点击 `Next`，开始烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5coreink/burner_m5coreink_06.png" width="70%"/>

配置信息说明：
- COM：选择设备对应的串口
- BaudRate：串口通信的波特率
- Server：设备连接的服务器地址
- WIFI SSID/WIFI Password：设备连接的 Wi-Fi 名称和密码
- SNTP 服务器：
  - SNTP0：阿里云 NTP 服务器（中国）
  - SNTP1：日本 NTP 服务器池
  - SNTP2：全球公共 NTP 服务器池
- Timezone：时区设置
- Boot Option：设置固件烧录完成后，设备的启动模式
  - Run main.py directly：烧录完成后，直接运行 main.py 中的程序，不联网且不显示 UiFlow2 的启动界面
  - Show startup menu and network setup：设备联网，带屏幕的设备会显示 UiFlow2 的启动界面
  - Only network setup：设备仅进行联网，不显示 UiFlow2 的启动界面

当提示 `Burn successfully, click here to return` 时，表示烧录成功。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5coreink/burner_m5coreink_07.png" width="70%"/>

6. 完成固件烧录后，如果需要修改设备配置，可以保持 USB 连接，重新启动设备，点击 `Configure` 选项，根据界面提示进行修改。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_07.jpg" width="70%"/>


## 3. 设备连接

设备支持 `Access Code`（通过无线网络）或 `USB`（有线连接电脑）方式连接 UiFlow2，实现程序的推送与调试，详细可参考以下教程操作：

### Access Code 无线连接

1. 连接前，请通过屏幕上的 Wi-Fi 图标确保设备已连接网络。如果未联网成功，请确认烧录固件时填写的 Wi-Fi 名称和密码是否正确，并通过 M5Burner 上的 `Configure` 选项进行修改后，重新烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_11.jpg" width="40%"/><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_12.jpg" width="40%"/>


2. 在设备的 UiFlow2 启动界面查看当前生成的有效 `Access Code`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_08.jpg" width="50%"/>


3. 访问 [uiflow2.m5stack.com](https://uiflow2.m5stack.com/) 打开 UiFlow2 Web IDE。
4. 点击页面上的 `Select Your Controller`（首次进入时会显示）或 `Controller` 按钮，进入 `Select Device` 页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_34.jpg" width="70%"/>

5. 点击 `Connect Device`，输入访问码以及自定义设备名称后，单击 `Confirm` 即可将 CoreInk 连接到 UiFlow2 中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_36.jpg" width="70%"/>

6. 在 `Select Device` 页面选中已经连接的 `CoreInk` 设备，单击 `Confirm`，就可以进入 UiFlow2 的编程界面了。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_01.jpg" width="70%"/>

### USB 有线连接

1. 访问 [uiflow2.m5stack.com](https://uiflow2.m5stack.com/) 打开 UiFlow2 Web IDE，并将 **CoreInk** 通过 USB 线连接至电脑。
2. 点击页面上的 `Select Your Controller`（首次进入时会显示）或 `Controller` 按钮，进入 `Select Device` 页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_34.jpg" width="70%"/>

3. 在设备列表选择 **CoreInk** 设备后，单击 `Confirm`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_02.jpg" width="70%"/>

4. 点击 `WebTerminal` 按钮，在弹框中选择 `CoreInk` 的串行端口，点击 `连接`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_03.jpg" width="70%"/>

当 WebTerminal 屏幕显示 `Connected to Serial Port!` 时，说明 USB 连接成功。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_04.jpg" width="70%"/>

## 4. 程序运行与下载

设备连接到 UiFlow2 后，就可以拖拽 Blockly，进行程序编辑了。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_11.gif" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_10.jpg" width="40%"/>

程序编辑完成后，单击界面右下角的 `Run Once` 按钮，可以单次运行测试程序；单击 `Run Always` 按钮，可以将程序下载到设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_05.jpg" width="70%"/>


也可以在 **WebTerminal** 窗口，单次运行或者下载程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048_CoreInk_uiflow2_06.jpg" width="70%"/>

## 5. 相关链接

- [UiFlow2 Blockly 介绍](https://uiflow-micropython.readthedocs.io/zh-cn/latest/)
- [UiFlow2 固件源码](https://github.com/m5stack/uiflow-micropython/tree/master)

### 自带外设开发

- [Display](https://uiflow-micropython.readthedocs.io/zh-cn/latest/widgets/index.html)
- [Button](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hardware/button.html)
- [Battery](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hardware/power.html)
- [Buzzer](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hardware/speaker.html)
- [RTC](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hardware/rtc.html)

### 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009397663711&bvid=BV1CfWUecEXd&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/sj-mXNTW_GE?si=iY477W-ciB49wXwB" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
