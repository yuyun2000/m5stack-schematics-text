# Unit CamS3-5MP Arduino 示例程序编译与烧录

## 1.准备工作

1. Arduino IDE 安装：参考 [Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。

2. 板管理安装：打开 Arduino IDE，点击菜单栏中的`文件`>`首选项`（Windows）或`Arduino IDE`>`首选项`（macOS）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/Arduino_IDE_1.png" width="70%">

3. 在`添加板管理 URLs`框中输入：

``` shell
https://espressif.github.io/arduino-esp32/package_esp32_index.json
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/Arduino_IDE_2.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/Arduino_IDE_3.png" width="70%">

- 点击侧边栏中的板管理，输入`esp32`，安装最新的`esp32 by Espressif Systems`最新版本。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/Arduino_IDE_4.png" width="70%">

4. 硬件连接：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/d361e7c8cd2fdbd0aecd8cbe4d959ae.png" width="70%">

5. 检测硬件版本：

Unit CamS3-5MP 有两个硬件版本，我们需要先跑一段代码检测硬件版本。

``` cpp line-num
#include <Wire.h>

#define SIOD_GPIO_NUM 17
#define SIOC_GPIO_NUM 41

void setup() {
  Serial.begin(115200);
  Wire.begin(SIOD_GPIO_NUM, SIOC_GPIO_NUM);

  Serial.println("\n####################");
  Serial.println("Start checking Unit CamS3-5MP hardware version");
}

void loop() {
  byte version = readRegister(0x1f, 0x0200);

  if (version == 0x01) {
    Serial.println("New Version (0x01)");
  } else if (version == 0xFF) {
    Serial.println("Old Version (0xFF)");
  } else {
    Serial.print("Unknown Version: 0x");
    Serial.println(version, HEX);
  }

  delay(1000);
}

byte readRegister(byte slaveAddr, unsigned int regAddr) {
  Wire.beginTransmission(slaveAddr);

  Wire.write((byte)(regAddr >> 8));
  Wire.write((byte)(regAddr & 0xFF));

  Wire.endTransmission(false);

  Wire.requestFrom(slaveAddr, (byte)1);

  if (Wire.available()) {
    return Wire.read();
  }

  return 0x00;
}
```

将以上代码粘贴进 Arduino IDE，选择`esp32`板管理中的`M5UnitCAMS3`开发板，点击左上角的上传按钮。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/Check_Version_1.png" width="70%">

#> | 若上传失败，请在上电前用配备的公对公面包线短接排母的 G0 和 GND 引脚，使设备进入下载模式。

上传完成后打开串口监视器，查看程序的输出。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/Check_Version_2.png" width="70%">

若输出`New Version (0x01)`则为新版本硬件，输出`Old Version (0xFF)`则为旧版本硬件。

## 2.旧版硬件兼容处理

#> 新版硬件请跳过此步骤。

在侧边栏的板管理中，安装`esp32 by Espressif Systems`的`3.1.0`版本。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/Old_Compatibility_1.png" width="70%">

下载 [libespressif__esp32-camera.zip](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/libespressif__esp32-camera.zip)，解压得到`libespressif__esp32-camera.a`文件，放入以下路径并替换掉原有的同名文件：

- Windows
``` shell
C:\Users\[Username]\AppData\Local\Arduino15\packages\esp32\tools\esp32-arduino-libs\idf-release_v5.3-083aad99-v2\esp32s3\lib\
```

- macOS
``` shell
/Users/[Username]/Library/Arduino15/packages/esp32/tools/esp32-arduino-libs/idf-release_v5.3-083aad99-v2/esp32s3/lib/
```

- Linux
``` shell
/home/[Username]/.arduino15/packages/esp32/tools/esp32-arduino-libs/idf-release_v5.3-083aad99-v2/esp32s3/lib/
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/Old_Compatibility_2.png" width="50%">

## 3.获取示例程序

下载 [CameraWebServer.zip](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/CameraWebServer.zip)，解压并打开其中的`CameraWebServer.ino`，填入 Unit CamS3-5MP 要连接的 Wi-Fi 名称及密码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/CameraWebServer_1.png" width="70%">

## 4.程序编译和烧录

在 Arduino IDE 的菜单栏 - 工具中修改以下配置：

- 选择开发板：Tools -> Board -> **esp32** -> M5UnitCAMS3
- 配置 USB CDC：Tools -> USB CDC On Boot -> Enabled
- 配置 PSRAM：Tools -> PSRAM -> OPI PSRAM

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/CameraWebServer_2.png" width="70%">

选择设备对应的端口，编译并上传程序后，串口监视器中将会输出一个 IP 地址。如果没有输出，可以重新插拔数据线、检查串口监视器波特率是否为 115200。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/CameraWebServer_3.png" width="70%">

## 5.程序运行结果

在与 Unit CamS3-5MP 同一局域网的设备上，用浏览器打开程序输出的 IP 地址（包含前面的 `http://`），点击 Get Still 即可获取一张图片，点击 Start Stream 即可查看实时图像流（视频）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/CameraWebServer_4.png" width="70%">
