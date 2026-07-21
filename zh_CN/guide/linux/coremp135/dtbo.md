# CoreMP135 Overlay Device Trees支持

#>DTBO介绍: | 在 Linux 中，Overlay Device Trees(DTBO)是一种特殊的设备树，用于在不修改主设备树(DTB)的情况下动态添加或修改硬件配置。这对于某些需要运行时硬件配置更改的应用非常有用，如根据不同的外设需求调整系统。DTBO 的支持可分为两个阶段，第一个阶段是 uboot 引导阶段，uboot 直接将 dtbo 覆盖到设备树中，在启动内核后，这便是一个已经调整过的设备，内核对这种调整是没有感知的，属于不可更改的调整。第二个阶段就是 linux 启动后的调整，linux 启动后在 dtbo 的帮助下可以动态的调整设备树，从而控制固定设备的开启与关闭，和相关运行参数的调整。

?>版本要求: | 请使用镜像`M5_CoreMP135_debian12_20240515`, `M5_CoreMP135_buildroot_20240515`及以上版本(开启`CONFIG_OF_OVERLAY`支持)

## 1.设备树插件格式

1.设备树插件是在设备树基础上增加的内容，与设备树语法完全相同, 你可以将之前编写的设备树节点复制到设备树插件里中。设备树插件拥有相对固定的格式，甚至可以认为它只是把设备节点加了一个"壳"编译后内核能够动态加载它。 格式如下，具体节点省略。

```dts
/dts-v1/;
/plugin/;

 / {
        fragment@0 {
            target-path = "/";
            __overlay__ {
                /*在此添加要插入的节点*/
                .......
            };
        };

        fragment@1 {
            target = <&XXXXX>;
            __overlay__ {
                /*在此添加要插入的节点*/
                .......
            };
        };
    .......
 };
```


- 第1行： 用于指定dts的版本。
- 第2行： 表示允许使用未定义的引用并记录它们，设备树插件中可以引用主设备树中的节点，而这些“引用的节点”对于设备树插件来说就是未定义的，所以设备树插件应该加上“/plugin/”。
- 第6行： 指定设备树插件的加载位置，默认我们加载到根节点下，既target-path ="/",或者使用target = <&XXXXX>，增加节点或者属性到某个节点下。
- 第7-8行： 我们要插入的设备及节点或者要引用(追加)的设备树节点放在__overlay__ {…}内，你可以增加、修改或者覆盖主设备树的节点。

另外一种设备树插件格式：这种插件的书写方式和正式的 dts 格式相同，唯一的区别是在第二行声明了这个是以插件的形式应用。

```dts
/dts-v1/;
/plugin/;

&{/} {
    /*此处在根节点"/"下,添加要插入的节点或者属性*/
};

&XXXXX {
    /*此处在节点"XXXXX"下,添加要插入的节点或者属性*/
};
```

## 2.设备树插件案例

1.以CoreMP135设备为例, 编写一个插入led设备节点的设备树插件`led-overlay.dts`

```dts
// file: led-overlay.dts
/dts-v1/;
/plugin/;

/ {
    fragment@0 {
        target-path = "/";
        __overlay__ {
            leds {
                compatible = "gpio-leds";

                led-blue {
                    function = "heartbeat"; // LED_FUNCTION_HEARTBEAT
                    color = <3>;            // LED_COLOR_ID_BLUE
                    gpios = <&gpioc 13 1>;  // &gpioc 13 GPIO_ACTIVE_LOW
                    linux,default-trigger = "heartbeat";
                    default-state = "off";
                };
            };
        };
    };
};
```

2.使用dtc工具编译设备树

```bash
dtc -I dts -O dtb -o led-overlay.dtbo led-overlay.dts

ls
led-overlay.dtbo  led-overlay.dts
```

## 3.DTBO在uboot中的使用

1.在CoreMP135根文件系统的`/boot`目录下存放的引导文件，其中`/boot/extlinux/extlinux.conf`是`uboot`的开机引导脚本。通过该脚本，可以设置开机叠加的设备树。

