# Atom Printer

<span class="product-sku">SKU:K118</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_09.webp">
</PictureViewer>

## 描述

**Atom Printer** 是一款 DIY **热敏打印机** 套件，硬件采用 **Atom-Lite** 物联网核心主控 + 58mm 规格热敏打印机搭配。 支持字符，图形，条形码，一维码，二维码等内容打印。机身使用全硬纸皮外壳覆盖，极具的创客风格。内置固件支持 `AP连接打印`+`MQTT消息推送打印` 两种模式，基于 ATOM 物联网控制核心，你还可以二次开发出更多酷炫打印应用。

\#> 注意：该套装没有配套电源适配器，用户需自行准备规格为`DC 12V`(5.5mm 规格) 的电源适配器。为获得最优打印质量，适配器要求供电能力在`2.5A`以上，其供电能力将直接影响打印的显示质量。

## 教程 & 快速上手

learn>| ![Atom Printer](https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_02.webp) | [Quick Start](/zh_CN/guide/hobby_kit/atom_printer/usage) | 本教程将向你介绍，Atom Printer 设备教程 & 快速上手 |

## 产品特性

- Atom-Lite: ESP32-PICO-D4 4MB Flash 物联网控制器
- 极客风硬纸皮外壳
- 支持打印字符，图形，条形码，二维码
- 通信接口 UART
- 打印速度快，分辨率高
- 使用方式:
  - AP 热点连接，web 控制打印
  - MQTT 下发内容打印 (Topic 为设备 Mac 地址)
  - 串口指令控制 (UART 9600bps 8N1)
  - 开发平台: UiFlow，Arduino

## 包装内容

- 1 x Atom Printer
- 1 x 热敏打印纸卷
- 1 x 贴纸热敏打印纸卷

## 应用场景

- 各种票据打印场景

## 规格参数

| 规格              | 参数                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| 打印方式          | 热敏打印                                                                                        |
| 支持的文本和图形  | 文字、图形、字符、条形码 (Codebar、code93、code39、code128、ENA13、ITF25、UPC-A、UPC-E)、二维码 |
| 供电电压          | DC 12V                                                                                          |
| 工作电流          | 2.5A                                                                                            |
| 打印颜色          | 黑白                                                                                            |
| 打印速度 / 分辨率 | 60mm/s 203dpi 8 点 /mm 每行最多 384 点                                                          |
| 打印宽度          | 58mm                                                                                            |
| 使用寿命          | 打印距离 50km                                                                                   |
| 切纸方式          | 手动撕纸                                                                                        |
| 热敏纸卷规格      | 58mm±0.05mm (宽度) 0.05 ~ 0.1mm (厚度)，最大直径≤40mm                                           |
| 打印速度          | 60mm/s                                                                                          |
| 通讯接口          | USB/RS232/TTL (ATOM 默认连接至 TTL 接口 UART 9600bps 8N1)                                       |
| 产品尺寸          | 151 x 79 x 66mm                                                                                 |
| 产品重量          | 285g                                                                                            |
| 包装尺寸          | 158 x 82 x 70mm                                                                                 |
| 毛重              | 321g                                                                                            |

## 管脚映射

- Atom PRINTER

| Atom         | G23 | G33 | G19 |
| ------------ | --- | --- | --- |
| Atom PRINTER | TX  | RX  | CTS |

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_printer/atom_printer_sch_01.webp" width="80%">

## 软件开发

### Arduino

