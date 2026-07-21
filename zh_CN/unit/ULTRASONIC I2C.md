# Unit Ultrasonic-I2C

<span class="product-sku">SKU:U098-B1</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC I2C/img-1e58d893-802c-4b8b-ad5e-704933a3c76e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC I2C/img-deba1486-f2e6-4ab1-9b87-4d8acae20a51.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC I2C/img-6bf63229-2b8d-4085-9a6b-da13cc903e75.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC I2C/img-0b9f0e1e-0856-4346-acee-fd06690402a7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC I2C/img-0a0df04b-9bbd-4cfb-a521-290409d30ef4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC I2C/img-66f70d6f-eae1-433a-b8f2-a8f64b4c9239.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC I2C/img-765d42b8-3471-4151-841e-9fe803eb95ad.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC I2C/img-d2bff0f2-d608-4c04-ba30-3165b3d8f4bd.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/697/U098-B1-weight.jpg">
</PictureViewer>

## 描述

**Unit Ultrasonic-I2C**是一款 **I2C** 通信接口的 **超声波测距** 传感器。硬件采用 RCWL-9620 超声波测距单芯片搭配 16 mm 探头，能够实现 **2 cm ~ 450 cm** 范围内的精准测距（精度达 ±2%）。传感器作为 I2C 从设备能够与其他的 I2C 设备共享总线资源，能够最大程度节省 IO 使用。非常适合应用于机器人避障，液面检测等应用场景。

\#> 注意：测量大于 3.5m 时，测距数据响应会稍有延迟。

## 产品特性

- RCWL-9620
- I2C 通信接口 (addr: 0x57)
- 量程: 2cm-450cm
- 覆盖保护外壳，电路运行更稳定
- 内置温度补偿，减小探头温飘影响
- 支持 UiFlow 图形化编程

## 包装内容

- 1 x Unit Ultrasonic-I2C
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 机器人避障
- 液位测量
- 坐姿检测

## 规格参数

| 规格             | 参数                 |
| ---------------- | -------------------- |
| 超声波测距单芯片 | RCWL-9620            |
| 量程             | 2cm ~ 450cm          |
| 通信接口         | I2C 通信 @ 0x57      |
| 探头规格         | 16mm                 |
| 接收 / 发射频率  | 40KHz                |
| 接收灵敏度       | -65dB                |
| 指向角           | 60°                  |
| 测量精度         | ±2%                  |
| 测量周期         | 50ms                 |
| 工作电流         | 3mA                  |
| 产品尺寸         | 56.0 x 24.0 x 15.2mm |
| 产品重量         | 12.2g                |
| 包装尺寸         | 75.0 x 46.0 x 36.0mm |
| 毛重             | 27.1g                |

## 管脚映射

### Unit Ultrasonic-I2C

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT%20SONIC%20I2C/model%20size.jpg" width="100%" />

## 结构文件

- [Unit Ultrasonic-I2C 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U098-B1_Unit_Ultrasonic-I2C/Structures)

## 数据手册

- [RCWL-9620 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/697/RCWL-9620-V1.0.pdf)

## 软件开发

### Arduino

- [Unit Ultrasonic-I2C Test Example with M5Atom](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5Atom/Unit_SonicI2C_M5Atom.ino)
- [Unit Ultrasonic-I2C Test Example with M5Core](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5Core/Unit_SonicI2C_M5Core.ino)
- [Unit Ultrasonic-I2C Test Example with M5Core2](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5Core2/Unit_SonicI2C_M5Core2.ino)
- [Unit Ultrasonic-I2C Test Example with M5StickC](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5StickC/Unit_SonicI2C_M5StickC.ino)
- [Unit Ultrasonic-I2C Test Example with M5StickCPlus](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5StickCPlus/Unit_SonicI2C_M5StickCPlus.ino)

### UiFlow2

- [Unit Ultrasonic-I2C UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ultrasonic.html)

## 相关视频

- 超声波小车避障

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/sonic_i2c_gpio_video.mp4" type="video/mp4"></video>

- UiFlow2 Unit Ultrasonic-I2C

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112828656715349&bvid=BV1Xi8QeNEW9&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/JwLsdgIdaJc?si=QEsZMJ6tK2DVgV4R" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
