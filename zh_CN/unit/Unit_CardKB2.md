# Unit CardKB2

<span class="product-sku">SKU:U215</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215_main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215-weight.jpg">
</PictureViewer>

## 描述

Unit CardKB2 是一款 卡片大小 的 42 键便携式键盘输入单元，机身小巧轻便，适合随身携带与嵌入式集成，内置 ESP32-C61HF4 主控，支持 2.4 GHz Wi-Fi 6。设备预置固件可灵活配置 I2C、UART、BLE HID 和 ESP-NOW 四种通信方式，与主控设备进行连接。板载 HY2.0-4P 接口，用于 I2C / UART 模式下的通信，并提供 USB Type-C 用于设备供电与程序下载。同时配备 RGB LED 指示灯、复位与 Boot 按键，并集成输入电源过压保护，适用于无线输入、交互控制及各类便携式应用场景。

## 产品特性

- 搭载 ESP32-C61HF4，支持 Wi-Fi 6 / BLE 无线通信
- 全键盘输入，支持多种按键组合（单击、Sym、Fn）
- 板载 RGB LED（XL-1615RGBC-RF），可指示键盘状态
- 预留 M2 固定孔位，方便应用集成
- 供电方式:
  - USB Type-C 供电
  - DC 5V

## 包装内容

- 1 x Unit CardKB2
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 便携设备文本输入
- 嵌入式系统人机交互
- IoT 设备无线控制终端
- 教育编程与创客项目

## 规格参数

| 规格       | 参数                                                   |
| ---------- | ------------------------------------------------------ |
| SoC        | ESP32-C61HF4 @ RISC-V 32 位单核，主频 120 MHz          |
| Flash      | 4MB                                                    |
| Wi-Fi      | 2.4 GHz Wi-Fi 6                                        |
| 按键       | 42 键键盘，1x 复位按键，1x Boot 按键                   |
| USB Type-C | 设备供电 / 程序下载，默认固件日志输出: 115200bps @ 8N1 |
| RGB LED    | 1x RGB LED                                             |
| 拓展接口   | 1x HY2.0-4P                                            |
| 待机功耗   | 5V@19.31mA (Grove 接口供电条件下)                      |
| 产品尺寸   | 84.7 x 54.3 x 1.0mm                                    |
| 产品重量   | 22.4g                                                  |
| 包装尺寸   | 170.0 x 120.0 x 8.0mm                                  |
| 毛重       | 28.9g                                                  |

## 操作说明

### 按键说明

- **Aa 键（大写切换）**：

  - **单击**：启用一次性大写，输入一个字符后自动恢复小写。
  - **双击**：启用大写锁定，再次单击或双击解除锁定并恢复小写。
  - **长按**：按住期间保持大写输出，释放后恢复小写。
  - 大写启用时**绿色指示灯亮起**，禁用时熄灭。

- **Sym 键（符号键）**：单击**激活**字符输入，再次单击取消。

- **Fn 键（功能键）**：用于模式切换和组合功能。Fn 按下时**红色指示灯亮起**。

以下仅在 BLE HID 模式下起作用：

- **Fn + 1**：输出 Esc

- **Fn + D**：光标上移（↑）

- **Fn + X**：光标下移（↓）

- **Fn + Z**：光标左移（←）

- **Fn + C**：光标右移（→）

- **模式切换（Fn + Sym + 数字键）**：切换后自动保存，下次上电时保持新设置的模式。
  - **Fn + Sym + 1**：切换至 I2C 模式（出厂默认），白色指示灯闪烁 1 次
  - **Fn + Sym + 2**：切换至 UART 模式，白色指示灯闪烁 2 次
  - **Fn + Sym + 3**：切换至 ESP-NOW 广播模式，白色指示灯闪烁 3 次
  - **Fn + Sym + 4**：切换至 BLE HID 模式，白色指示灯闪烁 4 次

### BLE HID 模式

**Unit CardKB2** 可作为无线键盘，连接至支持 BLE HID 的设备，使用步骤如下：

1. 按 **Fn + Sym + 4** 切换到 BLE HID 模式
2. 在手机 / 平板 / 电脑上搜索附近无线设备，设备名：`CardKB2-xxxx`（`xxxx` 为 MAC 地址后四位）
3. 配对连接后即可作为无线键盘使用

其他模式（UART / I2C / ESP-NOW）的使用方法请参考[Unit CardKB2 用户手册 & 寄存器](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2_User_Manual_CN.pdf)。<!--注意，中英文链接不一样-->

## 管脚映射

### Unit CardKB2

::grove-table
| HY2.0-4P    | Black | Red | Yellow              | White               |
| ----------- | ----- | --- | ------------------- | ------------------- |
| PORT.CUSTOM | GND   | 5V  | SDA / UART_RX / G26 | SCL / UART_TX / G25 |
::

## 原理图

- [Unit CardKB2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2_page_04.png">
</SchViewer>

## 尺寸图

- [Unit CardKB2 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215-Unit_CardKB2_Dimension_Diagram.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215-Unit_CardKB2_Dimension_Diagram_page_01.png">
</SchViewer>

## 数据手册

[ESP32-C61HF4](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/esp32-c61_datasheet_cn.pdf) <!--注意，中英文链接不一样-->

## 软件开发

### Arduino

- [Unit CardKB2 Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_cardkb2)
- [Unit CardKB2 Arduino 驱动库](https://github.com/m5stack/M5Unit-KEYBOARD)

### UiFlow2

coming soon...

### 内置固件

- [Unit CardKB2 内置固件](https://github.com/m5stack/M5Unit-CardKB2-UserDemo)

### 通信协议

- [Unit CardKB2 用户手册 & 寄存器](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2_User_Manual_CN.pdf)

## 相关视频

- Unit CardKB2 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/U215-UnitCardKB2_video_ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116493085837987&bvid=BV1Zq9aBRERm&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/UgvV7Qe3QPI?si=skCXyjayQRV90lcz" title="YouTube video player" frameborder="0" loading="lazy"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>