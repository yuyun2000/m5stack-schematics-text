# M5Unified PlatformIO使用指南  

本文将详细介绍如何通过Visual Studio Code 及其扩展PlatformIO来构建基于M5Unified的开发环境。  

## 1. 环境准备  

### 下载安装VSCode  

访问[VSCode官网下载页面](https://code.visualstudio.com/download), 并选择对应操作系统的安装包进行下载和安装。 

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_01.webp" width="70%">

### 安装PlatformIO插件  

启动VSCode并安装嵌入式开发环境插件[PlatformIO](https://platformio.org/)  

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_02.webp" width="100%">

操作步骤：  
- 点击左侧活动栏的"Extensions"图标  
- 搜索框中输入"PlatformIO"  
- 在搜索结果中选择"PlatformIO IDE"  
- 点击安装按钮  

## 2. 项目创建与配置  

### 创建新项目  

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_03.webp" width="100%">

操作步骤：  
- 点击左侧活动栏的"PlatformIO"图标  
- 选择"Create New Project"  
- 在PIOHome选项卡中点击"New Project"  

###  项目配置向导  

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_04.webp" width="50%">

配置项说明：  
- Name：输入项目名称  
- Board：选择目标开发板（如M5Stack Core2、M5Stack AtomS3等）  
- Framework：选择Arduino框架  

完成配置后点击"Finish"  

## 3. 添加M5Unified库  

### 添加库到项目  

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_05.webp" width="100%">

操作步骤：  
1. 点击左侧活动栏的"PlatformIO"图标  
2. 选择"Libraries"  
3. 搜索框中输入"M5Unified"  
4. 在搜索结果中选择"M5Unified"  

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_06.webp" width="100%">

5. 找到M5Stack官方提供的M5Unified库（作者lovyan03）  
6. 点击"Add to Project"  

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_07.webp" width="50%">

7. 选择之前创建的项目  
8. 点击"Add"按钮  

安装成功后会出现"Congrats"提示对话框，表示库已成功添加到项目中。

## 4. 程序编译与烧录  

### 编译烧录程序  

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_09.webp" width="100%">

操作步骤：  
1. 点击左侧活动栏的"Explorer"图标  
2. 打开"src/main.cpp"文件，并粘贴下方案例程序

```cpp line-num
#include <M5Unified.h> // Make the M5Unified library available to your program.

// global variables (define variables to be used throughout the program)
uint32_t count;


// setup function is executed only once at startup.
// This function mainly describes the initialization process.
void setup() {

  auto cfg = M5.config(); // Assign a structure for initializing M5Stack
  // If config is to be set, set it here
  // Example.
  // cfg.external_spk = true;

  M5.begin(cfg);                        // initialize M5 device

  M5.Display.setTextSize(3);            // change text size
  M5.Display.print("Hello World!!!") ;  // display Hello World! and one line is displayed on the screen
  Serial.println("Hello World!!!") ;    // display Hello World! and one line on the serial monitor
  count = 0;                            // initialize count

}

// loop function is executed repeatedly for as long as it is running.
// loop function acquires values from sensors, rewrites the screen, etc.
void loop() {

  M5.Display.setCursor(0, 20);             // set character drawing coordinates (cursor position)
  M5.Display.printf("COUNT: %d\n", count); // display count on screen
  Serial.printf("COUNT: %d\n", count);  // display count serially
  count++;                              // increase count by 1
  delay(1000);                          // wait 1 second(1,000msec)

}
```

<img src="https://static-cdn.m5stack.com/resource/docs/quick_start/m5unified/intro_vscode_10.webp" width="100%">

编译烧录：  
- 点击(1)仅编译  
- 点击(2)编译并烧录到设备  
- 成功时终端会显示(3)"Success"提示  
