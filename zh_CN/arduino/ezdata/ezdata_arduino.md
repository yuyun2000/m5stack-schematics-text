# EzData 1.0 - Arduino

## 1. 功能说明

EzData 是 M5Stack 提供的一个 IoT 云端数据储存服务，不同的设备之间可以通过`唯一Token`，向储存队列中插入或提取数据，实现数据共享。

<img src="https://static-cdn.m5stack.com/resource/docs/static/image/iotservice/ezdata/ezdata_01.webp" width="60%">

### 1.1 介绍

- Token：访问和读写数据的唯一字段
- Topic：Token 下存储**队列**形式数据的 key，同一 Token 下允许保存的 Topic 数量: Topic + List Topic ≤ 100
  - 每个 Topic 允许插入数据 `≤1000` 条
  - 通过 `setData` 插入新数据到队列中，使用堆栈的方式 (先入后出)，每次插入数据到队列的首位。
  - 通过 `getData` 取出位于队列首位的数据。 原数据在序列中删除。
- List Topic：
  - Token 下存储**列表**形式数据的 key，同一 Token 下允许保存的 Topic 数量: Topic + List Topic ≤ 100
  - 通过 `addToList` 插入新数据到列表中，每次插入新数据，追加到列表未尾。
  - 通过 `getData` 读取指定索引或范围的列表数据。 返回数据为一个列表

### 1.2 获取 Token

打开 [UiFlow Web IDE 1.0 版本](https://flow.m5stack.com/)，在 Blockly 列表中点击 `EzData` 选项，可查看当前浏览器的 Token。为保证 Token 的唯一性，请使用固定的浏览器，且不要开启无痕模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/EzData_01.png" width="70%">

## 2. 案例程序

该案例程序使用 CoreS3 设备实现 Ezdata 数据上传与获取测试，程序编译前需安装以下依赖库，并将 Token 及 Wi-Fi 信息填写到代码中。

- [M5Unified](https://github.com/m5stack/M5Unified)
- [M5GFX](https://github.com/m5stack/M5GFX)
- [M5_EzData](https://github.com/m5stack/M5_EzData)

```cpp
#include "M5Unified.h"
#include "M5_EzData.h"

const char* ssid     = "ssid";
const char* password = "password";
const char* token    = "token";

void setup()
{
    M5.begin();
    M5.Display.println("Wi-Fi connecting...");
    if (setupWifi(ssid, password)) {
        M5.Display.println("Wi-Fi connected!");
    } else {
        M5.Display.println("Wi-Fi connect failed");
    }
}

void loop()
{
    // Save the data 100 to the top of the testData topic queue.
    // 保存数据 100 至 testData 队列首位
    if (setData(token, "testData", 100)) {
        M5.Display.println("Success sending data to the testData");
    } else {
        M5.Display.println("Fail");
    }
    delay(5000);

    // Save 3 data in sequence to the first place of testList.
    // 依次保存3个数据至 testList 首位
    for (int i = 0; i < 3; i++) {
        if (addToList(token, "testList", i)) {
            M5.Display.printf("Success sending %d to the list\n", i);
        } else {
            M5.Display.println("Fail");
        }
        delay(100);
    }
    delay(5000);

    // Get a piece of data from a topic and store the value in result.
    // 从一个 topic 中获取一个数据,并将值存储在 result
    int result = 0;
    if (getData(token, "testData", result)) {
        M5.Display.printf("Success get data %d\n", result);
    } else {
        M5.Display.print("Fail to get data\n");
    }
    delay(5000);

    // Get a set of data from a list and store the values in the Array array.
    // 从一个 list 中获取一组数据,并将值存储在 Array 数组中
    int Array[3] = {0};
    if (getData(token, "testList", Array, 0, 3)) {
        M5.Display.print("Success get list\n");
        for (int i = 0; i < 3; i++) {
            M5.Display.printf("Array[%d]=%d,", i, Array[i]);
        }
        M5.Display.println("");
    } else {
        M5.Display.println("Fail to get data");
    }
    delay(5000);

    // Remove data
    // 移除数据
    if (removeData(token, "testData"))
        M5.Display.printf("Success remove data\n");
    else
        M5.Display.println("Fail to remove data");

    if (removeData(token, "testList"))
        M5.Display.printf("Success remove data from the list\n");
    else
        M5.Display.println("Fail to remove data");
    delay(5000);
    M5.Display.fillScreen(BLACK);
    M5.Display.setCursor(0, 0);
}
```

## 3. 控制面板

如果需要查看或者分享数据，可以通过以下 URL 地址，并传入 Token 参数访问 EzData 控制面板页面。

```bash
# https://ezdata.m5stack.com/debugger/?token=dCtdfg3u5id72J8xxxxxxxxxxxxxxx
https://ezdata.m5stack.com/debugger/?token={token}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/ezdata1_arduino_demo_01.jpg" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/ezdata1_arduino_demo_02.png" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/ezdata1_arduino_demo_03.png" width="70%" />

## 4. API

- [M5_EzData Arduino 驱动库](https://github.com/m5stack/M5_EzData)

### 4.1 setData

**函数原型:**

```cpp
int setData(const char *token, const char *topic, int val);
```

**功能说明:**

- 保存数据 val 至指定 topic 队列首位

**传入参数:**

- const char \*token
  - Ezdata token
- const char \*topic
  - Ezdata 的数据 topic
- int val
  - 写入的数值

**返回值:**

- int:
  - 1: 发送成功
  - 0: 发送失败

### 4.2 getData

**函数原型:**

```cpp
int getData(const char *token, const char *topic, int &result);
```

**功能说明:**

- 从指定的 topic 队列首位获取一个数据，并存储在 result 中

**传入参数:**

- const char \*token
  - Ezdata token
- const char \*topic
  - Ezdata 的数据 topic
- int \&result
  - 存储数据的变量引用

**返回值:**

- int:
  - 1: 读取成功
  - 0: 读取失败

### 4.3 addToList

**函数原型:**

```cpp
int addToList(const char *token, const char *list, int val);
```

**功能说明:**

- 保存数据至指定数据列表首位

**传入参数:**

- const char \*token
  - Ezdata token
- const char \*list
  - Ezdata 的数据 list topic
- int val
  - 写入的数值

**返回值:**

- int:
  - 1: 发送成功
  - 0: 发送失败

### 4.4 getData (list)

**函数原型:**

```cpp
int *getData(const char *token, const char *list, int *Array, int offset, int count);
```

**功能说明:**

- 从指定的数据列表中获取一组数据。使用列表储存的优点是，支持指定数据索引偏移且可一次获取多个数据，返回值为一个 list。

**传入参数:**

- const char \*token
  - Ezdata token
- const char \*list
  - Ezdata 的数据 list topic
- int \*Array
  - 存储列表数据的变量指针
- int offset
  - 相对于数据列表首位的偏移
- int count
  - 读取数据个数

**返回值:**

- int \*:
  - int \*Array: 成功读取，返回数据列表指针
  - 0: 读取失败

### 4.5 removeData

**函数原型:**

```cpp
int removeData(const char *token, const char *field);
```

**功能说明:**

- 删除 topic 或 list topic，并清空队列数据

**传入参数:**

- const char \*token
  - Ezdata token
- const char \*field
  - Ezdata topic / list topic

**返回值:**

- int:
  - 1: 删除成功
  - 0: 删除失败
