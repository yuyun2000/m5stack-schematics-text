# Base M5GO RFID

<span class="product-sku">SKU:A014-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_rfid/m5go_rfid_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_rfid/m5go_rfid_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_rfid/m5go_rfid_03.webp">
</PictureViewer>

## 描述

**Base M5GO RFID** 是 [Base M5GO Bottom](/zh_CN/base/m5go_bottom) 的升级版，底座内置 RFID。相比普通版本 [Base M5GO Bottom](/zh_CN/base/m5go_bottom)，**底座少了磁铁且电池容量减少**，多了 **RFID 线圈** 和 **红外发射管**。

**Base M5GO RFID** 由 330 mAh 的电池（充满 3.7V）、M - Bus 总线接口、麦克风、红色的充电指示 LED、2 条 RGB 灯条（10 颗）、**RFID 线圈**、**红外发射管**、PORT.B 和 PORT.C 组成。

## 管脚映射

### POGO Pin

| POGO Pin | ESP32 Chip |
| :------: | :--------: |
| SCL      | G22        |
| SDA      | G21        |

### LED Bar

_有 10 颗 RGB 灯，左右各 5 颗_

| LED Pin | ESP32 Chip |
| :-----: | :--------: |
| LED Pin | G15        |

### MIC

模拟输入麦克风

| MIC Pin | ESP32 Chip |
| :-----: | :--------: |
| MIC Pin | G34        |

### HY2.0-4P

| PORT B(I/O) | ESP32 Chip |
| :---------: | :--------: |
| G36         | G36        |
| G26         | G26        |
| 5V          | 5V         |
| GND         | GND        |

| PORT C(UART2) | ESP32 Chip |
| :-----------: | :--------: |
| RXD           | G16        |
| TXD           | G17        |
| 5V            | 5V         |
| GND           | GND        |

### IR 发射管

| IR Transmitter | ESP32 Chip |
| :------------: | :--------: |
| IR Transmitter | G13        |
