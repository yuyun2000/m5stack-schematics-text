# Unit Grove to Grove Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Grove to Grove](https://shop.m5stack.com/products/grove2grove-expansion-unit)


<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_grove2grove/unit_grove2grove_cover_01.webp" width="20%">

## 2.案例程序

#>案例说明|Unit Grove to Grove能够测量从Grove接口通过的电流值, 并支持控制接口电源线路的通断。该Unit提供两个IO接口分别用于电流模拟信号读取和电源通断数字信号控制。


### 电流值计算

```cpp line-num
uint32_t adc_raw    = adc1_get_raw((adc1_channel_t)ADC1_CHANNEL_7);
uint32_t voltage_mv = (uint32_t)(esp_adc_cal_raw_to_voltage(adc_raw, adc_chars));
float voltage       = (voltage_mv - offset) / 1000.0f;
float grove_current = (voltage / 50.0f / 0.02f);
```

### 供电开关

```cpp line-num
pinMode(POWER_CTL_PIN, OUTPUT);
// Power on!
digitalWrite(POWER_CTL_PIN, HIGH);
// Power off!
digitalWrite(POWER_CTL_PIN, LOW);
```


### 完整程序

基于M5Unified和M5GFX添加基本的显示, 和开关控制，实现电流值读取，和触摸控制电源通断。

?>ADC Channel注意事项:| 该案例中我们使用到了ESP32-S3的ADC输入引脚为GPIO8, 因此在初始化时候需要配置为`ADC1_CHANNEL_7`, 当你使用不同的主控设备时, 你需要参考其对应的ESP32芯片手册, 查看ADC章节了解具体使用的GPIO与通道。并对案例程序进行修改。


```cpp line-num
#include <M5Unified.h>
#include "driver/adc.h"
#include "esp_adc_cal.h"
#include "math.h"

#define POWER_CTL_PIN 9
#define ANALOG_PIN    8
esp_adc_cal_characteristics_t *adc_chars;
bool power_status = false;
float offset      = 0.0f;

void adc_init()
{
    gpio_pad_select_gpio(ANALOG_PIN);
    gpio_set_direction((gpio_num_t)ANALOG_PIN, GPIO_MODE_INPUT);
    adc1_config_width(ADC_WIDTH_BIT_12);
    adc1_config_channel_atten(ADC1_CHANNEL_7, ADC_ATTEN_DB_11);
    adc_chars = (esp_adc_cal_characteristics_t *)calloc(1, sizeof(esp_adc_cal_characteristics_t));
    esp_adc_cal_characterize(ADC_UNIT_1, ADC_ATTEN_DB_11, ADC_WIDTH_BIT_12, 3300, adc_chars);
}

void cal_adc_offset()
{
    float sum = 0;
    for (int i = 0; i < 100; i++) {
        uint32_t adc_raw    = adc1_get_raw((adc1_channel_t)ADC1_CHANNEL_7);
        uint32_t voltage_mv = (uint32_t)(esp_adc_cal_raw_to_voltage(adc_raw, adc_chars));
        sum += voltage_mv;
    }
    offset = sum / 100.0f;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    pinMode(POWER_CTL_PIN, OUTPUT);
    // Power on!
    digitalWrite(POWER_CTL_PIN, power_status);
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    M5.Display.println(power_status ? "Grove Power On" : "Grove Power Off");

    adc_init();
    cal_adc_offset();
}

time_t last_update_time = 0;

void loop()
{
    M5.update();
    auto t = M5.Touch.getDetail();
    if (t.wasClicked() || M5.BtnA.wasClicked()) {
        Serial.println("click!");
        power_status = !power_status;
        digitalWrite(POWER_CTL_PIN, power_status);
        M5.Display.fillRect(0, 0, 320, 50, BLACK);
        M5.Display.setCursor(0, 0);
        M5.Display.println(power_status ? "Grove Power On" : "Grove Power Off");
        if (!power_status) {
            cal_adc_offset();
        }
    }

    if (millis() - last_update_time > 1000) {
        last_update_time = millis();
        M5.Display.fillRect(0, 50, 320, 100, BLACK);
        M5.Display.setCursor(0, 50);
        uint32_t adc_raw    = adc1_get_raw((adc1_channel_t)ADC1_CHANNEL_7);
        uint32_t voltage_mv = (uint32_t)(esp_adc_cal_raw_to_voltage(adc_raw, adc_chars));
        float voltage       = (voltage_mv - offset) / 1000.0f;
        float grove_current = (voltage / 50.0f / 0.02f);
        M5.Display.printf("Grove Current:%.3fA\r\n", grove_current);
        Serial.printf("Grove Current:%.3fA\r\n", grove_current);
    }
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">


- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_grove_to_grove/unit_grove_to_grove_01.jpg" width="70%">


## 4.电流监控&供电控制

通过触屏可控制Unit Grove to Grove的供电线路开关, 并实时显示当前电流值状态。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_grove_to_grove/unit_grove_to_grove_02.jpg" width="70%">




