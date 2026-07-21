# UiFlow1 文件管理

> UiFlow1 提供了文件管理功能，为开发者提供了一个统一、便捷的平台，用于处理和管理各种项目文件。

## 文件管理系统

文件管理系统分为 USB 模式和 WiFi 模式，区别如下：

- UiFlow 连接设备后，USB 模式只能读取到设备中的文件，WiFi 模式可以读取到保存在云端中的文件以及设备中的文件。
- WiFi 模式可以实现远程为设备下载程序和文件。

## USB 模式资源引用

设备在通过 USB 连接 UiFlow1 前，需要把设备的连接模式切换为 USB 模式。 方法：设备开机后，在设备界面栏 App/Flow/Setup 三个选项中选择 `Flow` 设置，点击 Flow 设置后，设备界面弹出 `choose mode(will reboot)`，选择 USB 模式即可切换 USB 模式。

### 1. 连接设备

将设备通过 USB 线连接至电脑，点击 Terminal (Beta) 按键，设备连接成功后，点击 Get 打开文件管理系统。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow01_filemanager/filemanger_01.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow01_filemanager/filemanger_03.png" width="70%"/>

在文件管理系统中，可浏览设备中保存的文件：点击 `Select` 可以选择需要上传的文件后；再点击 `Send` 可以上传电脑中的文件到设置中；点击 `Get `可以下载设备中的文件。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow01_filemanager/filemanger_02.png" width="70%"/>

### 2.Block 块引入图片

拖动 Image Block，填写图片名称以及格式，点击 Run 运行预览结果。如：CoreS3.png。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow01_filemanager/filemanger_04.png" width="70%"/>

### 3. 代码方式引入图片

找到指定修改图片的默认地址，把默认地址修改为需要展示的图片，点开 Terminal ，点击运行 (三角形) 预览结果。例如：下图中 CoreS3.png 图片地址是 flash/CoreS3.png，修改默认 image0 的引入资源，替换为 CoreS3.png 的图片路径即可。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow01_filemanager/filemanger_05.png" width="70%"/>

## WiFi 模式资源引用

设备通过 WiFi 连接至电脑前，设备需要提前开机并连接到 WiFi，当设备在线后，将设备 API Key 绑定到该账号下，实现 UiFlow1 与设备的连接。拖动图片 UI ，在图片 UI 中通过 Image Path 点击引入，可在线保存图片并在线预览。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow01_filemanager/filemanger_06.png" width="70%"/>

在 UI 编辑页，可以通过点击图片添加按钮，添加图片资源到设备中，同时，Web IDE 在连接网络的情况下，可以支持图片在线预览，同时可直接通过代码块引入。

## 视频演示 (bilibili)

<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1605881221&bvid=BV1Mm421573j&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0"></iframe>
</div>
