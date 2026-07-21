# CoreMP135 分区扩容

\#>CoreMP135 分区扩容 | 为了适应不同的 microSD 卡容量以及加快固件烧写速度，镜像的根文件系统分区并不会完全填充所有容量。你可以参考以下几种方式对 microSD 卡重新分区，实现扩容。

## 1. 使用脚本分区

在`M5_CoreMP135_debian12_20240507`/`M5_CoreMP135_buildroot_20240508`以上版本，在`/usr/local/m5stack`路径下提供了`resize_mmc.sh`扩容脚本，可直接执行进行自动扩容，完成后重启即可。

```bash
cd /usr/local/m5stack
./resize_mmc.sh
```

## 2. 通过配置工具分区

使用`core-config`配置工具实现扩容。

```bash
core-config
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_coreconfig_resize_01.png" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/coremp135_coreconfig_resize_02.jpg" width="50%">

## 3.fdisk 手动分区

参考以下流程，使用`fdisk`指令实现扩容。

### 查看分区

```bash
fdisk /dev/mmcblk0

# 查看当前分区
Command (m for help): p

Disk /dev/mmcblk0: 29.72 GiB, 31914983424 bytes, 62333952 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 7067FB81-6C05-45AC-9375-326E6B8BE20A

Device           Start     End Sectors  Size Type
/dev/mmcblk0p1      34     545     512  256K Linux reserved
/dev/mmcblk0p2     546    1057     512  256K Linux reserved
/dev/mmcblk0p3    1058    1569     512  256K Linux reserved
/dev/mmcblk0p4    1570    2081     512  256K Linux reserved
/dev/mmcblk0p5    2082   10273    8192    4M unknown
/dev/mmcblk0p6   10274   18465    8192    4M unknown
/dev/mmcblk0p7   18466   19489    1024  512K Linux reserved
/dev/mmcblk0p8   19490  150561  131072   64M Linux filesystem
/dev/mmcblk0p9  150562  183329   32768   16M Linux filesystem
/dev/mmcblk0p10 183330 2621406 2438077  1.2G Linux filesystem

```

### 重建分区

1\. 使用 d 指令删除第 10 号分区

```bash
Command (m for help): d
Partition number (1-10, default 10): 10

Partition 10 has been deleted.
```

2\. 再次创建分区，`注意：新分区的First sector地址需要与原分区信息一致(183330)，否则将导致数据丢失`, 提示是否移除存在的分区标志，选择 no。

```bash
Command (m for help): n
Partition number (10-128, default 10):
First sector (183330-62333918, default 184320): 183330
): t sector, +/-sectors or +/-size{K,M,G,T,P} (183330-62333918, default 62332927)

Created a new partition 10 of type 'Linux filesystem' and of size 29.6 GiB.
Partition #10 contains a ext4 signature.

Do you want to remove the signature? [Y]es/[N]o: n

```

### 保存修改

3\. 输入指令 p 查看新的分区信息，输入指令 w 写入保存。

```bash
Command (m for help): p
Disk /dev/mmcblk0: 29.72 GiB, 31914983424 bytes, 62333952 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 7067FB81-6C05-45AC-9375-326E6B8BE20A

Device           Start      End  Sectors  Size Type
/dev/mmcblk0p1      34      545      512  256K Linux reserved
/dev/mmcblk0p2     546     1057      512  256K Linux reserved
/dev/mmcblk0p3    1058     1569      512  256K Linux reserved
/dev/mmcblk0p4    1570     2081      512  256K Linux reserved
/dev/mmcblk0p5    2082    10273     8192    4M unknown
/dev/mmcblk0p6   10274    18465     8192    4M unknown
/dev/mmcblk0p7   18466    19489     1024  512K Linux reserved
/dev/mmcblk0p8   19490   150561   131072   64M Linux filesystem
/dev/mmcblk0p9  150562   183329    32768   16M Linux filesystem
/dev/mmcblk0p10 183330 62332927 62149598 29.6G Linux filesystem


Command (m for help): w

The partition table has been altered.
Syncing disks.

```

### 扩容完成

4\. 使用`resize2fs`指令更新文件系统大小，然后重启设备即可完成扩容。

```bash
resize2fs -f /dev/mmcblk0p10
```
