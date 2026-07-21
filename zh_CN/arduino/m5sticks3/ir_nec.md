# StickS3 IR 红外发送 & 接收

StickS3 IR 红外发送 & 接收相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18

### 发送端

```cpp line-num
#include "M5Unified.h"
#include "driver/rmt_tx.h"
#include "driver/rmt_encoder.h"

#define IR_SEND_PIN    46      // GPIO pin connected to IR LED transmitter

// NEC protocol parameters
uint16_t address = 0x0000;     // NEC address (8-bit or 16-bit)
uint8_t  command = 0x55;       // NEC command byte
uint8_t  repeats = 0;          // Number of repeat frames (0 = no repeat)

rmt_channel_handle_t tx_chan = NULL;
rmt_encoder_handle_t copy_encoder = NULL;

// NEC protocol timing constants (microseconds)
#define NEC_HEADER_MARK     9000
#define NEC_HEADER_SPACE    4500
#define NEC_BIT_MARK        560
#define NEC_BIT_0_SPACE     560
#define NEC_BIT_1_SPACE     1690
#define NEC_REPEAT_MARK     9000
#define NEC_REPEAT_SPACE    2250

// IR carrier configuration
#define IR_CARRIER_FREQ_HZ  38000
#define IR_DUTY_CYCLE       0.33

// Function prototypes
void setup_rmt_tx();
bool sendNEC(uint16_t address, uint8_t command, uint8_t repeats);
void encodeNEC(uint32_t raw_data, rmt_symbol_word_t *symbols, size_t *symbol_count);
uint32_t NECRaw(uint16_t address, uint8_t command);

void setup() {
    M5.begin();
    Serial.begin(115200);

    // Display initialization
    M5.Display.setRotation(3);
    M5.Display.setTextFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.clear();
    M5.Display.setCursor(0, 0);
    M5.Display.printf("StickS3 IR example");

    Serial.println("StickS3 IR example");

    // Initialize RMT TX channel
    setup_rmt_tx();

    Serial.printf("IR Send Pin: %d\n", IR_SEND_PIN);

    // Enable external power output for IR LED module
    M5.Power.setExtOutput(true, m5::ext_none);
    delay(100);
}

void loop() {
    // Build 32-bit NEC frame data
    uint32_t raw = NECRaw(address, command);

    Serial.printf("Send NEC: addr=0x%04X, cmd=0x%02X, raw=0x%08X\n", address, command, raw);

    // -------- Send NEC frame --------
    sendNEC(address, command, repeats);

    M5.Display.fillRect(0, 30, 240, 105, TFT_BLACK);
    M5.Display.setCursor(0, 30);
    M5.Display.printf("Send NEC:\n");
    M5.Display.printf(" addr=0x%04X\n", address);
    M5.Display.printf(" cmd =0x%02X\n", command);
    M5.Display.printf(" raw =0x%08X\n", raw);

    address += 0x0001;
    command += 0x01;
    repeats = 0;

    delay(2000);
}

// Initialize RMT TX channel
void setup_rmt_tx() {
    // Configure RMT TX channel
    rmt_tx_channel_config_t tx_chan_config = {
        .gpio_num = (gpio_num_t)IR_SEND_PIN,
        .clk_src = RMT_CLK_SRC_DEFAULT,
        .resolution_hz = 1000000, // 1 us per tick
        .mem_block_symbols = 64,
        .trans_queue_depth = 4,
        .flags = {
            .invert_out = false,
            .with_dma = false,
        }
    };
    ESP_ERROR_CHECK(rmt_new_tx_channel(&tx_chan_config, &tx_chan));

    // Configure 38kHz carrier wave for IR transmission
    rmt_carrier_config_t carrier_cfg = {
        .frequency_hz = IR_CARRIER_FREQ_HZ,
        .duty_cycle = IR_DUTY_CYCLE,
        .flags = {
            .polarity_active_low = false,
        }
    };
    ESP_ERROR_CHECK(rmt_apply_carrier(tx_chan, &carrier_cfg));

    // Create copy encoder for pre-encoded symbols
    rmt_copy_encoder_config_t encoder_config = {};
    ESP_ERROR_CHECK(rmt_new_copy_encoder(&encoder_config, &copy_encoder));

    // Enable TX channel
    ESP_ERROR_CHECK(rmt_enable(tx_chan));
}

/*
 * Send NEC IR frame via RMT.
 *
 * @param address NEC address (8-bit or 16-bit)
 * @param command NEC command byte
 * @param repeats Number of repeat frames to send
 *
 * @return true if transmission successful
 */
bool sendNEC(uint16_t address, uint8_t command, uint8_t repeats) {
    // Build 32-bit NEC raw data
    uint32_t raw = NECRaw(address, command);

    // Buffer for RMT symbols
    rmt_symbol_word_t symbols[68]; // Header + 32 bits + ending mark
    size_t symbol_count = 0;

    encodeNEC(raw, symbols, &symbol_count);

    // RMT transmit configuration
    rmt_transmit_config_t tx_config = {
        .loop_count = 0,
        .flags = {
            .eot_level = 0,
        }
    };

    // Transmit the frame
    esp_err_t ret = rmt_transmit(tx_chan, copy_encoder, symbols,
                                  symbol_count * sizeof(rmt_symbol_word_t),
                                  &tx_config);

    if (ret == ESP_OK) {
        // Wait for transmission completion
        ret = rmt_tx_wait_all_done(tx_chan, 1000);
    }

    // Send repeat frames if requested
    for (int i = 0; i < repeats; i++) {
        delay(108); // NEC repeat frame interval

        // TODO: Implement repeat frame
        // Repeat frame: 9ms mark + 2.25ms space + 560us mark
    }

    return (ret == ESP_OK);
}

/*
 * Encode NEC protocol data into RMT symbols.
 *
 * @param raw_data     32-bit NEC frame data
 * @param symbols      Output buffer for RMT symbols
 * @param symbol_count Number of symbols generated
 */
void encodeNEC(uint32_t raw_data, rmt_symbol_word_t *symbols, size_t *symbol_count) {
    size_t idx = 0;

    // NEC header: ~9 ms mark + ~4.5 ms space
    symbols[idx].duration0 = NEC_HEADER_MARK;
    symbols[idx].level0 = 1;
    symbols[idx].duration1 = NEC_HEADER_SPACE;
    symbols[idx].level1 = 0;
    idx++;

    // Encode 32 data bits (LSB first)
    for (int i = 0; i < 32; i++) {
        // Mark duration: always 560 us
        symbols[idx].duration0 = NEC_BIT_MARK;
        symbols[idx].level0 = 1;

        // Space duration distinguishes logic 0 and logic 1
        if (raw_data & (1UL << i)) {
            symbols[idx].duration1 = NEC_BIT_1_SPACE; // Logic 1: 1690 us
        } else {
            symbols[idx].duration1 = NEC_BIT_0_SPACE; // Logic 0: 560 us
        }
        symbols[idx].level1 = 0;
        idx++;
    }

    // Ending mark: 560 us
    symbols[idx].duration0 = NEC_BIT_MARK;
    symbols[idx].level0 = 1;
    symbols[idx].duration1 = 0;
    symbols[idx].level1 = 0;
    idx++;

    *symbol_count = idx;
}

/*
 * Build 32-bit NEC raw data from address and command.
 *
 * NEC frame format (LSB first):
 *   bit  0-15 : Address field (8-bit + inverse, or full 16-bit)
 *   bit 16-23 : Command byte
 *   bit 24-31 : Inverse of command byte
 *
 * @param address NEC address (8-bit with auto-inverse, or 16-bit extended)
 * @param command NEC command byte
 *
 * @return 32-bit NEC raw data ready for encoding
 */
uint32_t NECRaw(uint16_t address, uint8_t command) {
    uint16_t nec_addr;

    // Standard NEC: 8-bit address + inverse byte
    if (address <= 0x00FF) {
        uint8_t addr8 = address & 0xFF;
        nec_addr = ((uint16_t)(~addr8) << 8) | addr8;
    }
    // Extended NEC: full 16-bit address
    else {
        nec_addr = address;
    }

    // Assemble 32-bit NEC frame
    uint32_t raw = 0;
    raw |= (uint32_t)nec_addr;            // Address field
    raw |= (uint32_t)command << 16;       // Command byte
    raw |= (uint32_t)(~command) << 24;    // Inverted command byte

    return raw;
}
```

