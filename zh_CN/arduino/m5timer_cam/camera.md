# TimerCAM Camera 摄像头

## 案例程序

```cpp line-num
#include "M5TimerCAM.h"

void setup() {
    TimerCAM.begin();

    if (!TimerCAM.Camera.begin()) {
        Serial.println("Camera Init Fail");
        return;
    }
    Serial.println("Camera Init Success");

    TimerCAM.Camera.sensor->set_pixformat(TimerCAM.Camera.sensor,
                                          PIXFORMAT_JPEG);
    TimerCAM.Camera.sensor->set_framesize(TimerCAM.Camera.sensor,
                                          FRAMESIZE_QVGA);

    TimerCAM.Camera.sensor->set_vflip(TimerCAM.Camera.sensor, 1);
    TimerCAM.Camera.sensor->set_hmirror(TimerCAM.Camera.sensor, 0);
}

void loop() {
    if (TimerCAM.Camera.get()) {
        Serial.printf("pic size: %d\n", TimerCAM.Camera.fb->len);
        TimerCAM.Camera.free();
    }
}
```


## begin


函数原型:

```cpp
bool begin();
```

功能说明:

- 初始化摄像头

传入参数:

- null

返回值:

- bool:
  - true: 初始化成功
  - false: 初始化失败


## get

函数原型:

```cpp
bool get();
```

功能说明:

- 获取一帧图像数据

传入参数:

- null

返回值:

- bool:
  - true: 图像获取成功
  - false: 图像获取失败


## free

函数原型:

```cpp
bool free();
```

功能说明:

- 释放当前图像数据内存

传入参数:

- null

返回值:

- bool:
  - true: 图像资源释放成功
  - false: 没有资源需要释放

