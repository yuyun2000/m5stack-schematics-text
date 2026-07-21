# UiFlow2 Web IDE 介绍

## UiFlow2 介绍

UiFlow2 是一款图形化编程网页集成开发环境（IDE），基于 Blockly 积木式拖拽开发，支持有线/无线一键推送程序，免编译运行，无需编写代码即可快速控制 M5Stack 设备及上百种传感器模块。在 UiFlow 1 的基础上，UiFlow 2 新增项目分享、设备共享等功能，便于团队协作，提供更高效的开发体验，帮助用户更快实现从构思到产品的转化。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_02.jpg" width="70%">

- 访问 [UiFlow2 Web IDE](https://uiflow2.m5stack.com/)
- 参见 [UiFlow2 开发指南](/zh_CN/uiflow2/uiflow2_layout)

## 设备连接方式

设备开发前，需要烧录对应的 UiFlow2 固件，通过 Access Code 或 USB 连接方式将设备连接到 UiFlow2 后，即可实现程序的推送与调试，以下为两种连接方式说明：

- Access Code（访问码）方式：设备通过网络方式推送程序。在 UiFlow2 页面输入设备的访问码，完成配置后，即可无线推送程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_32.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_31.jpg" width="70%">

- USB 方式：使用 USB Type-C 数据线将设备与电脑相连，在 UiFlow2 页面选中对应串口，完成连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_32.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_33.jpg" width="70%">

## M5Burner

M5Burner 为 M5Stack 官方专用固件烧录软件，全系产品的 UiFlow2 固件均可通过 M5Burner 进行烧录，同时支持在烧录阶段预置 Wi-Fi 等设备配置信息。
<br>除固件烧录功能，M5Burner 还支持**固件导出**与**固件分享**，可将开发完成的固件发布到 M5Burner 上，供其他用户下载。详细操作教程可参见[固件导出](/zh_CN/uiflow/m5burner/export)、[固件发布](/zh_CN/uiflow/m5burner/publish)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/m5burner_intro_pic_01.jpg" width="70%">

请根据操作系统下载对应版本的 M5Burner，解压后运行程序：

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 固件烧录

参考对应产品的教程，烧录 UiFlow2 固件并运行程序。

<div class="directory-links-container">

<div class="directory-links-item">
    <div class="directory-links-body">
        <ul>
            <li><a href="/zh_CN/uiflow2/m5core/program">Basic</a></li>
            <li><a href="/zh_CN/uiflow2/m5core2/program">Core2</a></li>
            <li><a href="/zh_CN/uiflow2/m5tough/program">Tough</a></li>
            <li><a href="/zh_CN/uiflow2/m5cores3/program">CoreS3</a></li>
            <li><a href="/zh_CN/uiflow2/m5fire/program">Fire</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/atom_echos3r/program">Atom VoiceS3R</a></li>
            <li><a href="/zh_CN/uiflow2/atomlite/program">Atom-Lite</a></li>
            <li><a href="/zh_CN/uiflow2/atommatrix/program">Atom-Matrix</a></li>
            <li><a href="/zh_CN/uiflow2/atomu/program">AtomU</a></li>
            <li><a href="/zh_CN/uiflow2/atoms3/program">AtomS3</a></li>
            <li><a href="/zh_CN/uiflow2/atoms3r/program">AtomS3R</a></li>
            <li><a href="/zh_CN/uiflow2/atoms3u/program">AtomS3U</a></li>
            <li><a href="/zh_CN/uiflow2/atoms3lite/program">AtomS3-Lite</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/m5stickc/program">StickC</a></li>
            <li><a href="/zh_CN/uiflow2/m5stickcplus/program">StickC-Plus</a></li>
            <li><a href="/zh_CN/uiflow2/m5stickcplus2/program">StickC-Plus2</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/stamps3/program">Stamp-S3</a></li>
            <li><a href="/zh_CN/uiflow2/stamp_p4/program">Stamp-P4</a></li>
            <li><a href="/zh_CN/uiflow2/stamplc/program">StamPLC</a></li>
            <li><a href="/zh_CN/uiflow2/stamppico/program">Stamp-Pico</a></li>
            <li><a href="/zh_CN/uiflow2/m5dial/program">Dial</a></li>
            <li><a href="/zh_CN/uiflow2/m5capsule/program">Capsule</a></li>
            <li><a href="/zh_CN/uiflow2/cardputer/program">Cardputer</a></li>
            <li><a href="/zh_CN/uiflow2/cardputer-adv/program">Cardputer-Adv</a></li>
            <li><a href="/zh_CN/uiflow2/airq/program">Air Quality</a></li>
            <li><a href="/zh_CN/uiflow2/m5dinmeter/program">DinMeter</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/m5paper/program">Paper</a></li>
            <li><a href="/zh_CN/uiflow2/papercolor/program">PaperColor</a></li>
            <li><a href="/zh_CN/uiflow2/m5papers3/program">PaperS3</a></li>
            <li><a href="/zh_CN/uiflow2/m5coreink/program">CoreInk</a></li>
            <li><a href="/zh_CN/guide/linux/coremp135/uiflow2">CoreMP135</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/m5station/program">Station-Bat</a></li>
            <li><a href="/zh_CN/uiflow2/stopwatch/program">StopWatch</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/Tab5/program">Tab5</a></li>
            <li><a href="/zh_CN/uiflow2/powerhub/program">PowerHub</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/unit_c6l/program">Unit C6L</a></li>
            <li><a href="/zh_CN/uiflow2/unit_poe_p4/program">Unit PoE-P4</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/stackchan/program">StackChan</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow2/chain_dualKey/program">Chain DualKey
</a></li>
        </ul>
    </div>
</div>

</div>
