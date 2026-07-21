# Module Audio Arduino 使用教程

## 1. 准备工作

- 1\. 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 2\. 使用到的驱动库:

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Module-Audio](https://github.com/m5stack/M5Module-Audio)

- 3\. 使用到的硬件产品:
  - [Core2 For AWS](https://shop.m5stack.com/products/m5stack-core2-esp32-iot-development-kit-for-aws-iot-edukit)
  - [Module Audio](https://shop.m5stack.com/products/m5stack-audio-module-stm32g030)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_cover_01.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_04.webp" width="20%">

## 2. 初始化配置

Module Audio 集成了 STM32 主控用于实现耳机接口标准切换，灯光控制，耳机插入检测（仅通道 2 可用），麦克风输入模式配置等功能。

\#> 接口标准选择 | 由于不同的耳机接口标准的所使用的线序不同，使用需根据实际情况使用`device.setHPMode(AUDIO_HPMODE_NATIONAL);`函数切换耳机接口标准以实现兼容。`OMTP`（AUDIO_HPMODE_NATIONAL），`CTIA`（AUDIO_HPMODE_AMERICAN）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_Earphone_instruction.jpg" width="70%">

```cpp line-num
#include "M5Unified.h"
#include "audio_i2c.hpp"
#include "es8388.hpp"
#include "driver/i2s.h"

#define SYS_I2C_SDA_PIN  21
#define SYS_I2C_SCL_PIN  22
#define SYS_I2S_MCLK_PIN 0
#define SYS_I2S_SCLK_PIN 19
#define SYS_I2S_LRCK_PIN 27
#define SYS_I2S_DOUT_PIN 2
#define SYS_I2S_DIN_PIN  34
#define SYS_SPI_MISO_PIN 38
#define SYS_SPI_MOSI_PIN 23
#define SYS_SPI_CLK_PIN  18
#define SYS_SPI_CS_PIN   4

AudioI2c device;

ES8388 es8388(&Wire, SYS_I2C_SDA_PIN, SYS_I2C_SCL_PIN);

void setup()
{
    M5.begin();
    Serial.begin(115200);
    device.begin(&Wire, SYS_I2C_SCL_PIN, SYS_I2C_SCL_PIN);
    device.setHPMode(AUDIO_HPMODE_NATIONAL);
    //  device.setHPMode(AUDIO_HPMODE_AMERICAN);
    device.setMICStatus(AUDIO_MIC_OPEN);
    device.setRGBBrightness(100);
    for (int i = 0; i <= 2; i++) {
        device.setRGBLED(i, 0x0000ff);
    }
}

void loop()
{
    bool isHPInsert = device.getHPInsertStatus();
    if (isHPInsert) {
        Serial.println("Headphone Inserted");
    } else {
        Serial.println("Headphone Removed");
    }
    delay(500);
}
```

## 3. 输入接口配置

\#> 接口使用说明 | Module Audio 配有两组 3.5mm 音频接口（通道 1 和通道 2），其中通道 1 适用于 3.5mm TRS 音频信号接口的麦克风输入。通道 2 适用于 3.5mm TRRS 复合音频接口设备连接，同时也兼容 TRS 音频信号接口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/module_audio_interface_01.png" width="70%">

- TRS 音频信号接口接线方式：通道 1 接入 MIC 输入，通道 2 接入音频输出。适用于麦克风与音频输出分离的设备，如电脑头戴耳机等。
- TRRS 复合音频接口接线方式：通道 2 可接入复合音频输入输出，适用于带有麦克风的有线耳机，同时兼容 TRS 音频接口设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/module_audio_interface_02.png" width="70%">

在完成初始化后，通过调用以下 API 配置输入输出接口通道选择与音量增益等参数。

```cpp line-num
// Use input 1 for both channels
es8388.setADCInput(ADC_INPUT_LINPUT1_RINPUT1);

// Use input 2 for both channels
// es8388.setADCInput(ADC_INPUT_LINPUT2_RINPUT2);

es8388.setDACOutput(DAC_OUTPUT_OUT1);
es8388.setADCVolume(100);
es8388.setDACVolume(40);
es8388.setMicGain(MIC_GAIN_24DB);
es8388.setBitsSample(ES_MODULE_ADC, BIT_LENGTH_16BITS);
es8388.setSampleRate(SAMPLE_RATE_44K);
```

## 4. 录音和播放

使用 TRS 音频信号接口接线方式，配置通道 1 接入 MIC 输入，通道 2 音频输出，实现实时读取 MIC 输入数据和播放。

```cpp line-num
#include "M5Unified.h"
#include "audio_i2c.hpp"
#include "es8388.hpp"
#include "driver/i2s.h"
AudioI2c device;

#define SYS_I2C_SDA_PIN  21
#define SYS_I2C_SCL_PIN  22
#define SYS_I2S_MCLK_PIN 0
#define SYS_I2S_SCLK_PIN 19
#define SYS_I2S_LRCK_PIN 27
#define SYS_I2S_DOUT_PIN 2
#define SYS_I2S_DIN_PIN  34
#define SYS_SPI_MISO_PIN 38
#define SYS_SPI_MOSI_PIN 23
#define SYS_SPI_CLK_PIN  18
#define SYS_SPI_CS_PIN   4

ES8388 es8388(&Wire, SYS_I2C_SDA_PIN, SYS_I2C_SCL_PIN);

uint16_t rxbuf[256], txbuf[256];
size_t readsize = 0;
byte error, address;
const uint32_t color[]  = {0xFF0000, 0xFF0000, 0xFF0000, 0x00FF00, 0xFFFF00, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF};
i2s_config_t i2s_config = {.mode                 = (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_TX | I2S_MODE_RX),
                           .sample_rate          = 44100,
                           .bits_per_sample      = I2S_BITS_PER_SAMPLE_16BIT,
                           .channel_format       = I2S_CHANNEL_FMT_RIGHT_LEFT,
                           .communication_format = I2S_COMM_FORMAT_STAND_I2S,
                           .intr_alloc_flags     = 0,
                           .dma_buf_count        = 8,
                           .dma_buf_len          = 512,
                           .use_apll             = false,
                           .tx_desc_auto_clear   = true,
                           .fixed_mclk           = 0};

i2s_pin_config_t pin_config = {
    .mck_io_num   = SYS_I2S_MCLK_PIN,
    .bck_io_num   = SYS_I2S_SCLK_PIN,
    .ws_io_num    = SYS_I2S_LRCK_PIN,
    .data_out_num = SYS_I2S_DOUT_PIN,
    .data_in_num  = SYS_I2S_DIN_PIN,
};

void setup()
{
    M5.begin();
    Serial.begin(115200);
    device.begin(&Wire, SYS_I2C_SCL_PIN, SYS_I2C_SCL_PIN);
    device.setHPMode(AUDIO_HPMODE_NATIONAL);
    device.setMICStatus(AUDIO_MIC_OPEN);
    device.setRGBBrightness(100);
    Serial.printf("getHPMode:%d\n", device.getHPMode());
    Serial.printf("getMICStatus:%d\n", device.getMICStatus());
    for (int i = 0; i <= 2; i++) {
        device.setRGBLED(i, color[i + 3]);
        // Output the hexadecimal value of the current color
        Serial.printf("Set RGB to %06X\n", (unsigned int)color[i + 3]);
        Serial.printf("get RGB to %06X\n", device.getRGBLED(i));
    }
    Serial.println("Read Reg ES8388 : ");
    if (!es8388.init()) Serial.println("Init Fail");
    es8388.setADCInput(ADC_INPUT_LINPUT1_RINPUT1);
    es8388.setMicGain(MIC_GAIN_24DB);
    es8388.setADCVolume(100);
    // The volume output should not exceed 40, otherwise there will be noise or current sounds
    es8388.setDACVolume(40);
    es8388.setDACOutput(DAC_OUTPUT_OUT1);
    es8388.setBitsSample(ES_MODULE_ADC, BIT_LENGTH_16BITS);
    es8388.setSampleRate(SAMPLE_RATE_44K);
    uint8_t *reg;
    for (uint8_t i = 0; i < 53; i++) {
        reg = es8388.readAllReg();
        Serial.printf("Reg-%02d = 0x%02x\r\n", i, reg[i]);
    }
    // i2s
    i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
    i2s_set_pin(I2S_NUM_0, &pin_config);
}

void loop()
{
    i2s_read(I2S_NUM_0, &rxbuf[0], 256 * 2, &readsize, 1000);
    for (int i = 0; i < 256; i++) {
        // direct transfer too txbuff
        txbuf[i] = rxbuf[i];
        // txbuf[i] = 0; //mute
    }
    // play received buffer
    i2s_write(I2S_NUM_0, &txbuf[0], 256 * 2, &readsize, 1000);
}
```

## 5. 播放 microSD WAV

配置通道 2 音频输出，加载 microSD 卡中存储的 WAV 文件，并进行播放。使用前需添加 wav 文件至 microSD 卡，并插入至主控设备卡槽中。

```cpp line-num
#include "M5Unified.h"
#include "audio_i2c.hpp"
#include "es8388.hpp"
#include "driver/i2s.h"
#include <SPI.h>
#include <SD.h>
AudioI2c device;

#define SYS_I2C_SDA_PIN  21
#define SYS_I2C_SCL_PIN  22
#define SYS_I2S_MCLK_PIN 0
#define SYS_I2S_SCLK_PIN 19
#define SYS_I2S_LRCK_PIN 27
#define SYS_I2S_DOUT_PIN 2
#define SYS_I2S_DIN_PIN  34
#define SYS_SPI_MISO_PIN 38
#define SYS_SPI_MOSI_PIN 23
#define SYS_SPI_CLK_PIN  18
#define SYS_SPI_CS_PIN   4

ES8388 es8388(&Wire, SYS_I2C_SDA_PIN, SYS_I2C_SCL_PIN);
void i2s_write_task(void *arg);
uint16_t rxbuf[256], txbuf[256];
size_t readsize = 0;
byte error, address;
const uint32_t color[]  = {0xFF0000, 0xFF0000, 0xFF0000, 0x00FF00, 0xFFFF00, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF};
i2s_config_t i2s_config = {.mode                 = (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_TX | I2S_MODE_RX),
                           .sample_rate          = 44100,
                           .bits_per_sample      = I2S_BITS_PER_SAMPLE_16BIT,
                           .channel_format       = I2S_CHANNEL_FMT_RIGHT_LEFT,
                           .communication_format = I2S_COMM_FORMAT_STAND_I2S,
                           .intr_alloc_flags     = 0,
                           .dma_buf_count        = 8,
                           .dma_buf_len          = 512,
                           .use_apll             = false,
                           .tx_desc_auto_clear   = true,
                           .fixed_mclk           = 0};

i2s_pin_config_t pin_config = {
    .mck_io_num   = SYS_I2S_MCLK_PIN,
    .bck_io_num   = SYS_I2S_SCLK_PIN,
    .ws_io_num    = SYS_I2S_LRCK_PIN,
    .data_out_num = SYS_I2S_DOUT_PIN,
    .data_in_num  = SYS_I2S_DIN_PIN,
};

void setup()
{
    M5.begin();
    Serial.begin(115200);
    device.begin(&Wire, SYS_I2C_SCL_PIN, SYS_I2C_SCL_PIN);
    device.setHPMode(AUDIO_HPMODE_NATIONAL);
    device.setMICStatus(AUDIO_MIC_OPEN);
    device.setRGBBrightness(100);
    Serial.printf("getHPMode:%d\n", device.getHPMode());
    Serial.printf("getMICStatus:%d\n", device.getMICStatus());
    for (int i = 0; i <= 2; i++) {
        device.setRGBLED(i, color[i + 3]);
        // Output the hexadecimal value of the current color
        Serial.printf("Set RGB to %06X\n", (unsigned int)color[i + 3]);
        Serial.printf("get RGB to %06X\n", device.getRGBLED(i));
    }
    Serial.println("Read Reg ES8388 : ");
    if (!es8388.init()) Serial.println("Init Fail");
    es8388.setADCVolume(100);
    es8388.setDACVolume(80);
    es8388.setDACOutput(DAC_OUTPUT_OUT1);
    es8388.setBitsSample(ES_MODULE_ADC, BIT_LENGTH_16BITS);
    es8388.setSampleRate(SAMPLE_RATE_44K);
    uint8_t *reg;
    for (uint8_t i = 0; i < 53; i++) {
        reg = es8388.readAllReg();
        Serial.printf("Reg-%02d = 0x%02x\r\n", i, reg[i]);
    }
    // i2s
    i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
    i2s_set_pin(I2S_NUM_0, &pin_config);
    if (SD.begin(SYS_SPI_CS_PIN)) {
        Serial.println("SD card initialized successfully");

    } else {
        Serial.println("Failed to initialize SD card. Retrying...");
    }
    xTaskCreate(i2s_write_task, "i2s_write_task", 1024 * 8, NULL, 6, NULL);
}

void loop()
{
}

void i2s_write_task(void *arg)
{
    // Open the WAV file
    // Replace with the path of your WAV file
    File file = SD.open("/hello.wav", "r");
    if (!file) {
        Serial.println("Failed to open WAV file for reading");
        vTaskDelete(NULL);
    }

    // Obtain the file size and print
    size_t fileSize = file.size();
    Serial.printf("File size: %d bytes\n", fileSize);

    // Skip the WAV file header (44 bytes)
    file.seek(44);

    uint8_t txbuf[1024];

    while (1) {
        // Check whether the end of the file has been reached
        if (file.available() == 0) {
            // Go back to the beginning of the file in order to replay it
            file.seek(44);
        }

        // Read data
        size_t bytesRead = file.read(txbuf, sizeof(txbuf));

        // If data is read
        if (bytesRead > 0) {
            size_t bytesWritten = 0;
            esp_err_t result    = i2s_write(I2S_NUM_0, txbuf, bytesRead, &bytesWritten, portMAX_DELAY);
            // Check the writing result
            if (result != ESP_OK) {
                Serial.printf("I2S write error: %d\n", result);
            }
        } else {
            // If there is no more data, exit the loop
            break;
        }
    }

    // Close the file
    file.close();
    vTaskDelete(NULL);
}
```

## 6.RGB LED 控制

Module Audio 侧边集成了 3 颗可编程 RGB LED，可参考以下案例进行控制。

```cpp line-num
#include "M5Unified.h"
#include "audio_i2c.hpp"
#include "es8388.hpp"
#include "driver/i2s.h"

#define SYS_I2C_SDA_PIN 21
#define SYS_I2C_SCL_PIN 22

AudioI2c device;

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("Module Audio Init...");
    while (!device.begin(&Wire, SYS_I2C_SDA_PIN, SYS_I2C_SCL_PIN)) {
        delay(1000);
    };
    Serial.println("Module Audio Init OK!");
    device.setRGBBrightness(100);
}

void loop()
{
    for (int i = 0; i <= 2; i++) {
        device.setRGBLED(i, 0xff0000);
    }
    delay(1000);
    for (int i = 0; i <= 2; i++) {
        device.setRGBLED(i, 0x00ff00);
    }
    delay(1000);
    for (int i = 0; i <= 2; i++) {
        device.setRGBLED(i, 0x0000ff);
    }
    delay(1000);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/module_audio_rgb_led_example_01.jpg" width="70%">
