# Unit RTC

<span class="product-sku">SKU:U126</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/img-1d24e2f2-7e72-48df-91a3-db5d837ea3d7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/img-71b289e0-e14a-4a18-8745-a8a3c380d61d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/img-26e6b42d-6d00-43b8-9f61-b16130333c90.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/img-8db586cc-d573-4381-8628-44cfebed3fc3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/img-462bbb0c-4bf5-412d-9110-563c9298f367.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/img-4924d29a-8a3c-431c-9148-2a4b220a6375.webp">
</PictureViewer>

## 描述

**Unit RTC** 是一款可编程的实时时钟模块，集成 HYM8563 低功耗 CMOS 实时时钟 / 日历芯片，采用 I2C 通信接口，全覆盖外壳能够有效保护电路，使其运行更加稳定。适用于应用到各种嵌入式设备、仪表仪器中作为系统时钟。

## 产品特性

- 支持秒、分、时、星期、天、月、年，时间数据读写
- 32.768kHz 高精度时钟晶振，大幅度减少了时间误差
- 低功耗，纽扣电池供电可连续工作多年
- 带有世纪标志
- I2C 通信接口

## 包装内容

- 1 x Unit RTC
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 时钟、闹钟
- 掉电时间同步

## 规格参数

| 规格     | 参数                                  |
| -------- | ------------------------------------- |
| 时钟芯片 | HYM8563                               |
| 晶振频率 | 32.768kHz                             |
| 通信接口 | I2C 通信 @ 0x51，总线最大速度 400Kbps |
| 供电电压 | DC 5V                                 |
| 产品尺寸 | 48.0 x 24.0 x 8.0mm                   |
| 产品重量 | 7.4g                                  |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm                  |
| 毛重     | 12.8g                                 |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/img-6f0baa97-c15f-4c85-be56-12078e7a7dd2.webp" width="100%" />

## 管脚映射

### Unit RTC

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT%20RTC/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 数据手册

- [HYM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/rtc/HYM8563_Datasheet_V2.2_cn.pdf)

## 软件开发

### Arduino

- [Unit RTC 测试程序](https://github.com/m5stack/M5Unit-RTC/blob/master/examples/Unit_RTC_M5Series/Unit_RTC_M5Series.ino)
- [Unit RTC Test Example with M5Atom](https://github.com/m5stack/M5Unit-RTC/blob/master/examples/Unit_RTC_M5Atom/Unit_RTC_M5Atom.ino)
- [Unit RTC Test Example with M5Core](https://github.com/m5stack/M5Unit-RTC/blob/master/examples/Unit_RTC_M5Core/Unit_RTC_M5Core.ino)
- [Unit RTC Test Example with M5Core2](https://github.com/m5stack/M5Unit-RTC/blob/master/examples/Unit_RTC_M5Core2/Unit_RTC_M5Core2.ino)
- [Unit RTC Test Example with M5StickC](https://github.com/m5stack/M5Unit-RTC/blob/master/examples/Unit_RTC_M5StickC/Unit_RTC_M5StickC.ino)
- [Unit RTC Test Example with M5StickCPlus](https://github.com/m5stack/M5Unit-RTC/blob/master/examples/Unit_RTC_M5StickCPlus/Unit_RTC_M5StickCPlus.ino)

### UiFlow1

- [Unit RTC 测试程序](https://flow.m5stack.com/?examples=unit_rtc_demo)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/uiflowCase-1691550079203uiflow example.png" width="100%"/>

## 相关视频

- 时钟显示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UNIT_RTC_VIDEO.mp4" type="video/mp4"></video>
