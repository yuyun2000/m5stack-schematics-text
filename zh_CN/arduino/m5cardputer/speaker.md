# Cardputer Speaker 扬声器

Cardputer Speaker 扬声器相关 API 与案例程序，适用于 Cardputer 和 Cardputer-Adv。

#> 关于 3.5mm AUX 插孔 | Cardputer-Adv 的 3.5mm AUX 插孔同样适用本页面，只要连接到耳机或音箱等播放设备，音频输出就会从扬声器切换到 AUX 通道。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Cardputer
- M5Cardputer 库版本 >= 1.1.0
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.10

### 蜂鸣示例

```cpp line-num
#include "M5Cardputer.h"

void setup() {
  auto cfg = M5.config();
  M5Cardputer.begin(cfg);
}

void loop() {
  M5Cardputer.Speaker.tone(7000, 100);  // frequency, duration
  delay(1000);
  M5Cardputer.Speaker.tone(4000, 20);  // frequency, duration
  delay(1000);
}
```

### 播放 wav 文件示例

打开`M5Unified`驱动库中的示例程序`Advanced -> Speaker_SD_wav_file`。如下图箭头所指，将`SDCARD_CSPIN`的值改为`GPIO_NUM_12`，将`files[]`中的文件名改为你要播放的 wav 文件路径（开头的`/`表示 microSD 卡的根目录）。点击上传按钮，将程序编译并烧录至设备。将 microSD 卡插入设备（卡的触点朝向与设备屏幕朝向相反），启动设备即可按顺序播放程序中指定的 wav 文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_speaker_wav01.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_speaker_wav02.png" width="70%">

## API

`M5Cardputer`库基于`M5Unified`库实现，Speaker 扬声器部分驱动使用了`M5Unified`库中的`Speaker_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)