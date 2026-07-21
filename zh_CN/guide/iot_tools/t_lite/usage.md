# T-Lite使用教程 

## 产品介绍

T-Lite 是集成在线检测的热成像测温装置，由 M5StickC-Plus 与 HAT THERMAL 组成，搭载 MLX90640 红外传感器和 ESP32 主控，支持 Wi-Fi，搭配 135×240 屏及 160mAh 电池。具备高温预警，支持通过云端/局域网实时查看数据，可应用于温度检测预警、生物移动监控等场景。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_05.jpg" width="45%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_04.jpg" width="45%">


## 基础操作

### 开关机

- 单击PWR开机
- 长按PWR关机

### 切换预览模式

T-Lite支持切换界面UI布局、温度色彩显示模式和温度数值显示模式。

- 切换界面UI布局模式：长按`按键B`。
  
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_gif03.gif" width="40%">

- 切换温度色彩显示模式：单击`按键A`。
  
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_gif05.gif" width="40%">


- 切换温度数值显示模式：单击`按键B`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_gif04.gif" width="40%">
   

### 进入配置菜单

单击`PWR`按键，可进入主菜单界面。
主菜单界面说明如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_01.jpg" width="40%">


- Network：网络设置，包括运行模式设置，Wi-Fi设置等。
- Cloud：云监控设置，可设置数据上传的间隔时间。
- Alarm：报警设置。可设置报警触发的条件，包括高于设定、低于设定以及关闭报警。
- Sensor：传感器设置。包括刷新速度、噪点过滤、监视器、发射率相关的设置。
- Range：温度量程。包括打开/关闭自动量程、上限/下限温度的设置。
- Others：其他设置，包括语言设置、CPU主频设置、蜂鸣器音量、屏幕亮度、局域网视频流画质、恢复出厂设置等。

## 远程查看

### 工作模式

T-Lite提供四种查看温度的数据，分别如下：

- Offline模式 ：单机工作，仅通过设备屏幕查看。

- LAN局域网查看模式：连接Wi-Fi，局域网内通过IP访问查看。

- CLOUD模式：连接Wi-Fi， 设备将上传图像数据至Ezdata服务器，用户可通过外部网络访问查看。

- LAN + CLOUD 模式：支持局域网预览和远程图像查看。


### 网络配置

1. 单击电源键开机。
2. 单击`PWR`键，进入设置菜单。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_01.jpg" width="40%">

3. 选中`Network`，按`按键A`确定。
4. 选中Network下面的`Wi-Fi Setting`，通过`按键A`将其设置为`AP mode`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_08.jpg" width="40%">

5. 用手机或者电脑连接Wi-Fi：**T-Lite_xxx**。默认密码为：**12341234**。
  此时手机界面自动进入Wi-Fi设置界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_09.jpg" width="40%">


6. 在手机或电脑侧输入可用的Wi-Fi名称和密码，点击`save`保存。等待设备连接Wi-Fi。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_22.jpg" width="40%">


### LAN局域网预览

1. 设备连接Wi-Fi后，通过局域网访问设备IP：192.168.x.x（可在配置菜单的顶部， 或LAN Monitor选项进行查看）。
   
2. 单击`Stream Image`，输入Comfirm Code即可预览当前图像。
   
 <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_16.jpg" width="40%">


 <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_21.jpg" width="40%">


### CLOUD 云端预览

1. 设备连接Wi-Fi后，选中`Network`，单击`按键A`确定。
2. 通过`按键B`选到`cloud Online QR`选项，单击`按键A`。
3. 扫描弹出的二维码访问远程图像地址，输入Comfirm Code即可预览当前图像。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_12.jpg" width="40%">


### LAN + CLOUD 模式预览

LAN + CLOUD 模式能同时进行LAN局域网预览和CLOUD 云端预览。

操作方法：设备连接Wi-Fi后，在T-Lite设备上选中`Running Mode`，通过`按键A`将运行模式设置为`LAN+CLOUD`后，按照LAN局域网预览和CLOUD 云端预览的设置方式进行操作即可。



## 发射率配置

根据T-Lite不同的使用场景，设置对应的物体使用发射率，可提高温度检测的精确率。具体方法如下：

1. 单击`PWR键`开机。
2. 设备开机后，单击`PWR键`，进入设置菜单。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_01.jpg" width="50%">

3. 通过`按键B`选中`Sensor`，单击`按键A`确定。
4. 在Sensor的子菜单下，通过`按键B`滑动菜单，选中`Emissivity`，并单击`按键A`进入反射率设置状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_17.jpg" width="50%">

- 按键A：数值减小
- 按键B：数值增加

5. 设置完成后，单击`PWR键`保存。设置完成。


## 恢复出厂设置

#>说明|恢复出厂设置会清除所有自定义配置。

1. 单击`PWR键`开机。
2. 设备开机后，单击`PWR键`，进入设置菜单。
3. 通过`按键B`选中`Others`菜单，单击`按键A`确定。
4. 在弹出的子菜单中，通过`按键B`选中`Factory Reset`选项，单击`按键A`确定。操作完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/T-Lite_23.jpg" width="40%">