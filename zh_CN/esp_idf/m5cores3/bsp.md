# CoreS3 ESP-IDF BSP 使用教程

本教程将介绍如何在 ESP-IDF 开发环境中集成 CoreS3 板级支持包（BSP），以便快速初始化和管理板载外设驱动，提升开发效率。

## 1.准备工作

1. 环境配置： 本教程基于 Ubuntu 操作系统搭建 ESP-IDF 开发环境，其他平台的编译环境搭建方式，具体请参考[ESP-IDF - ESP32-S3上手教程](https://docs.espressif.com/projects/esp-idf/en/v5.4.1/esp32s3/get-started/linux-macos-setup.html)。

#>ESP-IDF 版本| 本教程推荐使用 ESP-IDF 版本`v5.4.1`

2. 使用 git 版本管理工具拉取 esp-idf 项目，切换至指定分支并执行脚本安装相关工具链。

?>注意事项|`. ./export.sh`指令的`"."`与脚本之间有一个空格，该指令等同于`source ./export.sh`

```bash
git clone -b v5.4.1 --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh
. ./export.sh
```

3. 后续教程使用到的 idf.py 指令均依赖 ESP-IDF，运行指令前需要在项目工程路径下调用 ESP-IDF 中`. ./export.sh`用于激活相关的环境变量。详细说明请参考[ESP-IDF - ESP32-S3上手教程](https://docs.espressif.com/projects/esp-idf/en/v5.4.1/esp32s3/get-started/linux-macos-setup.html)。

## 2.项目创建

1. 打开终端并进入工作目录，创建项目文件夹`cores3_projects`。切换路径进入文件夹后，调用 esp-idf 项目中`export.sh`用于激活相关的环境变量。以下指令适用于项目文件夹 cores3_projects 与 esp-idf 处于同级目录，其他路径则需根据实际情况修改指令。执行以下`idf.py create-project`指令创建空白项目模板，演示的项目名为`my_project`。

```bash
mkdir cores3_projects
cd cores3_projects
. ../esp-idf/export.sh
idf.py create-project my_project
```

2. 切换路径进入项目工程，并使用 Espressif Component Registry 组件管理工具指令添加 [M5Stack CoreS3 BSP](https://components.espressif.com/components/espressif/m5stack_core_s3/versions/3.0.0)。

```bash
cd my_project
idf.py add-dependency "espressif/m5stack_core_s3^3.0.0"
```

3. 设置编译目标芯片平台

```bash
idf.py set-target esp32s3
```

4. 由于 API 兼容性问题，程序编译前需参考下方指令进入配置菜单`Component config`->`Audio Codec Device Configuration`，关闭向后兼容`I2C Driver`选项。

```bash
idf.py menuconfig
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_bsp_audio_codec_i2c_config_01.jpg" width="70%">

## 3.案例程序

1. 打开空白模板的程序入口文件，并将下方案例程序内容复制到文件中。

```bash
vim main/my_project.c 
```

```cpp line-num
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"

#include "lv_demos.h"
#include "bsp/esp-bsp.h"

static char *TAG = "app_main";

#define LOG_MEM_INFO (0)

void app_main(void) {
    /* Initialize display and LVGL */
    bsp_display_start();
    /* Set display brightness to 100% */
    bsp_display_backlight_on();

    ESP_LOGI(TAG, "Display LVGL demo");
    bsp_display_lock(0);
    lv_demo_widgets(); /* A widgets example */
    // lv_demo_music(); /* A modern, smartphone-like music player demo. */
    // lv_demo_stress();       /* A stress test for LVGL. */
    // lv_demo_benchmark();    /* A demo to measure the performance of LVGL or
    // to compare different settings. */
    bsp_display_unlock();
}
```

2. 该案例程序演示如何驱动屏幕显示 LGVL 组件案例，您还可以切换不同的案例注释来编译不同的显示案例。使用对应的案例组件前，请使用`idf.py menuconfig`进入配置菜单`Component config`->`LVGL Configuration`->`Demos`，启用对应的 LGVL 案例。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_bsp_lvgl_config_01.jpg" width="70%">

## 4.程序编译与烧录

1. 长按设备复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

2. 执行以下指令进行程序编译与烧录。

```bash
idf.py flash
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_bsp_lvgl_example_01.jpg" width="70%">