### 接收端

!> 注意事项 | 1\. StickS3 红外接收解码**必须使用 ESP32 RMT 外设**，不支持通过 GPIO 方式进行接收解码。  
2\.使用 StickS3 红外接收功能时，需要关闭扬声器功放（即下方代码中的 `M5.Speaker.end();` 或使用 [M5PM1 SPK APM 小节相关 API](/zh_CN/arduino/m5sticks3/m5pm1)），否则无法正常接收。  
3\.红外发收过程中，要求发射端尽可能正对接收端，距离要求大于 30cm, 过近可能导致接收异常。

```cpp line-num
#include "M5Unified.h"
#include "driver/rmt_rx.h"

#define IR_RECEIVE_PIN 42

rmt_channel_handle_t rx_chan = NULL;
static rmt_symbol_word_t rx_raw_symbols[64]; // Buffer for received RMT symbols
static volatile bool rx_done = false;
static size_t rx_symbol_num = 0; // Number of symbols received in last RX transaction

// Function prototypes
bool rmt_rx_done_callback(rmt_channel_handle_t channel, const rmt_rx_done_event_data_t *edata, void *user_data);
void setup_rmt_rx();
void start_rmt_receive();
bool decodeNEC(rmt_symbol_word_t *rx_raw_symbols, uint32_t *out_raw, bool *out_repeat);

void setup() {
    M5.begin();
    M5.Speaker.end();// Disable speaker amp to avoid IR RX interference
    Serial.begin(115200);

    // Display initialization
    M5.Display.setRotation(3);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.clear();
    M5.Display.println("StickS3 IR example");
    M5.Display.setCursor(0, 30);
    M5.Display.println("Waiting for NEC...");

    setup_rmt_rx();      // Initialize RMT RX channel and register RX Done callback
    start_rmt_receive(); // Start first RMT receive operation

    // Enable external power output for IR receiver module
    M5.Power.setExtOutput(true, m5::ext_none);
}

void loop() {
    M5.update();
    
    // Check if a complete IR frame has been received
    if (rx_done) {
        rx_done = false;

        uint32_t rx_data = 0;
        bool repeat_frame = false;

        bool valid = decodeNEC(rx_raw_symbols, &rx_data, &repeat_frame);

        if (repeat_frame) {
            Serial.println("NEC Repeat Frame");
            M5.Display.fillRect(0, 30, 240, 105, TFT_BLACK);
            M5.Display.setCursor(0, 30);
            M5.Display.setTextColor(YELLOW);
            M5.Display.println("NEC Repeat");
        }
        else if (valid) {
            uint16_t rx_addr = rx_data & 0xFFFF;
            uint8_t  rx_cmd  = (rx_data >> 16) & 0xFF;
            Serial.printf(
                "Received NEC: Addr: 0x%04X, Cmd: 0x%02X, Raw: 0x%08X\n",
                rx_addr, rx_cmd, rx_data
            );

            M5.Display.fillRect(0, 30, 240, 105, TFT_BLACK);
            M5.Display.setCursor(0, 30);
            M5.Display.setTextColor(GREEN);
            M5.Display.printf("Received NEC:\n");
            M5.Display.printf("Addr: 0x%04X\n", rx_addr);
            M5.Display.printf("Cmd:  0x%02X\n", rx_cmd);
            M5.Display.printf("Raw:  0x%08X\n", rx_data);
        }
        else {
            Serial.println("Signal received, but not a valid NEC frame.");
        }
        // Re-arm RMT RX to receive the next IR frame
        start_rmt_receive();
    }

    delay(10);
    M5.Display.setTextColor(WHITE);
}

/*
 * RMT RX Done callback.
 *
 * Called in ISR context when a complete RX transaction finishes.
 *
 * @param channel   RMT channel handle
 * @param edata     RX event data containing symbol buffer and count
 * @param user_data User context pointer (unused)
 *
 * @return true to request deferred processing after ISR
 */
bool rmt_rx_done_callback( rmt_channel_handle_t channel, const rmt_rx_done_event_data_t *edata, void *user_data) {
    rx_symbol_num = edata->num_symbols;
    rx_done = true;
    return true; // Return true to allow post-ISR task scheduling
}

// Initialize RMT RX channel
void setup_rmt_rx() {
    rmt_rx_channel_config_t rx_chan_config = {
        .gpio_num = (gpio_num_t)IR_RECEIVE_PIN,
        .clk_src = RMT_CLK_SRC_DEFAULT,
        .resolution_hz = 1000000, // 1 us per tick
        .mem_block_symbols = 128,
    };
    ESP_ERROR_CHECK(rmt_new_rx_channel(&rx_chan_config, &rx_chan));
    rmt_rx_event_callbacks_t cbs = {
        .on_recv_done = rmt_rx_done_callback,
    };
    ESP_ERROR_CHECK(rmt_rx_register_event_callbacks(rx_chan, &cbs, NULL));
    ESP_ERROR_CHECK(rmt_enable(rx_chan));
}

// Start an RMT receive operation
void start_rmt_receive() {
    rmt_receive_config_t receive_config = {
        .signal_range_min_ns = 1000,
        .signal_range_max_ns = 20000000
    };

    ESP_ERROR_CHECK(rmt_receive(rx_chan, rx_raw_symbols, sizeof(rx_raw_symbols), &receive_config));
}

/*
 * Decode a NEC IR frame from RMT symbols.
 *
 * @param rx_raw_symbols Pointer to RMT RX symbol buffer
 * @param out_raw        Decoded 32-bit NEC raw data (LSB first)
 * @param out_repeat     Set to true if a NEC repeat frame is detected
 *
 * @return true if a valid NEC data frame is decoded
 */
bool decodeNEC(rmt_symbol_word_t *rx_raw_symbols, uint32_t *out_raw, bool *out_repeat) {

    *out_raw = 0;
    *out_repeat = false;

    uint32_t header_low  = rx_raw_symbols[0].duration0;
    uint32_t header_high = rx_raw_symbols[0].duration1;

    // Standard NEC header: ~9 ms LOW + ~4.5 ms HIGH
    if (header_low > 8000 && header_high > 4000) {
        // Valid NEC header, continue decoding
    }
    // NEC repeat frame: ~9 ms LOW + ~2.25 ms HIGH
    else if (header_low > 8000 &&
             header_high > 2000 &&
             header_high < 3000) {
        *out_repeat = true;
        return false;
    }
    else {
        return false;
    }

    // Decode 32 NEC data bits (LSB first)
    for (int i = 0; i < 32; i++) {
        uint32_t mark  = rx_raw_symbols[i + 1].duration0;
        uint32_t space = rx_raw_symbols[i + 1].duration1;

        // NEC mark duration should be ~560 us
        if (mark < 300 || mark > 800) {
            return false;
        }

        // Space duration distinguishes logic 0 and logic 1
        if (space > 1000) {
            *out_raw |= (1UL << i);
        }
    }

    // Verify command byte and its inverse
    uint8_t cmd     = (*out_raw >> 16) & 0xFF;
    uint8_t cmd_inv = (*out_raw >> 24) & 0xFF;

    if ((cmd ^ cmd_inv) != 0xFF) {
        return false;
    }

    return true;
}
```

