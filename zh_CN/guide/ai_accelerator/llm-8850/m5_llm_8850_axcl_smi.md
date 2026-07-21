# AXCL-SMI

## 概述

AXCL-SMI (System Management Interface) 工具用于设备信息收集，对设备进行配置等功能，支持收集如下设备信息：

- 硬件设备型号
- 固件版本号
- 驱动版本号
- 设备利用率
- 内存使用情况
- 设备芯片结温
- 其他信息

## 使用说明

### 快速使用

在正确安装 AXCL 驱动包后，AXCL-SMI 即安装成功，直接执行`axcl-smi`显示内容如下：

```bash
+------------------------------------------------------------------------------------------------+
| AXCL-SMI  V3.6.4_20250805020145                                  Driver  V3.6.4_20250805020145 |
+-----------------------------------------+--------------+---------------------------------------+
| Card  Name                     Firmware | Bus-Id       |                          Memory-Usage |
| Fan   Temp                Pwr:Usage/Cap | CPU      NPU |                             CMM-Usage |
|=========================================+==============+=======================================|
|    0  AX650N                     V3.6.4 | 0001:01:00.0 |                149 MiB /      945 MiB |
|   --   41C                      -- / -- | 1%        0% |                 18 MiB /     7040 MiB |
+-----------------------------------------+--------------+---------------------------------------+

+------------------------------------------------------------------------------------------------+
| Processes:                                                                                     |
| Card      PID  Process Name                                                   NPU Memory Usage |
|================================================================================================|
```

**字段说明**

| 字段             | 说明                                 | 字段         | 说明                 |
| ---------------- | ------------------------------------ | ------------ | -------------------- |
| Card             | 设备索引编号，注意不是 PCIe 的设备号 | Bus-Id       | 设备 Bus ID          |
| Name             | 设备名称                             | CPU          | CPU 平均利用率       |
| Fan              | 风扇转速比（未支持）                 | NPU          | NPU 平均利用率       |
| Temp             | 设备芯片结温 Tj                      | Memory-Usage | 系统内存： 使用/总量 |
| Firmware         | 设备固件版本号                       | CMM-Usage    | 媒体内存： 使用/总量 |
| Pwr: Usage/Cap   | 功耗（未支持）                       |              |                      |
|                  |                                      |              |                      |
| PID              | 主控进程 PID                         |              |                      |
| Process Name     | 主控进程名称                         |              |                      |
| NPU Memory Usage | 设备 NPU 已使用的 CMM 内存           |              |                      |

### 帮助 (-h) 和版本 (-v)

`axcl-smi -h`  查询帮助信息

```bash
m5stack@raspberrypi5:~ $ axcl-smi -h
usage: axcl-smi [<command> [<args>]] [--device] [--version] [--help]

axcl-smi System Management Interface V3.6.3_20250722020142

Commands
    info                                    Show device information
        --temp                                  Show SoC temperature
        --mem                                   Show memory usage
        --cmm                                   Show CMM usage
        --cpu                                   Show CPU usage
        --npu                                   Show NPU usage
    proc                                    cat device proc
        --vdec                                  cat /proc/ax_proc/vdec
        --venc                                  cat /proc/ax_proc/venc
        --jenc                                  cat /proc/ax_proc/jenc
        --ivps                                  cat /proc/ax_proc/ivps
        --rgn                                   cat /proc/ax_proc/rgn
        --ive                                   cat /proc/ax_proc/ive
        --pool                                  cat /proc/ax_proc/pool
        --link                                  cat /proc/ax_proc/link_table
        --cmm                                   cat /proc/ax_proc/mem_cmm_info
    set                                     Set
        -f[MHz], --freq=[MHz]                   Set CPU frequency in MHz. One of: 1200000, 1400000, 1700000
    log                                     Dump logs from device
        -t[mask], --type=[mask]                 Specifies which logs to dump by a combination (bitwise OR) value of blow:
                                                  -1: all (default) 0x01: daemon 0x02: worker 0x10: syslog 0x20: kernel
        -o[path], --output=[path]               Specifies the path to save dump logs (default: ./)
    sh                                      Execute a shell command
        cmd                                     Shell command
        args...                                 Shell command arguments
    reboot                                  reboot device
-d, --device                            Card index [0, connected cards number - 1]
-v, --version                           Show axcl-smi version
-h, --help                              Show this help menu

```

`axcl-smi -v` 查询 AXCL-SMI 工具的版本

```bash
m5stack@raspberrypi5:~ $ axcl-smi -v
AXCL-SMI V3.6.3_20250722020142 BUILD: Jul 22 2025 02:30:24
```

### 选项

#### 设备号 (-d, --device)

