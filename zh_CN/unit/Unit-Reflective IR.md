# Unit Reflective IR

<span class="product-sku">SKU:U175</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Reflective IR/img-c9762edb-419d-4e67-85ac-d0056667d97f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Reflective IR/img-fecea8eb-3396-40cd-9312-20971fb55496.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Reflective IR/img-3953028a-4deb-4231-b909-752c420c5126.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Reflective IR/img-98a85e73-cb56-4610-8c7e-5321537a9749.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Reflective IR/img-7cffcff7-e1e6-4432-b644-ca791e4b1bc9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Reflective IR/img-82f72d4e-f956-4564-a421-121cce86a806.webp">
</PictureViewer>

## 描述

**Unit Reflective IR** 是一款自收发红外传感器单元，主要用于检测目标物体的反射红外光，并通过模拟信号和数字信号输出来指示检测状态。其独特的设计结合了一个板载可调电位器，可调节数字输出的灵敏度，用户可以根据具体需求调整传感器的工作参数，为整机提供了灵活性和精准性。该产品适用于物体检测、循迹、距离检测、自动化系统等领域。

\#> 注：背部电位器作用是调节检测距离 (灵敏度)，在出厂前已将阀值比较电压 (1.65V) 通过电位器调节好，非特殊情况请勿随意调节电位器，阀值比较电压有效范围：0.3V≥1.65V≤2.15V，超过此范围后，当＞2.15V 时红灯长亮，＜0.3V 时红灯不亮导致检测失效。(测量电位器电压可以根据原理图中比较器 LM393 反向端测量)

## 产品特性

- 红外感测技术： 利用红外技术，可高效、准确地检测目标物体的反射红外光线。
- 模拟信号输出： 通过红外接收管和 10k 电阻分压，根据障碍物反射红外信号的强度，来产生对应的电压值。
- 数字信号输出： 集成了 LM393 比较器，将模拟信号转换为可靠的数字信号，便于在数字系统中处理和解读。
- LED 指示灯： 数字信号控制 LED 指示灯，直观显示传感器的检测状态，使用户能够迅速了解系统运行情况。
- 可调电位器： 配备 10k 可调电位器，用户可以通过调整灵敏度和阈值以优化传感器性能，适应不同环境和应用需求。
- 编程平台：Arduino、UiFlow 等

## 包装内容

- 1 x Unit Reflective IR
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 电位器螺丝刀

## 应用场景

- 物体检测
- 距离测量
- 自动化系统
- 安防系统
- 循迹

## 规格参数

| 规格             | 参数                  |
| ---------------- | --------------------- |
| 模拟信号输出范围 | 0-4096 (ESP32@12bit)  |
| 数字信号输出     | TTL                   |
| 工作电压         | 5V                    |
| 工作温度         | 0 ~ 40°C              |
| 产品尺寸         | 32.0 x 24.0 x 12.0mm  |
| 产品重量         | 4.6g                  |
| 包装尺寸         | 138.0 x 93.0 x 13.0mm |
| 毛重             | 14.6g                 |

## 操作说明

### 检测范围

|                        | 阀值比较电压：1.65V 时 (出厂默认值电位器调到最中间) | 阀值比较电压：2.15V 时                |
| ---------------------- | --------------------------------------------------- | ------------------------------------- |
| 检测黑色障碍物最远距离 | 0CM (测试物体：100% 黑色打印 A4 纸)                 | 6.5CM (测试物体：100% 黑色打印 A4 纸) |
| 检测白色障碍物最远距离 | 13CM (测试物体：白色 A4 纸)                         | 28CM (测试物体：白色 A4 纸)           |
| 检测彩色障碍物最远距离 | 14CM (测试物体：杂志封面蓝绿黄颜色)                 | 25.5CM (测试物体：杂志封面蓝绿黄颜色) |
| 检测光泽障碍物最远距离 | 31CM (测试物体：光泽的金属钢网)                     | 43CM (测试物体：光泽的金属钢网)       |

## 原理图

- [Unit Reflective IR 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/628/SCH_UNIT_Reflective_IR_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/628/SCH_UNIT_Reflective_IR_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Reflective IR

::grove-table
| HY2.0-4P | Black | Red | Yellow         | White         |
| -------- | ----- | --- | -------------- | ------------- |
| PORT.B   | GND   | 5V  | Digital Output | Analog Output |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Reflective IR/img-9dca38e0-16f9-4657-aecf-5c1c22cc1889.jpg" width="100%" />

## 软件开发

### Arduino

- [Unit Reflective IR Arduino 驱动库](https://github.com/m5stack/M5Unit-ReflectiveIR/blob/main/examples/detect.ino)

### UiFlow1

- [Unit Reflective IR UiFlow1 文档](/zh_CN/uiflow/blockly/unit/reflective_ir)

### UiFlow2

- [Unit Reflective IR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/reflective_ir.html)

## 相关视频

- Unit Reflective IR 示例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Reflective%20IR/U175%20Reflective%20IR%20Unit%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

- Unit Reflective IR UiFlow Use

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113342777657129&bvid=BV1UuyqYqE4w&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/1CiWcwn9tjo?si=LqU8r20oUJlsxjfI" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

| UNIT               | SKU  | NOTE                   |
| ------------------ | ---- | ---------------------- |
| IR Unit            | U002 | 可编码、解码           |
| Reflective IR Unit | U175 | 自收发，不可编码、解码 |
