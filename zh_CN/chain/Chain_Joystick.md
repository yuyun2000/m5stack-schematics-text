# Chain Joystick

<span class="product-sku">SKU:U205</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-joystick-main-pictures-10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-weight.jpg">
</PictureViewer>

## 描述

Chain Joystick 是 M5Stack Chain 系列中的一款 高精度霍尔电磁摇杆输入节点。支持三轴控制信号输入，其中包括 X/Y 轴的模拟量输入和 Z 轴的按键数字量输入。设备选用霍尔电磁摇杆，通过检测磁场变化实现高精度控制，具有无接触、耐磨损、精度高、抗干扰能力强等优点，确保了产品的稳定性和长寿命。同时集成可编程 RGB LED 用于状态指示和交互显示。适用于人机交互，机器人控制等应用场景。

Chain Joystick 集成 STM32G031G8U6 核心主控，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 拓展接口，可拓展更多 Chain 系列设备，构建更加丰富的交互应用。

## 产品特性

- M5Stack Chain 系列
- 高精度霍尔电磁摇杆
- STM32G031G8U6 核心主控
- X/Y/Z 三轴输入
- 1x RGB LED
- 采用 UART 串口级联通信协议
- 2x HY2.0-4P 拓展接口，可拓展 Chain 系列设备

## 包装内容

- 1 x Chain Joystick
- 1 x Chain Bridge

## 应用场景

- 机器人控制
- 人机交互

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32G031G8U6         |
| 输入电源 | DC 5V                 |
| 通信方式 | UART 115200bps@8N1    |
| 接口规格 | 2x HY2.0-4P           |
| RGB LED  | 1x WS2812C            |
| 工作功耗 | 25.4mA                |
| 工作温度 | 0 ~ 40°C              |
| 产品尺寸 | 23.9 x 23.9 x D30.4mm |
| 产品重量 | 8.6g                  |
| 包装尺寸 | 138.0 x 93.0 x 25.0mm |
| 毛重     | 12.0g                 |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain Joystick 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-SCH_Chain-Joystick_SCH_Main_V1.0_2025_09_29_23_34_52.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-SCH_Chain-Joystick_SCH_Main_V1.0_2025_09_29_23_34_52_page_01.png">
</SchViewer>

## 管脚映射

### RGB LED

| STM32G031 | PA8 |
| --------- | --- |
| WS2812C   | RGB |

### Joystick

| STM32G031 | PB0   | PA7  | PA6  |
| --------- | ----- | ---- | ---- |
| Button    | Input | XOUT | YOUT |

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain Joystick模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Model-size-chain-joystick.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Model-size-chain-joystick_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain Joystick Arduino 上手教程](/zh_CN/arduino/projects/chain/chain_joystick)
- [Chain Joystick Arduino 驱动库](https://github.com/m5stack/M5Chain)
- [Chain Joystick 测试程序](https://github.com/m5stack/M5Chain/tree/main/examples/Joystick_Example)

### UiFlow2

- [Chain Joystick UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/chain/joystick.html)

### 内置固件

- [Chain Joystick 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-Joystick)

### 通信协议

- [Chain Joystick通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/M5Stack-Chain-Joystick-Protocol-CN.pdf) <!--注意中英文链接不一样-->

## 相关视频

- Chain Joystick 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-Chain-Joystick-video-ZH.mp4" type="video/mp4"></video> <!--注意中英文链接不一样-->

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115732641743411&bvid=BV1WLq3BaEo5&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/GUrXaVJ0kPQ?si=Rvtm4RkBZsHzDojZ" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
