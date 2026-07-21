# Unit RGB LED Strip

<span class="product-sku">SKU:A093/A093-B/A093-C/A093-D</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/761/A093_Unit_RGB_LED_Strip_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb_led_strip/rgb_led_strip_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/761/A093-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb_led_strip/rgb_led_strip_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb_led_strip/rgb_led_strip_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb_led_strip/rgb_led_strip_05.webp">
</PictureViewer>

## 描述

**Unit RGB LED Strip** 是一款可编程灯条，采用灯珠 SK6812。该灯条支持数字寻址，这意味着你可以单独控制灯条上的每一个单独的 LED 灯显示的颜色、亮度。使用单总线编程，可进行灯条拓展。
采用灯条外层采用滴胶防水工艺加工，表层覆盖的透明防护硅胶支持 IP65 级别防水保护，能够适应多种适用环境。产品为柔性 FPC (软灯条板) / PCB (硬灯条板) 为基板焊接 LED，采用 5050 规格 RGB 灯珠，背面贴有 3M 强力双面胶，方便粘贴固定。工作电压为 5V 直流电压，通过控制器编程可实现各种灯光效果。

## 产品特性

- 产品类别：RGB LED Strip
- 灯珠型号：xdx-5050RGB-60-60
- IC 型号：SK6812
- 工作电压：5V
- 功率：5V@2A/m
- 板宽：10MM
- 显示灰度等级：256
- 灯珠数量：60 灯 / 米
- IC 数量：60 个 IC / 米 (IC 位于 FPC 板上) ，60 个像素点 / 米
- 工作温度：-40°C ~ 80°C
- 工作寿命：30Kh
- 板底颜色：白板 / 黑板
- 发光颜色：全彩 / 通过控制器控制能实现任意颜色 任意效果
- 数据传输速率：800K/S
- 防水等级：滴胶防水 - IP65
- 可选长度：0.5m / 30，1m / 60，2m / 120，5m / 300
- 开发平台：Arduino，UiFlow (Blockly，Python)
- 可拓展长度

## 包装内容

- 1 x Unit RGB LED Strip
  - SKU: A093 (1pcs, 30 LED / 0.5m )
  - SKU: A093-B (1pcs, 60 LED / 1m)
  - SKU: A093-C (1pcs, 120 LED / 2m)
  - SKU: A093-D (1pcs, 300 LED / 5m)
- 1 x HY2.0-4P Grove 转接线 (10cm)

## 应用场景

- 灯光装饰

## 规格参数

| 规格            | 参数                                      |
| --------------- | ----------------------------------------- |
| 长度 / 产品重量 | 0.5m / 37g，1m / 55g，2m / 86g，5m / 211g |
| 长度 / 毛重     | 0.5m / 45g，1m / 65g，2m / 86g，5m / 220g |
| 长度 / 灯珠个数 | 0.5m / 30，1m / 60，2m / 120，5m / 300    |
| 灯条宽度        | 10mm                                      |
| 包装类型        | 防静电袋包装，卷盘固定                    |

## 操作说明

\#> 功耗 | 随着灯条连接数量的逐渐增加，伴随的功耗也会增加，因此在使用 LED 个数较多的 RGB LED 灯条时，建议额外为其提供电源。

## 管脚映射

### Unit RGB LED Strip

| 灯条 PIN | VCC  | GND  | DATA |
| -------- | ---- | ---- | ---- |
| 导线颜色 | 红色 | 白色 | 绿色 |

## 软件开发

### Arduino

- [Unit RGB LED Strip 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/RGB_LED_SK6812/display_rainbow)
- [FastLED Arduino 驱动库](https://github.com/FastLED/FastLED)
