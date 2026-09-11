# Stamp UWB F

<span class="product-sku">SKU:S017-F</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F-weight.png">
</PictureViewer>

## 描述

Stamp UWB F 是一款超小体积的嵌入式 UWB 测距模组，**模组背部预焊 0.5mm‑12P FPC 座子，可通过 0.5mm‑12P FPC 排线对外引出**。内置 QM33120W 低功耗 UWB 收发器，兼容 IEEE 802.15.4‑2020 以及 IEEE 802.15.4z‑2020 BPRF，工作在 UWB Channel 9，中心频率 7987.2 MHz。模组体积小巧、射频性能稳定，支持搭建 TWR、TDoA 定位方案，可实现厘米级测距与高精度定位。目前驱动库支持单边双向测距（SS‑TWR）及双边双向测距（DS‑TWR）两种测距模式，适用于室内人员定位、货物资产追踪、近距检测、机器人导航等应用场景。

## 注意事项

!> 接线说明| 该模组可搭配 **Stamp‑C5 DIP** 使用，接线时请注意**区分 FPC 排线正反面**，切勿接反，否则会损坏设备。<br>该 Stamp UWB F 模组的 FPC 座线序与 Stamp-S3 / S3A 背部 FPC 线序不兼容，严禁直接连接，否则可能导致设备永久性损坏。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017_F_FPC_Warning.png" width="60%">

!>FPC 排线说明| 下方示意图使用的是 Stamp UWB F 配套的 FPC 排线。若用户自行更换第三方排线使用，请**务必仔细核对排线线序与触点方向**，线序或方向错误会损坏硬件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017_F_FPC_Warning_02.png" width="60%">

?>供电说明|为保证通信质量，请使用高 PSRR LDO 或电源纹波在 12mVpp 以内的电源给 Stamp UWB F 供电。

?>PCB 天线净空|在进行整机设计时，请注意 FPC 排线及其连接器对模组天线性能的影响。FPC 排线不得经过模组 PCB 天线下方或天线净空区域，否则可能改变天线阻抗和辐射特性，降低射频性能并引入测距误差。建议将 FPC 排线布置在天线区域之外，并在整机装配完成后进行实际测试，以确保产品的通信距离和测距精度满足设计要求。<br>**如需获得更好的射频性能，推荐使用 SMT 版本 Stamp UWB。**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F_operate_01.png" width="60%">

## 产品特性

- 集成 QM33120W UWB 收发器，支持增强型 Time-of-Flight 安全模式，集成 AES-256
- 支持 UWB Channel 9
- 支持 IEEE 802.15.4-2020 / IEEE 802.15.4z-2020 BPRF
- 支持 TWR、TDoA 定位方案
- 支持 850 kbps / 6.81 Mbps 无线通信速率
- SPI 通信接口
- 支持 0.5mm-12P FPC 连接方式

## 包装内容

- 1 x Stamp UWB F
- 1 x 0.5mm-12P FPC 排线

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
| 背部扩展接口 | FPC 0.5mm-12P                                                                                                                                             |
| 休眠功耗     | DC 3.3V@75.9uA                                                                                                                                            |
| 工作功耗     | 作为基站：DC 3.3V@5.23mA <br>作为从机：DC 3.3V@58.0mA                                                                                                     |
| 产品尺寸     | 11.5 x 12.0 x 2.8mm                                                                                                                                       |
| 产品重量     | 0.6g                                                                                                                                                      |
| 包装尺寸     | 138.0 x 93.0 x 17.0mm                                                                                                                                     |
| 毛重         | 4.8g                                                                                                                                                      |

## 原理图

- [Stamp UWB F 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/SCH_UWB_MODULE_SCH_main_V0.2_20251128_2026_06_01_11_54_35.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/SCH_UWB_MODULE_SCH_main_V0.2_20251128_2026_06_01_11_54_35_page_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F_Stamp_UWB_F.jpg">

## 尺寸图

- [Stamp UWB F 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F-Stamp_UWB_F_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1269/S017-F-Stamp_UWB_F_model_size_page_01.png" width="100%">

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

- [Stamp UWB F Arduino 上手教程](/zh_CN/arduino/projects/stamp/stamp_uwb)
- [Stamp UWB F 驱动库](https://github.com/m5stack/M5Stamp-UWB)

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
