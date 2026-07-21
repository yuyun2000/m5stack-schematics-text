# [Atomic GPS Base](/zh_CN/atom/Atomic%20GPS%20Base)

## 案例程序

获取时间，经纬度，和高度数据打印到串口中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_atomic_base_gps_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.GPS import GPS
import time

gps.deinit()
while True:
  print(gps.timestamp)
  print(gps.latitude)
  print(gps.longitude)
  print(gps.altitude)
  wait(2)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_deinit.svg">

```python
gps.deinit()
```

- 关闭或重置 GPS 模块的初始化设置，释放资源。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_init.svg">

```python
gps = GPS(0, '')
```

- 初始化 GPS 模块并设置时区。
  - timezone 用于设定时区偏移量。
  - formatting 指定时间格式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_init_sdcard.svg">

```python
gps._tf.init_sdcard(33, 19, 23, 20000000)
```

- 配置与 SD 卡通信的引脚以及 SPI 通信的频率。配置了 MISO(引脚33)，MOSI(引脚19)，SCK(引脚23)以及通信频率(20000000Hz)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_altitude.svg">

```python
gps.altitude
```

- 从 GPS 模块获取海拔信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_course.svg">

```python
gps.course
```

- 从 GPS 模块获取当前的航向(行驶方向)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_date.svg">

```python
gps.date
```

- 从 GPS 模块获取当前的日期信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_geoid_height.svg">

```python
gps.geoid_height
```

- 从 GPS 模块获取当前的位置的地球大地水准面高度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_hdop.svg">

```python
gps.hdop
```

- 获取 GPS 的水平精度(HDOP，Horizontal Dilution of Precision)，表示定位的准确度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_last_sv_sentence.svg">

```python
gps.last_sv_sentence
```

- 获取最后一次收到的 SV(卫星可见度)语句，通常用于调试 GPS 信号。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_latitude.svg">

```python
gps.latitude
```

- 获取当前位置的纬度值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_longitude.svg">

```python
gps.longitude
```

- 获取当前位置的经度值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_open_sdcard_file.svg">

```python
with open('/sd/', 'a')
  pass
```

- 在 SD 卡上以指定模式打开文件。path 指定文件路径，mode 指定打开模式(如读、写、追加等)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_pdop.svg">

```python
passprint(gps.pdop)
```

- 获取位置精度因子(PDOP，Position Dilution of Precision)，表示定位精度的一个指标。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_satellites_in_use.svg">

```python
gps.satellites_in_use
```

- 获取当前正在使用的卫星数量，用于计算当前位置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_satellites_in_view.svg">

```python
gps.satellites_in_view
```

- 获取当前可见的卫星数量，即设备可以检测到的卫星总数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_satellites_used.svg">

```python
gps.satellites_used
```

- 获取实际用于定位的卫星数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_satellite_data.svg">

```python
gps.satellite_data
```

- 从 GPS 模块获取当前卫星数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_file_get_seek.svg">

```python
fs.tell()
```

- 获取当前文件的读取位置指针。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_file_read.svg">

```python
fs.read(0)
```

- 从文件中读取指定数量的字节。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_file_read_all.svg">

```python
fs.read()
```

- 读取文件中的所有内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_file_read_line.svg">

```python
fs.readline()
```

- 从文件中读取一行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_file_set_seek.svg">

```python
fs.seek(0)
```

- 设置文件的指针位置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_file_write.svg">

```python
fs.write('')
```

- 将指定的文本写入文件。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_isdirectory.svg">

```python
gps._tf.is_folder_exist('')
```

- 检查指定路径的文件夹是否存在。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_isfile.svg">

```python
gps._tf.is_file_exist('')
```

- 检查指定路径的文件是否存在。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_listdir.svg">

```python
gps._tf.show_directory('')
```

- 显示指定路径中的文件和文件夹列表。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_mkdir.svg">

```python
gps._tf.create_folder('')
```

- 在指定路径创建一个新的文件夹。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_remove.svg">

```python
gps._tf.delete_file('')
```

- 删除指定路径的文件。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_rename.svg">

```python
gps._tf.rename_file('','')
```

- 将文件从旧路径重命名为新路径。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_sdcard_rmdir.svg">

```python
gps._tf.delete_folder('')
```

- 删除指定路径的文件夹。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_speed.svg">

```python
gps.speed
```

- 从 GPS 模块中获取当前速度数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_timestamp.svg">

```python
gps.timestamp
```

- 从 GPS 模块获取当前的时间戳信息，通常是从卫星信号中获得的精确时间。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_total_sv_sentence.svg">

```python
gps.total_sv_sentence
```

- 获取总的卫星可见性(SV)信息句子数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/gps/uiflow_block_base_gps_vdop.svg">

```python
gps.vdop
```

- 获取垂直精度衰减因子 (Vertical Dilution of Precision, VDOP)，它表示高度定位精度的一个衡量指标。

