# Module ASR 自定义固件生成与烧录

基于用户实际使用的命令词和多样化语言需求，Module ASR 离线语音识别单元可借助智能公元在线平台，灵活高效地调整命令词和回复语，并重新生成适配固件。

## 1.准备工作

1. 账号注册: 访问[智能公元平台](https://www.smartpi.cn/#/)完成账号注册与登录，并打开`产品管理`页面点击`所有产品`项。

2. 下载产品配置模板文件(.json)：下方链接中有中英两个版本的配置模板文件，请根据实际使用语言使用对应的模板文件，后续可基于模板进行固件定制化修改。

- [Download Module ASR Config Template Json File](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR-Config-Template.zip)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147_Template_json.png" width="80%">

?>语言支持|目前版本不支持语言混合使用，同一时刻仅能使用一种语言，如需配置不同语言可下载参考不同版本的`配置模板文件`或通过平台重新生成。

3. 硬件:

- Module ASR 仅需使用 USB Type-C 数据线连接至电脑即可进行烧录。

4. 使用到的软件工具:

- [Module ASR 固件烧录工具](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/CI-03T_Serial_burning_software_V3.7.3.zip)

## 2.配置模板

1\. 点击`导入产品`，导入之前步骤下载的产品配置模板文件(.json)，此教程以英文版本为例。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_0.png" width="80%">

2\. 点击`查看详情`，选中模板进行`继承`，这将基于出厂固件模板生成一个新的版本用于修改。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_1.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_2.png" width="80%">

3\. 点击`编辑`按钮，进入固件配置界面。滑动至`命令词自定义`选项，点击`+添加一条`创建新的命令。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_3.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_4.png" width="80%">

4\. 根据实际使用的语言类型填写触发的命令与回复的命令。**注意不允许出现多语言混合的情况**，需根据实际启用的语言进行配置。完成后，点击箭头按钮（`>>`），然后点击`+添加控制`配置当前命令详细参数。

#>唤醒词设置|模板文件中默认选取普通命令词列表中的部分指令用作`免唤醒词`(eg: Hi M Five, Hi ASR)用于设备的唤醒交互。该功能与普通`自定义唤醒词`部分存在冲突，若同时使用，则实际唤醒时候仅触发`自定义唤醒词`的响应回复。 因此设置唤醒词功能时，请直接选取命令词列表中的指令用为`免唤醒词`即可，无需设置`自定义唤醒词`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_5.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_6.png" width="80%">

#> 说明 | 若想配置其他触发方式（如串口输入、GPIO 输入等），可在上图中`命令词`一栏更改选择其他触发方式。

5\. 通过参数配置实现当语音命令触发后，Module ASR 模块通过 UART 响应的数据内容。为了兼容 [M5Unit-ASR](https://github.com/m5stack/M5Unit-ASR) Arduino 库，请按照原有格式进行修改。格式规则为`AA 55 ID 55 AA`, 其中**指令码 ID 唯一**，不可与其他命令重复。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_7.png" width="80%">

6\. 完成上述配置后就已经完成新指令 `Add` 的添加。接下来点击菜单栏的`配置检查`选项，检查是否存在错误。确认无误后点击`发布版本`进行固件打包。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_8.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_9.png" width="80%">

7\. 版本发布需要等待几分钟，等待完成固件生成后，点击`下载固件`，固件压缩包名称为 **jx_firm.tar.gz**。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_10.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_11.png" width="80%">

## 3.固件烧录

1\. 打开之前步骤下载的 Module ASR 固件烧录工具(.exe)，确保产品型号为 `CI1302`，点击 `Update` 启动工具。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_12.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_13.png" width="80%">


2\. 导入解压后的固件文件(.bin)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_14.png" width="80%">

3\. 烧录操作

Module ASR 烧录接口为 USB Type-C 接口，请通过此端口将模块连接至电脑。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_typec.jpg" width="40%">

待烧录工具检测到对应端口后，勾选端口激活下载等待，然后按一下 `Debug Rst` 按键，开始下载程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_15.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_debug_rst.png" width="40%">

4. 程序下载完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_firmware_16.png" width="80%">

#> 注意 | 烧录完成后，请及时取消勾选端口，否则烧录软件会一直重复烧录固件。

## 4.命令测试

给 Module ASR 模块供电，使用 `Hi M Five`命令唤醒，回应 `I'm here`，说明固件烧录成功。


