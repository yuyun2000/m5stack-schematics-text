# LoRaWAN470 网关与节点

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/layout.png" width="70%">

#>手把手搭建基于 M5Stack 设备的 LoRaWAN470 网关与节点 | 本教程将介绍如何通过 [M5 BASIC](/zh_CN/core/basic) 主机和 [Module LoRa (433MHz)](/zh_CN/module/lora) 实现 LoRaWAN470 网关和节点，并与 [TTN](https://www.thethingsnetwork.org) 进行通信，我们把固件放在 [Burner](/zh_CN/download)，用户可以通过 Burner 进行参数设置

## 1. 步骤一：组装

### 1.1 硬件准备

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/hardware.jpg" width="70%">

- BASIC 主机：3个(1个网关2个节点)
- Module LoRa (433MHz)：3个(1个网关2个节点)
- ENV-II Unit：2个

把433模块、ENV-II Unit 和 core 主机组装，其中两个作为LoRaWan的终端，一个作为LoRaWan的网关。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/hardware3.jpg" width="70%">

**注意**：Module LoRa (433MHz) 模块需要连接 DIO1 到 GPIO34

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/hardware2.jpg" width="70%">

## 2. 步骤二：固件烧录和配置

### 2.1 网关

#### 2.1.1 网关固件烧录和配置

打开 M5burner 应用程序，烧录网关固件

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_firmware.jpg" width="70%">

第一次烧录会提示你进入 M5BurnerNVS 进行设置, 这时我们点击按键B，就可以进入 BurnerNVS 设置程序
   
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_firmware0.jpg" width="50%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_firmware0-1.jpg" width="50%">
   
打开 M5Burner 进入 BurnerNVS 设置界面进行设置

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_firmware2.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_firmware3.jpg" width="70%">


1. 必须设置的参数
   1. WIFI_SSID: WIFI SSID
   2. WIFI_PASS: WIFI 密码

2. 其他的参数可以保持默认(**注意**：默认的频率是471.9MHz/SF7，默认的服务器是nam1.cloud.thethings.network，默认的时区是+8)
3. 完成设置后我们点击主机的B按键重启主机，至此网关固件配置完成


#### 2.1.2 在 TTN 上注册网关

