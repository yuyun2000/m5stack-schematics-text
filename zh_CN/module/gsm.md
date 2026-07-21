# Module GSM

<span class="product-sku">SKU:M026</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gsm/gsm_10.webp">
</PictureViewer>

## 描述

**Module GSM** 是 M5Stack 堆叠模块系列中的一款，GSM 通信模块。内部集成 **M6315** GSM/GPRS 工业级通信模组。支持 GPRS class12 和 GPRS CS-1,CS-2,CS-3,CS-4 编码，兼备性价比与出色的抗干扰性，可向电力、石油、水务、燃气、交通、金融等行业客户提供稳定的 M2M 通信功能。

## 产品特性

- SIM 卡类型: Nano
- 状态信号：两路 LED 指示灯
- 板载麦克风
- 串行通信：Uart2 16/17
- 板载双路扬声器信号输出:
  SPK1 扬声器信号输出接口
  SPK2 扬声器信号输出到主机
- 工作温度范围:-40°C 至 + 85°C
- 频段 (MHz):
  850/900/1800/1900
- 数据传输:
  速率 (kbps) 85.6 (UL)/85.6 (DL)
  GPRS 多时隙 Class12
  SMS 支持 PDU/TEXT 模式
  网络协议 IPV4/IPV6\*/TCP/UDP/PPP/HTTP/FTP/MQTT
- 耗流:
  <2mA@DRX=5
- 补充说明:
  G2 维持高电平 2s 开机
  G2 维持高电平 8s 关机
  电源按钮长按 2s 开机
  电源按钮长按 8s 关机
  G26 高电平模块复位

## 包装内容

- 1x Module GSM

## 应用场景

- 无线通信系统
- M2M 通信

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品重量 | 13g                  |
| 毛重     | 23g                  |
| 产品尺寸 | 54.2 x 54.2 x 12.8mm |
| 包装尺寸 | 60 x 57 x 17mm       |

## 原理图

- [Module GSM 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Modules/module_gsm_sch.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/954/M026-module_gsm_sch_page_01.png" width="100%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     |          |
| GND      | 5    | 6     |          |
|          | 7    | 8     | SPK2     |
|          | 9    | 10    | RST      |
|          | 11   | 12    | 3V3      |
|          | 13   | 14    |          |
| TXD      | 15   | 16    | RXD      |
|          | 17   | 18    |          |
| GSM_PWR  | 19   | 20    |          |
|          | 21   | 22    |          |
|          | 23   | 24    |          |
|          | 25   | 26    |          |
|          | 27   | 28    | 5V       |
|          | 29   | 30    |          |
::

## 数据手册

- [MC6315](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M6315_cn.pdf)

## 软件开发

### Arduino

- [Module GSM](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/GSM_M6315)

### 通信协议

- [MC6315 AT指令表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M6315%20AT_Command_Interface_Specification_cn.pdf)

### Easyloader

| Easyloader                                | 下载链接                                                                                             | 备注 |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| Module GSM Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_GSM_MODULE.exe) | /    |