```bash
-d, --device                             Card index [0, connected cards number - 1]
```

`[-d, --device]` 指定设备号索引，范围：[0, 连接设备数量 - 1]， **默认为 0 号设备**。

### 信息查询（info）

`axcl-smi info`用于显示设备的详细信息，支持子命令如下：

| 子命令 | 说明                                                                                                                              |
| ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| --temp | 显示设备芯片结温，单位是摄氏度 x1000。                                                                                            |
| --mem  | 显示设备系统详细内存使用情况。                                                                                                    |
| --cmm  | 显示设备媒体内存使用情况。如果需要更详细的媒体内存，执行`axcl-smi sh cat /proc/ax_proc/mem_cmm_info -d xx`  (xx 是 PCIe 设备号)。 |
| --cpu  | 显示设备 CPU 利用率。                                                                                                             |
| --npu  | 显示设备 NPU 利用率。                                                                                                             |

**示例**：查询索引号为 0 号的设备的媒体内存使用情况：

```bash
m5stack@raspberrypi5:~ $ axcl-smi info --cmm -d 0
Device ID           : 1 (0x1)
CMM Total           :  7208960 KiB
CMM Used            :    18876 KiB
CMM Remain          :  7190084 kiB
```

### PROC 查询（proc）

`axcl-smi proc`用于查询设备模块的 proc 信息，支持子命令如下：

| 子命令 | 说明                                                  |
| ------ | ----------------------------------------------------- |
| --vdec | 查询 VDEC 模块 proc (`cat /proc/ax_proc/vdec`)        |
| --venc | 查询 VENC 模块 proc (`cat /proc/ax_proc/venc`)        |
| --jenc | 查询 JENC 模块 proc (`cat /proc/ax_proc/jenc`)        |
| --ivps | 查询 IVPS 模块 proc (`cat /proc/ax_proc/ivps`)        |
| --rgn  | 查询 RGN 模块 proc (`cat /proc/ax_proc/rgn`)          |
| --ive  | 查询 IVE 模块 proc (`cat /proc/ax_proc/ive`)          |
| --pool | 查询 POOL 模块 proc (`cat /proc/ax_proc/pool`)        |
| --link | 查询 LINK 模块 proc (`cat /proc/ax_proc/link_table`)  |
| --cmm  | 查询 CMM 模块 proc (`cat /proc/ax_proc/mem_cmm_info`) |

**示例**：查询 0 号设备的 VENC proc 信息

```bash
m5stack@raspberrypi5:~ $ axcl-smi proc --venc -d 0
-------- VENC VERSION ------------------------
[Axera version]: ax_venc V3.6.3_20250722020142 Jul 22 2025 02:22:04 JK

-------- MODULE PARAM ------------------------
MaxChnNum   MaxRoiNum   MaxProcNum  
64          8           32        
```

### 参数设置（set）

`axcl-smi set` 用户配置设备信息，支持的子命令如下：

| 子命令                | 说明                                                           |
| --------------------- | -------------------------------------------------------------- |
| -f[MHz], --freq=[MHz] | 设置设备的 CPU 频率，只支持 1200000, 1400000, 1700000 三种频率 |

**示例**：设置索引号为 0 号的设备 CPU 主频为 1200MHz

```bash
m5stack@raspberrypi5:~ $ axcl-smi set -f 1200000 -d 0
set cpu frequency 1200000 to device 1 succeed.
```

### 下载日志（log）

`axcl-smi log` 用于下载设备的日志文件到主控侧，支持的参数如下：

| 参数                      | 说明                                                                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| -t[mask], --type=[mask]   | 指定下载的日志类别。设备侧日志类别如下：<br />-1： 全部日志<br />0x01：守护进程<br />0x02:  业务进程<br />0x10：syslog<br />0x20：内核日志<br />推荐使用`-1`下载全部日志 |
| -o[path], --output=[path] | 指定日志保存路径，支持绝对和相对路径，默认是当前目录。注意目录需要有写权限。                                                                                             |

**示例**：下载索引为 0 号的设备的全部日志，并保存到当前目录

```bash
m5stack@raspberrypi5:~ $ axcl-smi log -d 0
[2025-07-25 10:04:30.332][1802][C][log][dump][73]: log dump finished: ./dev1_log_20250724210251.tar.gz
```

### shell 命令（sh）

`axcl-smi sh` 支持 shell 命令查询设备信息，通常用于查询设备侧模块的运行 proc 信息。

**示例**：查询索引号为 0 号的设备 CMM 信息