1. 首先打开[TTN](https://www.thethingsnetwork.org)官网，注册账号(**注意**：图文可以查看我们的教程[ TTN(The Things Network)](/zh_CN/guide/lora/lorawan/ttn))
2. 网关的默认服务器是nam1.cloud.thethings.network
3. 必须设置的参数
   
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_ttn-1.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_ttn-2.jpg" width="70%">

1. Gateway ID: human readable string
2. Gateway EUI: 主机屏幕上的 `GW EUI` 项，基于MAC地址生成，保证全球唯一性

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_ttn.jpg" width="70%">

1. Schedule downlink late: 勾选，用于 downlink 功能
2. Frequency plan: 选择 China 470-510MHz, FSB11
3. 其他参数可以保持默认，至此网关在TTN上注册成功。

### 2.2 终端

#### 2.2.1 在 TTN 上创建节点

1. 创建应用

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node.jpg" width="70%">

2. 在该应用下创建两个入网类型为 OTAA 的节点，得到各个设备的 DEVEUI, APPEUI 和 APPKEY (**注意**：图文可以查看我们的教程 [TTN(The Things Network)](/zh_CN/guide/lora/lorawan/ttn)
   

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node2.jpg" width="70%">

3. 必须设置的参数
   1. Frequency plan: 选择 China 470-510MHz, FSB11
   2. LoRaWAN version: LoRaWAN Specifications 1.0.2
   3. Regional Parameters version: 我们选择 revision B
4. 其他的参数可以保持默认，至此节点在TTN上创建成功


#### 2.2.2 节点固件烧录和配置

1. 打开 M5burner 应用程序，烧录节点固件

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node_firmware.jpg" width="70%">

2. 点击 "info"->"burner setup" ，进入 BurnerNVS 设置程序

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node3.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node4.jpg" width="70%">

3. 打开 M5Burner 进入 BurnerNVS 设置界面进行设置

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node5.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node6.jpg" width="70%">

   
1. 必须设置的参数：
   1. APPEUI: 由 TTN 生成，可在TTN上查询
   2. DEVEUI: 由 TTN 生成，可在TTN上查询
   3. APPKEY: 由 TTN 生成，可在TTN上查询
2. 其他的参数可以保持默认(**注意**：默认八个通道都是471.9MHz，拓频因子SF7，入网模式OTAA，发送间隔20s)，至此节点固件配置完成

## 3. 步骤三：节点与 TTN 通信

### 3.1 Uplink

1. 我们使用了 CayeneLPP 库对信息进行封装，需要在TTN中把解码类型改为CayeneLPP才能看到节点上传的数据
   

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/uplink_settup.jpg" width="70%">


2. 通过上面的步骤配置完成后，节点会通过 ENV-II Unit 采集环境信息，并以20s的间隔上传到TTN上，与节点上显示的温湿度数据一致

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/uplink.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/uplink-1.jpg" width="70%">


### 3.2 Downlink

我们可以在 TTN 的网站上把下发信息加入到 downlink 队列中，这样节点在下一次的 Uplink 上传后会收到一条 Downlink 信息，节点上显示的数据与设置的数据一致

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/downlink.jpg" width="70%">


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/downlink-1.jpg" width="70%">

## 4. 步骤四：界面与 BurnerNVS 参数详解

### 4.1 网关

#### 4.1.1 gateway

开始页面:

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway-1.jpg" width="70%">

从上往下分别是：

1. 标题栏: LoRaWan470 GW

2. 状态灯: 正常工作时为绿色闪烁状态，黄色为初始化状态

3. GW EUI: 每个网关特有的 ID，由 MAC 地址生成

4. Freq: 侦听频率和拓频因子

5. Uplink: 网关上传 LoRa 数据包的数量

6. Downlink: 网关下发 LoRa 数据包的数量

7. Recently Node: 最近通信的节点地址和 RSSI

8. 按键：
   
   1. info: 可以进入信息页面。

信息页面:

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway-2.jpg" width="70%">


从上往下分别是：

1. 标题栏: LoRaWan470 GW

2. 状态灯: 正常工作时为绿色闪烁状态，黄色为初始化状态

3. WiFi SSID: WiFi ID

4. LoRaWAN Server: LoRaWAN 服务器地址

5. Port：LoRaWAN 服务器端口

6. NTP Server: NTP 服务器地址

7. Timezone: 时区

8. 按键：
   
   1. back：返回开始页面。
   
   2. burner setup: 进入 BurnerNVS 设置程序

#### 4.1.2 网关 BurnerNVS 参数

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_burner_nvs_01.png" width="70%">


1. WIFI_SSID: WIFI SSID

2. WIFI_PASS: WIFI password

3. Frequency: 网关的侦听频率，需要遵守 LoRaWAN 协议，LoRaWAN 470 的频谱范围是 470MHz 到 510MHz，具体的设定需要查看 LoRaWAN 协议，网关和节点的频率必须相同

4. SF: 拓频因子，范围是5-0，分别对应SF7到SF12，网关和节点的拓频因子必须相同

5. TTN_SERVER: LoRaWAN 服务器的地址

6. TTN_PORT: LoRaWAN 服务器的端口号

7. NTP_SERVER: NTP 服务器的地址

8. TIMEZONE: 时区

### 4.2 节点

#### 4.2.1 节点界面

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node-2.jpg" width="50%">


从上往下分别是：

1. 标题栏: LoRaWan470 Node

2. 状态灯: 正常工作时为绿色闪烁状态，黄色为初始化状态

3. CH Nums: 通道和它对应的频率

4. TX Interval: Uplink 的发送时间间隔

5. ENV-II Unit: ENV-II Unit 的状态，绿色是正常工作状态，否则是红色，右边还会显示温度和湿度

6. 按键：
   
   1. beep disable 说明喇叭处于关闭状态，按一下该按键会切换到 beep enable，这时如果收到 Downlink 消息，喇叭会响一声进行提示。
   
   2. info: 可以进入信息页面。
   
   3. uplink enable 说明 Uplink 处于使能状态，节点会以20s的间隔上传消息到TTN上，按一下该按键会切换到 uplink disable。


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node-1.jpg" width="50%">


从上往下分别是：

1. 标题栏: LoRaWan470 Node

2. 状态灯: 正常工作时为绿色闪烁状态，黄色为初始化状态

3. Spec Version: 这个是 LoRaWAN 协议的版本

4. Mode：入网模式，现在是 OTAA

5. DEVADDR：设备地址

6. 按键：
   
   1. back：返回开始页面。
   
   2. burner setup: 进入 BurnerNVS 设置程序

#### 4.2.2 节点 BurnerNVS 参数


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/burner_nvs_01.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/burner_nvs_02.png" width="70%">


1. APPEUI & DEVEUI & APPKEY: OTAA 的入网参数，由 TTN 生成

2. TX_INTERVAL: uplink 的时间间隔

3. CHANNEL0 ~ CHANNEL8: 每个通道的频率，需要遵守 LoRaWAN 协议，LoRaWAN 470 的频谱范围是 470MHz 到 510MHz，具体的设定需要查看 LoRaWAN 协议，网关和节点的频率必须相同

4. SF: 拓频因子，范围是5-0，分别对应SF7到SF12，网关和节点的拓频因子必须相同

5. POWER: 发射功率，范围是0-20，值越大功率越大，默认是20

6. ABP_ENABLE: ABP 入网模式使能。1为开启，0为关闭。如果是0即为 OTAA 入网模式，与 ABP 有关的设定无效。如果是1即为 ABP 入网模式，与 OTAA 有关的设定无效

7. NWKSKEY & APPSKEY & DEVADDR: ABP 入网的参数，可以由 TTN 生成。

8. ADR_ENABLE: ADR 使能。1为开启，0为关闭。

9. APP_PORT: 设置应用端口，范围是1-255

10. CONFIRM_MSG: 确认信息使能。1为开启，0为关闭。如果开启，每次 uplink 后都会收到一个 ACK。

## 5. 步骤五：其他应用

### 5.1 在运行中进入 BurnerNVS 程序

点击 `info` -> `burner setup`

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node3.jpg" width="50%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/node4.jpg" width="50%">


之后会进入到下面的页面，说明已经进入 Burner NVS 设置程序


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/gateway_firmware0-1.jpg" width="50%">

这时我们可以打开 Burner 应用设置 BurnerNVS

### 5.2 节点连接其他网关

当我们需要连接其他网关时，只需要修改 CHANNEL0 - CHANNEL8 的频率


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/other.jpg" width="70%">

### 5.3 节点使用ABP模式入网

如果我们需要使用ABP模式进行入网，只需要打开 ABP_ENABLE 使能

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/other_abp-1.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/other_abp.png" width="70%">

#>配置注意事项：| 需要在TTN ABP 节点管理页面下`General settings` -> `Network layer` -> `Advanced MAC settings`，把 Rx1 delay 改为5s，并把 `Resets frame counters` 选项勾上


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/abp-1.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/abp-2.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lora433/abp-3.jpg" width="70%">

