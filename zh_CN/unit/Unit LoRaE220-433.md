# Unit LoRaE220-433

<span class="product-sku">SKU:U170-433</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT_LoraE220(433MHz)/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT_LoraE220(433MHz)/8.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/847/U170-433-package.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT_LoraE220(433MHz)/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT_LoraE220(433MHz)/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT_LoraE220(433MHz)/7.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/847/U170-433_weight.jpg">
</PictureViewer>

## 描述

**Unit LoRaE220-433** 是 M5Stack 推出的适用于 433MHz 频段的 LoRa 通讯单元，采用 LLCC68 芯片方案。与传统的 SX1278 方案相比，LLCC68 具有传输距离更远、速度更快、功耗更低的优点。该单元支持空中唤醒、载波监听和通信密钥等功能，通过便捷的串口通信方式实现点对点发射模式和广播模式。模块通过板载拨码开关可切换四种不同的工作模式，用户无需复杂配置即可实现数据的发送和接收，满足各种通信需求。适用于家庭安防报警、楼宇自动化、智能家居以及汽车行业等应用场景。

## 产品特性

- 采用 LLCC68 芯片方案
- 最大发射功率 22dBm，软件多级可调
- 支持用户自行设定通信密钥
- 支持空中唤醒
- 支持定点传输、广播传输、信道监听
- 通信频段：支持 433MHz 频段 (410.125～493.125MHz)
- 板载拨码开关调节通讯模式
- 串口通信

## 包装内容

- 1 x LoRaE220-433 Unit
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 胶棒天线 (@2.5dBi 总长 110mm SMA 内针)

## 应用场景

- 家庭安防报警及远程无钥匙进入
- 智能家居以及工业传感器等
- 无线报警安全系统
- 楼宇自动化解决方案
- 无线工业级遥控器
- 医疗保健产品
- 高级抄表架构 (AMI)
- 汽车行业应用

## 规格参数

| 规格         | 参数                                                      |
| ------------ | --------------------------------------------------------- |
| Lora 模块    | E220-400T22S@LLCC68                                       |
| 支持频段     | 默认 433Mhz (支持 410.125～493.125MHz)                    |
| 最大发射功率 | 22dBm，软件多级可调                                       |
| 接收灵敏度   | -129 dBm                                                  |
| 供电电压     | 5V                                                        |
| 通讯方式     | 串口通信 (115200)                                         |
| 工作模式     | 传输模式<br/>WOR 发送 模式<br/>WOR 接收 模式<br/>休眠模式 |
| 天线         | 胶棒天线 (@2.5dBi 总长 110mm SMA 内针)                    |
| 工作温度     | 0 ~ 40°C                                                  |
| 产品尺寸     | 71.4 x 24.0 x 8.0mm                                       |
| 产品重量     | 19.5g                                                     |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm                                      |
| 毛重         | 24.9g                                                     |

## 操作说明

### 工作模式配置

Unit LoRaE220-433 工作模式

| 工作模式 (0-3)      | M0，M1         | 模式说明                                               |
| ------------------- | -------------- | ------------------------------------------------------ |
| 0: 发送接收传输模式 | M0:OFF，M1:OFF | 正常数据包收发模式                                     |
| 1:WOR 发送模式      | M0:ON，M1:OFF  | 发送 WOR 数据包，该模式同时支持数据接收 (支持空中唤醒) |
| 2:WOR 接收模式      | M0:OFF，M1:ON  | 关闭数据发送，该模式仅支持 WOR 数据包接收              |
| 3: 参数配置模式     | M0:ON，M1:ON   | 切换至配置模式，用于配置模组发射功率，信道，地址等信息 |

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT_LoraE220(433MHz)/5.jpg" width="100%" />

\#> 由于开关丝印原因，上表中所说的 "ON" 对应数据手册中的状态 "0"，"OFF" 对应数据手册中的状态 "1"。

\#> 注意供电电压不要超过 5.5V，否则超过 5.5V 可能永久烧毁模块.

## 原理图

