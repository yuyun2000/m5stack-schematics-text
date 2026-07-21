# UiFlow Web IDE 快速上手

#>|UiFlow 是一款所有人都能轻松上手的一款图形化编程 IDE，支持无线/有线程序推送，程序点击即可运行，无需反复编译。其支持 100+ M5 硬件外设与传感器，支持一键添加拓展，有效助力产品原型构建，加快开发过程到最终产品化。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_02.jpg" width="70%">

## 1.上手流程

使用 UiFlow 进行编程前的几个准备步骤：

1. 安装 M5Burner 固件烧录工具。
2. 使用 M5Burner 烧录对应设备的固件，并为设备配置 Wi-Fi 连接， 获取设备的 API KEY。
3. 打开[UiFlow Web IDE 1.0 版本](https://flow.m5stack.com/), 选择对应的设备选项，并填写设备的 API KEY。
4. 拖拽 Blockly 进行程序编辑，点击`Run`按键进行程序调试。

补充：
- M5Burner 是 M5Stack 推出的统一固件烧录工具， 通过该工具用户可以很方便的烧录 UiFlow 固件，并在烧录时一同写入 Wi-Fi 等配置信息。
- API KEY 是 UiFlow1 用于区分设备的密钥，该密钥会在设备完成 UiFlow 固件烧录时生成，UiFlow Web IDE 通过指定与设备相同的 API KEY 实现程序的远程推送。

## 2.M5Burner 安装

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，解压打开应用程序。

| 软件版本         | 下载链接                                                                    |
| ---------------- | --------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 3.固件烧录 & 运行程序

参考对应产品的教程进行固件烧录， 并上传程序。

<div class="directory-links-container">

<div class="directory-links-item">
    <div class="directory-links-body">
        <ul>
            <li><a href="/zh_CN/uiflow/m5core/program">Basic/Gray/Fire/M5GO</a></li>
            <li><a href="/zh_CN/uiflow/m5fire/program">Fire</a></li>
            <li><a href="/zh_CN/uiflow/m5core2/program">Core2/Core2 For AWS</a></li>
            <li><a href="/zh_CN/uiflow/m5tough/program">Tough</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow/m5atom_matrix/program">Atom-Matrix</a></li>
            <li><a href="/zh_CN/uiflow/m5atom_display/program">Atom Display</a></li>
            <li><a href="/zh_CN/uiflow/m5atom_lite/program">Atom-Lite</a></li>
            <li><a href="/zh_CN/uiflow/m5atomu/program">AtomU</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow/m5stickc/program">StickC</a></li>
            <li><a href="/zh_CN/uiflow/m5stickc_plus/program">StickC-Plus</a></li>
            <li><a href="/zh_CN/uiflow/m5stickc_plus2/program">StickC-Plus2</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow/m5paper/program">Paper</a></li>
            <li><a href="/zh_CN/uiflow/m5coreink/program">CoreInk</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow/m5station/program">Station-Bat</a></li>
        </ul>
        <ul>
            <li><a href="/zh_CN/uiflow/stamppico/program">Stamp-Pico</a></li>
        </ul>
    </div>
</div>

</div>