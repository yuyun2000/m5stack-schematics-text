# Unit Mini OLED

<span class="product-sku">SKU:U166</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-8d9a2ae0-331b-4c02-8e2f-0f9142a4395d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-41b7b812-ba0b-4fda-b62b-029c5c445ffd.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/756/U166-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-039e47f6-5b66-43eb-a8b7-6273294e4ebb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-6383aab5-00d1-49b9-8657-ec2db2c09cd5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-a04b6094-fda7-49b6-9d28-f18179016b25.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-773703ef-7737-432c-b328-f55d429b4d74.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-851eb5d5-258b-4d13-baf4-d938fd68701c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-731967a9-fe9e-45a6-ad1f-4da78a5baa11.webp">
</PictureViewer>

## 描述

**Unit Mini OLED** 是一款 **0.42 英寸** 的 OLED 屏幕单元，采用 I2C 接口，分辨率为 **72 x 40**，单色白色显示，通过 I2C (addr: 0x3C) 与 M5 主机进行通信。该 OLED 屏幕适合嵌入到各种家居产品 、 智能穿戴设备 、 便携式设备和工业仪表等。

## 产品特性

- 单色白色显示
- I2C 通讯 (0x3C)
- SSD1315 驱动

## 包装内容

- 1 x Unit Mini OLED
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 智能穿戴设备
- 便携式设备和工业仪表
- 家居产品

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 屏幕尺寸 | 0.42 英寸 OLED       |
| 分辨率   | 72 x 40              |
| 工作电压 | 3.3V                 |
| 控制芯片 | SSD1315              |
| 显示颜色 | 白色                 |
| 显示区域 | 9.196 x 5.18mm       |
| 像素间距 | 0.128 x 0.13mm       |
| 工作温度 | 0 ~ 40°C             |
| 视角方向 | 全视角               |
| 产品尺寸 | 25.8 x 12.0 x 6.8mm  |
| 产品重量 | 2.2g                 |
| 包装尺寸 | 138.0 x 93.0 x 7.8mm |
| 毛重     | 5.4g                 |

## 原理图

- [Unit Mini OLED 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/621/Sch_UNIT-MiniOLED.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/621/Sch_UNIT-MiniOLED_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Mini OLED

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/MiniOLED Unit/img-bd4c16f8-05f0-41d7-98a6-45d6405658ef.jpg" width="100%" />

## 数据手册

- [Unit Mini OLED Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/MiniOLED%20UNIT/0.42%20OLED.PDF)

## 软件开发

### Arduino

- [Unit Mini OLED 测试程序](https://github.com/m5stack/M5Stack/blob/master/examples/Unit/MiniOLED/MiniOLED.ino)

### UiFlow1

- [Unit Mini OLED UiFlow1 文档](/zh_CN/uiflow/blockly/unit/mini_oled)

### UiFlow2

- [Unit Mini OLED UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/minioled.html)

## 相关视频

- UiFlow2 Mini OLED Unit

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112970742891183&bvid=BV17Ke3eMEhP&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Ff8r6eHQyWY?si=simhH_hiaLFwwJkq" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
