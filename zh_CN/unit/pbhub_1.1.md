# Unit PbHub v1.1

<span class="product-sku">SKU:U041-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_09.webp">
</PictureViewer>

## 描述

**Unit PbHub v1.1**，是一款 I2C 控制的 6 路 PORT.B 扩展器，每路 Port B 接口均能实现 GPIO 、PWM 、Servo 控制、ADC 采样、RGB 灯光控制等功能。内部采用 STM32F030 控制。

## 产品特性

- 6 x GPIO HY2.0-4P PORTB 拓展
- 1 x I2C 输入
- 内部采用 STM32F030 控制
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit PbHub v1.1
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 规格参数

| 规格     | 参数                                   |
| -------- | -------------------------------------- |
| MCU      | STM32F030F4P6                          |
| 通信接口 | I2C 通信 @ 0x61 (可通过写入寄存器修改) |
| 产品尺寸 | 48.0 x 24.0 x 10.8mm                   |
| 产品重量 | 7.2g                                   |
| 包装尺寸 | 138.0 x 93.0 x 11.8mm                  |
| 毛重     | 12.5g                                  |

## 原理图

- [Unit PbHub v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/579/SHC_UNIT_PBHUB_v1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/579/SHC_UNIT_PBHUB_v1.1_sch_01.png">
</SchViewer>

## 管脚映射

### Unit PbHub v1.1

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/793/U040-B_Module_Size_sch_01.png" width="100%">

## 软件开发

### Arduino

- [Unit PbHub v1.1 Analog Read Example](https://github.com/m5stack/M5Unit-PbHub/tree/main/examples/analog_read)
- [Unit PbHub v1.1 Digital R/W Example](https://github.com/m5stack/M5Unit-PbHub/tree/main/examples/digital_write_read)
- [Unit PbHub v1.1 PWM Example](https://github.com/m5stack/M5Unit-PbHub/tree/main/examples/pwm)
- [Unit PbHub v1.1 RGB LED Example](https://github.com/m5stack/M5Unit-PbHub/tree/main/examples/rgb_led)
- [Unit PbHub v1.1 Servo Example](https://github.com/m5stack/M5Unit-PbHub/tree/main/examples/servo)

### UiFlow1

- [Unit PbHub v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/pbhub)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub_1.1/pbhub_1.1_uiflow_02.webp" width="50%">

### 内置固件

- [Unit PbHub v1.1 内置固件](https://github.com/m5stack/M5Unit-PbHub-Internal-FW)

| 固件版本 | 修改记录                                               | 通信协议                                                                                                               |
| -------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| v1       | 首次发布时版本                                         | [Unit PbHub v1.1 I2C Protocol v1](https://github.com/m5stack/M5Unit-PbHub/blob/main/docs/V1/PbHub_V1_I2C_Protocol.pdf) |
| v2       | 1. 新增 SK6812 灯珠支持 <br/> 2. 新增 I2C IAP 升级功能 | [Unit PbHub v1.1 I2C Protocol v2](https://github.com/m5stack/M5Unit-PbHub/blob/main/docs/V2/PbHub_V2_I2C_Protocol.pdf) |

\#> M5 DAPLink | 若您没有 STM32 下载器工具，可参考[M5 DAPLink](/zh_CN/guide/develop_tools/daplink)教程，使用 Core2 或 CoreS3 作为烧录器，为设备完成固件更新。

### 通信协议

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/796/PbHub_V2_I2C_Protocol_page_01.png" width="100%">

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112907928996428&bvid=BV11daoeCEHH&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/yE_FMxObeUk?si=svANLqUs94r86esD" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
