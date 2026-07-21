# Unit DAC

<span class="product-sku">SKU:U012</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dac/dac_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dac/dac_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dac/dac_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dac/dac_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dac/dac_06.webp">
</PictureViewer>

## 描述

**Unit DAC**，是一款高性能的数字 / 模拟信号转换器，其内置了 **MCP4725**。具备低功耗，高精度，单通道，12 位缓冲电压输出数模转换器 (DAC)，非易失性存储器 (EEPROM)。

用户可以使用 I2C 接口命令将 DAC 输入和配置烧写到非易失性存储器 (EEPROM) 中，使得 DAC 在断电期间仍能保持代码，上电后即可直接使用，I2C 地址为 0x60。

## 产品特性

- HY2.0-4P 接口，支持 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc).
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit DAC
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- MP3 音频播放器
- 迷你示波器

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 分辨率   | 12 位                 |
| 电压范围 | 0 ~ 3.3V              |
| 通信接口 | I2C 通信 @ 0x60       |
| 产品尺寸 | 32.0 x 24.0 x 10.2mm  |
| 产品重量 | 4.2g                  |
| 包装尺寸 | 138.0 x 93.0 x 11.3mm |
| 毛重     | 11.1g                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dac/dac_sch_01.webp" width="80%">

## 管脚映射

### Unit DAC

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

-[MCP4725](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/MCP4725_en.pdf)

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/dac/MODULE%20SIZE.jpg" width="100%" />

## 软件开发

### Arduino

- [Unit DAC 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/DAC_MCP4725)

### UiFlow1

- [Unit DAC UiFlow1 文档](/zh_CN/uiflow/blockly/unit/dac)

### UiFlow2

- [Unit DAC UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/dac.html)

## EasyLoader

| Easyloader               | 下载链接                                                                                    | 备注 |
| ------------------------ | ------------------------------------------------------------------------------------------- | ---- |
| Unit DAC Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_DAC.exe) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113501657892482&bvid=BV1TLUnYPECu&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/XPBNtrAOq7s?si=zGFVZAGCZUUg0aYV" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
