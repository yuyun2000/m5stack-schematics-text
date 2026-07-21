# Cardputer-Adv 固件烧录与程序推送

## 1. UiFlow2 固件烧录

1. 参考 [UiFlow2 Web IDE 教程](/zh_CN/uiflow2/uiflow_web)，了解使用 UiFlow2 的基本流程，并完成 M5Burner 固件烧录工具的安装。

2. 在 M5Burner 中下载适配 `Cardputer-Adv` 的固件，如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_01.jpg" width="70%"/>

3. 将 Cardputer-Adv 侧面的开关键置于 `OFF` 状态，然后在开机前按住 `G0` 按键，在设备通电后释放，之后设备将进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Cardputer-Adv_operation_01.jpg" width="60%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Cardputer-Adv_operation.gif" width="40%" />

4. 将设备通过 USB 线连接至电脑，在 M5Burner 中点击对应固件的 `Burn` 按钮，选择对应设备端口后，单击 `Start`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_02.jpg" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_03.jpg" width="70%"/>

5. 填写该设备需要连接的 Wi-Fi 配置，包括 Wi-Fi SSID 和 Wi-Fi Password，以及其他需要添加或修改的设备配置后，点击 `Next`，开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_05.jpg" width="70%"/>

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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_06.jpg" width="70%"/>

7. 完成固件烧录后，如果需要修改设备配置，可以保持 USB 连接，重新启动设备，点击 `Configure` 选项，根据界面提示进行修改。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_07.jpg" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_18.jpg" width="70%"/>

## 2. 设备连接

设备支持 `Access Code` (通过无线网络) 或 `USB` (有线连接电脑) 方式连接 UiFlow2，实现程序的推送与调试，详细可参考以下教程操作：

### Access Code 无线连接

1. 连接前，请确保设备已连接网络。如果未连接网络，请确认烧录固件时填写的 Wi-Fi 名称和密码是否正确，并通过 M5Burner 上的 `Configure` 选项进行修改后，重新烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_46.jpg" width="40%"/><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_47.jpg" width="40%"/>

2. 在设备的 UiFlow2 启动界面查看当前生成的有效 `Access Code`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_45.jpg" width="70%"/>