```bash
m5stack@raspberrypi5:~ $ axcl-smi sh cat /proc/ax_proc/mem_cmm_info -d 0
--------------------SDK VERSION-------------------
[Axera version]: ax_cmm V3.6.3_20250722020142 Jul 22 2025 02:21:25 JK
+---PARTITION: Phys(0x148000000, 0x2FFFFFFFF), Size=7208960KB(7040MB),    NAME="anonymous"
 nBlock(Max=0, Cur=23, New=0, Free=0)  nbytes(Max=0B(0KB,0MB), Cur=19329024B(18876KB,18MB), New=0B(0KB,0MB), Free=0B(0KB,0MB))  Block(Max=0B(0KB,0MB), Min=0B(0KB,0MB), Avg=0B(0KB,0MB)) 
   |-Block: phys(0x148000000, 0x148013FFF), cache =non-cacheable, length=80KB(0MB),    name="TDP_DEV"
   |-Block: phys(0x148014000, 0x148014FFF), cache =non-cacheable, length=4KB(0MB),    name="TDP_CMODE3"
   |-Block: phys(0x148015000, 0x148015FFF), cache =non-cacheable, length=4KB(0MB),    name="TDP_CMODE3_CPU"
   |-Block: phys(0x148016000, 0x148029FFF), cache =non-cacheable, length=80KB(0MB),    name="TDP_DEV"
   |-Block: phys(0x14802A000, 0x14802AFFF), cache =non-cacheable, length=4KB(0MB),    name="TDP_CMODE3"
   |-Block: phys(0x14802B000, 0x14802BFFF), cache =non-cacheable, length=4KB(0MB),    name="TDP_CMODE3_CPU"
   |-Block: phys(0x14802C000, 0x14862BFFF), cache =non-cacheable, length=6144KB(6MB),    name="vdec_ko"
   |-Block: phys(0x14862C000, 0x148647FFF), cache =non-cacheable, length=112KB(0MB),    name="VGP_DEV"
   |-Block: phys(0x148648000, 0x148648FFF), cache =non-cacheable, length=4KB(0MB),    name="VGP_CMODE3"
   |-Block: phys(0x148649000, 0x148649FFF), cache =non-cacheable, length=4KB(0MB),    name="VGP_CMODE3_CPU"
   |-Block: phys(0x14864A000, 0x148665FFF), cache =non-cacheable, length=112KB(0MB),    name="VPP_DEV"
   |-Block: phys(0x148666000, 0x148666FFF), cache =non-cacheable, length=4KB(0MB),    name="VPP_CMODE3"
   |-Block: phys(0x148667000, 0x148667FFF), cache =non-cacheable, length=4KB(0MB),    name="VPP_CMODE3_CPU"
   |-Block: phys(0x148668000, 0x1487E7FFF), cache =non-cacheable, length=1536KB(1MB),    name="h26x_ko"
   |-Block: phys(0x1487E8000, 0x148967FFF), cache =non-cacheable, length=1536KB(1MB),    name="h26x_ko"
   |-Block: phys(0x148968000, 0x148968FFF), cache =non-cacheable, length=4KB(0MB),    name="h26x_ko"
   |-Block: phys(0x148969000, 0x148969FFF), cache =non-cacheable, length=4KB(0MB),    name="GDC_CMDA3"
   |-Block: phys(0x14896A000, 0x14896AFFF), cache =non-cacheable, length=4KB(0MB),    name="GDC_CMDA3_CPU"
   |-Block: phys(0x14896B000, 0x14896DFFF), cache =non-cacheable, length=12KB(0MB),    name="GDC_CMD"
   |-Block: phys(0x14896E000, 0x148AEDFFF), cache =non-cacheable, length=1536KB(1MB),    name="jenc_ko"
   |-Block: phys(0x148AEE000, 0x148C6DFFF), cache =non-cacheable, length=1536KB(1MB),    name="jenc_ko"
   |-Block: phys(0x148C6E000, 0x148C6EFFF), cache =non-cacheable, length=4KB(0MB),    name="jenc_ko"
   |-Block: phys(0x148C6F000, 0x14926EFFF), cache =non-cacheable, length=6144KB(6MB),    name="vdec_ko"

---CMM_USE_INFO:
 total size=7208960KB(7040MB),used=18876KB(18MB + 444KB),remain=7190084KB(7021MB + 580KB),partition_number=1,block_number=23
```

?>重要|shell 命令参数如果包含`-`,`--`,`>`等字段，可以用双引号`"-l"`将命令和参数包含在一个字符串中，比如`axcl-smi >sh "ls -l" -d 0`<br/>。谨慎使用 shell 命令对设备进行配置。

### 重启（reboot）

`axcl-smi reboot` 命令首先复位指定设备，随后将自动加载固件，示例如下：

```bash
m5stack@raspberrypi5:~ $ axcl-smi reboot
Do you want to reboot device 0 ? (y/n): y
```
