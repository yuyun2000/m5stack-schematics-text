# Unit Limit

<span class="product-sku">SKU:U145</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit Limit/img-7da470fe-12b4-4694-bcd7-62077c1cce2e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit Limit/img-acbc90b9-37cd-4322-8cb2-14e4c0f2697f.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/700/U145-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit Limit/img-233adf9a-007d-4fd4-ac39-c9496e4e2b0f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit Limit/img-f4bd733d-dfb7-47c8-9c51-7d029f83a252.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit Limit/img-a29416df-6194-4961-908b-1035a06fb498.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit Limit/img-3e647b89-c78a-47ce-8f6a-d5df3effcac9.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/700/U145-weight.jpg">
</PictureViewer>

## 描述

**Unit Limit** 是一款行程开关单元，当开关柄受到外力闭合时，开关单元的数字信号接口将由 3.3V 高电平下拉至 0V 低电平，能够向 MCU 或其他主控外设提供一个限位触发信号。适用于各类运动机械设备，用以控制其行程、进行终端限位保护。

## 产品特性

- 触点式行程开关
- 性能稳定，可靠耐用，高达 40 万次的机械寿命
- 多种机械固定方式

## 包装内容

- 1 x Unit limit
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 急停控制 / 限位开关
- 3D 打印机限位开关

## 规格参数

| 规格             | 参数                  |
| ---------------- | --------------------- |
| 开关柄长         | 16mm                  |
| 机械寿命         | 40 万次               |
| 供电电压         | DC 5V                 |
| 按键输出逻辑信号 | DC 3.3V               |
| 待机电流         | DC 5V@2mA             |
| 工作电流         | DC 5V@3mA             |
| 产品尺寸         | 32.0 x 24.0 x 9.5mm   |
| 产品重量         | 6.4g                  |
| 包装尺寸         | 138.0 x 93.0 x 10.5mm |
| 毛重             | 11.5g                 |

## 原理图

- [Unit Limit 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/600/SCH_unitLimit_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/600/SCH_unitLimit_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Limit

::grove-table
| HY2.0-4P | Black | Red | Yellow | White          |
| -------- | ----- | --- | ------ | -------------- |
| PORT.B   | GND   | 5V  | NC     | Digital Output |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Limit/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit Limit 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U145_Unit_Limit/Structures)

## 软件开发

### Arduino

- [Unit Limit 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/LIMIT)

### UiFlow1

- [Unit Limit UiFlow1 文档](/zh_CN/uiflow/blockly/unit/limit)

### UiFlow2

- [Unit Limit UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/limit.html)

### EasyLoader

| Easyloader                 | 下载链接                                                                                                                              | 备注 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Limit Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit%20Limit/ezLoader-b443d1de-440e-4304-a4bb-3996e2f91242.exe) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113185910688959&bvid=BV1ERsUeoE4S&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/c9X2GVD3WDs?si=Gc3hyQtMzHbcpZLf" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
