# Chain Mono 使用教程

## 1.准备工作

- 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide) 完成 IDE 安装，并根据实际使用的开发板安装对应的板管理与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5Chain](https://github.com/m5stack/M5Chain)

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Chain Mono](https://shop.m5stack.com/products/chain-mono-matrix-with-8x8-leds-white)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_02.webp" width="20%">

## 2.示例程序

#> 编译要求 | M5Stack 板管理版本 >= 3.2.4<br>M5Chain 库版本 >= 1.0.4

### 像素模式

#### 单像素控制及批量写入

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

chain_status_t chain_status = CHAIN_OK;
uint8_t mono_id          = 0;
uint8_t operation_status = 0;

bool findFirstMonoDevice()
{
    // Enumerate devices and use the first Mono node
    uint16_t device_nums = 0;
    if (M5Chain.getDeviceNum(&device_nums) != CHAIN_OK || device_nums == 0) {
        Serial.println("No Chain devices found");
        return false;
    }

    device_info_t *infos = (device_info_t *)malloc(sizeof(device_info_t) * device_nums);
    if (infos == nullptr) {
        return false;
    }

    device_list_t devices;
    devices.count   = device_nums;
    devices.devices = infos;

    bool found = false;
    if (M5Chain.getDeviceList(&devices)) {
        for (uint8_t i = 0; i < devices.count; i++) {
            if (devices.devices[i].device_type == CHAIN_MONO_TYPE_CODE) {
                mono_id = devices.devices[i].id;
                found   = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("Mono device found, id=%d\r\n", mono_id);
    } else {
        Serial.println("No Mono device found");
    }
    return found;
}

bool prepareMono()
{
    // Initialize display mode, rotation, and brightness
    if (!findFirstMonoDevice()) {
        return false;
    }

    if (M5Chain.setMonoMode(mono_id, MONO_PIXEL_MODE, &operation_status) != CHAIN_OK || operation_status != 1) {
        return false;
    }

    M5Chain.setMonoRotation(mono_id, MONO_ROTATION_0, &operation_status);
    M5Chain.setMonoBrightness(mono_id, MONO_BRIGHTNESS_LEVEL_7, &operation_status);
    M5Chain.setMonoClear(mono_id, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("Pixel demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareMono()) {
        Serial.println("Chain Mono init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain Mono init success");
    }
}

void loop()
{
    static bool single_phase = true;
    static uint8_t single_x  = 0;
    static uint8_t single_y  = 0;
    static uint8_t block_x   = 0;
    static uint8_t block_y   = 4;

    if (single_phase) {
        // Walk through the first 4 rows with a single pixel
        M5Chain.setMonoClear(mono_id, &operation_status);
        chain_status = M5Chain.setMonoPixel(mono_id, single_x, single_y, true, &operation_status);
        if (chain_status == CHAIN_OK && operation_status == 1) {
            Serial.printf("Single pixel on: x=%d, y=%d\r\n", single_x, single_y);
        }

        delay(200);

        single_x++;
        if (single_x >= 8) {
            single_x = 0;
            single_y++;
        }

        if (single_y >= 4) {
            single_phase = false;
            block_x      = 0;
            block_y      = 4;
        }
    } else {
        // Walk through the last 4 rows with a 2x2 block
        MonoPixelInfo pixels[] = {
            {block_x, block_y, true},
            {(uint8_t)(block_x + 1), block_y, true},
            {block_x, (uint8_t)(block_y + 1), true},
            {(uint8_t)(block_x + 1), (uint8_t)(block_y + 1), true}};

        M5Chain.setMonoClear(mono_id, &operation_status);
        chain_status = M5Chain.setMonoPixel(mono_id, pixels, sizeof(pixels) / sizeof(pixels[0]), &operation_status);
        if (chain_status == CHAIN_OK && operation_status == 1) {
            Serial.printf("Block on: (%d,%d) (%d,%d) (%d,%d) (%d,%d)\r\n", pixels[0].x, pixels[0].y, pixels[1].x,
                          pixels[1].y, pixels[2].x, pixels[2].y, pixels[3].x, pixels[3].y);
        }

        delay(200);

        block_x++;
        if (block_x >= 7) {
            block_x = 0;
            block_y += 2;
        }

        if (block_y >= 8) {
            single_phase = true;
            single_x     = 0;
            single_y     = 0;
        }
    }
}
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/Chain_Mono_Arduino_pixel.gif" width="40%">

#### 字符显示

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

uint8_t mono_id          = 0;
uint8_t operation_status = 0;
const char text[]        = "I'mChainMono";

bool findFirstMonoDevice()
{
    // Enumerate devices and use the first Mono node
    uint16_t device_nums = 0;
    if (M5Chain.getDeviceNum(&device_nums) != CHAIN_OK || device_nums == 0) {
        Serial.println("No Chain devices found");
        return false;
    }

    device_info_t *infos = (device_info_t *)malloc(sizeof(device_info_t) * device_nums);
    if (infos == nullptr) {
        return false;
    }

    device_list_t devices;
    devices.count   = device_nums;
    devices.devices = infos;

    bool found = false;
    if (M5Chain.getDeviceList(&devices)) {
        for (uint8_t i = 0; i < devices.count; i++) {
            if (devices.devices[i].device_type == CHAIN_MONO_TYPE_CODE) {
                mono_id = devices.devices[i].id;
                found   = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("Mono device found, id=%d\r\n", mono_id);
    } else {
        Serial.println("No Mono device found");
    }
    return found;
}

bool prepareMono()
{
    // Initialize display mode, rotation, and brightness
    if (!findFirstMonoDevice()) {
        return false;
    }

    if (M5Chain.setMonoMode(mono_id, MONO_PIXEL_MODE, &operation_status) != CHAIN_OK || operation_status != 1) {
        return false;
    }

    M5Chain.setMonoRotation(mono_id, MONO_ROTATION_0, &operation_status);
    M5Chain.setMonoBrightness(mono_id, MONO_BRIGHTNESS_LEVEL_7, &operation_status);
    M5Chain.setMonoClear(mono_id, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("Character display demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareMono()) {
        Serial.println("Chain Mono init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain Mono init success");
    }
}

void loop()
{
    static uint8_t index = 0;

    // Show characters one by one from the array
    M5Chain.setMonoClear(mono_id, &operation_status);
    M5Chain.setMonoPrintChar(mono_id, text[index], 1, 1, &operation_status);
    Serial.printf("Character shown: %c\r\n", text[index]);

    delay(400);

    index++;
    if (index >= sizeof(text) - 1) {
        index = 0;
    }
}
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/Chain_Mono_Arduino_char.gif" width="40%">

#### 自定义图案显示与旋转

#> 说明 | 此处旋转指的是在绘制前对显示方向进行设置，设置后再进行的绘制操作都会以该方向为基准进行显示，并非直接对已绘制显示内容进行旋转变换。

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

uint8_t mono_id          = 0;
uint8_t operation_status = 0;

// 8x8 arrow pattern
uint8_t arrow[8] = {
    0b00011000,  //    ■■   
    0b00111100,  //   ■■■■  
    0b01111110,  //  ■■■■■■ 
    0b11111111,  // ■■■■■■■■
    0b00111100,  //   ■■■■  
    0b00111100,  //   ■■■■  
    0b00111100,  //   ■■■■  
    0b00111100   //   ■■■■  
};

bool findFirstMonoDevice()
{
    // Enumerate devices and use the first Mono node
    uint16_t device_nums = 0;
    if (M5Chain.getDeviceNum(&device_nums) != CHAIN_OK || device_nums == 0) {
        Serial.println("No Chain devices found");
        return false;
    }

    device_info_t *infos = (device_info_t *)malloc(sizeof(device_info_t) * device_nums);
    if (infos == nullptr) {
        return false;
    }

    device_list_t devices;
    devices.count   = device_nums;
    devices.devices = infos;

    bool found = false;
    if (M5Chain.getDeviceList(&devices)) {
        for (uint8_t i = 0; i < devices.count; i++) {
            if (devices.devices[i].device_type == CHAIN_MONO_TYPE_CODE) {
                mono_id = devices.devices[i].id;
                found   = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("Mono device found, id=%d\r\n", mono_id);
    } else {
        Serial.println("No Mono device found");
    }
    return found;
}

bool prepareMono()
{
    // Initialize pixel mode and brightness
    if (!findFirstMonoDevice()) {
        return false;
    }

    if (M5Chain.setMonoMode(mono_id, MONO_PIXEL_MODE, &operation_status) != CHAIN_OK || operation_status != 1) {
        return false;
    }

    M5Chain.setMonoBrightness(mono_id, MONO_BRIGHTNESS_LEVEL_7, &operation_status);
    M5Chain.setMonoClear(mono_id, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("Custom pattern rotation demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareMono()) {
        Serial.println("Chain Mono init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain Mono init success");
    }
}

void loop()
{
    // Rotate through 0/90/180/270 degree display states
    for (uint8_t rotation = MONO_ROTATION_0; rotation <= MONO_ROTATION_270; rotation++) {
        M5Chain.setMonoRotation(mono_id, (mono_rotation_t)rotation, &operation_status);
        M5Chain.setMonoBufferRefresh(mono_id, arrow, &operation_status);
        Serial.printf("Rotation set to: %d°\r\n", rotation*90);
        delay(800);
    }
}
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/Chain_Mono_Arduino_custom.gif" width="40%">

### 字符串滚动模式

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

chain_status_t chain_status = CHAIN_OK;
uint8_t mono_id          = 0;
uint8_t operation_status = 0;
const char text[]        = "Hi I'm Chain Mono! ";

bool findFirstMonoDevice()
{
    // Enumerate devices and use the first Mono node
    uint16_t device_nums = 0;
    if (M5Chain.getDeviceNum(&device_nums) != CHAIN_OK || device_nums == 0) {
        Serial.println("No Chain devices found");
        return false;
    }

    device_info_t *infos = (device_info_t *)malloc(sizeof(device_info_t) * device_nums);
    if (infos == nullptr) {
        return false;
    }

    device_list_t devices;
    devices.count   = device_nums;
    devices.devices = infos;

    bool found = false;
    if (M5Chain.getDeviceList(&devices)) {
        for (uint8_t i = 0; i < devices.count; i++) {
            if (devices.devices[i].device_type == CHAIN_MONO_TYPE_CODE) {
                mono_id = devices.devices[i].id;
                found   = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("Mono device found, id=%d\r\n", mono_id);
    } else {
        Serial.println("No Mono device found");
    }
    return found;
}

bool prepareMono()
{
    // Switch to string scroll mode and set basic parameters
    if (!findFirstMonoDevice()) {
        return false;
    }

    if (M5Chain.setMonoMode(mono_id, MONO_STRING_SCROLL_MODE, &operation_status) != CHAIN_OK ||
        operation_status != 1) {
        return false;
    }

    M5Chain.setMonoRotation(mono_id, MONO_ROTATION_0, &operation_status);
    M5Chain.setMonoBrightness(mono_id, MONO_BRIGHTNESS_LEVEL_7, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("Mono string scroll demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareMono()) {
        Serial.println("Chain Mono init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain Mono init success");
    }

    chain_status = M5Chain.setMonoStringScroll(mono_id, text, MONO_SCROLL_LEFT, MONO_SCROLL_MODE_LOOP, 100,
                                               &operation_status);
    if (chain_status == CHAIN_OK && operation_status == 1) {
        Serial.printf("String scroll started: %s\r\n", text);
    }
}

void loop()
{
    delay(1000);
}
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/Chain_Mono_Arduino_string_scroll_mode.gif" width="40%">