- [Unit LoRaE220-433 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/624/SCH_UNIT_LoraE220_433MHz.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/624/SCH_UNIT_LoraE220_433MHz_sch_01.png">
</SchViewer>

## 管脚映射

### Unit LoRaE220-433

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit LoRaE220-433/img-675ca98f-ee4c-4acf-8a83-540ce2ab7336.jpg" width="100%" />

## 数据手册

- [LORA Module_E220-400T22S](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT_LoraE220(433MHz)/E220-400T22S_UserManual_CN_v1.4.pdf>)

## 软件开发

### Arduino

- [Unit LoRaE220-433 Arduino 驱动库](https://github.com/m5stack/M5-LoRa-E220)

### UiFlow2

- [Unit LoRaE220-433 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/lora_e220_433.html)

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT_LoraE220(433MHz)/U170-433%20LoRaE220-433%20Unit%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114022473007765&bvid=BV1QbAceXEnz&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/HywSUQ65LEM?si=CFOjdDbflfWef41S" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

### LoRa Unit

| 产品名称            | SKU      | 芯片方案            | 频段    | 最大发射功率 | 接收灵敏度 | 数据传输速率   | 理论通信距离 | 天线接口     | 协议类型 | 典型适用地区                                                             |
| ------------------- | -------- | ------------------- | ------- | ------------ | ---------- | -------------- | ------------ | ------------ | -------- | ------------------------------------------------------------------------ |
| LoRaE220-433 Unit   | U170-433 | E220-400T22S@LLCC68 | 433 MHz | 22 dBm       | -129 dBm   | 2.4k-62.5 kbps | 5 km         | 外接胶棒天线 | LoRa     | 欧盟国家，加拿大，美国，中国，日本，澳大利亚，新西兰，南美，南非，中东等 |
| LoRa-e220-JP unit   | U170     | E220-900T22S@LLCC68 | 920 MHz | 13 dBm       | -124 dBm   | 1.7k-62.5 kbps | 5 km         | 外接胶棒天线 | LoRa     | 日本，韩国，美国，巴西，澳大利亚，新西兰，欧洲等                         |
| LoRaWAN Unit 868MHz | U117     | ASR6501@SX1262      | 868 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN  | 欧盟国家，俄罗斯，中东，印度等                                           |
| Unit LoRaWAN915     | U115     | ASR6501@SX1262      | 915 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN  | 美国，加拿大，澳大利亚，新西兰，巴西，阿根廷，台湾，日本，以色列等       |
| Unit LoRaWAN470     | U116     | ASR6501@SX1262      | 470 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN  | 中国                                                                     |

### LoRa Module

| 产品名称            | SKU      | 芯片方案       | 频段    | 最大发射功率 | 接收灵敏度 | 数据传输速率   | 理论通信距离 | 天线接口     | 协议类型     | 典型适用地区                                                             |
| ------------------- | -------- | -------------- | ------- | ------------ | ---------- | -------------- | ------------ | ------------ | ------------ | ------------------------------------------------------------------------ |
| Module-LoRa868_V1.1 | M029-V11 | Ra-01H@SX1276  | 868 MHz | 19 dBm       | -148 dBm   | UP to 300 kbps | 2-5 km       | 外接胶棒天线 | LoRa         | 欧盟国家，俄罗斯，中东，印度等                                           |
| Module-LoRa433_V1.1 | M005-V11 | Ra-02@SX1278   | 433 MHz | 18 dBm       | -141 dBm   | UP to 300 kbps | 2-5 km       | 外接胶棒天线 | LoRa         | 欧盟国家，加拿大，美国，中国，日本，澳大利亚，新西兰，南美，南非，中东等 |
| Module LoRa 433MHz  | M005     | Ra-02@SX1278   | 433 MHz | 18 dBm       | -141 dBm   | UP to 300 kbps | 2-5 km       | FPC 天线     | LoRa         | 欧盟国家，加拿大，美国，中国，日本，澳大利亚，新西兰，南美，南非，中东等 |
| Module LoRa868      | M029     | Ra-01H@SX1276  | 868 MHz | 19 dBm       | -148 dBm   | UP to 300 kbps | 2-5 km       | FPC 天线     | LoRa         | 欧盟国家，俄罗斯，中东，印度等                                           |
| COM.LoRaWAN 868     | M031-C   | ASR6501@SX1262 | 868 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN      | 欧盟国家，俄罗斯，中东，印度等                                           |
| COM.LoRaWAN470      | M031-C2  | ASR6501@SX1262 | 470 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN      | 中国                                                                     |
| COM.LoRaWAN868 v2.0 | M031-C4  | ASR6501@SX1262 | 868 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN      | 欧盟国家，俄罗斯，中东，印度等                                           |
| COM.LoRaWAN915      | M031-C3  | ASR6501@SX1262 | 915 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRa/LoRaWAN | 美国，加拿大，澳大利亚，新西兰，巴西，阿根廷，台湾，日本，以色列等       |

### LoRa Atom DTU

| 产品名称            | SKU  | 芯片方案       | 频段    | 最大发射功率 | 接收灵敏度 | 数据传输速率   | 理论通信距离 | 天线接口     | 协议类型 | 典型适用地区                                                       |
| ------------------- | ---- | -------------- | ------- | ------------ | ---------- | -------------- | ------------ | ------------ | -------- | ------------------------------------------------------------------ |
| ATOM DTU LoRaWAN915 | K061 | ASR6501@SX1262 | 915 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN  | 美国，加拿大，澳大利亚，新西兰，巴西，阿根廷，台湾，日本，以色列等 |
| ATOM DTU LoRaWAN868 | K063 | ASR6501@SX1262 | 868 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN  | 欧盟国家，俄罗斯，中东，印度等                                     |
| ATOM DTU LoRaWAN470 | K062 | ASR6501@SX1262 | 470 MHz | 21 dBm       | -136 dBm   | 0.3k-37.5 kbps | 2-5 km       | 外接胶棒天线 | LoRaWAN  | 中国                                                               |
