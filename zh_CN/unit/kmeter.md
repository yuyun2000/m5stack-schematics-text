# Unit KMeter

<span class="product-sku">SKU:U133</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/kmeter/kmeter_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/kmeter/kmeter_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/kmeter/kmeter_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/kmeter/kmeter_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/kmeter/kmeter_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/kmeter/kmeter_06.webp">
</PictureViewer>

## 描述

**Unit KMeter** 是一款 I2C 通信接口的 K 型热电偶传感器，硬件采用 ESP32-C3 主控 + **MAX31855KASA + T** 14bit 热电偶数字转换芯片。内部 ESP32-C3 集成固件与热电偶数字 IC 通信处理原始数据并暴露出 I2C 接口，用户能够非常轻松地获取已经处理好的温度数据。该产品专为 K 型热电偶设计，转换芯片支持接入测量范围 -200 °C ~ 1350 °C 的热电偶探头，且采用通用标准扁形接口，方便后续更换不同量程测量探头匹配不同需求。适用于工业温度采集、监控等对测温范围有着较高需求的场景。

## 产品特性

- ESP32-C3 (支持 I2C 固件更新)
- MAX31855KASA+T:
  - 14Bit ADC
  - 0.25°C 分辨率，精度 ±2%
  - 支持探头类型: K 型
  - 支持接入探头测量范围 -200 ~ 1350°C
- I2C 通信接口 addr: 0x66

## 包装内容

- 1 x Unit KMeter
- 1 x K 型热电偶探头 (测量范围 -50 ~ 250°C 线长 1m)
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 工业温度采集
- 恒温控制 / 监控场景

## 规格参数

| 规格              | 参数                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| 热电偶数字转换 IC | MAX31855KASA+T:14Bit ADC，0.25°C 分辨率，精度 ±2%，支持探头类型: K 型，支持测量范围 - 200 ~ 1350°C |
| 标配探头规格      | K 型热电偶，测量范围 -50 ~ 250°C 线长 1m，热响应时间 < 1s，接口：标准扁形铜材质插头                |
| 通信接口          | I2C 通信 @ 0x66                                                                                    |
| 功耗情况          | 5V@24mA                                                                                            |
| 产品重量          | 9.3g                                                                                               |
| 毛重              | 21g                                                                                                |
| 产品尺寸          | 56 x 24 x 9.6mm                                                                                    |
| 包装尺寸          | 93 x 138mm                                                                                         |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/kmeter/kmeter_sch_01.webp" width="80%">

## 管脚映射

### Unit KMeter

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 软件开发

### Arduino

- [Unit KMeter Arduino 驱动库](https://github.com/m5stack/M5Unit-KMeter)
- [Unit KMeter Get Sample Example](https://github.com/m5stack/M5Unit-KMeter/blob/master/examples/Unit_KMeter_M5Device/simple/simple.ino)
- [Unit KMeter AutoScaleGraph](https://github.com/m5stack/M5Unit-KMeter/blob/master/examples/Unit_KMeter_M5Device/graph/graph.ino)

### UiFlow1

- [Unit KMeter UiFlow1 文档](/zh_CN/uiflow/blockly/unit/kmeter)

### UiFlow2

- [Unit KMeter UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/kmeter_iso.html)

## 内置固件

- [Unit KMeter 内置固件](https://github.com/m5stack/M5UnitKMeter_Firmware)

### 通讯协议

- 协议类型 I2C
- I2C Address: **0x66**

| 地址 | 数据长度 | 数据                 | 返回值                                                                                               |
| ---- | -------- | -------------------- | ---------------------------------------------------------------------------------------------------- |
| 0x66 | 4Byte    | 热电偶和内部温度数据 | Byte \[0] thermocouple_H<br/>Byte\[1] thermocouple_L<br/>Byte\[2] internal_H<br/>Byte\[3] internal_L |

- calculate

```cpp

thermocouple = (thermocouple_H << 8) + thermocouple_L;
internal = (internal_H << 8) + internal_L;

thermocouple_temp = 0.25f * (thermocouple >> 2);
internal_temp = 0.0625f * (internal >> 4);
```

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/kmeter_video.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113382371888828&bvid=BV1LE1GYEEGi&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/3u4YvigSAzs?si=tMk1D3hVR1RvL_e1" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