3. 访问 [uiflow2.m5stack.com](https://uiflow2.m5stack.com/) 打开 UiFlow2 Web IDE。

4. 点击页面上的 `Select Your Controller` (首次进入时会显示) 或 `Controller` 按钮，进入 `Select Device` 页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_34.jpg" width="70%"/>

5. 点击 `Connect Device`，输入访问码以及自定义设备名称后，单击 `Confirm` 即可将 Cardputer-Adv 连接到 UiFlow2 中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_36.jpg" width="70%"/>

#> Access Code 说明 | 1. 更换浏览器、使用隐私 / 无痕模式、清除 UiFlow 网站缓存，会导致原配对状态失效。<br>2. 仅关闭标签页、重启浏览器、登录或退出账号，不会影响已绑定的配对关系。<br>3. 设备一旦被其他浏览器绑定配对，原有浏览器的配对关系将立即失效。

6. 在 `Select Device` 页面选中已经连接的 `Cardputer-Adv` 设备，单击 `Confirm`，就可以进入 UiFlow2 的编程界面。

### USB 有线连接

1. 访问 [uiflow2.m5stack.com](https://uiflow2.m5stack.com/) 打开 UiFlow2 Web IDE，并将 **Cardputer-Adv** 通过 USB Type-C 线连接至电脑。

2. 点击页面上的 `Select Your Controller` (首次进入时会显示) 或 `Controller` 按钮，进入 `Select Device` 页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_34.jpg" width="70%"/>

3. 在设备列表选择 **Cardputer-Adv** 设备后，单击 `Confirm`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_14.jpg" width="70%"/>

4. 点击 `WebTerminal` 按钮，在弹框中选择 `Cardputer-Adv` 的串行端口，点击 `连接`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_15.jpg" width="70%"/>

当 WebTerminal 屏幕显示 `Connected to Serial Port!` 时，说明 USB 连接成功。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_17.jpg" width="70%"/>

## 3. 程序运行与下载

设备连接到 UiFlow2 后，就可以拖拽 Blockly，进行程序编辑了。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Cardputer-Adv_operation_02.gif" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_13.jpg" width="60%">

程序编辑完成后，单击界面右下角的 `Run Once` 按钮，可以单次运行测试程序；单击 `Run Always` 按钮，可以将程序下载到设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_41.jpg" width="70%"/>

也可以在 **WebTerminal** 窗口，单次运行或者下载程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_44.jpg" width="70%"/>

## 4. 相关链接

- [UiFlow2 Blockly 介绍](https://uiflow-micropython.readthedocs.io/zh-cn/latest/)
- [UiFlow2 固件源码](https://github.com/m5stack/uiflow-micropython/tree/master)
- [Cardputer 控制器文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/controllers/cardputer.html)

### UiFlow2 固件主界面功能模块说明

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/uilist.png" width="60%">

#> UiFlow2 程序包含五个功能模块 | DEVELOP：显示当前设备的基础信息，包括 MAC 地址及绑定的用户账号。<br>APP.RUN：配置 UiFlow2 下载程序的运行模式。<br>APP.LIST：管理已保存的程序列表。<br>EZDATA：提供与云端的数据交互功能，支持数据上传与同步。<br>SETTING：集中管理设备常用系统设置，如屏幕亮度调节、Wi-Fi 网络配置等。

设备 (Cardputer-Adv) 启动后，键盘默认处于低功耗休眠状态。为启用键盘输入功能，用户需同时执行以下操作：左手持续按住键盘上的 `fn` 键以唤醒键盘；右手在键盘上点击所需执行的按键。此操作可确保键盘成功激活并响应后续输入。具体操作方法，可以查阅 [官网文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/controllers/cardputer.html)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/IMG_20260305_153515.jpg" width="60%">

- DEVELOP
  - 设备 MAC 地址
  - M5Burner 烧录时绑定的账号，用于离线开发

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/ui_cardputeradv01.jpg" width="60%">

- APP.RUN
  - 当您使用 UiFlow2 将编辑好的程序下载到设备时，系统会自动将该程序写入 APP.RUN 目录下的 main.py 文件中 (覆盖原有内容)，并立即运行
  - 如果您通过其他方式 (如手动导入) 向 APP.RUN 目录中添加了名为 main.py 的程序，也可以在设备上通过 RUN(ONCE) 单次运行或 RUN(ALWAYS) 一直运行选项来运行它

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/ui_cardputeradv09.png" width="60%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/ui_cardputeradv10.png" width="60%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/ui_cardputeradv09.jpg" width="60%">

> 注意：main.py 不能删除，删除后，进入 APP.RUN 程序，设备会卡死。执行 UiFlow2 程序烧录或者 main.py 程序运行后，是无法回到 UiFlow2 主界面的，需重新使用 M5Burner 进行 Configure 配置，刷新固件。

- APP.LIST
  - 当您熟悉 UiFlow2 开发后，可以手动编写 Python 程序 (使用任意代码编辑器)，点击 UiFlow2 界面左下角 WebTerminal，使用 USB 连接设备，点击 file 文件夹，将程序文件导入到设备的 /flash/apps 目录中，放在目录中的文件，设备开机后，随时进行测试和运行

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/ui_cardputeradv04.png" width="60%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/ui_cardputeradv05.jpg" width="60%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/ui_cardputeradv06.jpg" width="60%">

- SETTING
  - 配置 Wi-Fi
  - 配置屏幕亮度

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/ui_cardputeradv02.png" width="60%">

### 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115184983149691&bvid=BV1XLHezdERQ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/SDxHjMCy_w4?si=YngLkj8EyXOhBbk0" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
