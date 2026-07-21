# PowerHub 出厂固件使用教程

PowerHub 是一款集成多路电源管理的可编程控制器。它的出厂固件功能丰富，可使用按键控制各接口的通断，通过 Wi-Fi 连接至 EZData 服务器，在手机 app 或者网页上方便地对各接口设置通断、监测电压电流、设定定时任务等。

## 1.按键与指示灯

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/button.png" width="45%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/light.png" width="45%">

- **按键**
  - **BtnPWR**：左侧灰色按钮
  - **BtnSEL**：正面右侧的黄色圆形小按钮
  - **BtnOK**：正面与天线相邻的半透明矩形按钮
- **指示灯**
  - **USB-C 接口指示灯**：与 USB-C 接口相邻的彩色指示灯
  - **USB-A 接口指示灯**：与 USB-A 接口相邻的彩色指示灯
  - **PORT.UART 接口指示灯**：与 PORT.UART <span style="color:blue">**蓝色**</span>接口相邻的彩色指示灯
  - **CAN/RS485 接口指示灯**：与 CAN / RS485 接口相邻的彩色指示灯
  - **PORT.I2C 接口指示灯**：与 PORT.I2C <span style="color:red">**红色**</span>接口相邻的彩色指示灯
  - **BtnSEL 指示灯**：与 BtnSEL 按键相邻的彩色指示灯
  - **BtnOK 指示灯**：BtnOK 按键内部的彩色指示灯

## 2.开关机

- **BtnPWR 短按**：关机时开机，开机时重启，启动时 BtnOK 指示灯会**闪烁两次**<span style="color:green">**绿色**</span>
- **BtnPWR 双击**：关机
- **BtnPWR 长按**：进入 Boot 启动模式，BtnOK 指示灯会**闪烁多次**<span style="color:blue">**蓝色**</span>

## 3.电池状态

BtnOK 指示灯会显示电池充电与电量状态：

- <span style="color:green">**绿色**</span>**常亮**：正在充电，电量充足
- <span style="color:green">**绿色**</span>**闪烁**：正在充电，电量不足
- <span style="color:red">**红色**</span>**常亮**：未在充电，电量充足
- <span style="color:red">**红色**</span>**闪烁**：未在充电，电量不足
- **白色常亮**：电池未检测到或电压过低

?> 注意 | 使用 USB C-C 线通过 PD 协议为 PowerHub 供电时，供电电压会高于 5V，可能造成无电池时电池检测异常、有电池时电池充电发热等问题。

## 4.通过按键设置各路通断

**基本步骤**：PowerHub 处于工作状态 - 进入设置状态 - 选择要设置的接口 - 设置接口通断

- **PowerHub 处于工作状态**：五个接口指示灯（不包括按键指示灯）不闪烁，以<span style="color:green">**绿色**</span>或<span style="color:red">**红色**</span>**常亮**。<span style="color:green">**绿色**</span>表示对应接口断开，<span style="color:red">**红色**</span>表示对应接口接通，<span style="color:red">**红色**</span>的亮度与对应接口当前负载成正比。
- **进入设置状态**：在工作状态下，**短按 BtnSEL 或 BtnOK** 进入设置状态。进入设置状态后，会有部分或全部接口指示灯开始（以<span style="color:green">**绿色**</span>或<span style="color:red">**红色**</span>）**快速闪烁**。在设置状态 5 秒钟无按键操作，会自动退出设置状态，回到工作状态。
- **选择要设置的接口**：在设置状态下，**快速闪烁**的接口指示灯代表对应接口被选中、可设置通断。**短按 BtnSEL** 切换要设置的接口，顺序为 USB-A/USB-C（两个接口同时控制）- PORT.UART - CAN/RS485（两个接口同时控制）- PORT.I2C - 以上接口全部选中，依次循环。
- **设置接口通断**：接口被选中可设置通断时，**短按 BtnOK** 设置该接口的通断状态，对应接口指示灯<span style="color:green">**绿色**</span>**闪烁**为断开，<span style="color:red">**红色**</span>**闪烁**为接通。

