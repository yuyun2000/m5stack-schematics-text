# UiFlow2 文件管理

> UiFlow2 提供了文件管理功能，为开发者提供了一个统一、便捷的平台，用于处理和管理各种项目文件。

## 文件管理系统

文件管理系统分为 USB 模式和 Wi-Fi 模式，区别如下：

- USB：素材资源仅在当前设备本地保存，并不保存至云端项目，不支持 IDE 在线预览，其他设备运行同一项目程序时需要手动导入相关资源。适合单一设备开发。
- Wi-Fi：素材资源将保存至项目中， 支持 IDE 在线预览， 当其同类型设备运行该程序时，将自动拉取下载相关资源。适合多设备开发情况。

## USB 模式资源引用

### 1.连接设备

将设备通过 USB 线连接至电脑，点击左侧 webterminal 按键，设备连接成功后，点击 File 打开文件管理系统。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_01.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_02.png" width="70%"/>

在文件管理系统中，可查看所有设备中存储的文件，并能对文档进行添加，删除，预览等操作。点击 `Get File` 和 `Delete` 添加或删除设置中的文件，点击 Send File to Here 上传电脑中的文件到设置储存器。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_03.png" width="70%"/>

### 2.Block 块引入图片

拖动 Image Block，填写图片名称以及格式，点击 Run 运行预览结果。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_05.png" width="70%"/>

### 3.代码方式引入图片

找到指定修改图片的默认地址，把默认地址修改为需要展示的图片，点开 WebTerminal ，点击三角形运行预览结果。例如：下图中 M5stack.png 图片地址是 flash/res/img/M5stack.png，修改默认 image0 的引入资源，替换为 M5stack.png 的图片路径即可。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_04.png" width="70%"/>

## Wi-Fi 模式资源引用

Wi-Fi 资源引用方式分为本地预览方式和云端项目引用方式，区别如下：

- 本地预览方式引入的文件资源会立即下载到当前连接的设备中，不会保存在云端项目中。
- 云端项目引用方式引入的文件资源会保存在云端项目中，且图片资源可在线预览，运行程序后，相关运行文件资源会下载到设备中。

### 1.本地预览

设备通过 Wi-Fi 连接至电脑前，设备需要提前开机并连接到 Wi-Fi，当设备在线时，在 UiFlow2 Web IDE 点击设备管理按钮，连接当前在线的需要使用的设备。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_06.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_07.png" width="70%"/>

点击设备文件管理系统，在设备文件管理系统中，可以上传项目文件以及静态资源文件，文件上传成功，都会下载到设备中，同时，设备中的文件也能在 Web IDE 中预览。注意：上传的文档应该小于 100kb，如果需要使用的文件太大，建议使用 SD 卡存储。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_08.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_09.png" width="70%"/>

### 2.云端项目引用

点击项目文件管理系统，在项目管理系统中，可以上传项目文件以及静态资源文件，文件上传成功，资源会保存在该项目中，同时，其他相同类型的设备也可共享文件资源。

> 注意：云端保存的项目是一个独立的存储空间。运行程序成功并不会把设备中的文件上传到云端项目中，但会把本次运行文件资源下载到设备中。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_12.png" width="70%"/>

在 UI 编辑页，可以通过点击图片添加按钮，添加图片资源到设备中，同时，Web IDE 在连接网络的情况下，可以支持图片在线预览，同时可直接通过代码块引入。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_10.png" width="70%"/>

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/uiflow02_filemanager/filemanger_11.png" width="70%"/>

## 视频演示(bilibili)

<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1855952936&bvid=BV1bs421M7XH&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0"></iframe>
</div>