```bash
label stm32mp135f-core135-buildroot
kernel /boot/zImage
devicetree /boot/stm32mp135f-core135.dtb
append root=/dev/mmcblk0p5 rw panic=5 quiet rootwait
```

- label : 启动标签，可以有多个启动标签，uboot 在开机时可以根据启动标签进行选择。
- kernel ：要启动的内核文件
- devicetree ： 要启动内核设备树
- append ： 添加的 kernel 启动参数
- 更多参数请参考 uboot 的 pxe 菜单。

2.我们需要关注的是，`fdtoverlays`参数，该参数用于定义开启覆盖的`dtbo`设备树文件。具体操作如下：

```bash
# 编译出 dtbo 设备树文件, 并通过传输到CoreMP135中(注: 默认root用户可能没有开启ssh权限请修改配置或创建新的用户进行传输)
scp led-overlay.dtbo root@192.168.2.52:/root
```

```bash
# 将设备树文件放在 /boot 引导目录下。
cp /root/led-overlay.dtbo /boot
```

3.在引导文件`/boot/extlinux/extlinux.conf `中设置`dtbo`参数

```bash
label stm32mp135f-core135-buildroot
kernel /boot/zImage
devicetree /boot/stm32mp135f-core135.dtb
fdtoverlays /boot/led-overlay.dtbo
append root=/dev/mmcblk0p5 rw panic=5 quiet rootwait
```

4.重启设备，我们就能在 /sys/class/leds 目录下看到我们添加的 led 设备了。

## 4.DTBO在linux中的使用

1.linux在运行时也能够对设备树进行动态的调整, 该方式依赖于`dtbocfg.ko`模块的支持, 相关注意事项如下。

#>使用dtbocfg模块: | 1.确保kernel 编译时开启`CONFIG_OF_OVERLAY`的支持。<br/>2.下载并交叉编译[https://github.com/m5stack/dtbocfg](https://github.com/m5stack/dtbocfg)内核项目，生成 `dtbocfg.ko`内核模块。<br/>3.系统中加载`dtbocfg.ko`


2.交叉编译模块前需完成内核编译工作, 模块通过外部编译方式生成ko文件。(请将$PROJECT_PATH替换为实际的工程路径)

```bash
git clone https://github.com/m5stack/dtbocfg.git
cd dtbocfg

make ARCH=arm KERNEL_SRC=$PROJECT_PATH/Core135_buildroot/output/build/linux-custom CROSS_COMPILE=$PROJECT_PATH/Core135_buildroot/output/host/bin/arm-buildroot-linux-gnueabihf- -j16
```

3.将生成的`dtbocfg.ko`放置到`/lib/modules/$version/kernel/drivers/`路径下, 运行`depmod -a`更新驱动依赖关系, 然后通过`modprobe`指令加载模块。

```bash
depmod -a
# 加载dtbocfg模块
modprobe dtbocfg
```

4.将先前编译好的`led-overlay.dtbo`复制到系统中, 按照以下流程进行导入。

```bash
# 挂载 configs 文件系统，如果系统没有自动挂载该目录，则需要进行手动挂载。
# mount -t configfs none /sys/kernel/config

# 创建加载目录
mkdir /sys/kernel/config/device-tree/overlays/leds

# 创建完成后目录中将会自动生成两个文件dtbo, status
ls /sys/kernel/config/device-tree/overlays/leds
dtbo  status

# 填充 dtbo
cat led-overlay.dtbo > /sys/kernel/config/device-tree/overlays/leds/dtbo

# 启动 dtbo
echo 1 > /sys/kernel/config/device-tree/overlays/leds/status
```

完成上述步骤后, 当前设备树插件就已经成功导入生效了。 

5.通过示波器查看PC13引脚状态或通过面包板搭建一个简单的LED电路查看实现效果。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/dtbo_led_01.gif" width="50%">