发送端与接收端分别运行在两台 StickS3 设备上，发送端每两秒发送一次 NEC 红外信号，接收端接收到信号后会在串口与屏幕上显示接收到的地址与命令。

\#> 说明 | 1. 下方图片未将右侧的反射平面拍摄入画面，实际使用中建议利用反射平面将发射端的红外信号反射至接收端，以获得最佳接收效果。  
2\. 当用户码（Address）不超过 0x00FF 时，发送端会以 NEC 标准码格式发送红外信号，此时地址字段由 8 位用户码与其反码组成，接收端解析出的地址与发送端不完全一致；反之，当用户码超过 0x00FF 时，发送端会以 NEC 扩展码格式发送红外信号，此时地址字段为完整的 16 位用户码，接收端解析出的地址与发送端一致。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_ir_nec.jpg" width="40%">

### IR 接收回传

```cpp line-num
#include "M5Unified.h"
#include "driver/rmt_rx.h"
#include "driver/rmt_tx.h"
#include "driver/rmt_encoder.h"

#define IR_RECEIVE_PIN 42
#define IR_SEND_PIN    46

rmt_channel_handle_t rx_chan = NULL;
rmt_channel_handle_t tx_chan = NULL;
rmt_encoder_handle_t copy_encoder = NULL;

static rmt_symbol_word_t rx_raw_symbols[256];
static volatile bool rx_done = false;
static size_t rx_symbol_num = 0;

#define IR_CARRIER_FREQ_HZ  38000
#define IR_DUTY_CYCLE       0.33

/* ================= Dump level data================= */
void dump_pulse_array(rmt_symbol_word_t *symbols, size_t count) {
    Serial.println("IR PULSE (us):(L0 | L1)");

    for (size_t i = 0; i < count; i++) {
        int32_t p0 = symbols[i].level0 ? symbols[i].duration0 : -symbols[i].duration0;
        int32_t p1 = symbols[i].level1 ? symbols[i].duration1 : -symbols[i].duration1;
        Serial.printf(" %d, %d\n", p0, p1);
    }
    Serial.println();
}

void dump_duration_array(rmt_symbol_word_t *symbols, size_t count) {
    Serial.println("IR DURATIONS (us):(L0 | L1)");

    for (size_t i = 0; i < count; i++) {
        Serial.printf(" %d, %d\n", symbols[i].duration0, symbols[i].duration1);
    }
    Serial.println();
}

void dump_raw_hex(rmt_symbol_word_t *symbols, size_t count) {
    Serial.println("IR RAW HEX:(L0 | L1)");

    for (size_t i = 0; i < count; i++) {
        Serial.printf(" %04X %04X\n", symbols[i].duration0, symbols[i].duration1);
    }
    Serial.println();
}

bool rmt_rx_done_callback(rmt_channel_handle_t, const rmt_rx_done_event_data_t *edata, void *) {
    rx_symbol_num = edata->num_symbols;
    rx_done = true;
    return true;
}

void setup_rmt_rx() {
    rmt_rx_channel_config_t rx_cfg = {
        .gpio_num = (gpio_num_t)IR_RECEIVE_PIN,
        .clk_src = RMT_CLK_SRC_DEFAULT,
        .resolution_hz = 1000000,
        .mem_block_symbols = 128,
    };

    if (rmt_new_rx_channel(&rx_cfg, &rx_chan) != ESP_OK) return;

    rmt_rx_event_callbacks_t cbs = {
        .on_recv_done = rmt_rx_done_callback,
    };

    rmt_rx_register_event_callbacks(rx_chan, &cbs, NULL);
    rmt_enable(rx_chan);
}

void start_rmt_receive() {
    rmt_receive_config_t cfg = {
        .signal_range_min_ns = 1000,
        .signal_range_max_ns = 20000000,
    };

    rmt_receive(rx_chan, rx_raw_symbols, sizeof(rx_raw_symbols), &cfg);
}

void setup_rmt_tx() {
    rmt_tx_channel_config_t tx_cfg = {
        .gpio_num = (gpio_num_t)IR_SEND_PIN,
        .clk_src = RMT_CLK_SRC_DEFAULT,
        .resolution_hz = 1000000,
        .mem_block_symbols = 128,
        .trans_queue_depth = 4,
    };

    rmt_new_tx_channel(&tx_cfg, &tx_chan);

    rmt_carrier_config_t carrier_cfg = {
        .frequency_hz = IR_CARRIER_FREQ_HZ,
        .duty_cycle = IR_DUTY_CYCLE,
    };

    rmt_apply_carrier(tx_chan, &carrier_cfg);

    rmt_copy_encoder_config_t enc_cfg = {};
    rmt_new_copy_encoder(&enc_cfg, &copy_encoder);

    rmt_enable(tx_chan);
}

void send_raw_symbols(rmt_symbol_word_t *symbols, size_t count) {
    rmt_transmit_config_t cfg = { .loop_count = 0 };
    rmt_transmit( tx_chan, copy_encoder, symbols, count * sizeof(rmt_symbol_word_t), &cfg);
    rmt_tx_wait_all_done(tx_chan, 1000);
    Serial.printf("Transmit back OK!\n\n");
}

void setup() {
    M5.begin();
    M5.Speaker.end();// Disable speaker amp to avoid IR RX interference
    Serial.begin(115200);

    // Display initialization
    M5.Display.setRotation(3);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.clear();
    M5.Display.println("StickS3 IR example");
    M5.Display.setCursor(0, 30);
    M5.Display.println("Waiting for NEC...");

    setup_rmt_rx();
    setup_rmt_tx();
    start_rmt_receive();

    // Enable external power output for IR receiver module
    M5.Power.setExtOutput(true, m5::ext_none);
}

void loop() {
    if (rx_done) {
        rx_done = false;

        Serial.printf("RX symbols num: %d\n", rx_symbol_num);
        dump_pulse_array(rx_raw_symbols, rx_symbol_num);
        dump_duration_array(rx_raw_symbols, rx_symbol_num);
        dump_raw_hex(rx_raw_symbols, rx_symbol_num);

        M5.Display.fillRect(0, 30, 240, 105, TFT_BLACK);
        M5.Display.setCursor(0, 30);
        M5.Display.setTextColor(GREEN);
        M5.Display.printf("Received!\nsymbols num: %d\nDetails see Serial", rx_symbol_num);

        send_raw_symbols(rx_raw_symbols, rx_symbol_num);
        start_rmt_receive();
    }
    delay(10);
}
```

