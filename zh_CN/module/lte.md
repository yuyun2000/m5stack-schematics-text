# Module LTE

<span class="product-sku">SKU:M027</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lte/lte_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lte/lte_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lte/lte_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_06.webp">
</PictureViewer>

## 描述

**Module LTE** 是 M5Stack 堆叠模块系列中的一款，LTE 通信模块。内部集成 **M8321** LTE 全网通工业级通信模组。提供 TD-LTE/FDD-LTE/WCDMA/TDSCDMA/GSM/GPRS/EDGE 的频段。丰富的 Internet 协议、行业标准接口和功能，支持多种操作系统的 USB 驱动程序，能够给用户带来快速且稳定的通信体验。

## 产品特性

- SIM 卡类型: Nano
- 状态信号：三路 LED 指示灯
- 板载麦克风
- 板载扬声器信号输出接口
- 板载 USB 测试点
- 单路开关机按钮
- 串行通信：Uart2 16/17
- 工作温度范围:-40°C 至 + 85°C
- 频段:
  LTE-TDD:B38/B39/B40/B41
  LTE-FDD:B1/B3/B8△
  TD-SCDMA:B34/B39△
  WCDMA:B1/B8△
  GSM (MHz):900/1800
- 数据传输:
  LTE 速率 (Mbps) LTE-FDD 50 (UL)/150 (DL)△　LTE-TDD 50 (UL)/100 (DL)
  HSPA+ 速率 (Mbps) 5.76 (UL)/21.6 (DL)△
  TD-SCDMA 速率 (Mbps) 2.2 (UL)/2.8 (DL)△
  EDGE 速率 (Kbps) 384 (UL)/384 (DL)
  GPRS 速率 (Kbps) 85.6 (UL)/85.6 (DL)
  SMS 支持 PDU/TEXT 模式
  网络协议 IPV4/IPV6/TCP/PPP/UDP/FTP/HTTP/NTP
- 耗流:
  17uA@Poweroff
  3mA@Sleep
  45mA@Idle

## 包装内容

- 1 x Module LTE
- 1 x 天线

## 应用场景

- 安防路由
- 车载后装
- 视频监控
- POC

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品重量 | 18g                  |
| 毛重     | 29g                  |
| 产品尺寸 | 54.2 x 54.2 x 12.8mm |
| 包装尺寸 | 60 x 57 x 17mm       |

## 原理图

- [Module LTE 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Modules/module_lte_sch.pdf)

## 管脚映射

| M5Core     | G16 | G17 | 5V  | GND |
| ---------- | --- | --- | --- | --- |
| Module LTE | RX  | TX  | 5V  | GND |

## 数据手册

- [M8321](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M8321_cn.pdf)

## 软件开发

### Arduino

- [Module LTE Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/LTE_M8321)

### 通信协议

- [M8321 AT 指令表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M8321%20AT_Command_Interface_Specification_cn.pdf)

### Easyloader

| Easyloader                                | 下载链接                                                                                             | 备注 |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| Module LTE Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_LTE_MODULE.exe) | /    |
