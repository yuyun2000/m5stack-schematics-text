# LLM-8850 Card Windows 环境配置

## Windows 版本要求

| Windows | 版本    |
| ------- | ------- |
| 10      | 22H2    |
| 11      | >= 23H2 |

- 按下`Win+R`，输入 `winver` ，可以查询当前的 Windows 版本信息。

- 仅支持 Windows 10 64 位及 Windows 11 64 位操作系统。

- 按下`Win+I` 打开设置 > 更新和安全 > Windows 更新，自动更新 Windows 版本，Windows 10 推荐用 **微软更新助手** 更新到 22H2 版本。

- 关闭系统睡眠功能：按下`Win+I` 打开设置 > 系统 > 电源和睡眠，将睡眠更改为`从不`。

## 环境准备

1. 建议关闭安全防护软件，避免被误杀。

2. 下载 Visual Studio 2022 运行时库 VC_redist.x64.exe，（[微软下载链接](https://aka.ms/vs/17/release/vc_redist.x64.exe)），并以管理员权限安装 VC_redist.x64.exe。

3. 关机断电后将设备接入主板，严禁带电操作。

4. 开机后按下`Win+R`, 输入 `devmgmt.msc` ，打开设备管理器，在其他设备中会出现未知的多媒体视频控制器，在属性中可确认设备 **VENDOR** 是 **1F4B**。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_001.png" width="60%" />

## 驱动安装

?> 注意 | 安装和卸载均需要管理员权限，需关闭系统睡眠功能。如果系统已经安装旧版本的 AXCL，请先卸载！

1. Windows 发布包 `axcl_win64_setup_Vx.x.x_yyyymmdd_NOxxxx.exe` 会自动安装驱动、动态链接库（含导入库）、可执行程序 (比如 axcl-smi.exe 等) 和 示例源码，使用管理员权限运行发布包，按向导提示完成安装。[点击下载](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/axcl_win64_setup_V3.6.4_20250822020158_NO4955.exe)

2. 点击安装。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_004.png" width="60%" />

3. 建议全选安装。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_005.png" width="60%" />

4. 注意选择安装路径，此目录包含可执行程序，卸载程序，头文件及动态库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_006.png" width="60%" />

5. 等待安装完成，并重启计算机。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_007.png" width="60%" />

6. 重启后，按下`Win+R`，输入 `devmgmt.msc` ，打开设备管理器，在系统设备中可发现 Axera NPU Accelerator Device 设备，如下图所示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_008.png" width="60%" />

7. 进入安装路径 `AXCL\axcl\out\axcl_win_x64\bin` 目录，在 **Windows Terminal** 中执行 `axcl-smi.exe`，显示如下：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_009.png" width="60%" />

## 驱动卸载

1. 进入安装路径 AXCL，运行 uninst.exe 执行卸载。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_010.png" width="60%" />

## 编译程序

?> 注意 | AXCL Windows SDK 可以使用 Visual Studio 2022/Visual Studio 2026 工具链进行编译，所需的环境依赖如下：<br>- [Visual Studio Community 2026](https://visualstudio.microsoft.com/vs/) ，参考[官方文档](https://learn.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=visualstudio)，必选的组件：使用 C++ 的桌面开发。<br>- CMake ，版本高于 3.20<br>- ninja，推荐 v1.31.1。将 ninja.exe 的路径配置到系统环境变量 Path。<br>- Python3 可以通过 conda 安装。

环境安装好如下：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_011.png" width="60%" />

进入安装路径 AXCL\axcl\scripts，执行 **build_win64.cmd** 编译。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_012.png" width="60%" />

编译成功如下：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_013.png" width="60%" />

进入编译输出目录，执行 **axcl_run_model.exe -m yolo11s.axmodel -r 10**，请替换为实际的模型文件路径。[预编译程序与模型下载](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/axcl-sample-windows.zip)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_014.png" width="60%" />

该目录包含第三方库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_015.png" width="60%" />

该目录包含 axcl 相关的头文件和动态库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_016.png" width="60%" />

以下为 [axcl-sample](https://github.com/AXERA-TECH/axcl-samples) 演示，[预编译程序及模型下载](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/axcl-sample-windows.zip)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_017.png" width="60%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/windows_018.png" width="60%" />

\#> 提示 | 编译 Demo 可参考 [仓库 Windows 分支](https://github.com/Abandon-ht/axcl-samples/tree/Windows)，建议使用 **vcpkg** 安装 **opencv4:x64-windows** 并在项目中配置。
