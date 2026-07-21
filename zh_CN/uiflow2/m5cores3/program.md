# CoreS3 固件烧录与程序推送

## 1. UiFlow2 固件烧录

1. 参考 [UiFlow2 Web IDE 教程](/zh_CN/uiflow2/uiflow_web)，了解使用 UiFlow2 的基本流程，并完成 M5Burner 固件烧录工具的安装。
2. 登录 M5Burner，设备烧录成功后，设备信息会同时绑定到该账号下。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_01.png" width="70%"/>

3. 在 M5Burner 中下载适配 `CoreS3` 的固件，如下图所示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_02.png" width="70%"/>

4. 将 CoreS3 通过 USB 线连接至电脑。连接 Type-C 数据线后，M5Burner 弹出 `Found New Device` 时表示连接成功。此时屏幕不显示内容，长按 G0 键，待指示灯由红色变为绿色后进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

5. 在 M5Burner 中点击对应固件的 `Burn` 按钮，选择对应设备端口后，单击 `Start`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_03.png" width="70%"/>

6. 填写该设备需要连接的 Wi-Fi 配置，包括 Wi-Fi SSID 和 Wi-Fi Password，以及其他需要添加或修改的设备配置后，点击 `Next`，开始烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_04.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_05.png" width="70%"/>

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
- 供电模式：
  - USB 输入供电
  - Grove 输出供电

7. 当提示 `Burn successfully, click here to return` 时，表示烧录成功，此时请复位设备。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_06.png" width="70%"/>

8. 完成固件烧录后，如果需要修改设备配置，可以保持 USB 连接，重新启动设备，点击 `Configure` 选项，根据界面提示进行修改。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_07.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_08.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/m5cores3/burrner_m5cores3_09.png" width="70%"/>

## 2. 设备连接

设备支持 `Access Code`（通过无线网络）或 `USB`（有线连接电脑）方式连接 UiFlow2，实现程序的推送与调试，详细可参考以下教程操作：

### Access Code 无线连接

1. 连接前，请确保设备已连接网络。如果未联网成功，请确认烧录固件时填写的 Wi-Fi 名称和密码是否正确，并通过 M5Burner 上的 `Configure` 选项进行修改后，重新烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_05.jpg" width="40%"/><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_06.jpg" width="40%"/>

2. 在设备的 UiFlow2 启动界面查看当前生成的有效 `Access Code`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_04.jpg" width="50%"/>

3. 访问 [uiflow2.m5stack.com](https://uiflow2.m5stack.com/) 打开 UiFlow2 Web IDE。

4. 点击页面上的 `Select Your Controller`（首次进入时会显示）或 `Controller` 按钮，进入 `Select Device` 页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_34.jpg" width="70%"/>

4. 点击 `Connect Device`，输入访问码以及自定义设备名称后，单击 `Confirm` 即可将 CoreS3 连接到 UiFlow2 中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_36.jpg" width="70%"/>

5. 在 `Select Device` 页面选中已经连接的 `CoreS3` 设备，单击 `Confirm`，就可以进入 UiFlow2 的编程界面。

### USB 有线连接

1. 访问 [uiflow2.m5stack.com](https://uiflow2.m5stack.com/) 打开 UiFlow2 Web IDE，并将 **CoreS3** 通过 USB 线连接至电脑。

2. 点击页面上的 `Select Your Controller`（首次进入时会显示）或 `Controller` 按钮，进入 `Select Device` 页面。

3. 在设备列表选择 **CoreS3** 设备后，单击 `Confirm`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_01.jpg" width="70%"/>

4. 点击 `WebTerminal` 按钮，在弹框中选择 `CoreS3` 的串行端口，点击 `连接`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/cardputer-adv_uiflow2_15.jpg" width="70%"/>

当 WebTerminal 屏幕显示 `Connected to Serial Port!` 时，说明 USB 连接成功。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_09.jpg" width="70%"/>

## 3. 程序运行与下载

设备连接到 UiFlow2 后，就可以拖拽 Blockly，进行程序编辑了。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_07.gif" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_08.jpg" width="50%"/>

程序编辑完成后，单击界面右下角的 `Run Once` 按钮，可以单次运行测试程序；单击 `Run Always` 按钮，可以将程序下载到设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_02.jpg" width="70%"/>

也可以在 **WebTerminal** 窗口，单次运行或者下载程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_CoreS3_uiflow2_03.jpg" width="70%"/>

## 4. 相关链接

- [UiFlow2 Blockly 介绍](https://uiflow-micropython.readthedocs.io/zh-cn/latest/)
- [UiFlow2 固件源码](https://github.com/m5stack/uiflow-micropython/tree/master)

### 自带外设开发

- [Button](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hardware/button.html)
- [SDCard](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/speaker.html#SDCard)
- [MIC](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hardware/mic.html)
- [Speaker](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hardware/speaker.html)
- [Screen](https://uiflow-micropython.readthedocs.io/zh-cn/latest/widgets/index.html)
- [ALS](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hardware/als.html)
- [Camera](https://uiflow-micropython.readthedocs.io/zh-cn/latest/advanced/camera.html)

### 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009263381356&bvid=BV1b2WUeuE96&p=1&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/YSjTbh8z6S4?si=jHhn-3qunirjuT3w" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
