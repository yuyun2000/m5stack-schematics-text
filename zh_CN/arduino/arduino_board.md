# Arduino 板管理

\#>Arduino 板管理介绍：| **Arduino IDE**板管理用于记录开发板的配置信息与开发过程使用到的工具链，参考下方教程安装 M5Stack 板管理，使用在线安装方式较为简单，可一键安装。部分区域若遇到网络因素影响无法正常下载，可尝试切换移动网络或是点击在首选项菜单中配置代理。

## 1. 安装板管理

**1. 板管理 URL 用于索引指定平台的开发板信息，在 Arduino IDE 菜单栏中选择 `文件`->`偏好设置`**

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/arduino/arduino_ide_02.webp" width="70%">

**2. 复制下方的 M5Stack 板管理 URL 到 `附加开发板管理 URLs:` 中**，并保存。

```shell
https://static-cdn.m5stack.com/resource/arduino/package_m5stack_index.json
```

\#> 中国地区镜像资源 | 中国用户使用以上链接时可能会遇到连接和下载速度问题，可改用以下镜像资源 URL。

```shell
https://static-cdn.m5stack.com/resource/arduino/package_m5stack_index_cn.json
```

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/arduino/arduino_ide_03.webp" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_ide_board_url.jpg" width="70%">

**3. 在侧边栏中选择 `开发板管理器`, 搜索`M5Stack`, 并点击`安装`。**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Arduino_board.png" width="70%">

## 2. 选择开发板

**根据使用的产品，在`Tools`->`Board`->`M5Stack`->`{Product Name}`选中对应的开发板**。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Arduino_selectboard.png" width="70%">

\#> 开发板选项 | 板管理列表中可能并未包含最新的开发板选项，若未有对应产品的板子选项，`可选择相同芯片类型的板子进行程序编译`，如`M5Dial`使用的是`ESP32S3`芯片，因此可使用 M5StampS3 板子选项用于编译。

## 3. 手动安装板管理

\#> 手动安装板管理 | 若因为网络因素导致无法正常下载 M5Stack 板管理，可通过以下方式手动安装。

**1. 下载板管理压缩包**

- [Google 云端硬盘 - M5Stack板管理](https://drive.google.com/drive/folders/1p-mJ30os1rCQcKgcM2imAXZkGNUZWEzY)
- [百度网盘 - M5Stack板管理, 提取码：f7rd](https://pan.baidu.com/s/1KspFcwiw-C2YSdvZeiKmDA?pwd=f7rd)

**2. 解压板管理压缩包**, 将下载下来的 M5Stack 板管理包，解压放置到以下路径。

- Windows OS（在文件资源管理器的地址栏中输入以下路径，按回车即可直接进入对应目录）：

```shell
%USERNAME%\AppData\Local\Arduino15\packages
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Arduino_board_manual.png" width="70%">

- Mac OS（注意修改路径`<Username>`为实际的用户名）：

```shell
/Users/<Username>/Library/Arduino15/packages
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/arduino_tutorial_01.png" width="70%">

\#> 特别提醒：| 解压后的文件夹名必须为 `m5stack` ，否则将无法使用相关库文件。

**3. 重启 Arduino IDE** 即可看到 M5Stack 控制板。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Arduino_selectboard_manual.png" width="70%">
