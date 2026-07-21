# Base AAA

<span class="product-sku">SKU:A122</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base_aaa/base_aaa_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base_aaa/base_aaa_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/533/A122-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base_aaa/base_aaa_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base_aaa/base_aaa_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base_aaa/base_aaa_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base_aaa/base_aaa_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base_aaa/base_aaa_08.webp">
</PictureViewer>

## 描述

**Base AAA** 是由四节 AAA 干电池提供供电的 “5X5cm” 系列的底座。不同于其他锂电池底座，**Base AAA** 采用安全可靠的干电池进行供电，同时板载电源物理开关可以彻底关断电源，减少干电池损耗。预留两个 PORT.B、PORT.C 接口提供拓展，提供 1 X 12P 2.54 间距排母拓展接口。侧面有圆形安装孔方便固定、拓展，底部支持磁吸安装以及底部内嵌两个提供安装的铜螺母。

## 产品特性

- 1 x 12P 2.54 接口
- PORT.B、PORT.C 接口
- 电源开关
- 支持两种供电方式：
  - 由四节 AAA 干电池提供供电，通过 DC/DC 降压 6V -> 4V，供给 BUS 总线 BAT Pin
  - 外部通过杜邦线接入 12P 2.54 接口的 BAT/GND 进行供电、
- 多种固定方式:
  - 底部磁吸固定
  - 底部内嵌两个铜螺母
  - 侧面预留三个固定孔，

## 包装内容

- 1 x Base AAA
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品尺寸 | 54.0 x 54.0 x 21.0mm |
| 产品重量 | 30.0g                |
| 包装尺寸 | 80.0 x 55.0 x 28.0mm |
| 毛重     | 51.2g                |

## 操作说明

### 焊点提示

在默认状态下 G35 引脚处于断开状态，如需读取电源电压请焊接该焊点，如下图所示：

- 焊接前 <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/533/Base_AAA_1.jpg" width="50%">

- 焊接后 <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/533/Base_AAA_2.jpg" width="50%">

## 原理图

- [Base AAA 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/533/SCH_Base_AAA_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/533/SCH_Base_AAA_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN     |
| ------- | ---- | ----- | ------- |
| GND     | 1    | 2     | NC      |
| GND     | 3    | 4     | PORT.B  |
| GND     | 5    | 6     | RST     |
| NC      | 7    | 8     | NC      |
| NC      | 9    | 10    | PORT.B  |
| NC      | 11   | 12    | 3V3     |
| NC      | 13   | 14    | NC      |
| UART_RX | 15   | 16    | UART_TX |
| I2C_SDA | 17   | 18    | I2C_SCL |
| NC      | 19   | 20    | NC      |
| PIN     | 21   | 22    | PIN     |
| NC      | 23   | 24    | PIN     |
| HPWR    | 25   | 26    | PIN     |
| HPWR    | 27   | 28    | 5V      |
| HPWR    | 29   | 30    | BAT     |
::

## 尺寸图

- [Base AAA 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/533/base-aaa_v2-A122.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/533/base-aaa_v2-A122_page_01.png" width="100%">

## 软件开发

### Arduino

- 使用 ADC 读取电源引脚的电压

```cpp
#include <M5Unified.h>

#define BAT_ADC_PIN 35

int16_t sensorValue = 0;
float voltage = 0.0;

void setup() {
  M5.begin();
  Serial.begin(115200);
  analogReadResolution(10);
}

void loop() {
  sensorValue = analogRead(BAT_ADC_PIN);
  voltage = (sensorValue * 3.0) / 1023.0;
  Serial.print("sensor = ");
  Serial.print(sensorValue);
  Serial.print("\t vol = ");
  Serial.print(voltage);
  Serial.println("V");
  delay(200);
}

```