上述程序烧录到 StickS3 上后，当接收到 IR 信号时，会在串口输出接收到的 IR 信号信息，包括每个符号的电平持续时间（以微秒为单位）以及对应的十六进制表示。同时，程序会将接收到的原始 IR 数据通过红外发送回去，用户可以使用支持红外协议的红外接收设备进行验证。

串口返回信息示例：

```
RX symbols num: 34
IR PULSE (us):(L0 | L1)
 -9008, 4488
 -591, 568
 -538, 567
 -565, 567
 -536, 1700
 -563, 567
 -540, 1724
 -540, 1696
 -538, 1726
 -538, 1698
 -540, 1722
 -542, 1696
 -539, 591
 -540, 1697
 -538, 594
 -538, 566
 -566, 566
 -540, 1697
 -567, 564
 -538, 1699
 -565, 1698
 -541, 1696
 -567, 1695
 -540, 592
 -540, 564
 -538, 594
 -542, 1696
 -564, 566
 -540, 566
 -566, 565
 -538, 566
 -570, 1667
 -567, 1697
 -567, 0

IR DURATIONS (us):(L0 | L1)
 9008, 4488
 591, 568
 538, 567
 565, 567
 536, 1700
 563, 567
 540, 1724
 540, 1696
 538, 1726
 538, 1698
 540, 1722
 542, 1696
 539, 591
 540, 1697
 538, 594
 538, 566
 566, 566
 540, 1697
 567, 564
 538, 1699
 565, 1698
 541, 1696
 567, 1695
 540, 592
 540, 564
 538, 594
 542, 1696
 564, 566
 540, 566
 566, 565
 538, 566
 570, 1667
 567, 1697
 567, 0

IR RAW HEX:(L0 | L1)
 2330 1188
 024F 0238
 021A 0237
 0235 0237
 0218 06A4
 0233 0237
 021C 06BC
 021C 06A0
 021A 06BE
 021A 06A2
 021C 06BA
 021E 06A0
 021B 024F
 021C 06A1
 021A 0252
 021A 0236
 0236 0236
 021C 06A1
 0237 0234
 021A 06A3
 0235 06A2
 021D 06A0
 0237 069F
 021C 0250
 021C 0234
 021A 0252
 021E 06A0
 0234 0236
 021C 0236
 0236 0235
 021A 0236
 023A 0683
 0237 06A1
 0237 0000

Transmit back OK!

```