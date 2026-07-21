# Atomic Battery Base

<span class="product-sku">SKU:A151</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_Weight.jpg">
</PictureViewer>

## 描述

**Atomic Battery Base** 是一款专为 Atom 系列产品供电的便携式电源底座，采用 ETA9085E10 高效升压方案和 LGS4056HDA 线性充电管理芯片，内置 **200mAh 可充电电池**，提供稳定的 5V **升压**输出，并实现安全高效的电池**充电**管理。产品内置电池**电量检测**电路，通过 LED 电量指示灯实时显示电池**电量状态**。配有**电池充放电切换开关**，支持升压与充电模式的一键切换，满足便携式电源需求。适用于物联网设备、便携式电子产品等对稳定电源有要求的应用场景。

## 产品特性

- ETA9085E10 高效升压芯片
- LGS4056HDA 充电芯片
- 内置 200mAh 可充电电池
- 电池电压 ADC 检测
- LED 电量指示灯
- 电池充放电切换开关

## 包装内容

- 1 x Atomic Battery Base

## 应用场景

- 物联网设备供电
- 便携式电子产品
- 移动测试平台

## 规格参数

| 规格                 | 参数                                |
| -------------------- | ----------------------------------- |
| 充放电芯片           | LGS4056HDA                          |
| 升压芯片             | ETA9085E10                          |
| 电池电量指示灯       | 4 档电量显示 (红色 LED)             |
| 充电指示灯           | 充电中 (蓝色 LED) , 充满 (绿色 LED) |
| 电池容量             | DC 3.7V@200mAh                      |
| 电池电路检测         | 分压检测电路                        |
| 充电电流             | DC 5V@223mA                         |
| 电池升压最大输出电流 | DC 5V@300mA                         |
| 待机电流（开关关闭） | DC 4.2V@2.55uA                      |
| 工作温度             | 0 ~ 40°C                            |
| 工作电流             | DC 4.2V@39.55mA                     |
| 产品尺寸             | 24.0 x 24.0 x 23.93mm               |
| 产品重量             | 9.9g                                |
| 包装尺寸             | 47.0 x 46.0 x 27.0mm                |
| 毛重                 | 15.8g                               |

## 操作说明

### 充放电说明

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/atomic_battery_base_status_led_01.png" width="100%">

\#> 充电提示 | 电源开关打开时（ON），电池升压到 5V 给 Atom 供电，电源开关关闭时（OFF），可通过 Atom USB 接口给电池充电，升压和充电状态需要手动切换开关，无法同时进行。<br/>4 档电池电量显示（红色 LED），充电状态显示（蓝色 LED：充电中，绿色 LED：充满电）。

### LED 显示与电压区间对应说明

| 电池电压范围  | 参考电量  |
| ------------- | --------- |
| 3.00V ~ 3.47V | 0 ~ 25%   |
| 3.48V ~ 3.61V | 25 ~ 50%  |
| 3.62V ~ 3.81V | 50 ~ 75%  |
| 3.82V ~ 4.20V | 75 ~ 100% |

### 补充说明

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/atomic_battery_base_pins_cut_01.png" width="60%">

\#> 兼容性 | 如需搭配 Atomic Voice Base 使用，需切断 Atomic Battery Base 右侧所有引脚 (5P)。如需搭配 Atom Voice 使用，需切断 G33 引脚连接。以上组合 Atomic Battery Base 仅作为供电使用，无法读取电池电压状态。

## 原理图

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_SCH_Atomic_Battery_Base_V1.1_2025_03_11_10_49_15_page_01.png">
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
|     |      | 1     |     |
|     | 2    | 3     |     |
|     | 4    | 5     | 5V  |
|     | 6    | 7     | GND |
|     | 8    | 9     |     |
::

### BAT ADC

| Atomic Battery Base                 | BAT ADC |
| ----------------------------------- | ------- |
| Atom-Lite / Atom-Matrix             | G33     |
| AtomS3 / AtomS3-Lite                | G8      |
| AtomS3R / AtomS3R-CAM / AtomS3R-M12 | G8      |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_Model_Size_page_01.png" width="100%">

## 结构文件

- [Atomic Battery Base 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/A151_Atomic_Battery_Base/Structures)

## 数据手册

- [ETA9085](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/ETA9085.pdf)
- [LGS4056H](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/LGS4056H.pdf)

## 软件开发

### Arduino

- 获取电池电量示例代码：

\#> 电池电压获取公式 | <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/batery_cal.png" width="20%"><br/>以 **Atom** 系列控制板为例，V_REF = 3.3V，ADC 读取分辨率设置 12 位，R14 和 R6 分别为 1MΩ，<br/> 则 V_BAT = 3.3 \* (检测到的 ADC 值 / 4095) \* 2

```cpp
#include "Arduino.h"

#define ATOM_BAT_ADC_PIN   33  // For Atom Series
#define ATOMS3_BAT_ADC_PIN 8   // For AtomS3 Series，AtomS3R Series


#define BAT_ADC_RESOLUTION 12

void setup()
{
    Serial.begin(115200);
    pinMode(ATOM_BAT_ADC_PIN, INPUT);
    analogReadResolution(BAT_ADC_RESOLUTION);
}

void loop()
{
    uint32_t adc_vol = 0;
    adc_vol          = analogReadMilliVolts(ATOM_BAT_ADC_PIN);
    uint32_t bat_vol = adc_vol * 2;
    Serial.printf("ADC:%d,Vol:%d\n", analogRead(ATOM_BAT_ADC_PIN), bat_vol);
}

```

## 相关视频

- Atomic Battery Base 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_Video.mp4" type="video/mp4"></video>