## 5.通过 EZData 使用设备

EZData 是 M5Stack 提供的 IoT 云端数据储存服务，可将不同设备、不同类型的数据汇集到云端服务器，方便存取读写、远程控制、历史统计等需求。

### (1)EZData 账号准备

- 对于 iPhone、iPad、Mac 等苹果设备，可以在 App Store 搜索下载安装 EZData app（版本**不低于 1.0.7**）。进入 app 后点击右上角的 Register 注册 M5Stack 账号，并在 app 中登录账号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/EZData_iOS_register.png" width="25%">

- 对于 Android、Windows、Linux 等其他设备，可以访问 [此链接](https://community.m5stack.com/register) 注册 M5Stack 账号。

### (2)连接 Wi-Fi

**长按 BtnSEL 7 秒**直到 BtnSEL 指示灯<span style="color:blue">**蓝色**</span>**闪烁**，PowerHub 进入配网模式，会创建名为`PowerHub-XXXX`的 Wi-Fi AP。

用手机或电脑等设备连接此 AP，会自动弹出配置页面。如果没有弹出，可以在浏览器输入`192.168.4.1`打开配置页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/WiFi_setup.jpg" width="25%">

在配置页面中输入要连接的 Wi-Fi 名称、密码，根据需要修改设备名称、与服务器通信间隔、所在时区等配置，点击`Start`确认配置后点击`Yes`，PowerHub 将重启并连接到刚才输入的 Wi-Fi 网络。

BtnSEL 指示灯会显示 Wi-Fi 与 EZData 连接状态：

- <span style="color:blue">**蓝色**</span>**闪烁**：配网模式，AP 开启
- <span style="color:red">**红**</span><span style="color:blue">**蓝**</span>**交替闪烁**：Wi-Fi 连接失败
- <span style="color:red">**红**</span><span style="color:purple">**紫**</span>**交替闪烁**：Wi-Fi 连接成功，EZData 连接中
- <span style="color:purple">**紫色**</span>**常亮**：EZData 连接成功
- <span style="color:purple">**紫色**</span>**闪烁一次**：与服务器通信

### (3)绑定到 EZData 账号

PowerHub 成功通过 Wi-Fi 连接到 EZData 服务器后，手机或电脑上的配置页面将会显示如下内容：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/EZData_connect.png" width="25%">

- 苹果设备可以**长按**`EZData://`开头的链接，选择在 EZData app 中绑定此 PowerHub；或者截图后打开 EZData app，点击底部 Data 页面右上角的扫描二维码按钮，绑定此 PowerHub。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/EZData_open.png" width="25%">

- 非苹果设备可以在浏览器中打开`HTTPS://`开头的链接，登录 EZData 账号后绑定此 PowerHub。

### (4)EZData app 操作

在苹果设备的 EZData app 中绑定 PowerHub 后，点击底部的 Data 页面并在顶部切换到 PowerHub 设备即可看到各项数据。点击每个项目可以查看详情、编辑配置，如下图所示点击 USB 并将 switch 的值设为 1 即可接通 USB（USB-A + USB-C）接口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/EZData_iOS_data.png" width="50%">

EZData app 支持通过 iOS 桌面小组件快捷控制设备。在 iOS 桌面长按空白处，点击左上角的编辑 - 添加小组件，搜索或在下方列表中找到 EZData，将其中的 Data PowerHub 小组件添加到桌面。在桌面长按新添加的小组件，点击编辑小组件，在 Select Group 中选择 powerhub 开头的设备，回到桌面即可在小组件中快速查看各通道状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/EZData_iOS_widget.png" width="95%">

### (5)网页操作

在浏览器网页中绑定 PowerHub 后，可以查看及控制各通道状态、设定定时任务等。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/PowerHub_web.png" width="50%">

#> 电池电流 | 电池电流值正数代表电池放电输出，负数代表电池充电输入。