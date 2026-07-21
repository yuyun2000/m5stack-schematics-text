# StackChan Core

<span class="product-sku">SKU:C156</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_weight.jpg">
</PictureViewer>

## 描述

**StackChan Core** 是 StackChan 机器人的核心控制器，可用于 StackChan 主控的维修替换。设备搭载 ESP32-S3 主控，配备 240 MHz 双核处理器，板载 16MB Flash、8MB PSRAM，原生支持 Wi-Fi 与 BLE 无线通信。
整机集成丰富外设：配备 2.0 英寸高强度玻璃电容触控屏、0.3 MP 摄像头，搭载接近传感器、环境光传感器与九轴姿态传感器；同时预留 microSD 卡槽，内置 1W 扬声器、双麦克风，并设有开关机、复位实体按键，可替代原装主机，适配 StackChan AI 桌面机器人使用。

## 注意事项

#>说明|**CoreS3**、**CoreS3-Lite** 和 **StackChan Core** 仅外观不同，硬件功能无区别。**StackChan Core**出厂预置了 StackChan 的固件，**CoreS3**、**CoreS3-Lite**在烧录 **StackChan** 固件后可以直接作为 StackChan 机器人核心主控使用。固件烧录的方法可参考 StackChan 产品页面的[恢复出厂固件](/zh_CN/StackChan#恢复出厂固件)章节。

## 产品特性

- 用于 StackChan 主控维修替换
- 基于 ESP32 开发，支持 Wi-Fi @16MB Flash，8MB PSRAM
- 内置摄像头、接近传感器、扬声器，电源指示灯，RTC，I2S 功放，双麦克风，电容式触摸屏幕，电源键，复位按键，陀螺仪
- 高强度玻璃材质
- 支持 OTG 和 CDC 功能
- 采用 AXP2101 电源管理，低功耗设计

## 包装内容

- 1 x StackChan Core
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x 内六角扳手 L 形 2.5mm (适配 M3 螺丝)

## 应用场景

- StackChan 主机更换

## 规格参数

| 规格              | 参数                                                                                                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SoC               | ESP32-S3@双核 Xtensa LX7 处理器，主频 240MHz                                                                                                                          |
| Flash             | 16MB                                                                                                                                                                  |
| PSRAM             | 8MB Quad                                                                                                                                                              |
| Wi-Fi             | 2.4 GHz Wi-Fi                                                                                                                                                         |
| 触摸 IPS LCD 屏幕 | 2.0"@320 x 240 ILI9342C                                                                                                                                               |
| 摄像头            | GC0308@ 0.3MP                                                                                                                                                         |
| 接近传感器        | LTR-553ALS-WA                                                                                                                                                         |
| 电源管理芯片      | AXP2101                                                                                                                                                               |
| 六轴姿态传感器    | BMI270                                                                                                                                                                |
| 三轴磁力计        | BMM150                                                                                                                                                                |
| RTC               | BM8563                                                                                                                                                                |
| 扬声器            | 16bits-I2S 功放芯片 AW88298@1W                                                                                                                                        |
| 音频编码芯片      | ES7210，双麦克风输入                                                                                                                                                  |
| 产品重量          | 40.6g                                                                                                                                                                 |
| 包装尺寸          | 134.0 x 91.0 x 20.5mm                                                                                                                                                 |
| 毛重              | 60.0g                                                                                                                                                                 |

## 原理图

- [StackChan Core 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_07.png">
</SchViewer>

## 尺寸图

- [StackChan Core 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_model_size.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1254/C156_StackChan_Core_model_size_page_01.png">
</SchViewer>

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116649550152796&bvid=BV1xYGQ6RE7e&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Zehps8nEVsM?si=AEVLKxfbT-TO1HrY" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>