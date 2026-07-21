# Base AC Power

<span class="product-sku">SKU:K116</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/ac_power/ac_power_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/ac_power/ac_power_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1004/K116-package.png">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/ac_power/ac_power_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/ac_power/ac_power_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/ac_power/ac_power_05.webp">
</PictureViewer>

## 描述

**Base AC Power** 是一款 **高性能 AC/DC** 转换模块。支持 **AC 100 ~ 230V** 输入，通过底座内部降压模块转换，可稳定输出 **DC 5V** 与 **DC 12V** 双通道直流供电。模块内置 EMC 和脉冲衰减器，抗干扰性好，稳定性强。使用该模块能够增强 M5 主控设备供电方式的灵活性，使其更加方便嵌入到各类应用场景中去。

## 注意事项

!> 注意:| 该产品使用时需输入 100 ~ 230V 交流电，为保证用电安全，请勿拆解该产品。

## 产品特性

- 输入电压:
  - AC 100 ~ 230V INPUT
- 输出电压:
  - DC 5V@1A OUPUT
  - DC 12V@0.3A OUPUT
- 内置熔断器保护 250V/1A

## 包装内容

- 1 x Base AC Power

## 规格参数

| 规格           | 参数                 |
| -------------- | -------------------- |
| 输入电压       | AC 100 ~ 230V        |
| 输出电压       | 5V@1A，12V@0.3A      |
| 电压精度       | ±1%                  |
| 效率 (Typ)     | 82%                  |
| AC 接口规格    | AC-018E              |
| 内置熔断器规格 | 250V@1A              |
| 电源指示灯     | 红色                 |
| 产品尺寸       | 56.0 x 54.0 x 33.0mm |
| 产品重量       | 81.0g                |
| 包装尺寸       | 79.0 x 55.5 x 34.0mm |
| 毛重           | 107.0g               |

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN |
| ---- | ---- | ----- | --- |
| GND  | 1    | 2     | NC  |
| GND  | 3    | 4     | NC  |
| GND  | 5    | 6     | NC  |
| NC   | 7    | 8     | NC  |
| NC   | 9    | 10    | NC  |
| NC   | 11   | 12    | 3V3 |
| NC   | 13   | 14    | NC  |
| NC   | 15   | 16    | NC  |
| NC   | 17   | 18    | NC  |
| NC   | 19   | 20    | NC  |
| NC   | 21   | 22    | NC  |
| NC   | 23   | 24    | NC  |
| HPWR | 25   | 26    | NC  |
| HPWR | 27   | 28    | 5V  |
| HPWR | 29   | 30    | BAT |
::

## 尺寸图

- [Base AC Power 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1004/K116-acpower.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1004/K116-acpower_page_01.png" width="100%">

## 结构文件

- [Base AC Power 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K116_Base_AC_Power/Structures)
