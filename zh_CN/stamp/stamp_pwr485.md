# Stamp PWR485

<span class="product-sku">SKU:S001</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_pwr485/stamp_pwr485_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_pwr485/stamp_pwr485_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1032/S001-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_pwr485/stamp_pwr485_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_pwr485/stamp_pwr485_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_pwr485/stamp_pwr485_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_pwr485/stamp_pwr485_06.webp">
</PictureViewer>

## 描述

**Stamp PWR485** 是一款**RS485 通信**拓展板，它能够将 MCU 串口的 3.3V TTL 电平转换为兼容 RS485 电气标准的差分信号。体积仅有 20 x 4.6 x 23mm 大小，能够集成到各类嵌入式设备中用于 RS485 通信接口拓展。适用于 RS485 传感器数据采集，Modbus 总线节点通信等应用场景。

## 产品特性

- SP485EEN-L/TR (RS485 收发器)
- 2x RS485 接口拓展 (并联), 可同时外接两组设备
- 红色电源指示灯
- PWR485 接口支持 9-24V 输入供电，内部 DC-DC 降压至 5V 为模组及主控设备供电
- 波特率实际测试数据：
  - 稳定通信波特率：9600bps/115200bps
  - 最大通信波特率测试：128000bps
- 多形态
  - 支持多种应用形态 (SMT,DIP, 飞线)
  - 配有高温塑料铠装，支持 SMT 过炉温度 (230°C)

## 包装内容

- 1 x Stamp PWR485
- 1 x HT3.96-4P 母座
- 2 x HY2.0-4P 母座 (蓝色 + 白色)
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)

## 应用场景

- RS485 通信
- Modbus 设备通信

## 规格参数

| 规格           | 参数                                                 |
| -------------- | ---------------------------------------------------- |
| RS485 收发器   | SP485EEN-L/TR                                        |
| 输入电压       | PWR485 接口支持 9 ~ 24V 输入供电 / TTL 侧输入电压 5V |
| 推荐工作波特率 | 9600bps/115200bps                                    |
| 工作电流       | DC 5V@3.2mA<br/>DC 12V@2.8mA<br/>DC 24V@2.1mA        |
| 输入逻辑电平   | 3.3V                                                 |
| 产品尺寸       | 20.0 x 4.6 x 23.0mm                                  |
| 产品重量       | 5.1g                                                 |
| 包装尺寸       | 138.0 x 93.0 x 10.0mm                                |
| 毛重           | 7.3g                                                 |

## 操作说明

### 外壳支持回流焊温度曲线

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_pico/stamp_pico_11_cn.webp">

## 原理图

- [Stamp PWR485 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/567/Sch_StampPWR485.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/567/Sch_StampPWR485_sch_01.png">
</SchViewer>

## 尺寸图

- [Stamp PWR485 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1032/S001-model-size-STAMP-485.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1032/S001-model-size-STAMP-485_page_01.png" width="100%">

## 软件开发

### Arduino

- Examples
  - [UART TEST](https://github.com/m5stack/M5Stack/blob/master/examples/Advanced/MultSerial/MultSerial.ino)
- Libraries
  - [ArduinoModbus Lib](https://github.com/m5stack/ArduinoModbus)
  - [Arduino485 Lib](https://github.com/m5stack/ArduinoRS485)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113461879180838&bvid=BV1LemyYLEV6&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/ql4Qhcg1bEI?si=_2azFEbZ2DoQrwxG" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
