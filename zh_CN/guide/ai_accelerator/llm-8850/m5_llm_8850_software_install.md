# LLM-8850 Card 环境配置

## 树莓派环境配置

参考以下文档或[官方链接](https://www.raspberrypi.com/news/using-m-2-hat-with-raspberry-pi-5/)完成树莓派环境配置，注意：以下命令在树莓派的终端执行。

如同 PC 中的 BIOS，EEPROM 设置独立于烧录 OS 的 TF 卡，烧录最新的树莓派镜像或者切换镜像版本并不会主动更新 EEPROM 的设置。

首先执行 update：

```bash
sudo apt update && sudo apt full-upgrade
```

然后检查一下 EEPROM 中的版本：

```bash
sudo rpi-eeprom-update
```

如果看到的日期早于 `2023 年 12 月 6 日`，运行以下命令以打开 Raspberry Pi 配置 CLI：

```bash
sudo raspi-config
```

在 Advanced Options > Bootloader Version （引导加载程序版本） 下，选择 Latest （最新）。然后，使用 Finish 或 ESC 键退出 raspi-config。

执行以下命令，将固件更新到最新版本。

```bash
sudo rpi-eeprom-update -a
```

最后使用 `sudo reboot` 重新启动。重启后就完成了 EEPROM 中 firmware 的更新。

```bash
sudo reboot
```

完成修改并重启后，可以使用 `lspci` 命令检查加速卡是否正确被识别：

```bash
lspci
```

命令执行结果如下：

```bash
m5stack@raspberrypi5:~ $ lspci
0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 30)
0001:01:00.0 Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev 01)
0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 30)
0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
```

其中 `Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev 01)` 就是 LLM-8850 加速卡。

## LLM-8850 Card 驱动安装

?> 提示 | 开发板需要编译支持，依赖 gcc, make, patch, linux-header-$(uname -r) 这几个包。需要提前安装好，或者保证安装时网络可用。

**更新软件源**

通过以下命令获取 aarch64/x86 deb 包：

```bash
sudo wget -qO /etc/apt/keyrings/StackFlow.gpg https://repo.llm.m5stack.com/m5stack-apt-repo/key/StackFlow.gpg
echo 'deb [signed-by=/etc/apt/keyrings/StackFlow.gpg] https://repo.llm.m5stack.com/m5stack-apt-repo axclhost main' | sudo tee /etc/apt/sources.list.d/axclhost.list
```

使用以下命令安装

```bash
sudo apt update
```

```bash
sudo apt install dkms
```

```bash
sudo apt install axclhost
```

安装将很快完成。安装时会自动增加环境变量，使得安装的 .so 和可执行程序可用。需要注意的是，如果需要可执行程序立即可用，还需要更新 bash 终端的环境：

```bash
source /etc/profile
```

如果是 ssh 的方式远程连接的板卡，还可以选择重连 ssh 进行自动更新 (本机终端登录还可以重开一个终端进行自动更新)。

输入以下命令，即可查看设备的信息：

```bash
axcl-smi
```

输出如下：

```bash
+------------------------------------------------------------------------------------------------+
| AXCL-SMI  V3.6.4_20250805020145                                  Driver  V3.6.4_20250805020145 |
+-----------------------------------------+--------------+---------------------------------------+
| Card  Name                     Firmware                                                          | Bus-Id       | Memory-Usage           |
| Fan   Temp                Pwr:Usage/Cap                                                          | CPU      NPU | CMM-Usage              |
| =========================================+==============+======================================= |
| 0  AX650N                     V3.6.4                                                             | 0001:01:00.0 | 148 MiB /      945 MiB |
| --   41C                      -- / --                                                            | 2%        0% | 18 MiB /     7040 MiB  |
+-----------------------------------------+--------------+---------------------------------------+

+------------------------------------------------------------------------------------------------+
| Processes:                                                                                       |
| Card      PID  Process Name                                                   NPU Memory Usage   |
| ================================================================================================ |
```

详情请查看 [AXCL-SMI](./m5_llm_8850_axcl_smi) 部分

## LLM-8850 Card 驱动卸载

?> 提示 | 如果遇到安装问题或需要更新驱动，使用以下命令卸载驱动。

```bash
sudo apt remove axclhost
```