- [Atom Printer Firmware](https://github.com/m5stack/ATOM-PRINTER)

### 通信协议

- [ATOM_PRINTER_CMD_v1.06 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_pritner/ATOM_PRINTER_CMD_v1.06.pdf)

#### Setting

| NO  | Function                | command                                                                                                  |
| --- | ----------------------- | -------------------------------------------------------------------------------------------------------- |
| 1   | Init                    | 0x1B,0x40                                                                                                |
| 2   | Set Print Position X mm | 0x1B,0x24,(X \* 8)&0x00ff,((X \* 8)>>8)&0x00ff                                                           |
| 3   | Set Left Margin X mm    | 0x1D,0X4C,(X \* 8)&0xff,((X \* 8)>>8)&0x00ff                                                             |
| 4   | Set Line Space X mm     | 0x1B,0x33,(X \*8)                                                                                        |
| 5   | Set Baud Rate: X        | 0x1B,0x23,0x23,0x53,0x42,0x44,0x52,X<br/>(9600:X=0x80,0x25,0x00,0x00)<br/>(115200:X=0x00,0xC2,0x01,0x00) |
| 6   | Set Character Size:X,Y  | 0x1D,0x21,((X&0x0f)<<4) (Y&0x0f)                                                                         |
| 7   | Set Bold:on/off         | 0x1B,0X47,0x01/0x00                                                                                      |
| 8   | Set Underline:on/off    | 0x1B,0x2D,0x01/0x00                                                                                      |

#### Print

| NO  | 功能                    | 指令                                                               |
| --- | ----------------------- | ------------------------------------------------------------------ |
| 1   | Print X at Y mm         | 0x1B,0x24,(Y \* 8)&0x00ff,((Y \* 8)>>8)&0x00ff,X                   |
| 2   | Set Print Position X mm | 0x1D,0x28,0x6B,0x03,0x00,0x31,0x45,X (L:0x48/M:0x49/Q:0x50/H:0x51) |

#### QRCode

| NO  | 功能                                | 指令                                                                |
| --- | ----------------------------------- | ------------------------------------------------------------------- |
| 1   | Set QRCode Adjust Level X           | 0x1D,0x28,0x6B,0x03,0x00,0x31,0x45,X (L:0x48/M:0x49/Q:0x50/H:0x51)  |
| 2   | Set QRCode Buffer Length:L Buffer:X | 0x1D,0x28,0x6B,(L+3)&0x00ff,((L+3)>>8)&0x00ff,0x31,0x50,0x30,X,0x00 |
| 3   | Print QRCode                        | 0x1D,0x28,0x6B,0x03,0x00,0x31,0x51,0x30,0x00                        |

#### BarCode

| NO  | 功能                                       | 指令                                                                                                                                               |
| --- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Barcode Sw:on/off                          | 0x1D,0x45,0x43,0x01/0x00                                                                                                                           |
| 2   | Set HRI Position                           | 0x1D,0x48,hide:0x00/above:0x01/below:0x02/both:0x03                                                                                                |
| 3   | Print BarCode <br/>Type:T Lenth:L Buffer:X | 0x1D,0x6B,T,L,X,0x00 <br/>Type: UPC-A=0x41/UPC-E=0x42/JAN13(EAN13)=0x43/JAN8(EAN8)=0x44/CODE39=0x45/ITF=0x46/CODABAR=0x47/CODE93=0x48/CODE128=0x49 |

#### Bmp

| NO  | 功能                             | 指令                                                                   |
| --- | -------------------------------- | ---------------------------------------------------------------------- |
| 1   | Print BMP Width:W Hight:H Data:X | 0x1D,0X76,0X30,(W/8)&0x00ff,((W/8)>>8)&0x00ff,H&0x00ff,(H>>8)&0x00ff,X |

### EasyLoader

| Easyloader                   | 下载链接                                                                                                           | 备注 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---- |
| Atom Printer Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atom_printer/ATOM_PRINTER.exe) | /    |

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atom_printer/M5Stack%E6%89%93%E5%8D%B0%E6%9C%BA%EF%BC%8CPM2.5%E6%A8%A1%E5%9D%97%E5%92%8CMQTT%E6%89%93%E5%8D%B0%E6%97%A5%E5%BF%97.mp4" type="video/mp4"></video>

<video width="800" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_PRINTER_GUIDE.mp4" type="video/mp4">
</video>
