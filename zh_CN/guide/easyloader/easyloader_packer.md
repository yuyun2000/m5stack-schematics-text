# EasyLoader Packer

## 使用说明

通过 M5Stack EasyLoader Packer 工具，可将.bin 格式固件打包为集成 esptool 的.exe 可执行文件，以简化烧录固件的流程。

## 操作步骤

1. 访问[EasyLoader Packer工具](https://tools.m5stack.com/easyloader-packer/)。

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/easyloader_packer/easyloader_packer_01.webp" width="70%">

2. 单击界面左边的`UI Settings`，可以设置窗体标题、主标题、字体颜色和背景颜色。在右侧预览框中会实时显示生成效果 。

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/easyloader_packer/easyloader_packer_02.webp" width="70%">

3. 单击界面左边的`Burn Settings`，进入烧录设置界面。

- 在`BaudRate Supported`下面可添加 / 删除波特率，不修改则保持默认。
- 在 `File` 中输入固件烧录的起始地址；单击 `Choose File` 上传 .bin 格式的固件。如果需要烧录多个固件到同一台设备，可以单击 `Add`添加其他固件。

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/easyloader_packer/easyloader_packer_03.webp" width="70%">

4. 单击 界面左下角的`Make`按钮，上传并编译 .exe，完成后单击 Download 下载到本地。

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/easyloader_packer/easyloader_packer_04.webp" width="50%">

## 烧录固件

1. 双击打开已经生成的.exe 文件，选择设备对应的端口和波特率。

2. 单击 Burn 烧录固件，等待烧录完成即可。

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/easyloader_packer/easyloader_packer_05.webp" width="70%">

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/easyloader_packer/easyloader_packer_06.webp" width="70%">
