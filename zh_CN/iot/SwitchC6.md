# SwitchC6 <!--勿直接机翻，部分链接中英日链接不一样-->

<span class="product-sku">SKU:K140</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/K140_weight.jpg">
</PictureViewer>

## 描述

**SwitchC6** 是一款物联网单火线开关控制器。内部集成 ESP32-C6-MINI-1 核心主控与磁保持继电器，支持接入 AC 100 ~ 230V 的电器负载线路，帮助快速构建 IoT 智能家居应用。控制器出厂预装 ESP-NOW 控制固件，同时提供相关控制协议与 SDK，用户可使用任意 ESP32 设备进行无线控制。背部采用导轨卡扣设计，方便实现 DIN 导轨安装，适用嵌入式智能家居控制，单火线照明电路升级改造等应用场景。

## 教程 & 快速上手

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/switch/switchc6) | 本教程介绍如何将 SwitchC6 单火线开关控制器集成至 Home Assistant。 |

## 产品特性

- 单火线开关控制器
- 基于 ESP32-C6-MINI-1 无线 SoC
- 适用于钨丝灯泡以及支持可控硅调光的灯
- 2.4 GHz Wi-Fi 6
- 集成磁保持继电器
- 宽电压设计：兼容 AC 100 ~ 230V 电器负载
- ESP-NOW 无线通信协议
- 状态指示灯
- DIN 导轨安装

## 包装内容

- 1 x SwitchC6

## 应用场景

- 智能家居控制
- 单火线照明改造

## 规格参数

| 规格         | 参数                                                                 |
| ------------ | -------------------------------------------------------------------- |
| SoC          | ESP32-C6-MINI-1，RISC-V 32 位单核处理器，支持高达 160 MHz 的时钟频率 |
| Wi-Fi        | 2.4 GHz Wi-Fi 6                                                      |
| 支持无线标准 | IEEE 802.11 b/g/n/ax                                                 |
| 最大负载     | AC 220V@10A (2200W) / AC 110V@10A (1100W)，最大电流限制 10A          |
| 支持电压输入 | AC 100 ~ 230V，50/60Hz                                               |
| 电源供应     | 仅限火线                                                             |
| 端子接线规格 | 硬线：0.5m㎡ ~ 4m㎡<br>软线：0.5mm² ~ 2.5mm²                         |
| 开机状态     | 关机状态记忆                                                         |
| 工作温度     | -10℃ ~ 60℃                                                           |
| 产品尺寸     | 58.0 x 46.0 x 27.0mm                                                 |
| 产品重量     | 40.0g                                                                |
| 包装尺寸     | 63.0 x 48.0 x 28.5mm                                                 |
| 包装重量     | 47.3g                                                                |

## 操作说明

### 接线

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/Wiring.png" width="50%">

如贴纸信息及上图所示，SwitchC6 作为单火开关需要接在火线上电源与负载电器之间，左侧 L-IN 靠近电源，右侧 L-OUT 靠近负载。接入开关的电线需要露出 10mm 的金属，线规符合电路最大负载电流。接线时先打开卡扣，将电线金属端头完全插入开孔，并压紧卡扣。

### MAC 地址获取

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/MAC_Address.png" width="50%">

产品背面贴纸上展示了 MAC 地址（相当于产品的唯一 ID）。如上图所示，用力拉开小挂钩并掀起盖板即可看到。此外，也可以对主控设备编程使其扫描读取 SwitchC6 向外广播的状态信息中的 MAC 地址，具体方法见 [Arduino 开发部分](#软件开发)。

请注意，在开发时需要将贴纸上的 `XX:XX:XX:XX:XX:XX` 格式改为 `XXXX-XXXX-XXXX` 格式。

### 状态指示灯

|     | 蓝灯                     | 绿灯               |
| --- | ------------------------ | ------------------ |
| ON  | 充电启动中，暂时无法工作 | 开关闭合，电路接通 |
| OFF | 充电启动完成，可正常工作 | 开关切断，电路断开 |

\#> 充电说明 | 若产品长时间未接入电路，自带电容可能缓慢放电至耗尽，重新接入电路时需要充电完成才能开始工作，这个过程可能需要几分钟。

### 按键控制

- **短按一次**：切换开关状态，然后广播状态信息（自身 MAC 地址、信道、新的开关状态、电容电压等）。
- **长按 5s**：广播状态信息（同上）。

### 无线控制

对主控设备（如 M5Stack CoreS3 等）编程，使其通过 ESP-NOW 与 SwitchC6 无线通信，实现控制开关、读取状态等操作。具体方法见 [Arduino 开发部分、UiFlow2 开发部分](#软件开发)。

## 管脚映射

### SwitchC6

| SwitchC6        | G7     | G14       | G15      | G6  |
| --------------- | ------ | --------- | -------- | --- |
| User Button     | Button |           |          |     |
| Relay Pulse OFF |        | Relay OFF |          |     |
| Relay Pulse ON  |        |           | Relay ON |     |
| EH_12V ADC      |        |           |          | ADC |

## 尺寸图

- [SwitchC6 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6_Model_Size_01_page_01.png" width="100%">

## 数据手册

- [ESP32-C6-MINI-1 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/esp32-c6-mini-1_datasheet_cn.pdf)

## 软件开发

### Arduino

- [SwitchC6 Arduino 使用教程](/zh_CN/arduino/projects/iot/switchc6)
- [SwitchC6 Arduino 驱动库](https://github.com/m5stack/M5SwitchC6-ESP-NOW)

### UiFlow2

- [SwitchC6 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/iot-devices/switchc6.html) <!--中英链接不一样-->

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/switch/switchc6)

### 通信协议

- [SwitchC6 控制协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6-ESP-NOW-Protocol-CN.pdf) <!--中英链接不一样-->

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/K140_SwitchC6-sticker.png" width="100%">

## 相关视频

- SwitchC6 产品介绍与使用案例 <!--中英链接不一样-->

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/ZH-K140_SwitchC6_video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115031840655486&bvid=BV1P8bnzsEP8&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/__759JQ2Vpk?si=B6p6wlCwu4FiaN8o" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
