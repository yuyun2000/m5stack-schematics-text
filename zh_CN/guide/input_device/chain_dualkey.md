# Chain DualKey 出厂固件使用教程

Chain Dualkey 是一款可编程双按键输入开发板。它的出厂固件可以设置按键功能与 RGB LED 灯色彩，也可以设置通过 Chain Bus 连接的其他 Chain 系列设备。

#> 固件更新 | 新版固件已发布，支持更多按键映射等功能，建议使用 M5Burner 一键更新。<br>
参考[产品页面](/zh_CN/chain/Chain_DualKey#%E6%93%8D%E4%BD%9C%E8%AF%B4%E6%98%8E)让设备进入下载模式连接电脑，[下载 M5Burner](/zh_CN/uiflow2/uiflow_web)，在左侧选择设备类型 Chain DualKey，右侧出现 Chain DualKey User Demo，点击 Download - Burn 即可更新。更新后重新给设备供电即可生效。<br>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/M5Burner_update.png" width="70%">

## 1.按键编号

Chain DualKey 的两个按键在出厂固件中分别称为 Key1（Left Key）与 Key2（Right Key）：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Keys.jpg" width="30%">

## 2.开关位置

- **OFF USB**：开关拨到中间，Chain DualKey 未连接外部电源时为 OFF 关机，连接外部电源时为 USB 有线模式（也会开启 BLE 与 Wi-Fi）。
- **BLE / Wi-Fi**：开关拨到左边或右边，在本固件中功能相同，会开启 BLE 与 Wi-Fi。

#> 关于电池充电 | 只要连接外部电源，无论开关拨到什么位置，都会给电池充电。

## 3.作为键盘连接主机

- **有线连接**：使用 USB-C 数据线连接 Chain DualKey 与电脑、手机等主机设备。
- **蓝牙连接**：给 Chain DualKey 连接外部电源或将开关拨至左右两侧，在电脑、手机等主机设备上连接名为 `DualKey-XXXX` 的蓝牙设备（XXXX 为四位字母数字码，用于区分不同设备），出现配对码弹框直接确认即可。本固件仅支持配对、连接一个蓝牙主机。如果需要连接其他主机，请先在已配对的主机上取消配对。

Chain DualKey 可以同时通过有线和蓝牙连接两个设备。

#> 各操作系统注意事项 | **macOS**：首次连接时，系统会弹出键盘设置向导，点击`退出`跳过即可，不影响正常使用。<br>
**iOS**：连接外置键盘时，部分情况下系统会禁用触屏键盘，只能使用 Chain DualKey。<br>
**Windows**、**Android**：暂未发现特殊注意事项，具体取决于系统版本和相关设置。

## 4.配置网页

给 Chain DualKey 连接外部电源或将开关拨至左右两侧，在电脑、手机等设备上连接 Wi-Fi AP（**名称**：`DualKey_XXXX`（XXXX 为四位字母数字码，用于区分不同设备），**密码**：`12345678`），然后在浏览器中访问 `192.168.4.1`，打开配置网页：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Web_settings.png" width="70%">

- 右上角可以切换页面语言（中 / 英），查看 Wi-Fi AP 连接状态、最近更新时间。
- 中部左侧 Basic Information 区域可以设置两个按键的 LED 灯色彩，查看按键状态（按下时圆环会变成深色，如下图所示）、开关位置、电池状态。<br>
如果你将两个按键的颜色都设为纯黑色（`0, 0, 0`），两个 LED 灯实际上并不会关闭，而是会以彩虹 🌈 色彩循环变化！
- 中部中间 HID Device Status 区域可以设置两个按键的功能、开关 USB 有线映射与 BLE 蓝牙无线映射，查看 USB 和蓝牙连接状态：
  - **Copy Paste**：模拟 **Ctrl+C / Ctrl+V** 快捷键，用于 Windows 复制粘贴；
  - **Copy Paste**：模拟 **Cmd+C / Cmd+V** 快捷键，用于 macOS 复制粘贴；
  - **Undo Redo**：模拟 **Ctrl+Z / Ctrl+Y** 快捷键，用于 Windows 上某些应用的撤销重做；
  - **Undo Redo**：模拟 **Cmd+Z / Cmd+Y** 快捷键，用于 macOS 上某些应用的撤销重做；
  - **Undo Redo**：模拟 **Cmd+Z / Cmd+Shift+Z** 快捷键，用于 macOS 上某些应用的撤销重做；
  - **Tab Switch**：模拟 **Ctrl+Tab / Ctrl+Shift+Tab** 快捷键，用于 Windows 和 macOS 上某些应用（比如 Chrome 浏览器）的标签页切换；
  - **Window Switch**：两个按键分别模拟 **Alt 和 Tab** 键，按住 Alt 多次按 Tab 可以在 Windows 上切换窗口；
  - **Window Switch**：两个按键分别模拟 **Cmd 和 Tab** 键，按住 Cmd 多次按 Tab 可以在 macOS 上切换应用；
  - **Zoom**：模拟 **Ctrl+减号 / Ctrl+加号** 快捷键，用于 Windows 缩小放大；
  - **Zoom**：模拟 **Cmd+减号 / Cmd+加号** 快捷键，用于 macOS 缩小放大；
  - **Page**：模拟 **PgUp / PgDn** 翻页键，用于 Windows 和 macOS 上下翻页；
  - **Volume Control**：模拟 **音量加 / 音量减** 按键，用于 Windows 和 macOS；
  - **Media Control**：模拟 **上一曲 / 下一曲** 媒体控制键，用于 Windows 和 macOS；
  - **Media Control**：模拟 **播放暂停 / 停止** 媒体控制键，用于 Windows 和 macOS；
  - **Home Key**：模拟 **Home / End** 键；
  - **Arrow Keys**：模拟 **上 / 下** 箭头方向键；
  - **Arrow Keys**：模拟 **左 / 右** 箭头方向键。<br>
以上选项部分支持 Android、iOS，请以具体情况为准。
- 中部右侧 Wi-Fi 区域可以设置要让 Chain DualKey 连接的 Wi-Fi 网络。输入 Wi-Fi 名称、密码并设置静态 IP 地址后点击 Apply，Chain DualKey 将关闭 AP 并连接到指定的网络，电脑 / 手机可访问指定的 IP 地址打开配置网页。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Web_dualkey.png" width="70%">

#> 重置 Wi-Fi | 如果需要重置 Wi-Fi 设置，方法是：两个按键同时长按 5 秒直到 Key1 LED 熄灭、Key2 LED 点亮，松开两个按键，两个 LED 会一起红色闪烁 3 次然后交替白色闪烁 3 次，Wi-Fi 设置会被重置，即忽略已连接的网络、开启 AP 热点。<br>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Reset_network.gif" width="50%">

## 5.Chain Bus

Chain DualKey 可通过两侧的 Chain Bus 连接其他 Chain 系列设备，如 Chain Key、Chain Joystick 等。（Chain 系列设备陆续上市中。）

Chain 系列设备之间可通过 [Chain Bridge](/zh_CN/accessory/converter/Chain_Bridge) 或 [Chain Return](/zh_CN/accessory/converter/Chain_Return) 连接。连接时需要注意方向，设备底部的三角箭头从 Chain DualKey（主控）指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

在配置网页的下部可以查看、设置 Chain Bus 上各个设备的功能：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Web_chain.png" width="70%">

- 点击上方拓扑图中的设备，可以快速跳转到下方设备详情中的对应位置。
- 每个设备的详情卡片中，会显示该设备最新的触发事件、采集数据的最新值，可以修改该设备指示灯的颜色。
- 点击 HID Function Config 可以为各种触发事件分配功能。其中部分触发事件之间存在逻辑冲突（尤其是 Press、Release 与其他按键事件），分配功能时请注意。
- 某个设备有触发事件或数据更新时，该设备的详情卡片会闪烁。
- Bus RGB 指的是这一路 Chain Bus（Chain DualKey 的一侧）上所有设备的指示灯颜色。