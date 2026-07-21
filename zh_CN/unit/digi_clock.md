# Unit DigiClock

<span class="product-sku">SKU:U146</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/digi_clock/digi_clock_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/digi_clock/digi_clock_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/754/U146-weight.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/digi_clock/digi_clock_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/digi_clock/digi_clock_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/digi_clock/digi_clock_05.webp">
</PictureViewer>

## 描述

**Unit DigiClock** 是一款 2.1 英寸 4 位 7 段数码管模块，带有小数点 ( **.** ) 和冒号 ( **：** )，可以显示小数点或者时间。采用 TM1637 驱动方案，驱动芯片选用 STM32F030 处理器进行 **I2C** 通信，使用时用户能够将其挂载到现有设备的 I2C 总线中，起到节省 IO 的作用。通过配置 4 位拨码开关可以修改设备 **I2C 地址**，红色发光数码管支持 8 级亮度调整。板上配置 4 个固定孔。

## 产品特性

- 4 位红色数字显示
- Port A 接口
- 可编程 I2C 地址
- 8 个可调亮度调整
- 低功耗功能
- 板载预留四个固定孔，多种固定方式

## 包装内容

- 1 x Unit DigiClock
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 时钟显示
- 数据显示
- 秒表

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32F030F4P6         |
| 驱动芯片 | TM1637                |
| 通信接口 | I2C 通信 @ 0x30       |
| 供电电压 | DC 5V                 |
| 产品尺寸 | 50.0 x 31.0 x 14.0mm  |
| 产品重量 | 12.5g                 |
| 包装尺寸 | 136.0 x 92.0 x 15.0mm |
| 毛重     | 17.8g                 |

### 功耗测试

| 环境        | DC 5V 下电流值 |
| ----------- | -------------- |
| 待机 (全关) | 2.5mA          |
| SG1         | 6.6mA          |
| SG2         | 10.3mA         |
| SG3         | 17.5mA         |
| SG4         | 38.7mA         |
| SG5         | 42.0mA         |
| SG6         | 45.7mA         |
| SG7         | 49.2mA         |
| SG8 (全开)  | 52.5mA         |

## 原理图

- [Unit DigiClock 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/601/Sch_UNIT_Digi-Clock.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/601/Sch_UNIT_Digi-Clock_sch_01.png">
</SchViewer>

## 管脚映射

### Unit DigiClock

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- **Datasheet**
  - [TM1637](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/digi_clock/TM1637.pdf)

## 软件开发

### Arduino

- [Unit DigiClock Arduino 驱动库](https://github.com/m5stack/M5Unit-DigiClock)

### UiFlow1

- [Unit DigiClock UiFlow1 文档](/zh_CN/uiflow/blockly/unit/digi_clock)

### UiFlow2

- [Unit DigiClock UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/digi_clock.html)

### 通信协议

- I2C 寄存器表

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/digi_clock/digi_clock_sch_02.webp" width="80%">

- 字符对照表

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/digi_clock/digi_clock_sch_03.webp" width="80%">

### 相关视频

- UiFlow2 Digi-Clock Unit

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113026963342961&bvid=BV13usLeJEZK&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/lJAH1jnpBV4?si=h0dltMXkE0Z___Ux" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
