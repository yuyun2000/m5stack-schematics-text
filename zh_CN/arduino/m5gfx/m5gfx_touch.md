# 屏幕触摸

- [触摸信息](#触摸信息)
  - [getTouch](#gettouch)
  - [getTouchRaw](#gettouchraw)
  - [convertRawXY](#convertrawxy)

- [校准屏幕](#校准屏幕)
  - [calibrateTouch](#calibratetouch)
  - [setTouchCalibrate](#settouchcalibrate)

## 触摸信息

### getTouch

**函数原型：**

```cpp
uint_fast8_t getTouch(touch_point_t *tp, uint_fast8_t count = 1)
```

**功能说明：** 

- 获取触摸面板的触摸信息

**传入参数:**

- tp：指向触摸点的指针
- count：触摸点数量，默认为 1

**返回值：** 

- uint_fast8_t：触摸点数量

### getTouchRaw

**函数原型：**

```cpp
uint_fast8_t getTouchRaw(touch_point_t *tp, uint_fast8_t count = 1)
``` 

**功能说明：**

- 获取触摸面板的原始触摸信息

**传入参数:**

- tp：指向触摸点的指针
- count：触摸点数量，默认为 1
 
**返回值：**

- uint_fast8_t：触摸点数量

#>说明：|1.此函数与 [getTouch](#gettouch) 的区别在于，getTouchRaw 返回的触摸点数据不经过处理，包含原始的触摸坐标和压力值，适用于需要获取更精确的触摸数据的场景。  
2.两函数使用方法可见[此例程](/zh_CN/arduino/m5tab5/touch#2.多点触摸检测)

### convertRawXY

**函数原型：**

```cpp
void convertRawXY(touch_point_t *tp, uint_fast8_t count = 1)
```

**功能说明：**

- 转化通过[getTouchRaw](#gettouchraw)获取的坐标

**传入参数：**

- tp：触摸点结构体指针 （关于[touch_point_t](/zh_CN/arduino/m5gfx/m5gfx_appendix#struct%20touch_point_t)）
- count：触摸点个数，默认为1个

**返回值：**

- null

## 校准屏幕

### calibrateTouch

**函数原型：** 

```cpp
void calibrateTouch(uint16_t* parameters, const T &color_fg, const T &color_bg, uint8_t size = 10)
```

**功能说明**
 
- 校准触摸板，传递一个指针给第一个参数，以获得一个校准值，你可以将这个值记录在 flash 中等等，并在下次启动时使用[setTouchCalibrate](#settouchcalibrate)来省略手工校准。

**传入参数：**

- parameters：校准值
- color_fg：前景色
- color_bg：背景色
- size：触摸点大小

**返回值:**

- null

### setTouchCalibrate

**函数原型：**

```cpp
void setTouchCalibrate(uint16_t *parameters)
```

**功能说明：**

- 使用 [calibrateTouch](#calibratetouch) 得到的校准值来进行校准


**传入参数:**

- parameters：指向包含校准值的 uint16_t 数组的指针，数组长度为 6。

**返回值：**

- null

#> 说明 | 此程序只有在第一次下载复位后会出现屏幕校准步骤，其他情况下只会显示第一次校准后存储的校准值。

**案例程序:**

```cpp line-num
#include <Arduino.h>
#include <Preferences.h>
#include <M5GFX.h>

M5GFX display;
uint16_t w;
uint16_t h;
const char* NAMESPACE = "m5_data";
const char* DATA_KEY = "user_data";
struct Calibration {
  bool calibration_flag = false;
  uint16_t touch_point[8];//4 point, each has (X,Y)
};


Calibration Cal;

void setup() {
    display.begin();

    display.setRotation(3);
    if(display.isEPD())
    {
        display.setColorDepth(8);//The ink screen product supports a maximum bit depth of 8 bits.
        display.setEpdMode(epd_fastest);
    }
    else
    {
        display.setColorDepth(16);
    }
    
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBoldOblique12pt7b);
    display.setTextColor(TFT_BLACK);
    display.setTextSize(1);
    display.setCursor(0, 0);
    
    // Initiate preferences
    Preferences preferences;
    
    // Open the namespace (create it if it does not exist)
    preferences.begin(NAMESPACE, false); // false -- read-write mode
    size_t readBytes = preferences.getBytes(DATA_KEY, &Cal, sizeof(Calibration));
    // Check whether the data has been successfully read
    if (readBytes == sizeof(Calibration)) {
        if(Cal.calibration_flag){
            display.setTouchCalibrate(Cal.touch_point);
            for (int i=0; i<8; i++) {
                display.printf("%d  ", Cal.touch_point[i]);
            }
            // display.setTextDatum(top_center);
            display.println("Read calibration setting data successfully!");
        }    
    } 
    else {
        // Initiate default
        display.calibrateTouch(Cal.touch_point, BLACK, YELLOW);
        display.clear();
        display.println("Set calibration data successfully, show as belows:\n");

        for (int i=0; i<8; i++) {
            display.printf("%d  ", Cal.touch_point[i]);
        }
        display.println();
        Cal.calibration_flag = true;

        // Save calibration data
        size_t writtenBytes = preferences.putBytes(DATA_KEY, &Cal, sizeof(Calibration));
        
        if (writtenBytes == sizeof(Calibration)) {
            display.println("\nCalibration Data Save Successfully");
        } else {
            display.println("\nCalibration Data Save Failed");
        }
        
        // Close namespace
        preferences.end();
    }
}

void loop() {
}
```