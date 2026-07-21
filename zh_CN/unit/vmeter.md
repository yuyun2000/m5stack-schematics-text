# Unit VMeter

<span class="product-sku">SKU:U087</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vmeter/vmeter_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vmeter/vmeter_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/713/U087-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vmeter/vmeter_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vmeter/vmeter_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vmeter/vmeter_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vmeter/vmeter_cover_01.webp">
</PictureViewer>

## 描述

**Unit VMeter** 是一款电压传感器，可以对电压进行实时监测。内部采用 16 位 ADC 数模转换器 ADS1115，通过 I2C (0X49) 进行通讯。为了保证测量精度，内置 DC/DC 隔离电源，同时 I2C 接口通过低功耗隔离器 CA-IS3020S 进行电气隔离，防止数据总线或其他电路上的噪声和浪涌进入本地接地端而干扰或损坏敏感电路。每个 **Unit VMeter** 在出厂时都单独进行校准，最大测量电压为 ±36V，精度为满量程的 1%，±1 位读数。

## 注意事项

?> 校准参数 | EEPROM (0x53) 在出厂时内置了校准参数，请勿对 EEPROM 进行写操作，否则校准数据将被覆盖导致测量结果不准确。

## 产品特性

- ±36V 量程
- 16 位 ADC 转换
- 分辨率：16V 以下 (含 16V) 为 1mV，16V 以上为 7.9mV
- 精度为满量程的 1%，±1 位读数
- LED 电源指示灯
- 免重新校准 (EEPROM 出厂写入)
- 内置 CA-IS3020S 隔离芯片，抗干扰
- 隔离 DC-DC
- 高达 1000 VRMS 隔离耐压
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit VMeter
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P 端子

## 应用场景

- 电压表

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 分辨率   | 读数 16V 为 7.9mV    |
| 测量范围 | ±36V                 |
| 通信接口 | I2C 通信 @ 0x49      |
| 产品尺寸 | 56.0 x 24.0 x 8.0mm  |
| 产品重量 | 8.2g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm |
| 毛重     | 16.5g                |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vmeter/vmeter_sch_01.webp" width="20%">

## 管脚映射

### Unit VMeter

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/vmeter/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit VMeter 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U087_Unit_VMeter/Structures)

## 数据手册

- [CA-IS3020S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/CA-IS3020S.pdf)
- [ADS1115](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/ADS1115.PDF)

## 软件开发

### Arduino

- [Unit VMeter with M5Core](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_VMeter_M5Core/Unit_VMeter_M5Core.ino)
- [Unit VMeter with M5Core2](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_VMeter_M5Core2/Unit_VMeter_M5Core2.ino)
- [Unit VMeter with M5Atom](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_VMeter_M5Atom/Unit_VMeter_M5Atom.ino)
- [Unit VMeter with M5StickC](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_VMeter_M5StickC/Unit_VMeter_M5StickC.ino)

### UiFlow1

- [Unit VMeter UiFlow1 Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/V_Meter_Unit/UIFlow)

### Home Assistant

- [Unit VMeter Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_vmeter_sensor)

### EasyLoader

| Easyloader                      | 下载链接                                                                                                                  | 备注                                                        |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Unit VMeter Example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_V_Meter_Unit.exe) | 测量电压，档位 0.512，最大测量电压 16V，模拟指针表示范围 5V |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/VMeter.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114153133967403&bvid=BV16FQwYGEHE&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/tV2VOMLg4ZA?si=4s6XQNl8dULkZ4mm" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
