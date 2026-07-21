# Hat Thermal

<span class="product-sku">SKU:U062</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-thermal/hat-thermal_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-thermal/hat-thermal_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/856/U062-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-thermal/hat-thermal_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-thermal/hat-thermal_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/856/U062-weight.jpg">
</PictureViewer>

## 描述

**Hat Thermal**是一款兼容 M5StickC 的人体红外热成像设备。内置 **MLX90640** 热电堆传感器，能够测量物体表面温度，并通过由表面温度形成的温度梯度，生成热成像图片（图片分辨率为 **32 x 24**）。**MLX90640** 红外（IR）传感器阵列具备了高分辨率与在恶劣环境中可靠工作的能力。与昂贵的高端热像仪相比，**Hat Thermal**是一个高性价比的替代方案。相对一般的微测辐射热计，该传感器优势在于，不需要频繁重复校准，从而确保了检测的连续性并降低了系统维护成本。

## 产品特性

- I2C 地址:**0x33**(GOIO 0/26)
- 工作电流: 23mA
- 视场角: 110°x75°
- 测温范围: -40°C ~ 300°C
- 精度: ±1.5°C
- 刷新频率: 0.5Hz-64Hz
- 工作温度: -40°C ~ 85°C

## 包装内容

- 1 x Hat Thermal
- 1 x 双面胶

## 应用场景

- 高精度的非接触性测温器
- 生物移动检测
- 可视化红外成像

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 通信接口 | I2C 通信 @ 0x33       |
| 产品尺寸 | 25.0 x 24.0 x 13.7mm  |
| 产品重量 | 5.7g                  |
| 包装尺寸 | 138.0 x 93.0 x 14.0mm |
| 毛重     | 8.0                   |

## 原理图

- [Hat Thermal 原理图PDF](https://github.com/m5stack/M5-Schematic/blob/master/Hat/StickHat_THERMAL.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/856/StickHat_THERMAL_page_01.png">
</SchViewer>

## 管脚映射

| StickC      | G0  | G26 | 3.3V | GND |
| ----------- | --- | --- | ---- | --- |
| HAT Thermal | SDA | SCL | 3.3V | GND |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/856/U062_model_size_page_01.png">

## 数据手册

- [MLX90640 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/MLX90640-Datasheet-Melexis_en.pdf)

## 软件开发

### Arduino

- [Hat Thermal StickC 测试程序](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/MLX90640)
- [Hat Thermal StickC-Plus 测试程序](https://github.com/m5stack/M5StickC-Plus/tree/master/examples/Hat/THERMAL_MLX90640)
- [Hat Thermal Arduino 上手教程](/zh_CN/arduino/projects/hat/hat_thermal)
- [Hat Thermal 驱动库](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/856/mlx90640-library.zip)

### UiFlow1

- [Hat Thermal UiFlow1 文档](/zh_CN/uiflow/blockly/hat/thermal)

### UiFlow2

- [Hat Thermal UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/thermal.html)

### EasyLoader

| Easyloader             | 下载链接                                                                                                          | 备注 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------- | ---- |
| Hat Thermal Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/THERMAL/EasyLoader_StickC_HAT_THERMAL.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/THERMAL-HAT.mp4" type="video/mp4">
</video>
