# Stamp-AddOn Cam3660

<span class="product-sku">SKU:A182</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png">
</PictureViewer>

## 描述

**Stamp-AddOn Cam3660** 是一款专为 Stamp-S3Bat 设计的微型 CMOS 摄像头拓展模组，采用 3MP OV3660 图像传感器和 L 型柔性 FPC 结构，底部集成 24Pin B2B 板对板连接器，镜头侧边设有金属固定孔。模组通过 8 位 DVP 并行接口输出图像数据，并使用 SCCB 总线进行寄存器配置，最高支持 3MP (2048 x 1536) 分辨率图像采集。其紧凑结构适合集成至空间受限的设备中，可用于图像采集、视觉识别、视频传输等嵌入式视觉应用。

## 产品特性

- 3MP OV3660 CMOS 图像传感器
- 最高支持 2048 x 1536 分辨率
- 支持 JPEG、RAW RGB、RGB565/555/444、CCIR656 和 YCbCr422 输出格式
- 8 位 DVP 并行图像输出接口
- SCCB 配置总线
- 支持 PWDN 低功耗控制与硬件复位
- L 型柔性 FPC 结构，集成 24Pin B2B 板对板连接器
- 侧边金属固定孔，便于螺丝安装固定
- 适配 Stamp-S3Bat

## 包装内容

- 1 x Stamp-AddOn Cam3660

## 应用场景

- 嵌入式图像采集
- 物体识别与视觉检测
- 二维码识别
- 视频监控与无线图传
- IoT 视觉传感节点

## 规格参数

| 规格                 | 参数                                                                      |
| -------------------- | ------------------------------------------------------------------------- |
| 图像传感器           | OV3660 CMOS                                                               |
| 有效像素             | 3MP                                                                       |
| 最大分辨率           | 2048 x 1536                                                               |
| 镜头尺寸             | 1/5 inch                                                                  |
| 焦距                 | 2.97 ±5% mm                                                               |
| 光圈                 | F2.0 ±5%                                                                  |
| 视场角               | 60°                                                                       |
| 畸变                 | <1.5%                                                                     |
| 对焦方式             | 固定焦距 (FF)                                                             |
| 拍摄范围             | 20cm ~ ∞                                                                  |
| 调焦距离             | 80cm，点胶                                                                |
| 支持分辨率           | QVGA (320 x 240) / VGA (640 x 480) / HD (1280 x 720) / QXGA (2048 x 1536) |
| 最大帧率             | 30fps                                                                     |
| 输出格式             | JPEG、RAW RGB、RGB565/555/444、CCIR656、YCbCr422                          |
| 图像输出接口         | 8 位 DVP 并行接口                                                         |
| 配置接口             | SCCB                                                                      |
| 通信地址             | 0x3C                                                                      |
| 连接方式             | 24Pin B2B 板对板连接器                                                    |
| 外部时钟             | 20MHz                                                                     |
| 数字电路电压 (DVDD)  | 1.5V ±5%                                                                  |
| 模拟电路电压 (AVDD)  | 2.6 ~ 3.3V                                                                |
| 接口电路电压 (DOVDD) | 1.8V / 2.8V                                                               |
| 控制信号             | PWDN、RESET                                                               |
| 工作温度             | -30 ~ 70°C                                                                |
| 适配设备             | Stamp-S3Bat                                                               |

## 原理图

- [Stamp-AddOn Cam3660 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1266/A182_Stamp-AddOn_Cam3660_HZVS6049_V1.0_CS-Model_3660_2026_04_13_15_25_47_page_01.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1266/A182_Stamp-AddOn_Cam3660_HZVS6049_V1.0_CS-Model_3660_2026_04_13_15_25_47_page_01.png">
</SchViewer>

## 管脚映射

| EXP.B2B | Stamp-AddOn Cam3660 |
| ------- | ------------------- |
| 1       | MCLK                |
| 2       | D7                  |
| 3       | NC                  |
| 4       | D6                  |
| 5       | RESET               |
| 6       | D5                  |
| 7       | NC                  |
| 8       | PCLK                |
| 9       | VS                  |
| 10      | D4                  |
| 11      | PWDN                |
| 12      | D3                  |
| 13      | GND                 |
| 14      | D2                  |
| 15      | HS                  |
| 16      | D1                  |
| 17      | NC                  |
| 18      | D0                  |
| 19      | SCL                 |
| 20      | VCC3.3V             |
| 21      | GND                 |
| 22      | SYS                 |
| 23      | SDA                 |
| 24      | SYS                 |

## 数据手册

- [OV3660](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/OV3660_datasheet.pdf)

## 软件开发

### Arduino

- [Stamp-AddOn Cam3660 摄像头示例程序](/zh_CN/arduino/m5stamp_s3bat/camera)
