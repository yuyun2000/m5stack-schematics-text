# Arduino 库管理

#>Arduino库管理介绍：| **Arduino IDE**库管理用于管理程序所调用到的驱动库, M5Stack会为每一款产品都提供对应的驱动库, 你可以根据使用情况选择适合的安装方式。

## Arduino库管理安装

**1.打开 Arduino IDE 2.X, 在侧边栏选择`库管理`**, 根据你所使用的设备, 在`搜索框`中搜索相关库名称(如M5CoreS3，M5Core2，M5Unified), 并点击`安装`。


<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/arduino/arduino_lib_01.webp" width="70%">

#>库安装注意事项: | 在安装库时, 若提示需要安装其他库作为依赖, 需点击`安装所有`,否则可能会导致一些案例程序或驱动无法正常编译。

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/arduino/arduino_lib_02.webp" width="70%">


**3.等待安装完成即刻可使用**

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/arduino/arduino_lib_03.webp" width="70%">


## Git手动安装

使用git版本管理工具手动安装到库管理路径, 注：不同系统下的Arduino libraries路径可能会有所不同。 使用手动安装的方式并不会自动拉去驱动库对应的依赖选项，你可以查看驱动库中的`library.properties`文件获取依赖库信息，然后手动安装。

#>库管理路径 | **Windows**: `C:\Users\{username}\Documents\Arduino`<br/>**macOS**: `/Users/{username}/Documents/Arduino`<br/>**Linux**: `/home/{username}/Arduino`

```shell
git clone https://github.com/m5stack/M5Unified.git
```

## 案例程序

1.完成库安装后重启Arduino IDE并选择M5Stack相关的开发板选项，在`文件`->`Examples`->{library name}中可找到对应库所提供的案例程序，如下图所示。

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/arduino/arduino_lib_04.webp" width="70%">

## 相关链接

- [M5Stack Github](https://github.com/m5stack)
