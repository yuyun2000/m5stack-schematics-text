# Atom HDriver

<span class="product-sku">SKU:K050</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_hdriver/atom_hdriver_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_hdriver/atom_hdriver_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_hdriver/atom_hdriver_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_hdriver/atom_hdriver_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_hdriver/atom_hdriver_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_hdriver/atom_hdriver_06.webp">
</PictureViewer>

## 描述

**Atom HDriver** 是一款适配 ATOM 控制器的 **H 桥** 电机驱动器。内置 DRV8876 电机驱动芯片，支持 9 - 24V/DC 电源输入 (内嵌 DC/DC 电路为整机设备供电，ADC 引脚 G33 直连分压电路可随时监测电源输入情况) ，输出电流可达 1.5A ，峰值 2A ，能够用于直流电机调速与正反转控制。驱动内部集成了 N 沟道 H 桥、充电泵稳压器、电流检测和调节、电流比例输出和保护电路 (保护功能集成：电源欠压锁定 (UVLO)、充电泵欠压 (CPUV)、输出过流 (OCP) 和器件超温 (TSD) ，故障情况并通过 **FAULT** 引脚指示) 。

## 产品特性

- N 沟道 H 桥电机驱动器
  - 驱动一台双向有刷直流电机
  - 其他阻性和感性负载
    – DRV8876:700mΩ(高侧 + 低侧)
- 高输出电流能力
  - 实际输出 1.5A, 峰值 2A
    – H 桥控制模式
- 3.3V 逻辑输入
- 扩频时钟可降低电磁干扰
- 集成保护功能
  - 欠压锁定 (UVLO)
  - 电荷泵欠压 (CPUV)
  - 过电流保护 (OCP)
  - 自动重试或锁存输出 (IMODE)
  - 热关机 (TSD)
  - 自动故障恢复
  - 故障指示器引脚 (nFAULT)

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic HDriver Base
- 1 x HT3.96-4P 端子
- 1 x M2 内六角扳手
- 1 x M2\*8 杯头机械牙螺丝
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- 直流电机控制

## 规格参数

| 规格     | 参数                   |
| -------- | ---------------------- |
| 输入电压 | DC 9 ~ 24V             |
| 输出电流 | 实际输出 1.5A, 峰值 2A |
| 产品尺寸 | 24 x 48 x 18mm         |
| 产品重量 | 16g                    |
| 包装尺寸 | 54 x 54 x 20mm         |
| 毛重     | 36g                    |

## 操作说明

\#> 故障提示:| 当故障发生时，将触发 FAULT (G22) 引脚下拉，G33 能够获取输入电压的 1/10, 能够用于检测当前的电源输入情况。

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_hdriver/atom_hdriver_sch_01.webp" width="80%">

## 管脚映射

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN |
| -------- | ---- | ----- | --- |
| 3V3      |      | 1     |     |
| FAULT    | 2    | 3     |     |
| IN1      | 4    | 5     | 5V  |
| IN2      | 6    | 7     | GDN |
| VIN-1/10 | 8    | 9     |     |
::

## 数据手册

- [DRV8876PWPR](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_hdriver/C575551_DRV8876PWPR_2020-06-01.PDF)

## 软件开发

- [Atom HDriver 测试程序](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_Hdriver)

### UiFlow1

- [Atom HDriver UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/h_driver)

### Easyloader

| Easyloader                   | 下载链接                                                                                                          | 备注 |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---- |
| Atom HDriver Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_Atom_Hdriver.exe) | /    |

## 相关视频

- 按下中间按键控制电机正反转，长按停止

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_HDRIVER.mp4" type="video/mp4">
</video>
