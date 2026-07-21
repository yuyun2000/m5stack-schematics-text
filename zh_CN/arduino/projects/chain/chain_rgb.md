# Chain RGB 使用教程

## 1.准备工作

- 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide) 完成 IDE 安装，并根据实际使用的开发板安装对应的板管理与需要的驱动库。

- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5Chain](https://github.com/m5stack/M5Chain)

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Chain RGB](https://shop.m5stack.com/products/chain-rgb-matrix-with-8x8-leds)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_02.webp" width="20%">

## 2.示例程序

实际连接如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_Arduino_connect.jpg" width="50%">

#> 编译要求 | M5Stack 板管理版本 >= 3.2.4<br>M5Chain 库版本 >= 1.0.5

### 像素模式

#### 单像素控制及批量写入

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

chain_status_t chain_status = CHAIN_OK;
uint8_t rgb_id           = 0;
uint8_t operation_status = 0;

const uint16_t colors[] = {
    0xF800,  // Red
    0x07E0,  // Green
    0x001F,  // Blue
    0xFFE0,  // Yellow
    0xF81F,  // Magenta
    0x07FF   // Cyan
};

bool findFirstRGBDevice()
{
    // Enumerate devices and use the first RGB node
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
            if (devices.devices[i].device_type == CHAIN_RGB_TYPE_CODE) {
                rgb_id = devices.devices[i].id;
                found  = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("RGB device found, id=%d\r\n", rgb_id);
    } else {
        Serial.println("No RGB device found");
    }
    return found;
}

bool prepareRGB()
{
    // Initialize pixel mode, rotation, and brightness
    if (!findFirstRGBDevice()) {
        return false;
    }

    if (M5Chain.setRGBMode(rgb_id, RGB_PIXEL_MODE, &operation_status) != CHAIN_OK || operation_status != 1) {
        return false;
    }

    M5Chain.setRGBRotation(rgb_id, RGB_ROTATION_0, &operation_status);
    M5Chain.setRGBBrightness(rgb_id, 50, &operation_status);
    M5Chain.setRGBClear(rgb_id, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("RGB pixel demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareRGB()) {
        Serial.println("Chain RGB init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain RGB init success");
    }
}

void loop()
{
    static bool single_phase = true;
    static uint8_t single_x  = 0;
    static uint8_t single_y  = 0;
    static uint8_t block_x   = 0;
    static uint8_t block_y   = 4;
    static uint8_t color_i   = 0;

    if (single_phase) {
        // Walk through the first 4 rows with one RGB pixel
        M5Chain.setRGBClear(rgb_id, &operation_status);
        chain_status = M5Chain.setRGBPixel(rgb_id, single_x, single_y, colors[color_i], &operation_status);
        if (chain_status == CHAIN_OK && operation_status == 1) {
            Serial.printf("Single pixel: x=%d, y=%d, color=0x%04X\r\n", single_x, single_y, colors[color_i]);
        }

        delay(160);

        single_x++;
        color_i = (color_i + 1) % (sizeof(colors) / sizeof(colors[0]));
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
        // Walk through the last 4 rows with a 2x2 RGB block
        RGBPixelInfo pixels[] = {
            {block_x, block_y, colors[color_i]},
            {(uint8_t)(block_x + 1), block_y, colors[(color_i + 1) % 6]},
            {block_x, (uint8_t)(block_y + 1), colors[(color_i + 2) % 6]},
            {(uint8_t)(block_x + 1), (uint8_t)(block_y + 1), colors[(color_i + 3) % 6]}};

        M5Chain.setRGBClear(rgb_id, &operation_status);
        chain_status = M5Chain.setRGBPixel(rgb_id, pixels, sizeof(pixels) / sizeof(pixels[0]), &operation_status);
        if (chain_status == CHAIN_OK && operation_status == 1) {
            Serial.printf("RGB block: x=%d, y=%d\r\n", block_x, block_y);
        }

        delay(160);

        block_x++;
        color_i = (color_i + 1) % (sizeof(colors) / sizeof(colors[0]));
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

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_Arduino_01.mp4" type="video/mp4"></video>

#### 字符显示

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

uint8_t rgb_id           = 0;
uint8_t operation_status = 0;
const char text[]        = "I'mChainRGB";
const uint16_t colors[]  = {0xFFE0, 0xF800, 0x07E0, 0x001F, 0xFD20, 0x07FF, 0xF81F};

bool findFirstRGBDevice()
{
    // Enumerate devices and use the first RGB node
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
            if (devices.devices[i].device_type == CHAIN_RGB_TYPE_CODE) {
                rgb_id = devices.devices[i].id;
                found  = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("RGB device found, id=%d\r\n", rgb_id);
    } else {
        Serial.println("No RGB device found");
    }
    return found;
}

bool prepareRGB()
{
    // Initialize pixel mode, rotation, and brightness
    if (!findFirstRGBDevice()) {
        return false;
    }

    if (M5Chain.setRGBMode(rgb_id, RGB_PIXEL_MODE, &operation_status) != CHAIN_OK || operation_status != 1) {
        return false;
    }

    M5Chain.setRGBRotation(rgb_id, RGB_ROTATION_0, &operation_status);
    M5Chain.setRGBBrightness(rgb_id, 50, &operation_status);
    M5Chain.setRGBClear(rgb_id, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("RGB character demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareRGB()) {
        Serial.println("Chain RGB init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain RGB init success");
    }
}

void loop()
{
    static uint8_t index = 0;
    char c               = text[index];
    uint16_t color       = colors[index % (sizeof(colors) / sizeof(colors[0]))];

    // Show characters one by one with changing colors
    M5Chain.setRGBClear(rgb_id, &operation_status);
    M5Chain.setRGBPrintChar(rgb_id, c, 1, 1, color, &operation_status);
    Serial.printf("Character shown: %c, color=0x%04X\r\n", c, color);

    delay(400);

    index++;
    if (index >= sizeof(text) - 1) {
        index = 0;
    }
}
```

例程效果如下：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_Arduino_02.mp4" type="video/mp4"></video>

#### 自定义图案显示与旋转

#> 说明 | 此处旋转指的是在绘制前对显示方向进行设置，设置后再进行的绘制操作都会以该方向为基准进行显示，并非直接对已绘制显示内容进行旋转变换。

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

uint8_t rgb_id           = 0;
uint8_t operation_status = 0;

// 8x8 green arrow pattern
uint16_t arrow[64] = {
    0x0000, 0x0000, 0x0000, 0x07E0, 0x07E0, 0x0000, 0x0000, 0x0000,  //    ■■   
    0x0000, 0x0000, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x0000, 0x0000,  //   ■■■■  
    0x0000, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x0000,  //  ■■■■■■ 
    0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x07E0,  // ■■■■■■■■
    0x0000, 0x0000, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x0000, 0x0000,  //   ■■■■  
    0x0000, 0x0000, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x0000, 0x0000,  //   ■■■■  
    0x0000, 0x0000, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x0000, 0x0000,  //   ■■■■  
    0x0000, 0x0000, 0x07E0, 0x07E0, 0x07E0, 0x07E0, 0x0000, 0x0000   //   ■■■■  
};

bool findFirstRGBDevice()
{
    // Enumerate devices and use the first RGB node
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
            if (devices.devices[i].device_type == CHAIN_RGB_TYPE_CODE) {
                rgb_id = devices.devices[i].id;
                found  = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("RGB device found, id=%d\r\n", rgb_id);
    } else {
        Serial.println("No RGB device found");
    }
    return found;
}

bool prepareRGB()
{
    // Initialize pixel mode and brightness
    if (!findFirstRGBDevice()) {
        return false;
    }

    if (M5Chain.setRGBMode(rgb_id, RGB_PIXEL_MODE, &operation_status) != CHAIN_OK || operation_status != 1) {
        return false;
    }

    M5Chain.setRGBBrightness(rgb_id, 50, &operation_status);
    M5Chain.setRGBClear(rgb_id, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("RGB custom pattern rotation demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareRGB()) {
        Serial.println("Chain RGB init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain RGB init success");
    }
}

void loop()
{
    // Rotate through 0/90/180/270 degree display states
    for (uint8_t rotation = RGB_ROTATION_0; rotation <= RGB_ROTATION_270; rotation++) {
        M5Chain.setRGBRotation(rgb_id, (rgb_rotation_t)rotation, &operation_status);
        M5Chain.setRGBBufferRefresh(rgb_id, arrow, &operation_status);
        Serial.printf("Rotation set to: %d°\r\n", rotation * 90);
        delay(800);
    }
}
```

例程效果如下：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_Arduino_03.mp4" type="video/mp4"></video>

#### 动态色彩瀑布

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

uint8_t rgb_id           = 0;
uint8_t operation_status = 0;
uint16_t frame[64]       = {0};
uint8_t color_offset     = 0;

uint16_t color565(uint8_t r, uint8_t g, uint8_t b)
{
    return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3);
}

uint16_t wheel(uint8_t pos)
{
    if (pos < 85) {
        return color565(255 - pos * 3, pos * 3, 0);
    }
    if (pos < 170) {
        pos -= 85;
        return color565(0, 255 - pos * 3, pos * 3);
    }

    pos -= 170;
    return color565(pos * 3, 0, 255 - pos * 3);
}

bool findFirstRGBDevice()
{
    // Enumerate devices and use the first RGB node
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
            if (devices.devices[i].device_type == CHAIN_RGB_TYPE_CODE) {
                rgb_id = devices.devices[i].id;
                found  = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("RGB device found, id=%d\r\n", rgb_id);
    } else {
        Serial.println("No RGB device found");
    }
    return found;
}

bool prepareRGB()
{
    // Initialize pixel mode, rotation, and brightness
    if (!findFirstRGBDevice()) {
        return false;
    }

    if (M5Chain.setRGBMode(rgb_id, RGB_PIXEL_MODE, &operation_status) != CHAIN_OK || operation_status != 1) {
        return false;
    }

    M5Chain.setRGBRotation(rgb_id, RGB_ROTATION_0, &operation_status);
    M5Chain.setRGBBrightness(rgb_id, 50, &operation_status);
    M5Chain.setRGBClear(rgb_id, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("RGB color waterfall demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareRGB()) {
        Serial.println("Chain RGB init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain RGB init success");
    }
}

void loop()
{
    // Move old rows down by one row
    for (int y = 7; y > 0; y--) {
        for (int x = 0; x < 8; x++) {
            frame[y * 8 + x] = frame[(y - 1) * 8 + x];
        }
    }

    // Generate a new color row at the top
    for (int x = 0; x < 8; x++) {
        frame[x] = wheel(color_offset + x * 16);
    }

    M5Chain.setRGBBufferRefresh(rgb_id, frame, &operation_status);
    Serial.printf("Waterfall frame offset: %d\r\n", color_offset);

    color_offset += 4;
    delay(80);
}
```

例程效果如下：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_Arduino_04.mp4" type="video/mp4"></video>

### 字符串滚动模式

```cpp line-num
#include "M5Chain.h"
#include "M5Unified.h"

#define TXD_PIN GPIO_NUM_2
#define RXD_PIN GPIO_NUM_1

Chain M5Chain;

chain_status_t chain_status = CHAIN_OK;
uint8_t rgb_id           = 0;
uint8_t operation_status = 0;
const char text[]        = "Hi I'm Chain RGB! ";

bool findFirstRGBDevice()
{
    // Enumerate devices and use the first RGB node
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
            if (devices.devices[i].device_type == CHAIN_RGB_TYPE_CODE) {
                rgb_id = devices.devices[i].id;
                found  = true;
                break;
            }
        }
    }

    free(infos);
    if (found) {
        Serial.printf("RGB device found, id=%d\r\n", rgb_id);
    } else {
        Serial.println("No RGB device found");
    }
    return found;
}

bool prepareRGB()
{
    // Switch to string scroll mode and set basic parameters
    if (!findFirstRGBDevice()) {
        return false;
    }

    if (M5Chain.setRGBMode(rgb_id, RGB_STRING_SCROLL_MODE, &operation_status) != CHAIN_OK ||
        operation_status != 1) {
        return false;
    }

    M5Chain.setRGBRotation(rgb_id, RGB_ROTATION_0, &operation_status);
    M5Chain.setRGBBrightness(rgb_id, 30, &operation_status);
    return true;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("RGB string scroll demo");
    M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);

    if (!prepareRGB()) {
        Serial.println("Chain RGB init failed");
        while (1) {
            delay(100);
        }
    } else {
        Serial.println("Chain RGB init success");
    }

    chain_status = M5Chain.setRGBStringScroll(rgb_id, text, RGB_SCROLL_LEFT, RGB_SCROLL_MODE_LOOP, 100,
                                              RGB_SCROLL_COLOR_GRADIENT, &operation_status);
    if(chain_status == CHAIN_OK && operation_status == 1) {
        Serial.printf("String scroll started: %s\r\n", text);
    }
}

void loop()
{
    delay(1000);
} 
```

例程效果如下：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_Arduino_05.mp4" type="video/mp4"></video>



