# Unit BLDC Driver

<span class="product-sku">SKU:U181</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-BLDC Driver/img-a97915ed-d14b-4dc2-a93d-e72f0d917e95.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-BLDC Driver/img-36fb7990-c6c6-446d-923e-00c95525845a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-BLDC Driver/img-f1760fde-ece9-47ba-a391-3e9cf476cb1d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-BLDC Driver/img-5cb8951d-04a1-4685-a209-402bd3d4d350.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-BLDC Driver/img-f04bc991-460e-4f62-985d-f1e9e174b415.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-BLDC Driver/img-5bc039cf-d654-4fb8-9c46-675a45ea43be.webp">
</PictureViewer>

## 描述

**Unit BLDC Driver** 是一款专为无刷直流电机 (BLDC) 设计的驱动单元，采用 STM32 为主控芯片，通过 I2C 通讯方式实现对 DRV11873PWPR 电机驱动芯片的精准控制，实现 PWM 转速控制调节和监控，方向切换等功能。该驱动芯片具有简化的控制接口和集成的堵转保护等功能，实现三相位小型无刷直流电机的高效、低噪音运行。板载 STM32 升级接口便于固件更新和功能扩展，适用于工业自动化、智能机器人、精密仪器等领域。

## 产品特性

- STM32 主控
- I2C 通讯 (0x65)
- DRV11873 驱动控制
- BLDC (无刷直流电机)
- PWM 转速配置以及控制、方向切换等功能
- 堵转保护
- 固件可升级

## 包装内容

- 1 x Unit-BLDC Driver
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P

## 应用场景

- 工业自动化
- 智能机器人
- 精密仪器

## 规格参数

| 规格         | 参数                                                |
| ------------ | --------------------------------------------------- |
| MCU          | STM32G030F6P6                                       |
| 电机驱动芯片 | DRV11873PWPR                                        |
| 电机类型     | 三相无传感器、无刷直流 (BLDC) 电机                  |
| 电机驱动电压 | 5V (由 Grove 口供电)                                |
| 通信接口     | I2C 通信 @ 0x65                                     |
| 输出带载能力 | DC 5V@508mA                                         |
| 功耗         | 待机电流：DC 5V@10.62mA<br/>工作电流：DC 5V@13.20mA |
| 工作温度     | 0 ~ 40°C                                            |
| 产品尺寸     | 32.0 x 24.0 x 11.3mm                                |
| 产品重量     | 6.2g                                                |
| 包装尺寸     | 138.0 x 93.0 x 12.3mm                               |
| 毛重         | 13.4g                                               |

## 原理图

- [Unit BLDC Driver 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/633/Sch_bldc_driver_V1.3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/633/Sch_bldc_driver_V1.3_sch_01.png">
</SchViewer>

## 管脚映射

### Unit BLDC Driver

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### 指示灯 LED

| STM32             | PB3/PB4/PB5/PB6 |
| ----------------- | --------------- |
| 指示灯 LED (绿色) | SYS_LED         |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-BLDC Driver/img-d749b649-9eec-4d72-9cf0-c80a878d4d55.jpg" width="100%" />

## 数据手册

- [DRV11873](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-BLDC%20Driver/drv11873.pdf)

## 软件开发

### Arduino

- [Unit BLDC Driver I2C Addr Modify Example](https://github.com/m5stack/M5Unit-BLDC/tree/master/examples/i2c_addr_modify)
- [Unit-BLDC-Driver PWM Example](https://github.com/m5stack/M5Unit-BLDC/tree/master/examples/pwm)
- [Unit-BLDC-Driver RPM Example](https://github.com/m5stack/M5Unit-BLDC/tree/master/examples/rpm)

### UiFlow1

- [Unit BLDC Driver UiFlow1 文档](/zh_CN/uiflow/blockly/unit/bldc_driver)

### UiFlow2

- [Unit BLDCDriver UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/bldc_driver.html)

### 通信协议

- [Unit BLDC Driver I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/772/Unit_BLDC_I2C_Protocol.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/772/Unit_BLDC_I2C_Protocol_page_01.png" width="100%">

## 相关视频

- Unit BLDC Driver 产品以及功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-BLDC%20Driver/U181%20BLDC%20Driver%20UNIT%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

- UiFlow2 Unit BLDC Driver

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112947556912906&bvid=BV1gEeFehEyt&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/8GUvJwVZpe0?si=vZpuTRjy6lgSy1uV" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
