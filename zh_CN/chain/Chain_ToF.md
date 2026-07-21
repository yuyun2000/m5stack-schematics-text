# Chain ToF

<span class="product-sku">SKU:U209</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209-weight.jpg">
</PictureViewer>

## 描述

Chain ToF 是 M5Stack Chain 系列中的一款激光测距传感器节点。设备内置 VL53L0C 激光测距模块，支持 3 ~ 200cm 测距范围，测量精度 ±3%，适用于短距离的隔空测距，或是物体接近检测等功能应用。
Chain ToF 集成 STM32G031G8U6 核心主控，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 拓展接口，可拓展更多 Chain 系列设备，构建更加丰富的交互应用。

## 产品特性

- M5Stack Chain 系列
- VL53L0C 激光测距模块
- 3 ~ 200cm 测距范围
- STM32G031G8U6 核心主控
- 采用 UART 串口级联通信协议
- 2x HY2.0-4P 拓展接口，可拓展 Chain 系列设备

## 包装内容

- 1 x Chain ToF
- 1 x Chain Bridge

## 应用场景

- 接近检测
- 距离测量

## 规格参数

| 规格         | 参数                                                                                                           |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| MCU          | STM32G031G8U6                                                                                                  |
| 激光测距模块 | VL53L0C                                                                                                        |
| 测距范围     | 3 ~ 200cm                                                                                                      |
| 测距精度     | ±3%                                                                                                            |
| 输入电源     | DC 5V                                                                                                          |
| 通信接口     | UART                                                                                                           |
| 接口规格     | 2x HY2.0-4P                                                                                                    |
| RGB LED      | 1x WS2812C                                                                                                     |
| 功耗         | 停止模式（白色 RGB 开启）：DC 5V@21.27mA<br>默认模式单次测距：DC 5V@20.26mA<br>默认模式连续测距：DC 5V@24.75mA |
| 工作温度     | 0 ~ 40°C                                                                                                       |
| 产品尺寸     | 23.9 x 23.9 x 16.0mm                                                                                           |
| 产品重量     | 5.8g                                                                                                           |
| 包装尺寸     | 138.0 x 93.0 x 14.0mm                                                                                          |
| 毛重         | 9.0g                                                                                                           |

## 操作说明

### 测试距离

\#> 测量环境 | 常规环境下，最大测试距离为 120cm；如果测试距离要到达 200cm， 需要设置 Long Range 模式且需处于无红外线干扰的黑暗环境下。

### 连接说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain ToF 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_Chain-ToF_SCH_Main_V1.0_20250515_2025_10_30_22_09_27.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_Chain-ToF_SCH_Main_V1.0_20250515_2025_10_30_22_09_27_page_01.png">
</SchViewer>

## 管脚映射

### RGB LED

| STM32G031 | PA8 |
| --------- | --- |
| WS2812C   | RGB |

### ToF

| STM32G031 | PA11 | PA12 |
| --------- | ---- | ---- |
| VL53L0C   | SCL  | SDA  |

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain ToF 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209-model-size-Chain-ToF.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209-model-size-Chain-ToF_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain ToF Arduino 上手教程](/zh_CN/arduino/projects/chain/chain_tof)
- [Chain 系列产品 驱动库](https://github.com/m5stack/M5Chain)

### UiFlow2

- [Chain ToF UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/chain/tof.html)

### 内置固件

- [Chain ToF 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-ToF)

### 通信协议

- [Chain ToF 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/M5Stack-Chain-ToF-Protocol-CN.pdf) <!--注意中英文链接不一样-->

## 相关视频

- Chain ToF 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209-Chain-ToF-video-ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115960073749695&bvid=BV1cfzYB8EEn&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/uk3gHfI6utI?si=QiU4aAuu6y_U3gBj" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>