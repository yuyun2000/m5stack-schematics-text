# Atomic Voice Base 小智语音助手

本教程将使用 AtomS3 系列设备 + [Atomic Voice Base](/zh_CN/atom/Atomic%20Echo%20Base)硬件组合，通过 M5Burner 烧录小智语音助手固件，构建个人语音助手应用。

## 1. 准备工作

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，并解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 2. 固件烧录

1. 双击打开 Burner 烧录工具，在左侧菜单中选择对应的设备类型`AtomS3`，根据实际使用的 AtomS3 系列设备选择对应的`XiaoZhi Voice Assistant`固件进行下载。

- 适用于**AtomSAR-CAM**和**AtomS3R-M12**的固件：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_xiaozhi01.jpg" width="80%" />

| 固件版本 | 适用主控                | 操作说明                             | 备注           |
| -------- | ----------------------- | ------------------------------------ | -------------- |
| v1.6.2   | AtomSAR-CAM/AtomS3R-M12 | 使用唤醒词 "你好小智" 进行唤醒与交互 | 支持语音唤醒词 |

- 适用于**AtomS3R**/**AtomS3**/**AtomS3-Lite**的固件：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_firmware_01.jpg" width="80%" />

\#> 说明 | M5Burner 提供多个不同版本的`XiaoZhi Voice Assistant`固件，用于适配不同的 AtomS3 主控。不同固件因硬件配置不同（是否集成 PSRAM），存在些许功能与操作上的差异。

| 固件版本            | 适用主控             | 操作说明                             | 备注             |
| ------------------- | -------------------- | ------------------------------------ | ---------------- |
| v1.3.0-NiHaoXiaoZhi | AtomS3R              | 使用唤醒词 "你好小智" 进行唤醒与交互 | 支持语音唤醒词   |
| v1.3.0-HiLeXin      | AtomS3R              | 使用唤醒词 "Hi, 乐鑫" 进行唤醒与交互 | 支持语音唤醒词   |
| v1.3.0-HiM5         | AtomS3R              | 使用唤醒词 "Hi,M5" 进行唤醒与交互    | 支持语音唤醒词   |
| v1.3.0-AtomS3       | AtomS3 / AtomS3-Lite | 单击 AtomS3 的中心按键触发对话       | 不支持语音唤醒词 |

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_firmware_02.jpg" width="80%" />

2. 设备连接 USB 后，长按复位按键（大约 2 秒）到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/AtomS3R_download_mode.gif" width="40%">

3. 选择设备对应的端口。点击`Burn`，等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_firmware_03.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_firmware_04.jpg" width="80%" />

## 3.Wi-Fi 配置

1. 设备启动后，将提示连接 AP 热点，。可在手机连接热点**小智 - xxx**，或者访问`192.168.4.1`进入网络配置页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_wifi_config_01.jpg" width="50%" />

2. 根据页面提示完成 Wi-Fi 配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_wifi_config_02.png" width="80%" />

## 4. 注册小智 AI

1. 访问[小智 AI 控制面板](https://xiaozhi.me/)，注册并登录账号。

2. 获取设备验证码。Wi-Fi 配置成功后，设备会自动播报`请登录到控制面板添加设备，输入验证码xxx`，带有屏幕的设备同时会在屏幕上显示验证码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_verify_code_01.jpg" width="50%" />

\#> 获取验证码 | 对于不带屏幕的 AtomS3 系列设备，例如 AtomS3R-CAM、AtomS3R-M12，在连接上网络后，会语音播报设备的验证码，也可以通过串口日志的方式进行查看。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/xiaozhi_03.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/xiaozhi_02.jpg" width="80%" />

3. 在小智 AI 控制面板，创建新的智能体。点击添加设备，并填入设备显示的验证码信息，实现设备绑定。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_web_config_01.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_web_config_02.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_web_config_03.jpg" width="80%" />

## 5. 开始使用

完成上述配置后，再次单击 AtomS3 系列设备屏幕或通过唤醒词唤醒，开始对话。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_listen_01.jpg" width="50%" />

## 6. 音色切换

小智 AI 提供了一些音色模板，您可以在控制面板中进入`配置角色`页面进行配置。注意：完成配置后需重启设备后生效。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_web_config_04.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_web_config_05.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_web_config_06.jpg" width="80%" />

## 7. 相关视频

- 烧录小智语音助手固件

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113858492567265&bvid=BV1bsw1e3EBS&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/RqMJ2y-FQpw?si=rb4tgfRx7iI9SDzu" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

- 小智语音助手视觉体验

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AtomS3R-M12-Atomic-Echo-Base-xiaozhi-AI-video.mp4" type="video/mp4"></video>
