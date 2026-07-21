# Module13.2 2Relay

<span class="product-sku">SKU:M124</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-07c98873-5b75-4c92-ab16-64c890c6166e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-1f94db97-1280-4697-980d-0712e26662cc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-36a9205c-bb89-4d35-b2bf-a95cd90a2845.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-12ba1c85-c34b-4056-9855-b9f46ce24108.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-a34c238a-a507-4798-845d-1dbfdb2c618c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-e0e8f9d8-fbfd-4a79-8be1-513ec4c142fd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-2ac016c2-b7c0-4a76-b3c7-8c82b4331cf6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-72857c9c-2fc6-4030-a2cc-33755599fd51.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-7a79ca72-16bd-41f9-8aa1-75f17c598681.webp">
</PictureViewer>

## 描述

**Module13.2 2Relay** 是一款双路交流继电器模块，内置 STM32F030 主控芯片，采用 I2C 总线通信。 集成双路交流继电器模块，最大支持 AC 250V@5A 线路通断。适用于电器负载，电磁阀控制等应用场景。

## 产品特性

- STM32F030F4
- I2C 通信 (地址：0x26)
- 2 x 继电器模块
- 电源输入 (支持交直流输入)
- 编程平台：Arduino/UIFLOW

## 包装内容

- 1 x Module13.2 2Relay
- 2 x HT3.96-2P 端子

## 应用场景

- 开 / 关控制
- 电磁阀控制
- 直流控制负载开 / 关
- 远程物联网开关

## 规格参数

| 规格        | 参数                 |
| ----------- | -------------------- |
| MCU         | STM32F030F4P6        |
| 执行器      | 2 路继电器           |
| 电气特性    | 交直流电             |
| 触点材料    | AgSnO2               |
| CH 最大功率 | 250VAC @ 5A          |
| 接触电阻    | ≤100mΩ               |
| 产品尺寸    | 54.0 x 54.0 x 19.7mm |
| 产品重量    | 33.5g                |
| 包装尺寸    | 95.0 x 66.0 x 26.0mm |
| 毛重        | 53,6                 |

## 原理图

- [Module13.2 2Relay 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/551/Sch_Module13.2_2Relay.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/551/Sch_Module13.2_2Relay_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     |          |
| GND      | 5    | 6     |          |
|          | 7    | 8     |          |
|          | 9    | 10    |          |
|          | 11   | 12    | 3V3      |
|          | 13   | 14    |          |
|          | 15   | 16    |          |
| SDA      | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    |          |
|          | 23   | 24    |          |
| HPWR     | 25   | 26    |          |
| HPWR     | 27   | 28    | 5V       |
| HPWR     | 29   | 30    |          |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/2Relay/img-f508ceef-20b6-4400-a00c-3d452707197a.png" width="100%" />

## 数据手册

- [932-5VDC-SL-AH RELAY](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/932-5VDC-SL-AG%20.pdf)
- [STM32F030F4P6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/STM32F030F4P6.pdf)

## 软件开发

### Arduino

- [Module13.2 2Relay 控制示例](https://github.com/m5stack/M5Module-2Relay-13.2/tree/main/examples)
- [Module13.2 2Relay 配置 I2C 地址示例](https://github.com/m5stack/M5Module-2Relay-13.2/tree/main/examples)

### UiFlow1

- [Module13.2 2Relay UiFlow1 文档](/zh_CN/uiflow/blockly/module/2relay)

### UiFlow2

- [Module13.2 2Relay UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/relay_2.html)

### 通信协议

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/2Relay/2relay.png" width="100%"/>

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114272805849469&bvid=BV12dZyYxEpm&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
    <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/mvvw6G2TuQU?si=MIKN43B2BguhhFtk" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
  </template>
</TabPanel>
