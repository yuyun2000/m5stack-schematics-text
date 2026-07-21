# SDK 示例

## runtime

### axcl_sample_runtime

调用运行时 API 的示例。

```
1. 通过 `axclInit` 初始化运行时。
2. 通过 `axclrtSetDevice` 激活设备。
3. 为 main 线程通过 `axclrtCreateDevice` 创建上下文（可选）。
4. 创建和销毁线程上下文（必须）。
5. 销毁 main 线程的上下文。
6. 通过 `axclrtResetDevice` 取消激活设备。
7. 通过 `axclFinalize` 取消初始化运行时。
```

#### 用法

```bash
m5stack@raspberrypi5:~ $ axcl_sample_runtime --help
[INFO ][                            main][  36]: ============== V3.6.3_20250722020142 sample started Jul 22 2025 02:31:26 =============
usage: axcl_sample_runtime [options] ...
options:
  -d, --device    device index [-1, connected device num - 1], -1: traverse all devices (int [=-1])
      --json      axcl.json path (string [=./axcl.json])
      --reboot    reboot device
  -?, --help      print this message
```

| 参数         | 默认值                                  | 描述                            |
| ------------ | --------------------------------------- | ------------------------------- |
| -d, --device | -1, range: \[-1, 0 - 已连接设备数量 -1] | 指定设备索引。 -1: 遍历所有设备 |
| --json       | [axcl.json](#json)                      | 文件路径                        |
| --reboot     | NA                                      | 让设备 Panic 并重启。           |

#### 示例 1

查询设备 #0 的属性。

```bash
m5stack@raspberrypi5:~ $ axcl_sample_runtime -d 0
[INFO ][                            main][  36]: ============== V3.6.3_20250722020142 sample started Jul 22 2025 02:31:26 =============
json file
[INFO ][                      operator()][ 130]: [0001:01.0] software version: Ax_Version V3.6.3_20250722020142

[INFO ][                      operator()][ 131]: [0001:01.0] uid             : 0x600408144b65d204
[INFO ][                      operator()][ 132]: [0001:01.0] temperature     : 49263
[INFO ][                      operator()][ 133]: [0001:01.0] total mem size  : 968356   KB
[INFO ][                      operator()][ 134]: [0001:01.0] free  mem size  : 815084   KB
[INFO ][                      operator()][ 135]: [0001:01.0] total cmm size  : 7208960  KB
[INFO ][                      operator()][ 136]: [0001:01.0] free  cmm size  : 7190084  KB
[INFO ][                      operator()][ 137]: [0001:01.0] avg cpu loading : 0.0%
[INFO ][                      operator()][ 138]: [0001:01.0] avg npu loading : 0.0%
[INFO ][                      operator()][ 149]: malloc 1048576 bytes memory from device  1 success, addr = 0x14926f000
[INFO ][                            main][ 215]: ============== V3.6.3_20250722020142 sample exited Jul 22 2025 02:31:26 ==============
```

#### 示例 2

通过发送 `echo c > /proc/sysrq-trigger` 手动让设备 #0 Panic，然后重启并再次下载固件。

```bash
m5stack@raspberrypi5:~ $ axcl_sample_runtime -d 0 --reboot
[INFO ][                            main][  36]: ============== V3.6.3_20250722020142 sample started Jul 22 2025 02:31:26 =============
json file
[INFO ][                      operator()][ 130]: [0001:01.0] software version: Ax_Version V3.6.3_20250722020142

[INFO ][                      operator()][ 131]: [0001:01.0] uid             : 0x600408144b65d204
[INFO ][                      operator()][ 132]: [0001:01.0] temperature     : 49263
[INFO ][                      operator()][ 133]: [0001:01.0] total mem size  : 968356   KB
[INFO ][                      operator()][ 134]: [0001:01.0] free  mem size  : 814888   KB
[INFO ][                      operator()][ 135]: [0001:01.0] total cmm size  : 7208960  KB
[INFO ][                      operator()][ 136]: [0001:01.0] free  cmm size  : 7190084  KB
[INFO ][                      operator()][ 137]: [0001:01.0] avg cpu loading : 1.2%
[INFO ][                      operator()][ 138]: [0001:01.0] avg npu loading : 0.0%
[INFO ][                      operator()][ 149]: malloc 1048576 bytes memory from device  1 success, addr = 0x14926f000
[INFO ][                            main][ 178]: panic device 0x1
[INFO ][                            main][ 185]: wait for device 0x1 to reboot in 60 seconds
[FAIL ][                            main][ 203]: device 0x1 reboot timeout
[INFO ][                            main][ 215]: ============== V3.6.3_20250722020142 sample exited Jul 22 2025 02:31:26 ==============
```

### axcl_sample_memory

主机（HOST）和设备（DEVICE）之间内存拷贝的示例。

```
         HOST          |               DEVICE
      host_mem[0] -----------> dev_mem[0]
                                    |---------> dev_mem[1]
      host_mem[1] <----------------------------------|

1. allocate host_mem[2] by `axclrtMallocHost` and dev_mem[2] by `axclrtMalloc`.
2. axclrtMemcpy(dev_mem[0], host_mem[0], size, AXCL_MEMCPY_HOST_TO_DEVICE)
3. axclrtMemcpy(dev_mem[1], dev_mem[0], size, AXCL_MEMCPY_DEVICE_TO_DEVICE)
4. axclrtMemcpy(host_mem[1], dev_mem[1], size, AXCL_MEMCPY_DEVICE_TO_HOST)
5. memcmp(host_mem[0], host_mem[1], size)
```

#### 用法

```bash
m5stack@raspberrypi5:~ $ axcl_sample_memory --help
[INFO ][                            main][  32]: ============== V3.6.3_20250722020142 sample started Jul 22 2025 02:31:27 ==============

usage: axcl_sample_memory [options] ...
options:
  -d, --device    device index from 0 to connected device num - 1 (int [=0])
      --json      axcl.json path (string [=./axcl.json])
  -?, --help      print this message
```

| 参数         | 默认值                            | 描述           |
| ------------ | --------------------------------- | -------------- |
| -d, --device | 0, 范围: \[0 - 已连接设备数量 -1] | 指定设备索引。 |
| --json       | [axcl.json](#json)                | 文件路径       |

#### 示例

```bash
m5stack@raspberrypi5:~ $ axcl_sample_memory  -d 0
[INFO ][                            main][  32]: ============== V3.6.3_20250722020142 sample started Jul 22 2025 02:31:27 ==============

[INFO ][                           setup][ 112]: json: ./axcl.json
json file
[INFO ][                           setup][ 131]: device index: 0, bus number: 1
[INFO ][                            main][  51]: alloc host and device memory, size: 0x800000
[INFO ][                            main][  63]: memory [0]: host 0x7fff277fc010, device 0x14926f000
[INFO ][                            main][  63]: memory [1]: host 0x7fff26ff8010, device 0x149a6f000
[INFO ][                            main][  69]: memcpy from host memory[0] 0x7fff277fc010 to device memory[0] 0x14926f000
[INFO ][                            main][  75]: memcpy device memory[0] 0x14926f000 to device memory[1] 0x149a6f000
[INFO ][                            main][  81]: memcpy device memory[1] 0x149a6f000 to host memory[0] 0x7fff26ff8010
[INFO ][                            main][  88]: compare host memory[0] 0x7fff277fc010 and host memory[1] 0x7fff26ff8010 success
[INFO ][                         cleanup][ 146]: deactive device 1 and cleanup axcl
[INFO ][                            main][ 106]: ============== V3.6.3_20250722020142 sample exited Jul 22 2025 02:31:27 ==============
```

## native

### axcl_sample_sys

- 原生 SYS 模块用法的示例，包括：

- 非缓存 CMM 内存的分配和释放。

- 缓存 CMM 内存的分配和释放。

- 通用内存池的分配和释放。

- 私有内存池的分配和释放。

- 模块链接和查询。

#### 用法

```bash
m5stack@raspberrypi5:~ $ axcl_sample_sys --help
usage: axcl_sample_sys [options] ...
options:
  -d, --device    device index from 0 to connected device num - 1 (unsigned int [=0])
      --json      axcl.json path (string [=./axcl.json])
  -?, --help      print this message
```

| 参数         | 默认值                            | 描述           |
| ------------ | --------------------------------- | -------------- |
| -d, --device | 0, 范围: \[0 - 已连接设备数量 -1] | 指定设备索引。 |
| --json       | [axcl.json](#json)                | 文件路径       |

#### 示例

```bash
m5stack@raspberrypi5:~ $ axcl_sample_sys -d 0
[INFO ][                            main][  35]: json: ./axcl.json
json file
[INFO ][                            main][  55]: device index: 0, bus number: 1
[INFO ][           sample_sys_alloc_free][  82]: sys_alloc_free begin
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x14926f000,pVirAddr=0xffffafafe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x14936f000,pVirAddr=0xffffaf9fe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x14946f000,pVirAddr=0xffffaf8fe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x14956f000,pVirAddr=0xffffaf7fe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x14966f000,pVirAddr=0xffffaf6fe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x14976f000,pVirAddr=0xffffaf5fe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x14986f000,pVirAddr=0xffffaf4fe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x14996f000,pVirAddr=0xffffaf3fe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x149a6f000,pVirAddr=0xffffaf2fe000
[INFO ][           sample_sys_alloc_free][  91]: alloc PhyAddr= 0x149b6f000,pVirAddr=0xffffaf1fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x14926f000,pVirAddr=0xffffafafe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x14936f000,pVirAddr=0xffffaf9fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x14946f000,pVirAddr=0xffffaf8fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x14956f000,pVirAddr=0xffffaf7fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x14966f000,pVirAddr=0xffffaf6fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x14976f000,pVirAddr=0xffffaf5fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x14986f000,pVirAddr=0xffffaf4fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x14996f000,pVirAddr=0xffffaf3fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x149a6f000,pVirAddr=0xffffaf2fe000
[INFO ][           sample_sys_alloc_free][ 100]: free PhyAddr= 0x149b6f000,pVirAddr=0xffffaf1fe000
[INFO ][           sample_sys_alloc_free][ 103]: sys_alloc_free end success
[INFO ][     sample_sys_alloc_cache_free][ 115]: sys_alloc_cache_free begin
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x14926f000,pVirAddr=0xffffafafe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x14936f000,pVirAddr=0xffffaf9fe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x14946f000,pVirAddr=0xffffaf8fe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x14956f000,pVirAddr=0xffffaf7fe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x14966f000,pVirAddr=0xffffaf6fe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x14976f000,pVirAddr=0xffffaf5fe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x14986f000,pVirAddr=0xffffaf4fe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x14996f000,pVirAddr=0xffffaf3fe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x149a6f000,pVirAddr=0xffffaf2fe000
[INFO ][     sample_sys_alloc_cache_free][ 124]: alloc PhyAddr= 0x149b6f000,pVirAddr=0xffffaf1fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x14926f000,pVirAddr=0xffffafafe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x14936f000,pVirAddr=0xffffaf9fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x14946f000,pVirAddr=0xffffaf8fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x14956f000,pVirAddr=0xffffaf7fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x14966f000,pVirAddr=0xffffaf6fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x14976f000,pVirAddr=0xffffaf5fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x14986f000,pVirAddr=0xffffaf4fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x14996f000,pVirAddr=0xffffaf3fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x149a6f000,pVirAddr=0xffffaf2fe000
[INFO ][     sample_sys_alloc_cache_free][ 133]: free PhyAddr= 0x149b6f000,pVirAddr=0xffffaf1fe000
[INFO ][     sample_sys_alloc_cache_free][ 136]: sys_alloc_cache_free end success
[INFO ][          sample_sys_commom_pool][ 148]: sys_commom_pool begin
[INFO ][          sample_sys_commom_pool][ 157]: AXCL_SYS_Init success!
[INFO ][          sample_sys_commom_pool][ 167]: AXCL_POOL_Exit success!
[INFO ][          sample_sys_commom_pool][ 199]: AXCL_POOL_SetConfig success!
[INFO ][          sample_sys_commom_pool][ 208]: AXCL_POOL_Init success!
[INFO ][          sample_sys_commom_pool][ 222]: AXCL_POOL_GetBlock success!BlkId:0x5E002000
[INFO ][          sample_sys_commom_pool][ 233]: AXCL_POOL_Handle2PoolId success!(Blockid:0x5E002000 --> PoolId=2)
[INFO ][          sample_sys_commom_pool][ 244]: AXCL_POOL_Handle2PhysAddr success!(Blockid:0x5E002000 --> PhyAddr=0x14ad8d000)
[INFO ][          sample_sys_commom_pool][ 255]: AXCL_POOL_Handle2MetaPhysAddr success!(Blockid:0x5E002000 --> MetaPhyAddr=0x14a18b000)
[INFO ][          sample_sys_commom_pool][ 265]: AXCL_POOL_ReleaseBlock success!Blockid=0x5e002000
[INFO ][          sample_sys_commom_pool][ 275]: AXCL_POOL_Exit success!
[INFO ][          sample_sys_commom_pool][ 285]: AXCL_SYS_Deinit success!
[INFO ][          sample_sys_commom_pool][ 288]: sys_commom_pool end success!
[INFO ][         sample_sys_private_pool][ 310]: sys_private_pool begin
[INFO ][         sample_sys_private_pool][ 319]: AXCL_SYS_Init success!
[INFO ][         sample_sys_private_pool][ 329]: AXCL_POOL_Exit success!
[INFO ][         sample_sys_private_pool][ 349]: AXCL_POOL_CreatePool[0] success
[INFO ][         sample_sys_private_pool][ 367]: AXCL_POOL_CreatePool[1] success
[INFO ][         sample_sys_private_pool][ 378]: AXCL_POOL_GetBlock success!BlkId:0x5E001000
[INFO ][         sample_sys_private_pool][ 389]: AXCL_POOL_Handle2PoolId success!(Blockid:0x5E001000 --> PoolId=1)
[INFO ][         sample_sys_private_pool][ 400]: AX_POOL_Handle2PhysAddr success!(Blockid:0x5E001000 --> PhyAddr=0x149879000)
[INFO ][         sample_sys_private_pool][ 411]: AXCL_POOL_Handle2MetaPhysAddr success!(Blockid:0x5E001000 --> MetaPhyAddr=0x149477000)
[INFO ][         sample_sys_private_pool][ 421]: AXCL_POOL_ReleaseBlock success!Blockid=0x5e001000
[INFO ][         sample_sys_private_pool][ 430]: AXCL_POOL_DestroyPool[1] success!
[INFO ][         sample_sys_private_pool][ 438]: AXCL_POOL_DestroyPool[0] success!
[INFO ][         sample_sys_private_pool][ 448]: AXCL_SYS_Deinit success!
[INFO ][         sample_sys_private_pool][ 451]: sys_private_pool end success!
[INFO ][                 sample_sys_link][ 472]: sample_sys_link begin
[INFO ][                 sample_sys_link][ 487]: AXCL_SYS_Init success!
[INFO ][                 sample_sys_link][ 554]: AXCL_SYS_Deinit success!
[INFO ][                 sample_sys_link][ 557]: sample_sys_link end success!
```

### axcl_sample_vdec

H264、H265 视频解码器 (VDEC) 的示例。

1. 加载 .mp4 文件或 .h264/.h265 原始码流文件。

2. 通过 ffmpeg 解复用 nalu 帧。

3. 逐帧将 nalu 发送到视频解码器。

4. 接收解码后的 nv12 图像信息。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/sample_vdec.png" width="70%" />

#### 用法

```bash
m5stack@raspberrypi5:~ $ axcl_sample_vdec --help
[INFO ][                            main][  43]: ============== V3.6.3_20250722020142 sample started Jul 22 2025 02:31:31 ==============

usage: axcl_sample_vdec --url=string [options] ...
options:
  -i, --url       mp4|.264|.265 file path (string)
  -d, --device    device index from 0 to connected device num - 1 (unsigned int [=0])
      --count     grp count (int [=1])
      --json      axcl.json path (string [=./axcl.json])
  -w, --width     frame width (int [=1920])
  -h, --height    frame height (int [=1080])
      --VdChn     channel id (int [=0])
      --yuv       transfer nv12 from device (int [=0])
  -?, --help      print this message
```

| 参数         | 默认值                            | 描述                                                                                                                                                      |
| ------------ | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -d, --device | 0, 范围: \[0 - 已连接设备数量 -1] | 指定设备索引。                                                                                                                                            |
| --json       | [axcl.json](#json)                | 文件路径                                                                                                                                                  |
| -i, --url    | NA                                | 指定流文件的路径。                                                                                                                                        |
| --count      | 1                                 | 指定组数量。                                                                                                                                              |
| -w, --width  | 1920                              | 指定解码的 YUV 图像的宽度。                                                                                                                               |
| -h, --height | 1080                              | 指定解码的 YUV 图像的高度。                                                                                                                               |
| --VdChn      | 0                                 | 指定 VDEC 的通道。<br>0: 输出输入流的原始宽高。<br>1: 输出范围 \[48x48, 4096x4096]，支持缩放宽高。<br>2: 输出范围 \[48x48, 1920x1080]，支持缩放宽高。<br> |
| --yuv        | 0                                 | 1: 从设备传输解码后的 YUV 图像。 0: 不传输图像。                                                                                                          |

**注意：**

如果遇到以下错误：

```bash
$ axcl_sample_vdec --help
axcl_sample_vdec: error while loading shared libraries: libavcodec.so.61: cannot open shared object file: No such file or directory
```

请先使用以下命令设置环境变量：

```bash
$ export LD_LIBRARY_PATH=/usr/lib/axcl/ffmpeg:$LD_LIBRARY_PATH
```

#### 示例

```bash
m5stack@raspberrypi5:~ $ axcl_sample_vdec -i input.mp4 -d 0
[INFO ][                            main][  43]: ============== V3.6.3_20250722020142 sample started Jul 22 2025 02:31:31 ==============

[INFO ][                            main][  68]: json: ./axcl.json
json file
[INFO ][                            main][  88]: device index: 0, bus number: 1
[INFO ][             ffmpeg_init_demuxer][ 439]: [0] url: input.mp4
[INFO ][             ffmpeg_init_demuxer][ 502]: [0] url input.mp4: codec 96, 1280x688, fps 30
[INFO ][                            main][ 116]: init sys
[INFO ][                            main][ 125]: init vdec
[INFO ][                            main][ 139]: start decoder 0
[INFO ][sample_get_vdec_attr_from_stream_info][ 252]: stream info: 1280x688 payload 96 fps 30
[INFO ][ sample_get_decoded_image_thread][ 311]: [decoder  0] decode thread +++
[INFO ][                            main][ 176]: start demuxer 0
[INFO ][          ffmpeg_dispatch_thread][ 189]: [0] +++
[INFO ][             ffmpeg_demux_thread][ 295]: [0] +++
[INFO ][             ffmpeg_demux_thread][ 328]: [0] reach eof
[INFO ][             ffmpeg_demux_thread][ 435]: [0] demuxed    total 281 frames ---
[INFO ][          ffmpeg_dispatch_thread][ 272]: [0] dispatched total 281 frames ---
[WARN ][ sample_get_decoded_image_thread][ 357]: [decoder  0] flow end
[INFO ][ sample_get_decoded_image_thread][ 392]: [decoder  0] total decode 281 frames
[INFO ][ sample_get_decoded_image_thread][ 398]: [decoder  0] dfecode thread ---
[INFO ][                            main][ 197]: stop decoder 0
[INFO ][                            main][ 202]: decoder 0 is eof
[INFO ][                            main][ 227]: stop demuxer 0
[INFO ][                            main][ 235]: deinit vdec
[INFO ][                            main][ 239]: deinit sys
[INFO ][                            main][ 243]: axcl deinit
[INFO ][                            main][ 247]: ============== V3.6.3_20250722020142 sample exited Jul 22 2025 02:31:31 ==============
```

### axcl_sample_venc

H264、H265、JPEG、MJPEG 编码器 (VENC) 的示例。

#### 用法

```bash
m5stack@raspberrypi5:~ $ axcl_sample_venc --help
[INFO][SAMPLE-VENC][main][39]: Build at Jul 22 2025 02:31:34

Usage:  axcl_sample_venc [options] -i input file

  -H --help                        help information

## Options for sample

  -i[s] --input                         Read input video sequence from file. [input.yuv]
  -o[s] --output                        Write output HEVC/H.264/jpeg/mjpeg stream to file.[stream.hevc]
  -W[n] --write                         whether write output stream to file.[1]
                                        0: do not write
                                        1: write

  -f[n] --dstFrameRate                  1..1048575 Output picture rate numerator. [30]

  -j[n] --srcFrameRate                  1..1048575 Input picture rate numerator. [30]

  -n[n] --encFrameNum                   the frame number want to encode. [0]
  -N[n] --chnNum                        total encode channel number. [0]
  -t[n] --encThdNum                     total encode thread number. [1]
  -p[n] --bLoopEncode                   enable loop mode to encode. 0: disable. 1: enable. [0]
  --codecType                           encoding payload type. [0]
                                        0 - SAMPLE_CODEC_H264
                                        1 - SAMPLE_CODEC_H265
                                        2 - SAMPLE_CODEC_MJPEG
                                        3 - SAMPLE_CODEC_JPEG
  --bChnCustom                          whether encode all payload type. [0]
                                        0 - encode all payload type
                                        1 - encode payload type codecType specified by codecType.
  --log                                 log info level. [2]
                                        0 : ERR
                                        1 : WARN
                                        2 : INFO
                                        3 : DEBUG
  --json                                axcl.json path
  --devId                               device index from 0 to connected device num - 1. [0]

  --bStrmCached                         output stream use cached memory. [0]
  --bAttachHdr                          support attach headers(sps/pps) to PB frame for h.265. [0]



## Parameters affecting input frame and encoded frame resolutions and cropping:


  -w[n] --picW                          Width of input image in pixels.
  -h[n] --picH                          Height of input image in pixels.

  -X[n] --cropX                         image horizontal cropping offset, must be even. [0]
  -Y[n] --cropY                         image vertical cropping offset, must be even. [0]
  -x[n] --cropW                         Height of encoded image
  -y[n] --cropH                         Width of encoded image

  --maxPicW                             max width of input image in pixels.
  --maxPicH                             max height of input image in pixels.

  --bCrop                               enable crop encode, 0: disable 1: enable crop. [0]


## Parameters picture stride:

  --strideY                             y stride
  --strideU                             u stride
  --strideV                             v stride


## Parameters  for pre-processing frames before encoding:


  -l[n] --picFormat                     Input YUV format. [1]
                                        1 - AX_FORMAT_YUV420_PLANAR (IYUV/I420)
                                        3 - AX_FORMAT_YUV420_SEMIPLANAR (NV12)
                                        4 - AX_FORMAT_YUV420_SEMIPLANAR_VU (NV21)
                                        13 - AX_FORMAT_YUV422_INTERLEAVED_YUYV (YUYV/YUY2)
                                        14 - AX_FORMAT_YUV422_INTERLEAVED_UYVY (UYVY/Y422)
                                        37 - AX_FORMAT_YUV420_PLANAR_10BIT_I010
                                        42 - AX_FORMAT_YUV420_SEMIPLANAR_10BIT_P010

## Parameters  affecting GOP pattern, rate control and output stream bitrate:


  -g[n] --gopLen                        Intra-picture rate in frames. [30]
                                        Forces every Nth frame to be encoded as intra frame.
                                        0 = Do not force

  -B[n] --bitRate                       target bitrate for rate control, in kbps. [2000]
  --ltMaxBt                             the long-term target max bitrate.
  --ltMinBt                             the long-term target min bitrate.
  --ltStaTime                           the long-term rate statistic time.
  --shtStaTime                          the short-term rate statistic time.
  --minQpDelta                          Difference between FrameLevelMinQp and MinQp
  --maxQpDelta                          Difference between FrameLevelMaxQp and MaxQp


## Parameters  qp:

  -q[n] --qFactor                       0..99, Initial target QP of jenc. [90]
  -b[n] --bDblkEnable                   0: disable Deblock 1: enable Deblock. [0]
  --startQp                             -1..51, start qp for first frame. [16]
  --vq                                  0..9 video quality level for vbr, def 0, min/max qp is invalid when vq != 0
  --minQp                               0..51, Minimum frame header qp for any picture. [16]
  --maxQp                               0..51, Maximum frame header qp for any picture. [51]
  --minIqp                              0..51, Minimum frame header qp for I picture. [16]
  --maxIqp                              0..51, Maximum frame header qp for I picture. [51]
  --chgPos                              vbr/avbr chgpos 20-100, def 90
  --stillPercent                        avbr still percent 10-100 def 25
  --stillQp                             0..51, the max QP value of I frame for still scene. [0]

  --deltaQpI                            -51..51, QP adjustment for intra frames. [-2]
  --maxIprop                            1..100, the max I P size ratio. [100]
  --minIprop                            1..maxIprop, the min I P size ratio. [1]
  --IQp                                 0..51, qp of the i frame. [25]
  --PQp                                 0..51, qp of the p frame. [30]
  --BQp                                 0..51, qp of the b frame. [32]
  --fixedQp                             -1..51, Fixed qp for every frame(only for Mjpeg)
                                          -1 : disable fixed qp mode.
                                          [0, 51] : value of fixed qp.

  --ctbRcMode                           0: diable ctbRc; 1: quality first; 2: bitrate first 3: quality and bitrate balance
  --qpMapQpType                         0: disable qpmap; 1: deltaQp; 2: absQp
  --qpMapBlkUnit                        0: 64x64, 1: 32x32, 2: 16x16;
  --qpMapBlkType                        0: disable; 1: skip mode; 2: Ipcm mode


  -r[n] --rcMode                        0: CBR 1: VBR 2: AVBR 3: QPMAP 4:FIXQP 5:CVBR. [0]


  -M[n] --gopMode                       gopmode. 0: normalP. 1: oneLTR. 2: svc-t. [0]


## other:

  --vbCnt                               total frame buffer number of pool [1, 100]. [10]
  --inFifoDep                           input fifo depth. [4]
  --outFifoDep                          output fifo depth. [4]
  --syncSend                            send frame mode. -1: block mode, >=0：non-block, in ms.
  --syncGet                             get stream mode. -1: block mode, >=0：non-block, in ms.

  --bLinkMode
  --strmBitDep                          encode stream bit depth. [8]
                                         8 : encode 8bit
                                         10: encode 10bit

  --strmBufSize                         output stream buffer size. [0]
                                        0: use default memory setting in sdk.
                                        >0：alloc some memory by user.

  --virILen                             virtual I frame duration. should less than gop length.
```

#### 示例 1

启用两个通道编码 1080p NV12 格式 (通道 0: H.264, 通道 1: H.265)

```bash
$ axcl_sample_venc -w 1920 -h 1080 -i 1080p_nv12.yuv -N 2 -l 3
```

#### 示例 2

启用两个通道循环编码 3840x2160 NV21 格式 (通道 0: H.264, 通道 1: H.265)，编码 10 帧

```bash
$ axcl_sample_venc -w 3840 -h 2160 -i 3840x2160_nv21.yuv -N 2 -l 4 -n 10
```

#### 示例 3

编码一个 MJPEG 流，分辨率 1920x1080，YUV420P 格式，编码 5 帧

```bash
$ axcl_sample_venc -w 1920 -h 1080 -i 1920x1080_yuv420p.yuv -N 1 --bChnCustom 1 --codecType 2 -l 1 -n 5
```

### axcl_sample_dmadim

DMA 示例，包括：

通过 `AXCL_DMA_MemCopy` 在两个设备内存之间进行内存拷贝 (memcpy)

通过 `AXCL_DMA_MemCopy` 将设备内存置为 0xAB (memset)

通过 `AXCL_DMA_CheckSum` 计算校验和 (checksum)

通过 `AXCL_DMA_MemCopyXD` (`AX_DMADIM_2D`) 从 (0, 0) 开始裁剪 1/4 图像

#### 用法

```bash
usage: ./axcl_sample_dmadim --image=string --width=unsigned int --height=unsigned int [options] ...
options:
  -d, --device    device index from 0 to connected device num - 1 (unsigned int [=0])
  -i, --image     nv12 image file path (string)
  -w, --width     width of nv12 image (unsigned int)
  -h, --height    height of nv12 image (unsigned int)
      --json      axcl.json path (string [=./axcl.json])
  -?, --help      print this message
```

| 参数         | 默认值                            | 描述               |
| ------------ | --------------------------------- | ------------------ |
| -d, --device | 0, 范围: \[0 - 已连接设备数量 -1] | 指定设备索引。     |
| --json       | [axcl.json](#json)                | 文件路径           |
| -i, --image  | NA                                | 输入图像文件路径。 |
| -w, --width  | NA                                | 输入图像的宽度。   |
| -h, --height | NA                                | 输入图像的高度。   |

#### 示例

```bash
$ axcl_sample_dmadim -i 1920x1080.nv12.yuv -w 1920 -h 1080 -d 0
[INFO ][                            main][  30]: ============== V3.5.0_20250515190238 sample started May 15 2025 19:29:17 ==============

[INFO ][                            main][  46]: json: ./axcl.json
json file
[INFO ][                            main][  66]: device index: 0, bus number: 3
[INFO ][                        dma_copy][ 119]: dma copy device memory succeed, from 0x14926f000 to 0x14966f000
[INFO ][                      dma_memset][ 139]: dma memset device memory succeed, 0x14926f000 to 0xab
[INFO ][                    dma_checksum][ 166]: dma checksum succeed, checksum = 0xaaa00000
[INFO ][                      dma_copy2d][ 281]: [0] dma memcpy 2D succeed
[INFO ][                      dma_copy2d][ 281]: [1] dma memcpy 2D succeed
[INFO ][                      dma_copy2d][ 308]: ./dma2d_output_image_960x540.nv12 is saved
[INFO ][                      dma_copy2d][ 328]: dma copy2d nv12 image pass
[INFO ][                            main][  82]: ============== V3.5.0_20250515190238 sample exited May 15 2025 19:29:17 ==============
```

### axcl_sample_ive

智能视频引擎 (IVE) 的示例。

**注意：**

- 示例代码仅用于 API 演示，但实际上需要根据用户上下文使用特定的配置参数。

- 关于参数限制，请参阅名为 `42 - AX IVE API` 的文档。

- 填充输入和输出数据的内存必须由用户分配。

- 输入和输出的图像数据必须由用户指定。

- 来自不同 CV 的输入图像（或数据）数量可能不同。

- 必须明确定义二维图像的数据类型，或使用默认值。

- 这些关键参数格式化为 Json 字符串或 Json 文件。请参考 /opt/data/ive/ 某些目录中的 .json 文件和代码。

#### 用法

```bash
m5stack@raspberrypi5:~ $ axcl_sample_ive --help
Usage : axcl_sample_ive -c case_index [options]
        -d | --device_id: Device index from 0 to connected device num - 1, optional
        -c | --case_index:Calc case index, default:0
                0-DMA.
                1-DualPicCalc.
                2-HysEdge and CannyEdge.
                3-CCL.
                4-Erode and Dilate.
                5-Filter.
                6-Hist and EqualizeHist.
                7-Integ.
                8-MagAng.
                9-Sobel.
                10-GMM and GMM2.
                11-Thresh.
                12-16bit to 8bit.
                13-Multi Calc.
                14-Crop and Resize.
                15-CSC.
                16-CropResize2.
                17-MatMul.
        -e | --engine_choice:Choose engine id, default:0
                0-IVE; 1-TDP; 2-VGP; 3-VPP; 4-GDC; 5-DSP; 6-NPU; 7-CPU; 8-MAU.
                For Crop and Resize case, cropimage support IVE/VGP/VPP engine, cropresize and cropresize_split_yuv support VGP/VPP engine.
                For CSC case, support TDP/VGP/VPP engine.
                For CropResize2 case, support VGP/VPP engine.
                For MatMul case, support NPU/MAU engine.
        -m | --mode_choice:Choose test mode, default:0
                For DualPicCalc case, indicate dual pictures calculation task:
                  0-add; 1-sub; 2-and; 3-or; 4-xor; 5-mse.
                For HysEdge and CannyEdge case, indicate hys edge or canny edge calculation task:
                  0-hys edge; 1-canny edge.
                For Erode and Dilate case, indicate erode or dilate calculation task:
                  0-erode; 1-dilate.
                For Hist and EqualizeHist case, indicate hist or equalize hist calculation task:
                  0-hist; 1-equalize hist.
                For GMM and GMM2 case, indicate gmm or gmm2 calculation task:
                  0-gmm; 1-gmm2.
                For Crop and Resize case, indicate cropimage, cropresize, cropresize_split_yuv calculation task:
                  0-crop image; 1-crop_resize; 2-cropresize_split_yuv.
                For CropResize2 case, indicate crop_resize2 or cropresize2_split_yuv calculation task:
                  0-crop_resize2; 1-cropresize2_split_yuv.
        -t | --type_image:Image type index refer to IVE_IMAGE_TYPE_E(IVE engine) or AX_IMG_FORMAT_E(other engine)
                Note:
                  1. For all case, both input and output image types need to be specified in the same order as the specified input and output file order.
                  2. If no type is specified, i.e. a type value of -1 is passed in, then a legal type is specified, as qualified by the API documentation.
                  3. Multiple input and output image types, separated by spaces.
                  4. For One-dimensional data (such as AX_IVE_MEM_INFO_T type data), do not require a type to be specified.
        -i | --input_files:Input image files, if there are multiple inputs, separated by spaces.
        -o | --output_files:Output image files or dir, if there are multiple outputs, separated by spaces
                Note:for DMA, Crop Resize, blob of CCL case and CropResize2 case must be specified as directory.
        -w | --width:Image width of inputs, default:1280.
        -h | --height:Image height of inputs, default:720.
        -p | --param_list:Control parameters list or file(in json data format)
                Note:
                  1. Please refer to the json file in the '/opt/data/ive/' corresponding directory of each test case.
                  2. For MagAng, Multi Calc and CSC case, no need control parameters.
        -a | --align_need:Does the width/height/stride need to be aligned automatically, default:0.
                  0-no; 1-yes.
        -? | --help:Show usage help.
```

#### 示例 1

DMA 用法 (源分辨率: 1280 x 720, 输入 / 输出类型 : U8C1, 使用 Json 文件配置控制参数)

```bash
$ axcl_sample_ive -c 0 -w 1280 -h 720 -i /opt/data/ive/common/1280x720_u8c1_gray.yuv -o /opt/data/ive/dma/ -t 0 0 -p /opt/data/ive/dma/dma.json
```

#### 示例 2

MagAndAng 用法 (源分辨率: 1280 x 720, 输入参数 (grad_h, grad_v) 的数据类型: U16C1, 输出参数 (ang_output) 的数据类型 : U8C1)

```bash
$ axcl_sample_ive -c 8 -w 1280 -h 720 -i /opt/data/ive/common/1280x720_u16c1_gray.yuv /opt/data/ive/common/1280x720_u16c1_gray_2.yuv -o /opt/data/ive/common/mag_output.bin /opt/data/ive/common/ang_output.bin -t 9 9 9 0
```

#### json

1. **dma.json**
   - `mode`, `x0`, `y0`, `h_seg`, `v_seg`, `elem_size` and `set_val` are the value of respective member in structure `AX_IVE_DMA_CTRL_T` such as `enMode`, `u16CrpX0`, `u16CrpY0`, `u8HorSegSize`, `u8VerSegRows`, `u8ElemSize`, `u64Val`.
   - `w_out` and `h_out` is respectivly the width and height of output image, only for `AX_IVE_DMA_MODE_DIRECT_COPY` mode in DMA.
2. **dualpics.json**
   - `x` and `y` are the value of `u1q7X` and `u1q7Y` in structure `AX_IVE_ADD_CTRL_T` for ADD CV.
   - `mode` is the value of `enMode` in structure `AX_IVE_SUB_CTRL_T` for Sub CV.
   - `mse_coef` is the value of `u1q15MseCoef` in structure `AX_IVE_MSE_CTRL_T` for MSE CV.
3. **ccl.json**
   - `mode` is the value of `enMode` of structure `AX_IVE_CCL_CTRL_T` for CCL CV.
4. **ed.json**
   - `mask` is all values of `au8Mask[25]` in structure `AX_IVE_ERODE_CTRL_T` for Erode CV or `AX_IVE_DILATE_CTRL_T` for Dilate CV.
5. **filter.json**
   - `mask` is all values of `as6q10Mask[25]` in structure `AX_IVE_FILTER_CTRL_T` for Filter CV.
6. **hist.json**
   - `histeq_coef` is the value of `u0q20HistEqualCoef` in structure `AX_IVE_EQUALIZE_HIST_CTRL_T` for EqualizeHist CV.
7. **integ.json**
   - `out_ctl` is the value of `enOutCtrl` in structure `AX_IVE_INTEG_CTRL_T` for Integ CV.
8. **sobel.json**
   - `mask` is the value of `as6q10Mask[25]` in structure `AX_IVE_SOBEL_CTRL_T` for Sobel CV.
9. **gmm.json**
   - `init_var`, `min_var`, `init_w`, `lr`, `bg_r`, `var_thr` and `thr` are respectivly the value of `u14q4InitVar`, `u14q4MinVar`, `u1q10InitWeight`, `u1q7LearnRate`, `u1q7BgRatio`, `u4q4VarThr` and `u8Thr` in structure `AX_IVE_GMM_CTRL_T` for GMM CV.
10. **gmm2.json:**
    - `init_var`, `min_var`, `max_var`, `lr`, `bg_r`, `var_thr`, `var_thr_chk`, `ct` and `thr` are respectivly the value of `u14q4InitVar`, `u14q4MinVar`, `u14q4MaxVar`, `u1q7LearnRate`, `u1q7BgRatio`, `u4q4VarThr`, `u4q4VarThrCheck`, `s1q7CT` and `u8Thr` in structure `AX_IVE_GMM2_CTRL_T` for GMM2 CV.
11. **thresh.json**
    - `mode`, `thr_l`, `thr_h`, `min_val`, `mid_val` and `max_val` are repectivly the value of `enMode`, `u8LowThr`, `u8HighThr`, `u8MinVal`, `u8MidVal` and `u8MaxVal` in structure `AX_IVE_THRESH_CTRL_T` for Thresh CV.
12. **16bit_8bit.json**
    - `mode`, `gain` and `bias` are repectivly the value of `enMode`, `s1q14Gain` and `s16Bias` in structure `AX_IVE_16BIT_TO_8BIT_CTRL_T` for 16BitTo8Bit CV.
13. **crop_resize.json**
    - When CropImage is enabled, num is the value of `u16Num` in structure `AX_IVE_CROP_IMAGE_CTRL_T` and boxs is the array type of crop image in which `x`,`y`,`w` and `h` are respecivly the value of `u16X`, `u16Y`, `u16Width` and `u16Height` in structure `AX_IVE_RECT_U16_T`.
    - When CropResize or CropResizeForSplitYUV mode is enabled, `num` is the value of `u16Num` in structure `AX_IVE_CROP_RESIZE_CTRL_T` and `align0`, `align1`, `enAlign[1]`, `bcolor`, `w_out` and `h_out` are respectivly the value of `enAlign[0]`, `enAlign[1]`, `u32BorderColor`, `width` and `height` of output image.
14. **crop_resize2.json**
    - `num` is the value of `u16Num` in structure `AX_IVE_CROP_IMAGE_CTRL_T`.
    - `res_out` is the arrayes of width and height of output image.
    - **`src_boxs` is the array of cropped range from source image, `dst_boxs` is the array of range to resized image.**
15. **matmul.json**
    - `mau_i`, `ddr_rdw`, `en_mul_res`, `en_topn_res`, `order` and `topn` are respectivly the value of `enMauId`, `s32DdrReadBandwidthLimit`, `bEnableMulRes`, `bEnableTopNRes`, `enOrder` and `s32TopN` in structure `AX_IVE_MAU_MATMUL_CTRL_T`.
    - `type_in` is the value of `stMatQ` and `stMatB` in structure `AX_IVE_MAU_MATMUL_INPUT_T`.
    - `type_mul_res` and `type_topn_res` are the value of `stMulRes` and `sfTopNRes` in structure `AX_IVE_MAU_MATMUL_OUTPUT_T`.
    - `q_shape` and `b_shape` are the value of `pShape` in `stMatQ` and `stMatB` of structure `AX_IVE_MAU_MATMUL_INPUT_T`

### axcl_sample_ivps

图像视频处理系统 (IVPS) 的示例，提供裁剪、缩放、旋转、流化、CSC、OSD、马赛克、四边形等功能。

#### 用法

```bash
m5stack@raspberrypi5:~ $ axcl_sample_ivps -h
AXCL IVPS Sample. Build at Jul 22 2025 02:31:34
axcl_sample_ivps: option requires an argument -- 'h'
INFO   :[IVPS_ArgsParser:698] pipeline_ini: (null)
INFO   :[IVPS_ArgsParser:699] region_ini: (null)
Usage: /axcl_sample_ivps
        -d             (required) : device index from 0 to connected device num - 1
        -v             (required) : video frame input
        -g             (optional) : overlay input
        -s             (optional) : sp alpha input
        -n             (optional) : repeat number
        -r             (optional) : region config and update
        -l             (optional) : 0: no link 1. link ivps. 2: link venc. 3: link jenc
        --pipeline     (optional) : import ini file to config all the filters in one pipeline
        --pipeline_ext (optional) : import ini file to config all the filters in another pipeline
        --change       (optional) : import ini file to change parameters for one filter dynamicly
        --region       (optional) : import ini file to config region parameters
        --dewarp       (optional) : import ini file to config dewarp parameters, including LDC, perspective, fisheye, etc.
        --cmmcopy      (optional) : cmm copy API test
        --csc          (optional) : color space covert API test
        --fliprotation (optional) : flip and rotation API test
        --alphablend   (optional) : alpha blending API test
        --cropresize   (optional) : crop resize API test
        --osd          (optional) : draw osd API test
        --cover        (optional) : draw line/polygon API test
        -a             (optional) : all the sync API test

        --json         (optional) : axcl.json path

            -v  <PicPath>@<Format>@<Stride>x<Height>@<CropW>x<CropH>[+<CropX0>+<CropY0>]>
           e.g: -v /opt/bin/data/ivps/800x480car.nv12@3@800x480@600x400+100+50

           [-g] <PicPath>@<Format>@<Stride>x<Height>[+<DstX0>+<DstY0>*<Alpha>]>
           e.g: -g /opt/bin/data/ivps/rgb400x240.rgb24@161@400x240+100+50*150

           [-n] <repeat num>]
           [-r] <region num>]

        <PicPath>                     : source picture path
        <Format>                      : picture color format
                   3: NV12     YYYY... UVUVUV...
                   4: NV21     YYYY... VUVUVU...
                  10: NV16     YYYY... UVUVUV...
                  11: NV61     YYYY... VUVUVU...
                 161: RGB888   24bpp
                 165: BGR888   24bpp
                 160: RGB565   16bpp
                 197: ARGB4444 16bpp
                 203: RGBA4444 16bpp
                 199: ARGB8888 32bpp
                 201: RGBA8888 32bpp
                 198: ARGB1555 16bpp
                 202: RGBA5551 16bpp
                 200: ARGB8565 24bpp
                 204: RGBA5658 24bpp
                 205: ABGR4444 16bpp
                 211: BGRA4444 16bpp
                 207: ABGR8888 32bpp
                 209: BGRA8888 32bpp
                 206: ABGR1555 16bpp
                 210: BGRA5551 16bpp
                 208: ABGR8565 24bpp
                 212: BGRA5658 24bpp
                 224: BITMAP    1bpp
        <Stride>           (required) : picture stride (16 bytes aligned)
        <Stride>x<Height>  (required) : input frame stride and height (2 aligned)
        <CropW>x<CropH>    (required) : crop rect width & height (2 aligned)
        +<CropX0>+<CropY0> (optional) : crop rect coordinates
        +<DstX0>+<DstY0>   (optional) : output position coordinates
        <Alpha>            (optional) : ( (0, 255], 0: transparent; 255: opaque)

Example1:
        /axcl_sample_ivps -d 0 -v /opt/data/ivps/1920x1088.nv12@3@1920x1088@1920x1088  -n 1
```

**注意：**

- **-v** 是必选项，带有输入源图像路径和帧信息。
  裁剪窗口应在源图像的高度范围内，即 CropX0 + CropW <= Stride, CropY0 + CropH <= Height。
  如果不进行裁剪，则 CropW = Width, CropH = Height, CropX0 = 0, and CropY0 = 0。

- **-n** 表示对源图像处理指定的次数。如果参数为 -1，则将一直循环执行。
  如果要查看 IVPS 的 proc 信息，需要将处理次数设置为较大的值或一直循环。

- **-r** 后面的输入参数是叠加的 REGION 数量，当前最大为 4。
  在 IVPS PIPELINE 上叠加 REGION 是异步操作，需要几帧之后才能真正叠加到输入源图像上。
  因此，如果要验证 REGION 功能，需要将 -n 后面的参数设置得更大，该值应大于 3.2。

#### 示例 1

处理源图像 (3840x2160 NV12 格式) 一次

```bash
$ axcl_sample_ivps -v /opt/data/ivps/3840x2160.nv12@3@3840x2160@0x0+0+0 -d 0 -n 1
```

#### 示例 2

处理源图像 (800x480 RGB 888 格式) 并进行裁剪 (X0=128 Y0=50 W=400 H=200)，处理三次

```bash
$ axcl_sample_ivps -v /opt/data/ivps/800x480logo.rgb24@161@800x480@400x200+128+50 -d 0 -n 3
```

#### 示例 3

处理源图像 (3840x2160 NV12 格式) 五次，并叠加三个 REGION

```bash
$ axcl_sample_ivps -v /opt/data/ivps/3840x2160.nv12@3@3840x2160@0x0+0+0 -d 0 -n 5 -r 3
```

### axcl_sample_transcode

转码示例，其流水线 (PPL) 如下所示：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/transcode_ppl.png" width="100%" />

1. 加载 .mp4 文件或 .h264/.h265 原始码流文件。

2. 通过 ffmpeg 解复用 nalu

3. 将 nalu 帧发送到 VDEC

4. VDEC 将解码后的 nv12 发送到 IVPS (如果调整大小)

5. IVPS 将 nv12 发送到 VENC

6. 通过 VENC 将编码后的 nalu 帧发送到主机。

#### deployment

```bash
| ----------------------------- |
| sample                        |
| ----------------------------- |
| libaxcl_ppl.so                |
| ----------------------------- |
| libaxcl_lite.so               |
| ----------------------------- |
| AXCL SDK                      |
| ----------------------------- |
```

#### attributes

```bash
        attribute name                       R/W    attribute value type
 *  axcl.ppl.transcode.vdec.grp             [R  ]       int32_t                            allocated by ax_vdec.ko
 *  axcl.ppl.transcode.ivps.grp             [R  ]       int32_t                            allocated by ax_ivps.ko
 *  axcl.ppl.transcode.venc.chn             [R  ]       int32_t                            allocated by ax_venc.ko
 *
 *  the following attributes take effect BEFORE the axcl_ppl_create function is called:
 *  axcl.ppl.transcode.vdec.blk.cnt         [R/W]       uint32_t          8                depend on stream DPB size and decode mode
 *  axcl.ppl.transcode.vdec.out.depth       [R/W]       uint32_t          4                out fifo depth
 *  axcl.ppl.transcode.ivps.in.depth        [R/W]       uint32_t          4                in fifo depth
 *  axcl.ppl.transcode.ivps.out.depth       [R  ]       uint32_t          0                out fifo depth
 *  axcl.ppl.transcode.ivps.blk.cnt         [R/W]       uint32_t          4
 *  axcl.ppl.transcode.ivps.engine          [R/W]       uint32_t   AX_IVPS_ENGINE_VPP      AX_IVPS_ENGINE_VPP|AX_IVPS_ENGINE_VGP|AX_IVPS_ENGINE_TDP
 *  axcl.ppl.transcode.venc.in.depth        [R/W]       uint32_t          4                in fifo depth
 *  axcl.ppl.transcode.venc.out.depth       [R/W]       uint32_t          4                out fifo depth

NOTE:
 The value of "axcl.ppl.transcode.vdec.blk.cnt" depends on input stream.
 Usually set to dpb + 1
```

#### 用法

```bash
$ axcl_sample_transcode --help
usage: axcl_sample_transcode --url=string [options] ...
options:
  -i, --url       mp4|.264|.265 file path (string)
  -d, --device    device index from 0 to connected device num - 1 (unsigned int [=0])
  -w, --width     output width, 0 means same as input (unsigned int [=0])
  -h, --height    output height, 0 means same as input (unsigned int [=0])
      --codec     encoded codec: [h264 | h265] (default: h265) (string [=h265])
      --json      axcl.json path (string [=./axcl.json])
      --loop      1: loop demux for local file  0: no loop(default) (int [=0])
      --dump      dump file path (string [=])
      --hwclk     decoder hw clk, 0: 624M, 1: 500M, 2: 400M(default) (unsigned int [=2])
      --ut        unittest
  -?, --help      print this message
```

| 参数         | 默认值                            | 描述                               |
| ------------ | --------------------------------- | ---------------------------------- |
| -d, --device | 0, 范围：\[0 - 已连接设备数量 -1] | 指定设备索引。                     |
| --json       | [axcl.json](#json)                | 文件路径                           |
| -i, --url    | NA                                | 指定流文件的路径。                 |
| -w, --width  | 1920                              | 指定解码的 YUV 图像的宽度。        |
| -h, --height | 1080                              | 指定解码的 YUV 图像的高度。        |
| --codec      | h265                              | 指定载荷类型。                     |
| --loop       | 0                                 | 1: 循环转码直到 CTRL+C 0: 不循环。 |
| --dump       |                                   | 指定转储文件路径。                 |
| --hwclk      | 2 (400M)                          | 以 MHz 为单位设置 VDEC 的时钟。    |
| --ut         |                                   | 内部使用                           |

如果出现以下错误：

```bash
m5stack@raspberrypi5:~ $ axcl_sample_transcode --help
axcl_sample_transcode: error while loading shared libraries: libavcodec.so.61: cannot open shared object file: No such file or directory

m5stack@raspberrypi5:~ $ export LD_LIBRARY_PATH=/usr/lib/axcl/ffmpeg:$LD_LIBRARY_PATH
```

请先通过 `export LD_LIBRARY_PATH=/usr/lib/axcl/ffmpeg:$LD_LIBRARY_PATH` 设置环境变量。

#### 示例

将输入的 1080P@30fps 264 转码为 1080P@30fps 265，并保存到 `/tmp/axcl/transcode.dump.pidxxx` 文件中。

```bash
$ axcl_sample_transcode -i bangkok_30952_1920x1080_30fps_gop60_4Mbps.mp4 -d 0 --dump /tmp/axcl/transcode.265
[INFO ][                            main][  67]: ============== V3.5.0_20250515190238 sample started May 15 2025 19:29:29 pid 91189 ==============

[WARN ][                            main][  92]: if enable dump, disable loop automatically
json file
[INFO ][                            main][ 131]: pid: 91189, device index: 0, bus number: 3
[INFO ][             ffmpeg_init_demuxer][ 439]: [91189] url: bangkok_30952_1920x1080_30fps_gop60_4Mbps.mp4
[INFO ][             ffmpeg_init_demuxer][ 502]: [91189] url bangkok_30952_1920x1080_30fps_gop60_4Mbps.mp4: codec 96, 1920x1080, fps 30
[INFO ][         ffmpeg_set_demuxer_attr][ 571]: [91189] set ffmpeg.demux.file.frc to 1
[INFO ][         ffmpeg_set_demuxer_attr][ 574]: [91189] set ffmpeg.demux.file.loop to 0
[INFO ][                            main][ 195]: pid 91189: [vdec 00] - [ivps -1] - [venc 00]
[INFO ][                            main][ 213]: pid 91189: VDEC attr ==> blk cnt: 8, fifo depth: out 4
[INFO ][                            main][ 214]: pid 91189: IVPS attr ==> blk cnt: 5, fifo depth: in 4, out 0, engine 1
[INFO ][                            main][ 216]: pid 91189: VENC attr ==> fifo depth: in 4, out 4
[INFO ][          ffmpeg_dispatch_thread][ 189]: [91189] +++
[INFO ][             ffmpeg_demux_thread][ 295]: [91189] +++
[INFO ][             ffmpeg_demux_thread][ 328]: [91189] reach eof
[INFO ][             ffmpeg_demux_thread][ 435]: [91189] demuxed    total 470 frames ---
[INFO ][          ffmpeg_dispatch_thread][ 272]: [91189] dispatched total 470 frames ---
[INFO ][                            main][ 247]: ffmpeg (pid 91189) demux eof
[2025-05-20 22:49:08.834][91195][W][axclite-venc-dispatch][dispatch_thread][44]: no stream in veChn 0 fifo
[INFO ][                            main][ 283]: total transcoded frames: 470
[INFO ][                            main][ 284]: ============== V3.5.0_20250515190238 sample exited May 15 2025 19:29:29 pid 91189 ==============
```

launch_transcode.sh 支持启动多个（最多 16 个）axcl_sample_transcode 并自动配置 LD_LIBRARY_PATH。

```bash
$ ./launch_transcode.sh 16 -i bangkok_30952_1920x1080_30fps_gop60_4Mbps.mp4  -d 3 --dump /tmp/axcl/transcode.265
```

\#> 第一个参数必须是 axcl_sample_transcode 进程的数量。范围: \[1, 16]
