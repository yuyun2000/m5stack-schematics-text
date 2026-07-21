# CoreS3 / CoreS3-SE 小智语音助手

\#> 案例说明 | 本教程将使用[CoreS3](/zh_CN/core/CoreS3)主控，通过 M5Burner 烧录小智语音助手固件，构建个人语音助手应用。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/realtime/xiaozhi/m5cores3/cores3_xiaozhi_assistant_01.jpg" width="50%" />

## 1. 准备工作

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 2. 固件烧录

- 1\. 双击打开 Burner 烧录工具，在左侧菜单中选择对应的设备类型`CoreS3`, 点击下载`XiaoZhi Voice Assistant For CoreS3`固件。 (注：该固件同样适用于 CoreS3 SE)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_firmware_01.jpg" width="80%" />

\#> 固件版本 | M5Burner 中提供多个不同版本的`XiaoZhi Voice Assistant For CoreS3`固件，存在些许功能与操作上的差异。

| 固件版本            | 适用主控           | 操作说明                             | 备注           |
| ------------------- | ------------------ | ------------------------------------ | -------------- |
| v1.3.0-NiHaoXiaoZhi | CoreS3 / CoreS3-SE | 使用唤醒词 "你好小智" 进行唤醒与交互 | 支持语音唤醒词 |
| v1.3.0-HiLeXin      | CoreS3 / CoreS3-SE | 使用唤醒词 "Hi, 乐鑫" 进行唤醒与交互 | 支持语音唤醒词 |
| v1.3.0-HiM5         | CoreS3 / CoreS3-SE | 使用唤醒词 "Hi,M5" 进行唤醒与交互    | 支持语音唤醒词 |

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_firmware_02.jpg" width="80%" />

- 2\. 设备连接 USB 后，长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="40%">

- 3\. 选择设备对应的端口。点击`Burn`, 等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_firmware_03.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_firmware_04.jpg" width="80%" />

## 3.Wi-Fi 配置

- 1\. 设备启动后，将提示连接 AP 热点，并访问`192.168.4.1`进入网络配置页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_wifi_config_01.jpg" width="50%" />

- 2\. 根据页面提示完成 Wi-Fi 配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_wifi_config_02.png" width="80%" />

## 4. 注册小智 AI

- 1\. 访问[小智 AI 控制面板](https://xiaozhi.me/), 注册并登录账号。

- 2\. 启动 CoreS3 并单击屏幕，首次配置需先用唤醒词唤醒设备。如 "你好，小智"(具体唤醒词根据使用的固件版本), 唤醒后通过语音输入 "请告诉我验证码" 。等待显示请登录控制面板添加设备与验证码信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_verify_code_01.jpg" width="50%" />

- 3\. 在小智 AI 控制面板，创建新的智能体。点击添加设备，并填入设备显示的验证码信息，实现设备绑定。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_web_config_01.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_web_config_02.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_web_config_03.jpg" width="80%" />

## 5. 开始使用

- 完成上述配置后，再次单击 CoreS3 屏幕或通过唤醒词唤醒，开始对话。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_listen_01.jpg" width="50%" />

## 6. 音色切换

- 小智 AI 提供了一些音色模板，你可以在控制面板中进入`配置角色`页面进行配置。注：完成配置后需重启设备后生效。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_web_config_04.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_web_config_05.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_xiaozhi_assistant_web_config_06.jpg" width="80%" />

## 7. 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113871595573206&bvid=BV1wbfaYnEDy&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/TDRtYZOosZg?si=E4XvbK02bj3u1v-X" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
