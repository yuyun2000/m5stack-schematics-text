# Unit C6L 固件烧录与程序推送

## 1. UiFlow2 固件烧录

1. 参考 [UiFlow2 Web IDE 教程](/zh_CN/uiflow2/uiflow_web)，了解使用 UiFlow2 的基本流程，并完成 M5Burner 固件烧录工具的安装。

2. 在 M5Burner 中下载适配 `Unit C6L` 的固件，如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_01.jpg" width="70%"/>

3. 请将设备通过 USB Type-C 数据线连接至电脑，长按侧面的复位按键 3 秒直到绿灯变红，此时设备进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Download_mode.gif" width="40%">

4. 在 M5Burner 中点击对应固件的 `Burn` 按钮，选择对应设备端口后，单击 `Start`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_02.jpg" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_03.jpg" width="70%"/>

5. 填写该设备需要连接的 Wi-Fi 配置，包括 Wi-Fi SSID 和 Wi-Fi Password，以及其他需要添加或修改的设备配置后，点击 `Next`，开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_06.jpg" width="70%"/>

配置信息说明：
- COM：选择设备对应的串口
- BaudRate：串口通信的波特率
- Server：设备连接的服务器地址
- WIFI SSID/WIFI Password：设备连接的 Wi-Fi 名称和密码
- SNTP 服务器：
  - SNTP0：阿里云 NTP 服务器 (中国)
  - SNTP1：日本 NTP 服务器池
  - SNTP2：全球公共 NTP 服务器池
- Timezone：时区设置
- Boot Option：设置固件烧录完成后，设备的启动模式
  - Run main.py directly：烧录完成后，直接运行 main.py 中的程序，不联网且不显示 UiFlow2 的启动界面
  - Show startup menu and network setup：设备联网，带屏幕的设备会显示 UiFlow2 的启动界面
  - Only network setup：设备仅进行联网，不显示 UiFlow2 的启动界面

6. 当提示 `Burn successfully, click here to return` 时，表示烧录成功，此时请复位设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_07.jpg" width="70%"/>

7. 完成固件烧录后，如果需要修改设备配置，可以保持 USB 连接，重新启动设备，点击 `Configure` 选项，根据界面提示进行修改。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_08.jpg" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_09.jpg" width="70%"/>

## 2. 设备连接

设备支持 `Access Code` (通过无线网络) 或 `USB` (有线连接电脑) 方式连接 UiFlow2，实现程序的推送与调试，详细可参考以下教程操作：

### Access Code 无线连接

1. 连接前，请确保设备已连接网络。网络连接成功时，设备界面会显示 `Wi-Fi OK` 字样。如果未连接网络，设备界面会显示 `Wi-Fi FAIL` 字样，请确认烧录固件时填写的 Wi-Fi 名称和密码是否正确，并通过 M5Burner 上的 `Configure` 选项进行修改后，重新烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_44.jpg" width="40%"/><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_43.jpg" width="40%"/>

2. 在设备的 UiFlow2 启动界面查看当前生成的有效 `Access Code`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_42.jpg" width="40%"/>

3. 访问 [uiflow2.m5stack.com](https://uiflow2.m5stack.com/) 打开 UiFlow2 Web IDE。

4. 点击页面上的 `Select Your Controller` (首次进入时会显示) 或 `Controller` 按钮，进入 `Select Device` 页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_34.jpg" width="70%"/>

5. 点击 `Connect Device`，输入访问码以及自定义设备名称后，单击 `Confirm` 即可将 Unit C6L 连接到 UiFlow2 中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_36.jpg" width="70%"/>

#> Access Code 说明 | 1. 更换浏览器、使用隐私 / 无痕模式、清除 UiFlow 网站缓存，会导致原配对状态失效。<br>2. 仅关闭标签页、重启浏览器、登录或退出账号，不会影响已绑定的配对关系。<br>3. 设备一旦被其他浏览器绑定配对，原有浏览器的配对关系将立即失效。

6. 在 `Select Device` 页面选中已经连接的 `Unit C6L` 设备，单击 `Confirm`，就可以进入 UiFlow2 的编程界面。

### USB 有线连接

1. 访问 [uiflow2.m5stack.com](https://uiflow2.m5stack.com/) 打开 UiFlow2 Web IDE，并将 **Unit C6L** 通过 USB Type-C 线连接至电脑。

2. 点击页面上的 `Select Your Controller` (首次进入时会显示) 或 `Controller` 按钮，进入 `Select Device` 页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_34.jpg" width="70%"/>

3. 在设备列表选择 **Unit C6L** 设备后，单击 `Confirm`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_17.jpg" width="70%"/>

4. 点击 `WebTerminal` 按钮，在弹框中选择 `Unit C6L` 的串行端口，点击 `连接`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_18.jpg" width="70%"/>

当 WebTerminal 屏幕显示 `Connected to Serial Port!` 时，说明 USB 连接成功。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_20.jpg" width="70%"/>

## 3. 程序运行与下载

设备连接到 UiFlow2 后，就可以拖拽 Blockly，进行程序编辑了。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/u202.gif" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_16.jpg" width="40%"/>

程序编辑完成后，单击界面右下角的 `Run Once` 按钮，可以单次运行测试程序；单击 `Run Always` 按钮，可以将程序下载到设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_40.jpg" width="70%"/>

也可以在 **WebTerminal** 窗口，单次运行或者下载程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/unitc6l_uiflow2_docs_41.jpg" width="70%"/>

## 4. 相关链接

- [UiFlow2 Blockly 介绍](https://uiflow-micropython.readthedocs.io/zh-cn/latest/)
- [UiFlow2 固件源码](https://github.com/m5stack/uiflow-micropython/tree/master)
