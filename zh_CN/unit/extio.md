# Unit EXT.IO

<span class="product-sku">SKU:U011</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio/extio_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio/extio_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio/extio_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio/extio_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio/extio_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio/extio_06.webp">
</PictureViewer>

## 描述

**Unit EXT.IO**是一款并行端口拓展器。集成了 IO 拓展芯片 PCA9554PW，支持拓展至 8 个 GPIO，能够用于 2.3 ~ 5.5V VCC 、开漏、上拉、中断输出操作。通过 I2C 接口 (串行时钟 SCL，串行数据 SDA) 辅助多数的微控制器提供 I/O 拓展，对于 I/O 引脚紧缺，又不想浪费资源添加额外控制器的开发者来说，**Unit EXT.IO**会是一个不错辅助。

### 产品特性

- I2C 通讯
- 输入输出拓展
- HY2.0-4P 接口，支持 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc).
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit EXT.IO
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 规格参数

| 规格         | 参数            |
| ------------ | --------------- |
| 通信接口     | I2C 通信 @ 0x27 |
| I/O 扩展数量 | 8               |
| 净量         | 5g              |
| 毛重         | 16g             |
| 产品尺寸     | 32 x 24 x 11mm  |
| 包装尺寸     | 67 x 53 x 12mm  |

## 操作说明

参考原理图及 PCA9554PW 数据手册可知，该 Unit 能够通过控制 A0~A2 引脚的电平组合，修改设备的 I2C 地址。(默认地址为 0x27，更多信息请查看 datasheet)
在 Unit 的 PCB 板上预留了三个贴片电阻焊接位，分别为 A0-A2 (R6-R8)，如下图所示。

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio/extio_sch_01.webp" width="80%">

## 管脚映射

### Unit EXT.IO

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

- [Unit EXT.IO 尺寸图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/788/U011_B_Model_Size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/788/U011_B_Model_Size.png" width="100%">

## 数据手册

- [PCA9554PW](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/PCA9554PW_en.pdf)

## 软件开发

### Arduino

- [Unit EXT.IO Test Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/EXT_IO_PCA9554PW)

### UiFlow1

- [Unit EXT.IO UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ext_io)

### UiFlow2

- [Unit EXT.IO UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/extio.html)

### EasyLoader

| Easyloader             | 下载链接                                                                                       | 备注 |
| ---------------------- | ---------------------------------------------------------------------------------------------- | ---- |
| Unit EXT.IO Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_EXT_IO.exe) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113423190853328&bvid=BV1AcDnYhEFa&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/goepTBsgYWk?si=uyT2ye0dgfuswlo3" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
