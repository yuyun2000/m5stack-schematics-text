# Stamp UWB

<span class="product-sku">SKU:S017</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017-weight.png">
</PictureViewer>

## 描述

Stamp UWB 是一款超小体积的嵌入式 UWB 测距模组，**支持邮票孔 SMT 贴片安装**，内置 QM33120W 低功耗 UWB 收发器，兼容 IEEE 802.15.4‑2020 以及 IEEE 802.15.4z‑2020 BPRF，工作在 UWB Channel 9，中心频率 7987.2 MHz。模组体积小巧、射频性能稳定，支持搭建 TWR、TDoA 定位方案，可实现厘米级测距与高精度定位。目前驱动库支持单边双向测距（SS‑TWR）及双边双向测距（DS‑TWR）两种测距模式，适用于室内定位、安全测距、资产追踪、近距检测及机器人导航等应用场景。

## 注意事项

?>供电说明|为保证通信质量，请使用高 PSRR LDO 或电源纹波在 12mVpp 以内的电源给 Stamp UWB 供电。

?> 兼容性注意 | 该 Stamp UWB 模组的 FPC 焊盘线序与 Stamp-S3 / S3A 背部 FPC 线序不兼容，实际应用请确认引脚实际连接情况，否则可能导致设备永久性损坏。

?>模组布局|如使用模组进行板上（on-board）设计，需注意模组在底板上的布局，尽可能减小底板对模组 PCB 天线性能及测距精度的影响。
建议将模组天线区域完全伸出底板边缘，并使天线馈点一侧靠近底板板边放置。天线区域下方及周围应避免铺铜、走线、放置器件或其他金属结构。在下图所示的模组摆放位置中，“✓”表示强烈推荐的摆放位置，其他位置不推荐。<br>在进行整机设计时，需注意外壳、电池、显示屏及其他金属结构对模组天线的影响，建议天线在各方向保留净空区域。整机装配完成后，应进行射频性能和测距精度测试，以确保产品性能满足设计要求。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_operate_01.png" width="60%">

## 产品特性

- 集成 QM33120W UWB 收发器，支持增强型 Time-of-Flight 安全模式，集成 AES-256
- 支持 UWB Channel 9
- 支持 IEEE 802.15.4-2020 / IEEE 802.15.4z-2020 BPRF
- 支持 TWR、TDoA 定位方案
- 支持 850 kbps / 6.81 Mbps 无线通信速率
- SPI 通信接口
- 支持邮票孔 SMT 贴片安装，间距 1.27 mm

## 包装内容

- 1 x Stamp UWB

## 应用场景

- 室内人员定位
- 货物资产追踪
- 近距检测
- 机器人导航

## 规格参数

| 规格         | 参数                                                                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UWB 芯片     | QM33120W                                                                                                                                                  |
| UWB 频率范围 | 8GHz (7987.2 MHz)<br>**Channel 9：7987.2 MHz**<br>Low frequency: 7737.6 MHz<br>Mid frequency: 7987.2 MHz<br>High frequency: 8236.8 MHz<br>带宽：499.2 MHz |
| UWB 通信接口 | SPI                                                                                                                                                       |
| 支持的标准   | IEEE 802.15.4-2020 / IEEE 802.15.4z-2020 BPRF                                                                                                             |
| 无线通信速率 | 850 kbps / 6.81 Mbps                                                                                                                                      |
| 测距功能     | 支持 SS-TWR / DS-TWR 测距                                                                                                                                 |
| 最远通信距离 | 55m （正对）                                                                                                                                              |
| 定位功能     | 支持 TWR、TDoA 定位方案                                                                                                                                   |
| 测量误差     | DS-TWR：约 0.14m                                                                                                                                          |
| 邮票孔间距   | 1.27 mm                                                                                                                                                   |
| 休眠功耗     | DC 3.3V@75.9uA                                                                                                                                            |
| 工作功耗     | 作为基站：DC 3.3V@5.23mA <br>作为从机：DC 3.3V@58.0mA                                                                                                     |
| 产品尺寸     | 11.5 x 12.0 x 1.6mm                                                                                                                                       |
| 产品重量     | 0.5g                                                                                                                                                      |
| 包装尺寸     | 138.0 x 93.0 x 15.0mm                                                                                                                                     |
| 毛重         | 4.6g                                                                                                                                                      |

## 原理图

- [Stamp UWB 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/SCH_UWB_MODULE_SCH_main_V0.2_20251128_2026_06_01_11_54_35.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/SCH_UWB_MODULE_SCH_main_V0.2_20251128_2026_06_01_11_54_35_page_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_pinmap.jpg">

## 尺寸图

- [Stamp UWB 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017-Stamp_UWB_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017-Stamp_UWB_model_size_page_01.png" width="100%">

## PCB

- [Stamp UWB PcbDoc](https://github.com/m5stack/M5_Hardware/tree/master/Products/S017_Stamp_UWB/Footprint)
- [Stamp UWB KiCad 封装库](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/Footprints/M5Stack.pretty/Stamp_UWB.kicad_mod)

## 结构文件

- [Stamp UWB KiCad 3D](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/3D/M5Stack.3dshapes/Stamp_UWB.step)

## 数据手册

- [QM33120W Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/QM33120W_datasheet.pdf)
- [QM33120W Product Brief](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/QM33120W_Product_Brief.pdf)

## 软件开发

### Arduino

- [Stamp UWB Arduino 上手教程](/zh_CN/arduino/projects/stamp/stamp_uwb)
- [Stamp UWB 驱动库](https://github.com/m5stack/M5Stamp-UWB)

## 相关视频

<VideoGallery>
  <VideoItem title="Stamp UWB 产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_video_CN.mp4" />
</VideoGallery>

## 产品对比

::compare-table
| 产品对比表                      | [Stamp UWB F](/zh_CN/stamp/Stamp_UWB_F) ![Stamp UWB F](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_02.webp)                        | [Stamp UWB](/zh_CN/stamp/Stamp_UWB) ![Stamp UWB](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/S017_Stamp_UWB_main_pictures_02.webp)                                    |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 是否默认焊接 0.5mm-12P FPC 座子 | ✅                                                                                                                                                                             | ❌                                                                                                                                                                               |
| 是否标配 0.5mm-12P FPC 排线     | ✅                                                                                                                                                                             | ❌                                                                                                                                                                               |
::
