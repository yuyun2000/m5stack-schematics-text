# Unit ASR 自定义固件生成与烧录

基于用户实际使用的命令词和多样化语言需求，Unit ASR 离线语音识别单元可借助智能公元在线平台，灵活高效地调整命令词和回复语，并重新生成适配固件。

## 1. 准备工作

1. 账号注册：访问[智能公元平台](https://www.smartpi.cn/#/)完成账号注册与登录，并打开产品管理页面。

2. 下载产品配置模板文件 (.json)

- [Download Unit ASR Config Template Json File](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1091/Unit_ASR_Config_Template.zip)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1091/U194_Template_json.png" width="80%">

?> 语言支持 | 目前版本不支持语言混合使用，同一时刻仅能使用一种语言，如需配置不同语言可下载参考不同版本的`配置模板文件`或通过平台重新生成。

1. 使用到的硬件产品:

- [ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)
- [Unit ASR](https://shop.m5stack.com/products/asr-unit-with-offline-voice-module-ci-03t)
- [Grove Cable](https://shop.m5stack.com/products/4pin-buckled-grove-cable)

<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_03.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U914_04.webp" width="20%"><img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/accessory/cable/grove_cable/grove_cable_cover_01.webp" width="20%">

4. 使用到的软件工具:

- [Unit ASR 固件烧录工具](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/CI-03T_Serial_burning_software_V3.7.3.zip)

## 2. 配置模板

1. 点击`导入产品`，导入之前步骤下载的`产品配置模板文件(.json)`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_01.jpg" width="80%">

2. 点击`查看详情 `，选中模板进行继承。这将基于出厂固件模板生成一个新的版本用于修改。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_02.jpg" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_03.jpg" width="80%">

3. 点击`编辑`按钮，进入固件配置界面。滑动至`命令词自定义`选项，选中已有命令词复制创建新的命令。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_04.jpg" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_05.jpg" width="80%">

4. 根据实际使用的语言类型填写触发的命令与回复的命令。注意不允许出现中英混合的情况，需根据实际启用的语言进行配置。完成后，点击箭头按钮，配置当前命令详细参数。

\#> 唤醒词设置 | 模板文件中默认选取普通命令词列表中的部分指令用作`免唤醒词`(eg: Hi M Five, Hi ASR) 用于设备的唤醒交互。该功能与普通`自定义唤醒词`部分存在冲突，若同时使用，则实际唤醒时候仅触发`自定义唤醒词`的响应回复。 因此设置唤醒词功能时，请直接选取命令词列表中的指令用为`免唤醒词`即可，无需设置`自定义唤醒词`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_06.jpg" width="80%">

5. 通过参数配置实现当命令触发后，Unit ASR 通过 UART 响应的数据内容。为了兼容 [M5Unit-ASR](https://github.com/m5stack/M5Unit-ASR) Arduino 和 UiFlow2 库，请按照原有格式进行修改。格式规则为`AA 55 ID 55 AA`, 其中指令码 ID 不可与其他命令重复。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_07.jpg" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_08.jpg" width="80%">

6. 完成上述配置后就已经完成新指令 `Just` 的添加。接下来点击菜单栏的`配置检查`选项，检查是否存在错误。确认无误后点击`发布版本`进行固件打包。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_09.jpg" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_10.jpg" width="80%">

7. 等待完成固件生成，点击下载。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_11.jpg" width="80%">

## 3. 固件烧录

1. 打开之前步骤下载的 Unit ASR 固件烧录工具，确保模组型号配置正确，点击`Update`启动工具。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_12.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_13.jpg" width="50%">

2. 导入解压后的固件文件 (.bin)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_14.jpg" width="80%">

3. Unit ASR 的通信接口同时也是烧录接口，程序使用 UART 的方式进行下载。本教程使用 ESP32 Downloader 进行操作，具体线序如下所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_download_pinmap_01.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_download_pinmap_02.png" width="50%">

1. 首选连接 ESP32 Downloader 到电脑，待烧录工具检测到对应端口后，勾选端口激活下载等待。然后连接 Unit ASR，开始下载程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_15.jpg" width="80%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_16.jpg" width="50%">

5. 程序下载完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/uart_asr_gen_firmware_17.jpg" width="80%">

## 4. 命令测试

1. Unit ASR 供电
2. 使用 `Hi M Five`命令唤醒，回应 `I'm here`。
3. 使用 `Just` 命令，回应 `Do it`。
