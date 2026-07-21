# Chain 系列设备 Bus 通信使用教程

## 1. Chain Bus 总线说明

M5Stack Chain Bus 是一种采用 UART 通信接口的链式级联拓扑结构，由一个主控（Master）和多个节点（Node）构成。主控作为链路起点，其余节点按顺序依次串联在同一条总线上。系统工作时，各节点通过逐级转发数据包的方式与主控进行通信。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/chain_bus_connect_01.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/chain_bus_connect_02.jpg" width="70%">

### 主控（Master）

主控设备通过 **UART 接口** 与 Chain Bus 进行通信。 主控可以拓展多条 Chain Bus 总线，数量取决于其可用的 UART 接口数量，从而实现多总线、多节点的灵活扩展。

### 节点（Node）

Chain 节点通常集成 **STM32G031G8U6** 作为核心控制器，使用 **Chain 系列专用的 UART 串口级联通信协议** 进行数据交互。 节点板载 **2 个 HY2.0-4P 扩展接口**，分别用于： **数据输入（IN）** 与 **数据输出（OUT）**。连接时需要注意连接方向，主控连接至节点的数据输入（IN），然后由节点的数据输出（OUT）继续向后连接下一级的输入。

- Chain 系列主控:
  - [Chain DualKey](https://shop.m5stack.com/products/chain-dual-key-with-esp32-s3)
- Chain 系列连接器:
  - [Chain Bridge](https://shop.m5stack.com/products/chain-bridge-connector-for-chain-series)
  - [Chain Return](https://shop.m5stack.com/products/chain-return-connector-for-chain-series)
- Chain 系列输入设备:
  - [Chain Joystick](https://shop.m5stack.com/products/chain-joystick-stm32g031)
  - [Chain Key](https://shop.m5stack.com/products/chain-mechanical-key-button-stm32g031)
  - [Chain Angle](https://shop.m5stack.com/products/chain-angle-stm32g031)
  - [Chain Encoder](https://shop.m5stack.com/products/chain-encoder-stm32g031)
  - [Chain ToF](https://shop.m5stack.com/products/chain-tof-vl53l0)

推荐使用 Chain DualKey 或是 Atom 系列主控搭配 Atomic ToChain Base 作为 Chain Bus 主控。

## 2. 驱动库

M5Chain Arduino 驱动库对 Chain Bus 协议进行了封装，能够方便主控对总线中的设备状态进行读取，控制和枚举扫描。

- 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide) 完成 IDE 安装，并根据实际使用的开发板安装对应的板管理与需要的驱动库。
- 使用到的驱动库：
  - [M5Chain](https://github.com/m5stack/M5Chain)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_library.png" width="70%">

### 示例程序

以主控 Chain DualKey 举例，拓展连接 Chain 系列输入设备。

\#> 编译要求 | M5Stack 板管理版本 >= 3.2.4<br>M5Chain 库版本 >= 1.0.0

```cpp line-num
#include "M5Chain.h"

#define RXD_PIN GPIO_NUM_5  // 47 for the other side of Chain DualKey
#define TXD_PIN GPIO_NUM_6  // 48 for the other side of Chain DualKey

Chain M5Chain;

chain_status_t chain_status;
device_list_t *device_list = NULL;
uint16_t device_count = 0;
uint8_t opr_status = 0;
uint8_t rgb_test[] = { 255, 255, 255 };

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("======================");
  Serial.println("M5Stack Chain Bus Test");
  M5Chain.begin(&Serial2, 115200, RXD_PIN, TXD_PIN);
}

void loop() {
  Serial.println();
  delay(2000);

  if (!M5Chain.isDeviceConnected()) {
    Serial.println("No device connected");
    return;
  }

  chain_status = M5Chain.getDeviceNum(&device_count);
  if (chain_status == CHAIN_OK) {
    device_list = (device_list_t *)malloc(sizeof(device_list_t));
    device_list->count = device_count;
    device_list->devices = (device_info_t *)malloc(sizeof(device_info_t) * device_count);
  } else {
    Serial.printf("Get device count failed, chain status: %d\r\n", chain_status);
    return;
  }

  if (!M5Chain.getDeviceList(device_list)) {
    Serial.println("Get device list failed");
    return;
  }

  if (device_list == NULL) {
    Serial.println("Device list is NULL");
    return;
  }

  Serial.printf("Device count: %d\r\n", device_list->count);

  for (int i = 0; i < device_list->count; i++) {
    Serial.print("- Device ID: ");
    Serial.print(device_list->devices[i].id);
    Serial.print(", type: ");
    switch (device_list->devices[i].device_type) {
      case CHAIN_UNKNOWN_TYPE_CODE:
        Serial.println("Unknown");
        break;
      case CHAIN_ENCODER_TYPE_CODE:
        Serial.println("Chain Encoder");
        break;
      case CHAIN_ANGLE_TYPE_CODE:
        Serial.println("Chain Angle");
        break;
      case CHAIN_KEY_TYPE_CODE:
        Serial.println("Chain Key");
        break;
      case CHAIN_JOYSTICK_TYPE_CODE:
        Serial.println("Chain Joystick");
        break;
      case CHAIN_TOF_TYPE_CODE:
        Serial.println("Chain ToF");
        break;
        // case CHAIN_UART_TYPE_CODE:
        //   Serial.println("Chain UART");
        //   break;
        // case CHAIN_SWITCH_TYPE_CODE:
        //   Serial.println("Chain Switch");
        //   break;
        // case CHAIN_PEDAL_TYPE_CODE:
        //   Serial.println("Chain Pedal");
        //   break;
        // case CHAIN_PIR_TYPE_CODE:
        //   Serial.println("Chain PIR");
        //   break;
        // case CHAIN_MIC_TYPE_CODE:
        //   Serial.println("Chain Mic");
        //   break;
        // case CHAIN_BUZZER_TYPE_CODE:
        //   Serial.println("Chain Buzzer");
        //   break;
    }

    // Device ID, LED brightness (0-100), operation status pointer
    chain_status = M5Chain.setRGBLight(device_list->devices[i].id, 100, &opr_status);
    if (chain_status == CHAIN_OK && opr_status) {
      Serial.println("  Set RGB brightness succeeded");
    } else {
      Serial.printf("  Set RGB brightness failed, chain status: %d, operation status: %d\r\n", chain_status, opr_status);
    }

    rgb_test[0] = random(0, 256);  // [0, 255]
    rgb_test[1] = random(0, 256);  // [0, 255]
    rgb_test[2] = random(0, 256);  // [0, 255]

    // Device ID, LED start index, LED count, RGB color, size of RGB color, operation status pointer
    chain_status = M5Chain.setRGBValue(device_list->devices[i].id, 0, 1, rgb_test, 3, &opr_status);
    if (chain_status == CHAIN_OK && opr_status) {
      Serial.println("  Set RGB color succeeded");
    } else {
      Serial.printf("  Set RGB color failed, chain status: %d, operation status: %d\r\n", chain_status, opr_status);
    }
  }
}
```

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

将以上程序编译并上传至设备，程序会每 2 秒检测一次 Chain DualKey 的 G5、G6 引脚一侧 Chain Bus 上的设备连接情况，打印到串口，并随机改变 RGB 灯的颜色。你可以在程序运行时热插拔多种、多个 Chain 系列设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_bus.png" width="90%">

若需要同时使用 Chain DualKey 两边的接口，需要在程序中创建两个 Chain 类型的实例，分别管理各自对应接口上的设备。

```cpp line-num
#include "M5Chain.h"

//Left side of Chain DualKey
#define RXD_PIN_L GPIO_NUM_5
#define TXD_PIN_L GPIO_NUM_6

//Right side of Chain DualKey
#define RXD_PIN_R GPIO_NUM_47
#define TXD_PIN_R GPIO_NUM_48

Chain M5ChainLeft;
Chain M5ChainRight;

void setup() {
  M5ChainLeft.begin(&Serial1, 115200, RXD_PIN_L, TXD_PIN_L);
  M5ChainRight.begin(&Serial2, 115200, RXD_PIN_R, TXD_PIN_R);
}

void loop(){

}

```

## 3.API

### 操作结果状态码

```cpp
typedef enum {
    CHAIN_OK                  = 0x00,  // Operation successful
    CHAIN_PARAMETER_ERROR     = 0x01,  // Parameter error
    CHAIN_RETURN_PACKET_ERROR = 0x02,  // Return packet error
    CHAIN_BUSY                = 0x04,  // Device is busy
    CHAIN_TIMEOUT             = 0x05   // Operation timeout
} chain_status_t;
```

### begin

**函数原型：**

```cpp
void begin(HardwareSerial *serial, unsigned long baud = 115200, int8_t rxPin = -1, int8_t txPin = -1);
```

**功能说明：**

- 初始化 Chain Bus 通信总线

**传入参数：**

- HardwareSerial \*serial
  - 用于串行通信的硬件串口对象的指针
- unsigned long baud
  - 串行通信的波特率，默认 115200
- int8_t rxPin
  - 信号接收引脚的 GPIO 编号
- int8_t txPin
  - 信号发送引脚的 GPIO 编号

**返回值：**

- null

### isDeviceConnected

**函数原型：**

```cpp
bool isDeviceConnected();
```

**功能说明：**

- 检查 Chain Bus 上是否有设备连接

**传入参数：**

- null

**返回值：**

- bool
  - true：有设备连接
  - false：无设备连接

### getDeviceNum

**函数原型：**

```cpp
chain_status_t getDeviceNum(uint16_t *deviceNum);
```

**功能说明：**

- 获取 Chain Bus 上连接的设备数量

**传入参数：**

- uint16_t \*deviceNum
  - 指针，用于存储设备数量的值

**返回值：**

- chain_status_t
  - 操作结果状态码

### getDeviceList

**函数原型：**

```cpp
bool getDeviceList(device_list_t *list);
```

**功能说明：**

- 获取 Chain Bus 上连接的设备列表

**传入参数：**

- device_list_t \*list
  - 指针，用于存储设备列表。其结构体中包含设备数量、各设备具体信息数组

```cpp
typedef struct {
    uint16_t count;          // Number of devices
    device_info_t *devices;  // Array of devices
} device_list_t;
```

**返回值：**

- bool
  - true：获取成功
  - false：获取失败

### 设备具体信息

通过 getDeviceList 函数获取的设备列表，类型为 device_list_t，其结构体中包含设备数量、各设备具体信息数组。而设备具体信息的类型为 device_info_t，其结构体中包含设备 ID、设备类型。

```cpp
typedef struct {
    uint16_t id;                      // Device ID
    chain_device_type_t device_type;  // Device type
} device_info_t;
```

- 设备 ID

在一条 Chain Bus 上连接的各个设备都有唯一的设备 ID，用于单独识别和控制。每个设备的 ID 值由系统自动分配，按**从主控向外**的连接顺序**从 1 开始**递增：

```cpp
Main Controller -> 1 -> 2 -> 3 -> ...
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/chain_bus_device_id_01.jpg" width="70%">

- 设备类型

设备类型枚举值如下：

```cpp
typedef enum {
    CHAIN_UNKNOWN_TYPE_CODE  = 0x0000,  // Unknown device type
    CHAIN_ENCODER_TYPE_CODE  = 0x0001,  // Chain Encoder
    CHAIN_ANGLE_TYPE_CODE    = 0x0002,  // Chain Angle
    CHAIN_KEY_TYPE_CODE      = 0x0003,  // Chain Key
    CHAIN_JOYSTICK_TYPE_CODE = 0x0004,  // Chain Joystick
    CHAIN_TOF_TYPE_CODE      = 0x0005,  // Chain ToF
    CHAIN_UART_TYPE_CODE     = 0x0006,  // Chain UART
    CHAIN_SWITCH_TYPE_CODE   = 0x0007,  // Chain Switch
    CHAIN_PEDAL_TYPE_CODE    = 0x0008,  // Chain Pedal
    CHAIN_PIR_TYPE_CODE      = 0x0009,  // Chain PIR
    CHAIN_MIC_TYPE_CODE      = 0x000A,  // Chain Microphone
    CHAIN_BUZZER_TYPE_CODE   = 0x000B,  // Chain Buzzer
} chain_device_type_t;
```

### setRGBLight

**函数原型：**

```cpp
chain_status_t setRGBLight(uint16_t id, uint8_t rgbBrightness, uint8_t *operationStatus);
```

**功能说明：**

- 设定设备上 RGB LED 灯的亮度

**传入参数：**

- uint16_t id
  - 设备 ID
- uint8_t rgbBrightness
  - 亮度值（0 - 100）
- uint8_t \*operationStatus
  - 指针，用于存储操作结果（0 为操作失败，1 为操作成功）

**返回值：**

- chain_status_t
  - 操作结果状态码

### setRGBValue

**函数原型：**

```cpp
chain_status_t setRGBValue(uint16_t id, uint8_t index, uint8_t num, uint8_t *rgb, uint8_t size, uint8_t *operationStatus);
```

**功能说明：**

- 设定设备上 RGB LED 灯的颜色

**传入参数：**

- uint16_t id
  - 设备 ID
- uint8_t index
  - 要控制的 LED 灯编号，从 0 开始
- uint8_t num
  - 要控制的 LED 灯数量
- uint8_t \*rgb
  - 指针，指向 RGB 颜色数组，格式为 \[R0, G0, B0, R1, G1, B1, ...]
- uint8_t size
  - RGB 颜色数组的长度，需要等于灯数量的 3 倍
- uint8_t \*operationStatus
  - 指针，用于存储操作结果（0 为操作失败，1 为操作成功）

**返回值：**

- chain_status_t
  - 操作结果状态码

## 4. 通信机制

Chain Bus 支持多设备热插拔、链式通信功能，得益于背后的 Chain Bus 通信机制，包含设备发现、ID 分配、命令传递等部分。

### 设备 ID

在一条 Chain Bus 上连接的各个设备具有唯一的设备 ID，用于单独识别和控制。每个设备的 ID 值由系统自动分配，从主控向外，按照连接顺序从 1 开始递增。

### 设备类型

设备类型 `chain_device_type_t` 用于区分不同类型的设备，如 `CHAIN_ENCODER_TYPE_CODE`、`CHAIN_KEY_TYPE_CODE` 等。

### 数据传输与响应

主控向 Chain Bus 发送的数据包从主控串口发出，进入设备链路。与主控相连的第一个设备会检查数据包中的目标设备 ID。如果 `ID == 1`，说明该设备就是目标设备，直接处理此数据包；如果 `ID > 1`，该设备会执行 `ID = ID - 1`，然后将数据包转发给链路中的下一个设备。以此类推，直到数据包被传递到对应的目标设备，触发 `ID == 1`，由该设备完成数据处理。

数据包处理完成后，设备会向链路反方向发送响应数据包。每个设备在转发响应数据包之前会执行 `ID = ID + 1`，最终将响应数据包发回主控，主控便可得知响应数据包来自哪个设备。

### 尾部设备

每个 Chain 系列设备在上电初始化时，默认将自身视为链路的 **尾部设备**。设备首次接收到来自链路中下一个设备的完整数据包后，会将自身状态更新为 **非尾部设备**。

### 心跳包

心跳包是 Chain Bus 链路中一种特殊的数据包，用于设备之间的定期通信。链路中的设备每秒钟主动向下一个设备发送心跳包，下一个设备收到心跳包会立即将其原样返回作为应答。

如果一个设备连续三次发送心跳包均未收到下一个设备的应答，则认为下一个设备已离线，该设备会将自身状态更新为 **尾部设备**。

主控也会向链路发送心跳包。如果收到有效应答，表明链路中有设备连接；如果未收到应答，则表明链路中无设备连接。

### 枚举包

枚举包是 Chain Bus 链路中一种特殊的数据包，用于更新链路连接结构。一个新设备进入链路时，会自动发送 3 次枚举请求（每次时间间隔为 180 ms），以通知主控链路发生了变化。主控收到这样的枚举数据包，会重新发起设备枚举，以更新链路连接结构和设备列表。

反之当链路中某处断开，断开处上一个设备发送的心跳包收不到应答，会将自身状态从 **非尾部设备** 更新为 **尾部设备**，并主动发送 3 次枚举请求，以通知主控链路发生了变化。

对于主控发起的设备枚举指令，链路的尾部设备负责终止枚举流程，将结果数据包传回主控，完成整个链路的枚举操作。

## 5. 参考链接

- [M5Chain Lib - GitHub](https://github.com/m5stack/M5Chain)
