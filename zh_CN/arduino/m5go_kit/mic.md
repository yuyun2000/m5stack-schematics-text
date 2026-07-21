# M5GO 底座模拟麦克风

M5GO 底座模拟麦克风使用案例程序。

## 案例程序

```cpp line-num
#include <SPI.h>       
#include <SD.h>       
#include <M5Unified.h> 

// Pin definitions
#define AIN_PIN 34            // Analog input pin for microphone signal
#define SD_SPI_CS_PIN     4   // Chip Select pin for SD card SPI communication
#define SD_SPI_SCK_PIN    18  // SPI Clock pin for SD card
#define SD_SPI_MISO_PIN   19  // SPI MISO (Master In Slave Out) pin for SD card
#define SD_SPI_MOSI_PIN   23  // SPI MOSI (Master Out Slave In) pin for SD card

// Recording parameters
constexpr size_t record_length     = 512;    // Number of samples per recording loop
constexpr size_t record_samplerate = 12000;  // Sampling frequency in Hertz (Hz)
constexpr uint8_t bitsPerSample    = 16;     // Bit depth per audio sample
constexpr uint8_t numChannels      = 1;      // Number of audio channels (1 = mono)

static int16_t *rec_data;                  // Buffer to store current batch of samples
static volatile bool isRecording = false;  // Flag indicating recording state
static size_t totalSamples = 0;            // Total number of samples recorded
unsigned long record_start_ms = 0;         // Timestamp when recording started
static int32_t w;                          // Display width (for UI positioning)

// Structure defining the WAV file header format
struct WavHeader {
    char riff[4];         // "RIFF" identifier (Resource Interchange File Format)
    uint32_t fileSize;    // Total file size minus 8 bytes (size of RIFF chunk)
    char wave[4];         // "WAVE" identifier (specifies WAV format)
    char fmt[4];          // "fmt " identifier (format subchunk)
    uint32_t fmtSize;     // Size of the format subchunk (16 for PCM)
    uint16_t format;      // Audio format (1 = PCM, linear quantization)
    uint16_t channels;    // Number of audio channels
    uint32_t sampleRate;  // Sampling frequency in Hz
    uint32_t byteRate;    // Byte rate (sampleRate * channels * bitsPerSample/8)
    uint16_t blockAlign;  // Block alignment (channels * bitsPerSample/8)
    uint16_t bitsPerSample;// Number of bits per sample
    char data[4];         // "data" identifier (data subchunk)
    uint32_t dataSize;    // Size of the audio data in bytes
};

/**
 * Writes the WAV file header to a file
 * @param file Reference to the open WAV file
 * @param pcmBytes Total size of the audio data in bytes
 */
void writeWavHeader(File &file, uint32_t pcmBytes) {
    WavHeader header;
    memcpy(header.riff, "RIFF", 4);               // Set RIFF identifier
    header.fileSize      = 36 + pcmBytes;          // Calculate total file size
    memcpy(header.wave, "WAVE", 4);               // Set WAVE identifier
    memcpy(header.fmt, "fmt ", 4);                // Set format subchunk identifier
    header.fmtSize       = 16;                     // PCM format subchunk size
    header.format        = 1;                      // PCM format
    header.channels      = numChannels;            // Set number of channels
    header.sampleRate    = record_samplerate;      // Set sampling rate
    header.byteRate      = record_samplerate * numChannels * (bitsPerSample / 8);  // Calculate byte rate
    header.blockAlign    = numChannels * (bitsPerSample / 8);  // Calculate block alignment
    header.bitsPerSample = bitsPerSample;          // Set bit depth
    memcpy(header.data, "data", 4);                // Set data subchunk identifier
    header.dataSize      = pcmBytes;               // Set audio data size
    file.seek(0);                                  // Move to start of file
    file.write((const uint8_t*)&header, sizeof(WavHeader));  // Write header data
}

File wavFile;  // File object for the WAV recording

void setup(void) {
    auto cfg = M5.config(); 
    M5.begin(cfg);       
    M5.Display.setRotation(1);  
    w = M5.Display.width();  
    M5.Display.setTextDatum(top_center);  
    M5.Display.setTextColor(TFT_BLACK, TFT_WHITE); 
    M5.Display.setFont(&fonts::FreeSansBoldOblique9pt7b); 

    SPI.begin(SD_SPI_SCK_PIN, SD_SPI_MISO_PIN, SD_SPI_MOSI_PIN, SD_SPI_CS_PIN);
    M5.Display.drawCenterString("SD Initializing...", w/2, 0);

    if (!SD.begin(SD_SPI_CS_PIN, SPI, 25000000)) {
        M5.Display.drawCenterString("SD Init Error!", w/2, 50); 
        while (1);  // Halt execution if SD card fails
    } else {
        M5.Display.drawCenterString("SD Ready", w/2, 30);
    }

    // Allocate memory buffer for audio samples with specific memory capabilities
    rec_data = (int16_t*)heap_caps_malloc(record_length * sizeof(int16_t), MALLOC_CAP_8BIT | MALLOC_CAP_32BIT);
    if (!rec_data) {  // Check if memory allocation failed
        M5.Display.drawCenterString("Memory Alloc Error", w/2, 60);  // Show error message
        while (1);  // Halt execution if memory allocation fails
    }
    memset(rec_data, 0, record_length * sizeof(int16_t));  // Initialize buffer to zero

    M5.Display.clear(TFT_WHITE);
    M5.Display.drawCenterString("ADC Mic Recording Example", w/2, 10);
    M5.Display.drawCenterString("A:Start   C:Stop", w/2, 45);
    M5.Display.drawCenterString("Start                                  Stop", w/2, 210);
}

uint32_t previous_sample_us = 0;  // Timestamp of previous sample (for rate control)
// Calculate microseconds between samples to maintain target sampling rate
const uint32_t sampling_interval_us = 1000000UL / record_samplerate;

void loop(void) {
    M5.update();

    // Start recording when Button A is pressed (and not already recording)
    if (M5.BtnA.wasClicked() && !isRecording) {
        M5.Display.fillRect(0, 110, w, 100, TFT_WHITE);
        isRecording = true;                             
        totalSamples = 0;                            

        // Delete existing recording file if it exists
        if (SD.exists("/recording.wav")) {
            SD.remove("/recording.wav");
            M5.Display.drawCenterString("Old File Deleted", w/2, 80);
        }

        // Open new WAV file for writing
        wavFile = SD.open("/recording.wav", FILE_WRITE);
        if (!wavFile) {  // Check if file creation failed
            M5.Display.drawCenterString("Create WAV File Error!", w/2, 100);
            isRecording = false;  
            return;
        }

        writeWavHeader(wavFile, 0);  // Write initial header (will be updated later)
        record_start_ms = millis();  // Record start time
        M5.Display.drawCenterString("Recording...", w/2, 160);  
        delay(15);  // Short delay to debounce button
    }

    // Stop recording when Button C is pressed (and currently recording)
    if (M5.BtnC.wasClicked() && isRecording) {
        isRecording = false;  
    }

    // Main recording process - runs while recording is active
    if (isRecording && wavFile) {
        uint32_t now = micros();  // Get current time in microseconds
        int32_t sum = 0;          // Accumulator for sample analysis (not used in output)

        // Collect record_length samples
        for (size_t i = 0; i < record_length; ++i) {
            // Wait until correct time for next sample (maintains sampling rate)
            while (micros() - now < i * sampling_interval_us) {}
            
            // Read analog value from microphone pin
            int adval = analogRead(AIN_PIN);
            
            // Convert 12-bit ADC value (0-4095) to 16-bit signed sample:
            // - Subtract 2048 to center around 0 (DC offset removal)
            // - Shift left by 4 bits to scale 12-bit range to 16-bit range
            rec_data[i] = (int16_t)((adval - 2048) << 4);
            sum += rec_data[i];  // Accumulate sample (for potential future use)
        }

        // Write collected samples to SD card
        size_t written = wavFile.write((const uint8_t*)rec_data, record_length * sizeof(int16_t));
        totalSamples += record_length;  // Update total sample count

        // Calculate and display recording status
        float sec = ((float)totalSamples) / record_samplerate;  // Calculate recording time in seconds
        uint32_t pcmBytes = totalSamples * sizeof(int16_t);     // Calculate total data size
        char info[64];
        sprintf(info, "Time: %.2fs Size:%dKB", sec, pcmBytes/1024); 
        M5.Display.drawCenterString(info, w/2, 110); 
    }

    // Finalize recording when stopped
    if (!isRecording && wavFile) {
        uint32_t pcmBytes = totalSamples * sizeof(int16_t);  // Calculate total data size
        writeWavHeader(wavFile, pcmBytes);  // Update header with final data size
        wavFile.close();               
        wavFile = File();               

        // Display final recording information
        float sec = ((float)totalSamples) / record_samplerate;  // Calculate total recording time
        char info[64];
        sprintf(info, "New WAV Saved: %.2fs, %dKB", sec, pcmBytes/1024);
        M5.Display.drawCenterString(info, w/2, 160); 
        delay(35);  // Short delay for stability
    }
}
```

上方例程下载成功后，按下 A 键开始录音，按下 C 键停止录音。录音文件会保存到 SD 卡根目录下，文件名为 `recording.wav`。录制过程如下：

<video style="width:40vw;max-width:30%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/661/m5go_Arduino_mic.mp4" type="video/mp4"></video>

