# Unit Grove to Grove

<span class="product-sku">SKU:U148</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/790/U148-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_09.webp">
</PictureViewer>

## 描述

**Unit Grove to Grove** 是一款提供 **通断控制** + **电流测量** 的 **一进一出** GROVE 扩展控制单元。通断控制采用开关量信号，电流测量为 0 ~ 1000mA 模拟信号。

## 产品特性

- 通断控制: 5V/1A
- 电流测量: 0~1000mA

## 包装内容

- 1 x Unit Grove to Grove
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 规格参数

| 规格         | 参数                 |
| ------------ | -------------------- |
| 工作电压     | 5V                   |
| 通断电流     | 1000mA               |
| 通断回路电压 | 5V                   |
| 电流测量阈值 | 0~1000mA             |
| 产品尺寸     | 32.0 x 24.0 x 8.1mm  |
| 产品重量     | 4.9g                 |
| 包装尺寸     | 138.0 x 93.0 x 9.1mm |
| 毛重         | 10.0g                |

## 原理图

- [Unit Grove to Grove 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/602/Sch_Unit_Grove2Grove_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/602/Sch_Unit_Grove2Grove_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Grove to Grove

::grove-table
| HY2.0-4P | Black | Red | Yellow | White         |
| -------- | ----- | --- | ------ | ------------- |
| PORT.B   | GND   | 5V  | PWR_EN | Analog Output |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/unit_grove2grove/model%20size.jpg" width="100%" />

## 软件开发

### Arduino

```cpp
#include <Arduino.h>
#include "driver/adc.h"
#include "esp_adc_cal.h"
#include "math.h"
#include <M5GFX.h>

#define Din_Pin  26
#define Aout_Pin 36
#define groveOn HIGH
#define groveOff LOW

esp_adc_cal_characteristics_t *adc_chars;
float groveVref;

M5GFX display;
M5Canvas canvas(&display);

int get_battery_voltage(void) {
    uint32_t adc_reading = 0;
    // Multisampling
    for (int i = 0; i < 64; i++) {
        adc_reading += adc1_get_raw((adc1_channel_t)ADC1_CHANNEL_0);
    }
    adc_reading /= 64;
    // Convert adc_reading to voltage in mV
    uint32_t voltage =
        (uint32_t)(esp_adc_cal_raw_to_voltage(adc_reading, adc_chars));
    // Serial.printf("Raw: %dtVoltage: %dmVrn", adc_reading, voltage);
    return voltage;
}

void getVerf() {
    float sampleVari = 1.0f;
    while (sampleVari > 0.20f) {
        sampleVari = 1.0f;
        float sampleVol[100] = {};
        float sampleVolAll = 0;
        groveVref = 0;
        for (int i = 0; i < 100; i++) {
        sampleVol[i] = get_battery_voltage();
        groveVref = groveVref + get_battery_voltage();
        // Serial.println(sampleVol[i]);
        }
        // Serial.println(groveVref);
        for (int i = 0; i < 100; i++) {
            // Serial.println(sampleVol[i]);
            float avrAll = sampleVol[i] - (groveVref / 100.0f);
            // Serial.println(avrAll);
            sampleVolAll += avrAll * avrAll;
        }
        // Serial.println(sampleVolAll);
        sampleVari = sampleVolAll / 99.0f;
        Serial.println(sampleVari);
        Serial.println(groveVref);
    }
    // return groveVref;
}

void setup() {
    Serial.begin(115200);
    pinMode(Din_Pin, OUTPUT);
    digitalWrite(Din_Pin, groveOn);

    display.begin();
    if (display.width() < display.height())
    {
        display.setRotation(display.getRotation() ^ 1);
    }

    // ADC初始化
    gpio_pad_select_gpio(Aout_Pin);
    gpio_set_direction((gpio_num_t)Aout_Pin, GPIO_MODE_INPUT);
    adc1_config_width(ADC_WIDTH_BIT_12);
    adc1_config_channel_atten(ADC1_CHANNEL_0, ADC_ATTEN_DB_11);
    adc_chars = (esp_adc_cal_characteristics_t *)calloc(
        1, sizeof(esp_adc_cal_characteristics_t));
    esp_adc_cal_characterize(ADC_UNIT_1, ADC_ATTEN_DB_11, ADC_WIDTH_BIT_12,
                            3300, adc_chars);
    // groveVref = get_battery_voltage();
    // for (size_t i = 0; i < 5; i++) {
    //     groveVref = groveVref + get_battery_voltage();
    //     Serial.println(groveVref);
    // }
    // groveVref = groveVref / 5.0f / 1000.0f;
    getVerf();
    // Serial.println(groveVref);
    groveVref = groveVref / 100.0f / 1000.0f;
    // Serial.println(groveVref);

    canvas.setColorDepth(1); // mono color
    canvas.createSprite(display.width(), display.height());
    canvas.setTextSize((float)canvas.width() / 160);
    canvas.setTextScroll(true);
}

void loop() {
    // Serial.printf("Raw is %dn", analogRead(Aout_Pin));
    float groveVol = get_battery_voltage() / 1000.0f;
    // Serial.println(groveVol);
    Serial.printf("Voltage is: %fVrn", groveVol);
    canvas.printf("Voltage is: %fVrn", groveVol);
    // float groveCurrent = ((groveVol - groveVref) / 50.0f / 0.01f);
    // float groveCurrent = ((groveVol - groveVref) / 83.0f / 0.01f);
    float groveCurrent = ((groveVol - groveVref) / 50.0f / 0.02f);
    Serial.printf("Current is: %fArn", groveCurrent);
    canvas.printf("Current is: %fArn", groveCurrent);
    //digitalWrite(Din_Pin, groveOff);
    canvas.pushSprite(0, 0);
    delay(1000);
}
```

### UiFlow1

- [Unit Grove to Grove UiFlow1 文档](/zh_CN/uiflow/blockly/unit/grove2grove)

### UiFlow2

- [Unit Grove to Grove UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/grove2grove.html)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113208341825501&bvid=BV1PrsZetEdw&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/PEqz4iEvb-U?si=-j3G5x0Wf2ajREK1" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
