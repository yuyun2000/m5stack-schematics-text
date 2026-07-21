# Unit Mini PDM Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 使用到的硬件产品：
  - [Core2 v1.1](https://shop.m5stack.com/products/m5stack-core2-esp32-iot-development-kit)
  - [Unit Mini PDM](https://shop.m5stack.com/products/pdm-microphone-unit-spm1423)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2%20v1.1/img-9eb726ec-5729-42c3-9cce-e06140856095.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pdm/pdm_cover_01.webp" width="20%">

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，为了让用户更方便地使用，M5Stack 官方提供了引脚兼容性表，方便用户查看，请根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U089" type="UNIT"></ProductCompatible>

## 3. 案例程序

本教程中使用的主控设备为 Core2 v1.1 ，搭配 Unit Mini PDM。本单元采用 I2S 的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的 I2S 引脚为 `G33 (CLK)`，`G32 (DATA)`。

#> 说明 | 下方基于不同 API 的两个例程功能相同，仅 I2S 配置方式不同，用户可根据实际需求选择使用。

### 3.1 基础使用

#### 基于 M5Unified Mic API

```cpp line-num
#include <M5Unified.h>

#define PIN_CLK  33
#define PIN_DATA 32

// Audio recording configuration constants
static constexpr const size_t record_number     = 256;      // Number of recording buffers
static constexpr const size_t record_length     = 320;      // Samples per buffer (recommended to match LCD width)
static constexpr const size_t record_size       = record_number * record_length;  // Total recording size
static constexpr const size_t record_samplerate = 16000;    // Recording sample rate in Hz

// Variables for waveform drawing
static int16_t prev_y[record_length];  // Previous Y positions for waveform clearing
static int16_t prev_h[record_length];  // Previous heights for waveform clearing
static size_t rec_record_idx  = 2;     // Current recording buffer index
static size_t draw_record_idx = 0;     // Current buffer index for drawing
static int16_t *rec_data;              // Pointer to recording data buffer
static int32_t w;                      // Display width

void setup(void) {
    // Initialize M5 device with default configuration
    auto cfg = M5.config();
    M5.begin(cfg);
    
    // Configure display
    M5.Display.setRotation(1);          // Set display rotation
    w = M5.Display.width();             // Get display width
    M5.Display.startWrite();            // Start display write transaction
    M5.Display.setTextDatum(top_center);// Set text alignment
    M5.Display.setTextColor(TFT_WHITE); // Set text color
    M5.Display.setFont(&fonts::FreeSansBoldOblique9pt7b);  // Set display font

    // Configure microphone settings
    m5::mic_config_t mic_cfg = {
      .pin_data_in = PIN_DATA,          // Microphone data input pin
      .pin_bck = I2S_PIN_NO_CHANGE,     // No change for I2S bit clock
      .pin_mck = I2S_PIN_NO_CHANGE,     // No change for I2S master clock
      .pin_ws = PIN_CLK,                // Microphone word select (clock) pin
      .sample_rate = record_samplerate, // Microphone sample rate in Hz
      .dma_buf_len = 128,               // DMA buffer length
      .dma_buf_count = 2,               // Number of DMA buffers
      .i2s_port = i2s_port_t::I2S_NUM_0 // I2S port number
    };

    // Apply microphone configuration
    M5.Mic.config(mic_cfg);

    // Allocate memory for recording buffer
    rec_data = (typeof(rec_data))heap_caps_malloc(record_size * sizeof(int16_t), MALLOC_CAP_8BIT);
    memset(rec_data, 0, record_size * sizeof(int16_t));  // Initialize buffer to zero
    
    // Start microphone
    M5.Mic.begin();
    
    // Display recording status indicators
    M5.Display.fillCircle(200, 28, 8, RED);
    M5.Display.drawString("REC", w / 2, 18);
}

void loop(void) {
    // Update M5 device state
    M5.update();
    
    // Check if microphone is enabled
    if (M5.Mic.isEnabled()) {
        static constexpr int shift = 6;  // Shift value for amplitude scaling
        auto data = &rec_data[rec_record_idx * record_length];  // Get current recording buffer
        
        // Record audio data into buffer
        if (M5.Mic.record(data, record_length)) {
            data = &rec_data[draw_record_idx * record_length];  // Get buffer for drawing
            
            // Ensure display width doesn't exceed buffer size
            if (w > record_length - 1) {
                w = record_length - 1;
            }
            
            // Draw audio waveform
            for (int32_t x = 0; x < w; ++x) {
                // Clear previous waveform at this X position
                M5.Display.writeFastVLine(x, prev_y[x], prev_h[x], TFT_BLACK);
                
                // Calculate waveform points (scaled by shift)
                int32_t y1 = (data[x] >> shift);
                int32_t y2 = (data[x + 1] >> shift);
                
                // Ensure y1 is the lower value
                if (y1 > y2) {
                    int32_t tmp = y1;
                    y1          = y2;
                    y2          = tmp;
                }
                
                // Calculate display coordinates
                int32_t y = ((M5.Display.height()) >> 1) + y1;  // Base Y position
                int32_t h = ((M5.Display.height()) >> 1) + y2 + 1 - y;  // Waveform height
                
                // Store current values for next frame's clearing
                prev_y[x] = y;
                prev_h[x] = h;
                
                // Draw current waveform segment
                M5.Display.writeFastVLine(x, prev_y[x], prev_h[x], WHITE);
            }
            
            // Update display and maintain recording indicators
            M5.Display.display();
            M5.Display.fillCircle(200, 28, 8, RED);  // Red circle for recording status
            M5.Display.drawString("REC", w / 2, 18);   // "REC" text indicator
            
            // Update buffer indices (wrap around when reaching end)
            if (++draw_record_idx >= record_number) { draw_record_idx = 0; }
            if (++rec_record_idx >= record_number) { rec_record_idx = 0; }
        }
    }
} 
```

#### 基于 ESP32 I2S API

```cpp line-num
#include "driver/i2s_pdm.h"
#include <M5Unified.h>
#include <M5GFX.h>

// Define microphone pins
#define PIN_CLK  GPIO_NUM_33
#define PIN_DATA GPIO_NUM_32

// Audio buffer and recording settings
static constexpr const size_t record_number     = 2;      // Total number of recording buffers
static constexpr const size_t record_length     = 320;      // Samples per buffer (should match display width)
static constexpr const size_t record_size       = record_number * record_length;  // Total number of samples
static constexpr const size_t record_samplerate = 16000;    // Sample rate in Hz

// Arrays used for clearing previous waveform lines
static int16_t prev_y[record_length];  // Y-coordinates of previous frame lines
static int16_t prev_h[record_length];  // Heights of previous frame lines

// Indices for recording/drawing buffers
static size_t rec_record_idx  = 2;     // Index to current input buffer
static size_t draw_record_idx = 0;     // Index to current drawing buffer

static int16_t *rec_data;              // Pointer to audio buffer
static int32_t w;                      // Display width

// I2S hardware handle for ESP32
i2s_chan_handle_t rx_handle = nullptr;
#define I2S_PORT  I2S_NUM_0

void setup(void) {
    // Initialize M5 hardware (screen, etc.)
    auto cfg = M5.config();
    M5.begin(cfg);

    // Initialize display parameters
    M5.Display.setRotation(1);
    w = M5.Display.width();
    M5.Display.startWrite();
    M5.Display.setTextDatum(top_center);
    M5.Display.setTextColor(TFT_WHITE);
    M5.Display.setFont(&fonts::FreeSansBoldOblique9pt7b);

    // Create I2S channel
    i2s_chan_config_t chan_cfg = I2S_CHANNEL_DEFAULT_CONFIG(I2S_PORT, I2S_ROLE_MASTER);
    ESP_ERROR_CHECK(i2s_new_channel(&chan_cfg, NULL, &rx_handle));

    // Configure PDM microphone parameters (clock, slots, gpio)
    i2s_pdm_rx_config_t pdm_rx_cfg = {
        .clk_cfg = I2S_PDM_RX_CLK_DEFAULT_CONFIG(record_samplerate),
        .slot_cfg = I2S_PDM_RX_SLOT_DEFAULT_CONFIG(I2S_DATA_BIT_WIDTH_16BIT, I2S_SLOT_MODE_MONO),
        .gpio_cfg = {
            .clk = PIN_CLK,
            .din = PIN_DATA,
            .invert_flags = {.clk_inv = false },
        }
    };
    ESP_ERROR_CHECK(i2s_channel_init_pdm_rx_mode(rx_handle, &pdm_rx_cfg));
    ESP_ERROR_CHECK(i2s_channel_enable(rx_handle));

    // Allocate memory for audio buffer and clear it
    rec_data = (typeof(rec_data))heap_caps_malloc(record_size * sizeof(int16_t), MALLOC_CAP_8BIT);
    memset(rec_data, 0, record_size * sizeof(int16_t));
    
    // Draw recording status indicators
    M5.Display.fillCircle(200, 28, 8, RED);
    M5.Display.drawString("REC", w / 2, 18);
}

// Read one frame of audio from microphone
bool mic_record(int16_t* buf, size_t samples) {
    size_t bytes_to_read = samples * sizeof(int16_t);
    size_t bytes_read    = 0;
    esp_err_t ret = i2s_channel_read(rx_handle, (void*)buf, bytes_to_read, &bytes_read, 50 / portTICK_PERIOD_MS);
    return (ret == ESP_OK && bytes_read == bytes_to_read);
}

void loop(void) {
    M5.update(); // Update button/status of M5
    static constexpr int shift = 6;  // Used for amplitude scaling (bit shift)
    auto data = &rec_data[rec_record_idx * record_length];  // Pointer to current record buffer
        
    // Record new audio data into buffer
    if (mic_record(data, record_length)) {
        data = &rec_data[draw_record_idx * record_length];  // Set pointer to buffer for drawing

        if (w > record_length - 1) {
            w = record_length - 1;
        }

        // Draw waveform on display buffer
        for (int32_t x = 0; x < w; ++x) {
            // Erase previous waveform line at position x
            M5.Display.writeFastVLine(x, prev_y[x], prev_h[x], TFT_BLACK);

            // Get two consecutive samples, scale down via shift
            int32_t y1 = (data[x] >> shift);
            int32_t y2 = (data[x + 1] >> shift);

            // Ensure y1<=y2 for drawing from low to high
            if (y1 > y2) {
                int32_t tmp = y1;
                y1          = y2;
                y2          = tmp;
            }

            // Calculate line's start vertical position and height
            int32_t y = ((M5.Display.height()) >> 1) + y1;  // Vertical origin is center
            int32_t h = ((M5.Display.height()) >> 1) + y2 + 1 - y;

            // Store for later clearing
            prev_y[x] = y;
            prev_h[x] = h;

            // Draw current waveform line in white
            M5.Display.writeFastVLine(x, prev_y[x], prev_h[x], TFT_WHITE);
        }
            
        // Commit display changes and redraw recording status
        M5.Display.display();
        M5.Display.fillCircle(200, 28, 8, RED);
        M5.Display.drawString("REC", w / 2, 18);

        // Move indices to next buffer, wrap around if necessary
        if (++draw_record_idx >= record_number) { draw_record_idx = 0; }
        if (++rec_record_idx >= record_number) { rec_record_idx = 0; }
    }
}
```

### 3.2 录音文件（wav 格式）存入 SD 卡

#### 基于 M5Unified Mic API

```cpp line-num
#include <SPI.h>
#include <SD.h>
#include <M5Unified.h>

// Pin definitions for SD card SPI communication
#define SD_SPI_CS_PIN     4     
#define SD_SPI_SCK_PIN    18    
#define SD_SPI_MISO_PIN   38    
#define SD_SPI_MOSI_PIN   23   

// Pin definitions for microphone I2S communication
#define MIC_I2S_PIN_CLK   33   
#define MIC_I2S_PIN_DATA  32   

// Audio recording configuration parameters
static constexpr size_t record_number     = 16;            // Number of recording buffers
static constexpr size_t record_length     = 512;           // Sample length per recording
static constexpr size_t record_samplerate = 16000;         // Recording sample rate in Hz
static constexpr uint8_t bitsPerSample    = 16;            // Bits per audio sample
static constexpr uint8_t numChannels      = 1;             // Number of audio channels (1 = mono)

// Global variables for recording
static int16_t *rec_data;               // Buffer to store recorded audio data
static bool isRecording = false;        // Flag indicating recording state
static size_t totalSamples = 0;         // Total number of recorded samples
unsigned long record_start_ms = 0;      // Timestamp when recording started
static int32_t w;                       // Display width

// Structure defining WAV file header format
struct WavHeader {
    char riff[4];         // "RIFF" identifier
    uint32_t fileSize;    // Total file size minus 8
    char wave[4];         // "WAVE" identifier
    char fmt[4];          // "fmt " identifier
    uint32_t fmtSize;     // Size of the format chunk
    uint16_t format;      // Audio format (1 = PCM)
    uint16_t channels;    // Number of audio channels
    uint32_t sampleRate;  // Audio sample rate
    uint32_t byteRate;    // Byte rate (sampleRate * channels * bitsPerSample/8)
    uint16_t blockAlign;  // Block alignment (channels * bitsPerSample/8)
    uint16_t bitsPerSample;// Bits per sample
    char data[4];         // "data" identifier
    uint32_t dataSize;    // Size of the audio data
};

/**
 * Writes the WAV file header to the specified file
 * @param file File object to write header to
 * @param pcmBytes Total size of PCM audio data in bytes
 */
void writeWavHeader(File &file, uint32_t pcmBytes) {
    WavHeader header;
    memcpy(header.riff, "RIFF", 4);
    header.fileSize      = 36 + pcmBytes;  // Calculate total file size
    memcpy(header.wave, "WAVE", 4);
    memcpy(header.fmt, "fmt ", 4);
    header.fmtSize       = 16;             // PCM format chunk size
    header.format        = 1;              // PCM format
    header.channels      = numChannels;
    header.sampleRate    = record_samplerate;
    header.byteRate      = record_samplerate * numChannels * (bitsPerSample / 8);
    header.blockAlign    = numChannels * (bitsPerSample / 8);
    header.bitsPerSample = bitsPerSample;
    memcpy(header.data, "data", 4);
    header.dataSize      = pcmBytes;
    file.seek(0);                          // Move to start of file
    file.write((const uint8_t*)&header, sizeof(WavHeader));  // Write header
}

File wavFile;  // File object for WAV recording

void setup(void) {
    auto cfg = M5.config();  // Get default M5 configuration
    M5.begin(cfg);           // Initialize M5Stack device
    M5.Display.setRotation(1);  // Set display rotation
    w = M5.Display.width();   // Get display width
    M5.Display.setTextDatum(top_center);  // Set text alignment
    M5.Display.setTextColor(TFT_BLACK, TFT_WHITE);  // Set text colors
    M5.Display.setFont(&fonts::FreeSansBoldOblique9pt7b);  // Set font

    // Initialize SD card
    SPI.begin(SD_SPI_SCK_PIN, SD_SPI_MISO_PIN, SD_SPI_MOSI_PIN, SD_SPI_CS_PIN);
    M5.Display.drawCenterString("SD Initializing...", w/2, 0);
    if (!SD.begin(SD_SPI_CS_PIN, SPI, 25000000)) {  // Attempt to initialize SD card
        M5.Display.drawCenterString("SD Init Error!", w/2, 50);
        while (1);  // Halt if SD card initialization fails
    } else {
        M5.Display.drawCenterString("SD Ready", w/2, 30);
    }

    // Configure microphone
    m5::mic_config_t mic_cfg = {
        .pin_data_in = MIC_I2S_PIN_DATA,
        .pin_bck = I2S_PIN_NO_CHANGE,
        .pin_mck = I2S_PIN_NO_CHANGE,
        .pin_ws = MIC_I2S_PIN_CLK,
        .sample_rate = record_samplerate,
        .dma_buf_len = 128,
        .dma_buf_count = 8,
        .i2s_port = I2S_NUM_0
    };
    M5.Mic.config(mic_cfg);  // Apply microphone configuration
    M5.Mic.begin();          // Initialize microphone
    if (M5.Mic.isEnabled()) { // Check if microphone initialized successfully
        M5.Display.drawCenterString("Mic Ready", w/2, 50);
    }
    M5.Mic.end();  // Temporary stop microphone
    delay(500);

    // Allocate memory for audio recording buffer
    rec_data = (int16_t*)heap_caps_malloc(
        record_length * sizeof(int16_t),
        MALLOC_CAP_8BIT | MALLOC_CAP_32BIT
    );
    if (!rec_data) {  // Check if memory allocation failed
        M5.Display.drawCenterString("Memory Alloc Error", w/2, 60);
        while (1);  // Halt if memory allocation fails
    }
    memset(rec_data, 0, record_length * sizeof(int16_t));  // Initialize buffer to zero
    
    M5.Display.clear(TFT_WHITE);
    // Display usage instructions
    M5.Display.drawCenterString("Mic Recording Example", w/2, 10);
    M5.Display.drawCenterString("Click Btn to Start/Stop", w/2, 45);
    M5.Display.drawCenterString("Start                                  Stop", w/2, 210);
}

void loop(void) {
    M5.update();  // Update M5Stack device state (buttons, sensors, etc.)

    //----------------- Start recording when Button A is pressed -----------------
    if (M5.BtnA.wasClicked() && !isRecording) {
        M5.Display.fillRect(0, 110, w, 100, TFT_WHITE);  // Clear previous status
        isRecording = true;
        totalSamples = 0;

        // Remove existing file if it exists
        if (SD.exists("/recording.wav")) {
            SD.remove("/recording.wav");
            M5.Display.drawCenterString("Old File Deleted", w/2, 80);
        }

        // Open new file for writing
        wavFile = SD.open("/recording.wav", FILE_WRITE);
        if (!wavFile) {  // Check if file opened successfully
            M5.Display.drawCenterString("Create WAV File Error!", w/2, 100);
            isRecording = false;
            return;
        }

        // Write temporary header (will be updated at end of recording)
        writeWavHeader(wavFile, 0);

        // Start microphone and begin recording
        if (M5.Mic.begin()) {
            record_start_ms = millis();
            M5.Display.drawCenterString("Recording...", w/2, 160);
        } else {
            M5.Display.drawCenterString("Mic Start Error!", w/2, 160);
            isRecording = false;
            wavFile.close();
        }
        delay(15);
    }

    //----------------- Stop recording when Button C is pressed -----------------
    if (M5.BtnC.wasClicked() && isRecording) {
        isRecording = false;
    }

    //----------------- Recording process (synchronous task) -----------------
    if (isRecording && M5.Mic.isEnabled() && wavFile) {
        // Submit recording block task
        bool submitted = M5.Mic.record(rec_data, record_length);
        if (submitted) {
            // Wait for recording to complete
            while (M5.Mic.isRecording()) {
                vTaskDelay(2);  // Short delay to reduce CPU usage
            }

            // Write recorded data to file
            size_t written = wavFile.write((const uint8_t*)rec_data, record_length * sizeof(int16_t));
            totalSamples += record_length;

            // Display recording status: time and file size
            float sec = ((float)totalSamples) / record_samplerate;
            uint32_t pcmBytes = totalSamples * sizeof(int16_t);
            char info[64];
            sprintf(info, "Time: %.2fs Size:%dKB", sec, pcmBytes/1024);
            M5.Display.drawCenterString(info, w/2, 110);
        } else {
            M5.Display.drawCenterString("Mic Record Fail!", w/2, 110);
            vTaskDelay(10);
        }
        // Short delay between recording blocks to reduce SD card stress
        vTaskDelay(5);
    }

    //------------------- Finalize recording and update file header ------------------
    if (!isRecording && wavFile) {
        M5.Mic.end();  // Stop microphone

        // Calculate total audio data size and update WAV header
        uint32_t pcmBytes = totalSamples * sizeof(int16_t);
        writeWavHeader(wavFile, pcmBytes);
        wavFile.close();
        wavFile = File();  // Clear file handle

        // Display recording summary
        float sec = ((float)totalSamples) / record_samplerate;
        char info[64];
        sprintf(info, "New WAV Saved: %.2fs, %dKB", sec, pcmBytes/1024);
        M5.Display.drawCenterString(info, w/2, 160);
        delay(35);
    }
}
```

#### 基于 ESP32 I2S API

```cpp line-num
#include <SPI.h>
#include <SD.h>
#include <driver/i2s_pdm.h>
#include <M5Unified.h>

// Pin definitions for SD card SPI communication
#define SD_SPI_CS_PIN     4     
#define SD_SPI_SCK_PIN    18    
#define SD_SPI_MISO_PIN   38    
#define SD_SPI_MOSI_PIN   23   

// Pin definitions for microphone I2S communication
#define MIC_I2S_PIN_CLK   GPIO_NUM_33   
#define MIC_I2S_PIN_DATA  GPIO_NUM_32   

// Audio recording configuration parameters
static constexpr size_t record_number     = 16;            // Number of recording buffers
static constexpr size_t record_length     = 512;           // Sample length per recording
static constexpr size_t record_samplerate = 16000;         // Recording sample rate in Hz
static constexpr uint8_t bitsPerSample    = 16;            // Bits per audio sample
static constexpr uint8_t numChannels      = 1;             // Number of audio channels (1 = mono)

// Global variables for recording
static int16_t *rec_data;               // Buffer to store recorded audio data
static bool isRecording = false;        // Flag indicating recording state
static size_t totalSamples = 0;         // Total number of recorded samples
unsigned long record_start_ms = 0;      // Timestamp when recording started
static int32_t w;                       // Display width

// I2S hardware handle for ESP32
i2s_chan_handle_t rx_handle = nullptr;
#define I2S_PORT  I2S_NUM_0

// Structure defining WAV file header format
struct WavHeader {
    char riff[4];         // "RIFF" identifier
    uint32_t fileSize;    // Total file size minus 8
    char wave[4];         // "WAVE" identifier
    char fmt[4];          // "fmt " identifier
    uint32_t fmtSize;     // Size of the format chunk
    uint16_t format;      // Audio format (1 = PCM)
    uint16_t channels;    // Number of audio channels
    uint32_t sampleRate;  // Audio sample rate
    uint32_t byteRate;    // Byte rate (sampleRate * channels * bitsPerSample/8)
    uint16_t blockAlign;  // Block alignment (channels * bitsPerSample/8)
    uint16_t bitsPerSample;// Bits per sample
    char data[4];         // "data" identifier
    uint32_t dataSize;    // Size of the audio data
};

/**
 * Writes the WAV file header to the specified file
 * @param file File object to write header to
 * @param pcmBytes Total size of PCM audio data in bytes
 */
void writeWavHeader(File &file, uint32_t pcmBytes) {
    WavHeader header;
    memcpy(header.riff, "RIFF", 4);
    header.fileSize      = 36 + pcmBytes;  // Calculate total file size
    memcpy(header.wave, "WAVE", 4);
    memcpy(header.fmt, "fmt ", 4);
    header.fmtSize       = 16;             // PCM format chunk size
    header.format        = 1;              // PCM format
    header.channels      = numChannels;
    header.sampleRate    = record_samplerate;
    header.byteRate      = record_samplerate * numChannels * (bitsPerSample / 8);
    header.blockAlign    = numChannels * (bitsPerSample / 8);
    header.bitsPerSample = bitsPerSample;
    memcpy(header.data, "data", 4);
    header.dataSize      = pcmBytes;
    file.seek(0);                          // Move to start of file
    file.write((const uint8_t*)&header, sizeof(WavHeader));  // Write header
}

File wavFile;  // File object for WAV recording

void setup(void) {
    auto cfg = M5.config();  // Get default M5 configuration
    M5.begin(cfg);           // Initialize M5Stack device
    M5.Display.setRotation(1);  // Set display rotation
    w = M5.Display.width();   // Get display width
    M5.Display.setTextDatum(top_center);  // Set text alignment
    M5.Display.setTextColor(TFT_BLACK, TFT_WHITE);  // Set text colors
    M5.Display.setFont(&fonts::FreeSansBoldOblique9pt7b);  // Set font

    // Initialize SD card
    SPI.begin(SD_SPI_SCK_PIN, SD_SPI_MISO_PIN, SD_SPI_MOSI_PIN, SD_SPI_CS_PIN);
    M5.Display.drawCenterString("SD Initializing...", w/2, 0);
    if (!SD.begin(SD_SPI_CS_PIN, SPI, 25000000)) {  // Attempt to initialize SD card
        M5.Display.drawCenterString("SD Init Error!", w/2, 50);
        while (1);  // Halt if SD card initialization fails
    } else {
        M5.Display.drawCenterString("SD Ready", w/2, 30);
    }

    // Create I2S channel
    i2s_chan_config_t chan_cfg = I2S_CHANNEL_DEFAULT_CONFIG(I2S_PORT, I2S_ROLE_MASTER);
    ESP_ERROR_CHECK(i2s_new_channel(&chan_cfg, NULL, &rx_handle));
    // Configure PDM microphone parameters (clock, slots, gpio)
    i2s_pdm_rx_config_t pdm_rx_cfg = {
        .clk_cfg = I2S_PDM_RX_CLK_DEFAULT_CONFIG(record_samplerate),
        .slot_cfg = I2S_PDM_RX_SLOT_DEFAULT_CONFIG(I2S_DATA_BIT_WIDTH_16BIT, I2S_SLOT_MODE_MONO),
        .gpio_cfg = {
            .clk = MIC_I2S_PIN_CLK,
            .din = MIC_I2S_PIN_DATA,
            .invert_flags = {.clk_inv = false },
        }
    };
    ESP_ERROR_CHECK(i2s_channel_init_pdm_rx_mode(rx_handle, &pdm_rx_cfg));
    ESP_ERROR_CHECK(i2s_channel_enable(rx_handle));

    // Allocate memory for audio recording buffer
    rec_data = (int16_t*)heap_caps_malloc(
        record_length * sizeof(int16_t),
        MALLOC_CAP_8BIT | MALLOC_CAP_32BIT
    );
    if (!rec_data) {  // Check if memory allocation failed
        M5.Display.drawCenterString("Memory Alloc Error", w/2, 60);
        while (1);  // Halt if memory allocation fails
    }
    memset(rec_data, 0, record_length * sizeof(int16_t));  // Initialize buffer to zero
    
    M5.Display.clear(TFT_WHITE);
    // Display usage instructions
    M5.Display.drawCenterString("Mic Recording Example", w/2, 10);
    M5.Display.drawCenterString("Start                                  Stop", w/2, 210);
}

// Read one frame of audio from microphone
bool mic_record(int16_t* buf, size_t samples) {
    size_t bytes_to_read = samples * sizeof(int16_t);
    size_t bytes_read    = 0;
    esp_err_t ret = i2s_channel_read(rx_handle, (void*)buf, bytes_to_read, &bytes_read, 50 / portTICK_PERIOD_MS);
    return (ret == ESP_OK && bytes_read == bytes_to_read);
}

void loop(void) {
    M5.update();  // Update M5Stack device state (buttons, sensors, etc.)

    //----------------- Start recording when Button A is pressed -----------------
    if (M5.BtnA.wasClicked() && !isRecording) {
        M5.Display.fillRect(0, 110, w, 100, TFT_WHITE);  // Clear previous status
        isRecording = true;
        totalSamples = 0;

        // Remove existing file if it exists
        if (SD.exists("/recording.wav")) {
            SD.remove("/recording.wav");
            M5.Display.drawCenterString("Old File Deleted", w/2, 80);
        }

        // Open new file for writing
        wavFile = SD.open("/recording.wav", FILE_WRITE);
        if (!wavFile) {  // Check if file opened successfully
            M5.Display.drawCenterString("Create WAV File Error!", w/2, 100);
            isRecording = false;
            return;
        }

        // Write temporary header (will be updated at end of recording)
        writeWavHeader(wavFile, 0);

        record_start_ms = millis();
        M5.Display.drawCenterString("Recording...", w/2, 160);
        delay(15);
    }

    //----------------- Stop recording when Button C is pressed -----------------
    if (M5.BtnC.wasClicked() && isRecording) {
        isRecording = false;
    }

    //----------------- Recording process (synchronous task) -----------------
    if (isRecording && wavFile) {
        // Submit recording block task
        bool submitted = mic_record(rec_data, record_length);
        if (submitted) {
            // Write recorded data to file
            size_t written = wavFile.write((const uint8_t*)rec_data, record_length * sizeof(int16_t));
            totalSamples += record_length;

            // Display recording status: time and file size
            float sec = ((float)totalSamples) / record_samplerate;
            uint32_t pcmBytes = totalSamples * sizeof(int16_t);
            char info[64];
            sprintf(info, "Time: %.2fs Size:%dKB", sec, pcmBytes/1024);
            M5.Display.drawCenterString(info, w/2, 110);
        } else {
            M5.Display.drawCenterString("Mic Record Fail!", w/2, 110);
            vTaskDelay(10);
        }
        // Short delay between recording blocks to reduce SD card stress
        vTaskDelay(5);
    }

    //------------------- Finalize recording and update file header ------------------
    if (!isRecording && wavFile) {
        M5.Mic.end();  // Stop microphone

        // Calculate total audio data size and update WAV header
        uint32_t pcmBytes = totalSamples * sizeof(int16_t);
        writeWavHeader(wavFile, pcmBytes);
        wavFile.close();
        wavFile = File();  // Clear file handle

        // Display recording summary
        float sec = ((float)totalSamples) / record_samplerate;
        char info[64];
        sprintf(info, "New WAV Saved: %.2fs, %dKB", sec, pcmBytes/1024);
        M5.Display.drawCenterString(info, w/2, 160);
        delay(35);
    }
}
```

## 4. 编译上传

- 根据需求复制粘贴上述例程代码到项目代码区，选中设备端口（详情请参考 [程序编译与烧录](/zh_CN/arduino/m5core2/program)），点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/734/Unit_Mini_PDM__arduino_example.png" width="70%">

## 5. 麦克风功能效果展示

- 1.基础使用

该例程效果为实时绘制音频波形，主控设备显示如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/734/Unit_Mini_PDM_basic_example.jpg" width="35%">

- 2.录音文件存入 SD 卡

按下按键 A 开始录音，再按下按键 C 停止录音，录制音频会保存为 WAV 文件，录制过程中主控屏幕会实时显示录音时间及 WAV 文件大小，成功完成一次录音并保存文件后，屏幕显示如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/734/Unit_Mini_PDM_wav_SD_example.jpg" width="35%">


