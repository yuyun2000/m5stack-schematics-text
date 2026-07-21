# PaperColor IR NEC 发射器

PaperColor IR NEC 发射器相关 API 与案例程序。本案例使用 [Arduino-IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote) 库实现 NEC 编码。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.7
- 开发板选项 = M5PaperColor
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21

```cpp line-num
#include <Arduino.h>
#include <M5Unified.h>
#include <IRremote.hpp>

#define IR_TX_PIN 48

static constexpr uint16_t IR_ADDRESS       = 0x1111;
static constexpr uint8_t IR_START_COMMAND  = 0x34;
static constexpr uint8_t IR_REPEATS        = 0;
static constexpr uint32_t SEND_INTERVAL_MS = 1000;

M5Canvas canvas(&M5.Display);

static uint8_t currentCommand      = IR_START_COMMAND;
static uint32_t sendCount          = 0;
static uint32_t lastMinuteChangeMs = 0;
static uint32_t lastSendMs         = 0;

static void drawStatusScreen(const String& title, const String& detail, uint16_t accentColor)
{
    const int screenW = M5.Display.width();
    const int screenH = M5.Display.height();

    canvas.fillSprite(WHITE);
    canvas.fillRect(0, 0, screenW, 42, BLACK);
    canvas.fillRect(0, 42, screenW, 6, accentColor);

    canvas.setTextDatum(top_center);
    canvas.setTextSize(1);

    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(WHITE);
    canvas.drawString(title, screenW / 2, 8);

    canvas.setFont(&fonts::FreeSansBold12pt7b);
    canvas.setTextColor(accentColor);
    canvas.drawString(detail, screenW / 2, 72);

    canvas.pushSprite(0, 0);
}

static void drawIrScreen()
{
    const int screenW = M5.Display.width();
    const int screenH = M5.Display.height();
    char commandBuf[24];

    snprintf(commandBuf, sizeof(commandBuf), "0x%02X", currentCommand);

    canvas.fillSprite(WHITE);
    canvas.fillRect(0, 0, screenW, 50, BLACK);
    canvas.fillRect(0, 50, screenW, 6, RED);

    canvas.setTextDatum(top_center);
    canvas.setTextSize(1);

    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(WHITE);
    canvas.drawString("IR NEC SEND TEST", screenW / 2, 12);

    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.setTextDatum(middle_center);
    canvas.setTextColor(BLUE);
    canvas.drawString("0x1111", screenW / 2, screenH / 2 - 60);

    canvas.setTextColor(RED);
    canvas.drawString(commandBuf, screenW / 2, screenH / 2 + 60);

    canvas.setFont(&fonts::FreeSansBold12pt7b);
    canvas.setTextDatum(top_center);
    canvas.setTextColor(BLACK);
    canvas.drawString("ADDR", screenW / 2, screenH / 2 - 105);
    canvas.drawString("CMD", screenW / 2, screenH / 2 + 15);

    canvas.pushSprite(0, 0);
}

static void sendCurrentCommand()
{
    IrSender.sendNEC(IR_ADDRESS, currentCommand, IR_REPEATS);
    ++sendCount;

    Serial.printf("IR NEC sent: addr=0x%04X cmd=0x%02X repeats=%u count=%lu\r\n", IR_ADDRESS,
                  currentCommand, IR_REPEATS, static_cast<unsigned long>(sendCount));
}

void setup()
{
    auto cfg          = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);
    Serial.begin(115200);

    M5.Display.setEpdMode(epd_mode_t::epd_fastest);
    M5.Display.setRotation(1);

    canvas.createSprite(M5.Display.width(), M5.Display.height());

    gpio_reset_pin(gpio_num_t(IR_TX_PIN));

    IrSender.begin(DISABLE_LED_FEEDBACK);
    IrSender.setSendPin(IR_TX_PIN);

    const uint32_t now = millis();
    lastMinuteChangeMs = now;
    lastSendMs         = now;
    drawIrScreen();
    sendCurrentCommand();
}

void loop()
{
    M5.update();

    const uint32_t now = millis();

    if (now - lastMinuteChangeMs >= 60000) {
        lastMinuteChangeMs = now;
        currentCommand     = static_cast<uint8_t>(currentCommand + 1);
        drawIrScreen();
    }

    if (now - lastSendMs >= SEND_INTERVAL_MS) {
        lastSendMs = now;
        sendCurrentCommand();
    }

    delay(50);
}
```

该程序将通过设备上的红外发射器发送 NEC 协议信号：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_ir_nec_demo_01.jpg" width="50%">

## API

PaperColor IR NEC 发射器部分驱动使用了 `IRremote` 库中的 `IrSender_Class`，更多相关 API 可参考下方文档：

- [Arduino-IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote)
- [Arduino-IRremote API 文档](https://github.com/Arduino-IRremote/Arduino-IRremote#api-documentation)
