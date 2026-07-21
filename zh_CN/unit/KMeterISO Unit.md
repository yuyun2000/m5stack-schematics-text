# Unit KMeter-ISO

<span class="product-sku">SKU:U133-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-636d2fa0-a416-48b9-a667-57defaa0291e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-307032da-7c86-4677-a8d8-d058aa0558b0.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/742/U133-V11-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-794d033d-e060-4d83-8b2a-46c1a20bfcb1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-da9fa02e-85be-4a25-9ac0-be741136e044.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-57739578-19d8-4a9a-9414-57073039dd92.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-2bfc6e62-8966-4d02-bfa4-45515c72f18b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-926ef2c5-272f-4b00-abcc-5f36e8db797a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-54fce494-248f-4395-8b03-5fff6ce4d19a.webp">
</PictureViewer>

## 描述

**Unit KMeter-ISO**是一款集合 “采集 + 隔离 + 通信” 功能的一体化 K 型热电偶传感器单元，采用 STM32F030 + MAX31855KASA 14bit 热电偶数字转换芯片方案，实现高精度的温度采集、转换。MCU 采用 STM32F030 实现数据采集以及 I2C 通信接口，采用 **CA-IS3641HW** 作为信号隔离器。该单元支持接入测量范围 -200°C ~ 1350°C 的热电偶探头，采用通用标准 K 型扁形接口，方便后续更换不同量程测量探头匹配的不同需求。该模块适用于工业自动化、仪器仪表、电力电气、热处理等领域的温度采集、控制、监测等应用场景。

## 产品特性

- STM32F030，高性能 ARM Cortex-M0 内核，支持 I2C 固件更新
- MAX31855KASA+T: (14Bit ADC、0.25°C 分辨率，精度 ±2%)
- 支持探头类型: K 型 - 支持接入探头测量范围 -200 ~ 1350°C
- I2C 通信接口 addr: 0x66
- 信号隔离器 CA-IS3641HW 隔离输入和输出信号，提高稳定性、安全性和可靠性。
- 支持编程平台：Arduino、UiFlow

## 包装内容

- 1 x Unit KMeter-ISO
- 1 x K 型热电偶探头 (测量范围 -50 ~ 250°C 线长 1m)
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 工业自动化
- 仪器仪表
- 电力电器
- 热处理

## 规格参数

| 规格                 | 参数                                     |
| -------------------- | ---------------------------------------- |
| MCU                  | STM32F030F4P6                            |
| 通信接口             | I2C 通信 @ 0x66                          |
| 温度传感器芯片       | MAX31855KASA+T                           |
| 信号隔离芯片         | CA-IS3641HW                              |
| 分辨率               | 14 位                                    |
| 热电偶工作温度范围   | -200-1350°C                              |
| 热电偶类型           | K                                        |
| 最大采样速率         | 10 Hz                                    |
| SPI 接口时钟频率范围 | 最高 5 MHz                               |
| 内部温度传感器精度   | ±2°C                                     |
| 热电偶测量精度       | ±2°C                                     |
| 异常检测             | 开路、短路和热电偶低电压                 |
| STM32F030            | ARM Cortex-M0，48MHz，64K flash，8K SRAM |
| 产品尺寸             | 56.0 x 24.0 x 8.0mm                      |
| 产品重量             | 10.0g                                    |
| 包装尺寸             | 138.0 x 93.0 x 9.0mm                     |
| 毛重                 | 22.0g                                    |

## 原理图

- [Unit KMeter-ISO 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/596/Sch_UNIT-KMeter_ISO.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/596/Sch_UNIT-KMeter_ISO_sch_01.png">
</SchViewer>

## 管脚映射

### Unit KMeter-ISO

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/img-b09b086d-a26c-40d3-9ef5-f5f24a4e6028.png" width="100%" />

## 数据手册

- [STM32F030F4P6 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)
- [MAX31855KASA+](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U133-V11%20KMeterISO%20Unit/MAX31855KASA%2B.PDF)
- [CA-IS3641HW](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U133-V11%20KMeterISO%20Unit/CA-IS3641HW.PDF)

## 软件开发

### Arduino

- [Unit KMeter-ISO Arduino 驱动库](https://github.com/m5stack/M5Unit-KMeterISO)

### UiFlow1

- [Unit KMeter-ISO UiFlow1 文档](/zh_CN/uiflow/blockly/unit/kmeter_iso)
- [Unit KMeter-ISO 测试程序](https://flow.m5stack.com/?examples=unit_kmeteriso_demo)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO Unit/uiflowCase-1678354080359image.png" width="100%"/>

### Home Assistant

- [Unit KMeter-ISO Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_kmeteriso_sensor)

### 通信协议

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/KMeterISO%20Unit/i2c%20protol.png" width="100%" />

## 相关视频

- Unit KMeter-ISO 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/kmeter_video.mp4" type="video/mp4"></video>

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

## 版本变更

| 上市日期 | 产品变动                                                       |
| -------- | -------------------------------------------------------------- |
| 2023.4   | 主控由 ESP32-C3 修改为 STM32F030，添加了信号隔离器 CA-IS3641HW |
