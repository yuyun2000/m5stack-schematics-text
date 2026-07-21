# Chain Key

<span class="product-sku">SKU:U206</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-key-main-pictures-10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-weight.jpg">
</PictureViewer>

## 描述

Chain Key 是 M5Stack Chain 系列中的一款 单按键输入节点。按键采用热插拔机械键盘按键设计，搭配强段落感青轴轴体，同时集成可编程 RGB LED。 适用于人机交互，智能家居控制等应用场景。

Chain Key 集成 STM32G031G8U6 核心主控，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 拓展接口，可拓展更多 Chain 系列设备，构建更加丰富的交互应用。

## 产品特性

- M5Stack Chain 系列
- 单按键输入
- STM32G031G8U6 核心主控
- 热插拔青轴机械键盘按键
- 2x RGB LED
- 采用 UART 串口级联通信协议
- 2x HY2.0-4P 拓展接口，可拓展 Chain 系列设备

## 包装内容

- 1 x Chain Key
- 1 x Chain Bridge
- 1 x 键帽贴纸

## 应用场景

- 智能家居控制
- 人机交互

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32G031G8U6         |
| 输入电源 | DC 5V                 |
| 通信方式 | UART 115200bps@8N1    |
| 接口规格 | 2x HY2.0-4P           |
| RGB LED  | 2x WS2812B            |
| 工作功耗 | 28.24mA               |
| 工作温度 | 0 ~ 40°C              |
| 产品尺寸 | 23.9 x 23.9 x 34.4mm  |
| 产品重量 | 9.1g                  |
| 包装尺寸 | 138.0 x 93.0 x 26.0mm |
| 毛重     | 14.4g                 |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain Key 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-SCH_Chain-Key_SCH_Main_V1.0_20250823_2025_09_30_21_04_28.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-SCH_Chain-Key_SCH_Main_V1.0_20250823_2025_09_30_21_04_28_page_01.png">
</SchViewer>

## 管脚映射

### RGB LED

| STM32G031 | PA8 |
| --------- | --- |
| WS2812C   | RGB |

### Button

| STM32G031 | PB0   |
| --------- | ----- |
| Button    | Input |

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain Key模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-model-size-chain-key.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-model-size-chain-key_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain Key Arduino 上手教程](/zh_CN/arduino/projects/chain/chain_key)
- [Chain Key Arduino 驱动库](https://github.com/m5stack/M5Chain)
- [Chain Key 测试程序](https://github.com/m5stack/M5Chain/tree/main/examples/Key_Example)

### UiFlow2

- [Chain Key UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/chain/key.html)

### 内置固件

- [Chain Key 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-Key)

### 通信协议

- [Chain Key通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/M5Stack-Chain-Key-Protocol-CN.pdf) <!--注意中英文链接不一样-->

## 相关视频

- Chain Key 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-Chain-Key-video-ZH.mp4" type="video/mp4"></video> <!--注意中英文链接不一样-->

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115732641743263&bvid=BV1WLq3BaESF&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/pPNE2FIrDk4?si=1MRxFTNT8tbSY920" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
