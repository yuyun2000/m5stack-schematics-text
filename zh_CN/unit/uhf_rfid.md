# Unit UHF-RFID

<span class="product-sku">SKU:U107</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_04.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_cover_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/842/U107-weight.jpg">
</PictureViewer>

## 描述

**Unit UHF-RFID** 是一款超高频（UHF）嵌入式无线射频读写模块。采用 JRD-4035 模块方案，内置陶瓷天线，完全免除普通 UHF 模块需要另配天线而给用户带来的技术的不确定性。优化 RF 设计实现模块的低耗电高性能，使用串行通信接口，配合内置封装的 AT 指令集，实现即插即用，提供良好的开发与使用体验。适用仓储物流管理与智慧零售等应用场景，满足监控读取多个产品标签的应用需求。

## 产品特性

- 检测距离：1m
- 工作频谱范围：840 ~ 960 MHz
- 空中接口协议:
  - EPCglobal UHF Class 1 Gen 2
  - ISO/IEC 18000-6C
- UART 通信接口 (波特率：115200bps)
- 缓存区最大容纳 200 标签
- 标签识别灵敏，稳定

## 包装内容

- 1 x Unit UHF-RFID
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x RFID 标签 (840 ~ 960 MHz)

## 应用场景

- 仓储物流托盘管理
- 车辆管理
- 智慧零售

## 规格参数

| 规格         | 参数                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| 空中接口协议 | EPCglobal UHF Class 1 Gen 2<br>ISO/IEC 18000-6C                                                                    |
| 工作区域支持 | 美国、加拿大及其他遵循 FCC 的地区<br>欧洲及其他遵循 ETSI EN 302 208 的地区<br>中国大陆、台湾、日本、韩国、马来西亚 |
| 工作频谱范围 | 840 ~ 960 MHz                                                                                                      |
| 输出功率范围 | 18 ~ 26 dBm                                                                                                        |
| 标签缓存区   | 200 标签                                                                                                           |
| 通信协议     | UART (波特率：115200bps)                                                                                           |
| 外壳材质     | Plastic (PC)                                                                                                       |
| 产品尺寸     | 56.0 x 48.0 x 11.5mm                                                                                               |
| 产品重量     | 41.0g                                                                                                              |
| 包装尺寸     | 88.0 x 61.0 x 21.0mm                                                                                               |
| 毛重         | 58.8g                                                                                                              |

## 操作说明

\#> 读取距离说明 | 关于 Unit UHF-RFID 读取距离，若实际使用中未达到文档标称的 1m，可从两方面排查：一是需确认是否将发射功率设置为最大值；二是该设备天线频率已固定为 922MHz，若软件中设置的频率与天线频率偏差较大，也会导致读取距离改变。

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_sch_01.webp" width="80%">

## 管脚映射

### Unit UHF-RFID

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/uhf_rfid/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="80%">

## 数据手册

- [UHF RFID Unit (JRD-4035) 规格说明](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U107%20UHF-RFID/JRD-100%EF%BC%8CSDK%20%E5%8C%85.zip)

## 软件开发

### Arduino

- [Unit UHF-RFID Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_rfid_uhf)
- [Unit UHF-RFID Arduino 驱动库与测试程序](https://github.com/m5stack/M5Unit-UHF-RFID)

### 通信协议

- [Unit UHF-RFID 常用控制指令](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/842/Unit-RFID-UHF-Protocol-CN.pdf) <!--注意中英文链接不一样！！-->

### EasyLoader

| Easyloader                    | 下载链接                                                                                                              | 备注 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit UHF-RFID Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_UHF_RFID.exe) | /    |

### UiFlow2

- [Unit UHF-RFID UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/uhf_rfid.html)

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UHF-RFID_VIDEO.mp4" type="video/mp4">
</video>
