# [Atomic SPK Base](/zh_CN/atom/Atomic%20SPK%20Base)

## 案例程序

该程序配置了 SD 卡以播放 WAV 音频文件，并执行文件读写操作。当按下按钮 A 时，标志变量`flag`设置为1，触发写入随机数到“test.txt”文件。如果 SD 卡写入成功，RGB 灯变为黄色，否则变为红色。然后尝试从文件中读取数据并将其转换为音频频率播放，成功时 RGB 灯变为绿色，否则为红色。最后，`flag`复位为0。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_atomic_base_spk_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.Speaker import Speaker
import time

flag = None
random_num = None
read_data = None

spk = Speaker()

import random

def buttonA_wasPressed():
  global flag, random_num, read_data
  flag = 1
  pass
btnA.wasPressed(buttonA_wasPressed)

flag = 0
spk._tf.init_sdcard(33, 19, 23, 20000000)
spk.playWAV('res/mix.wav', rate=44100, data_format=Speaker.F32B, channel=Speaker.CHN_L, volume=0)
while True:
  random_num = random.randint(100000000, 999999999)
  if flag:
    try :
      with open('/sd/test.txt', 'w+') as fs:
        fs.write(str(random_num))
        rgb.setColorAll(0xffff00)
      pass
    except:
      print('cannot write, please check the sdcard')
      rgb.setColorAll(0xff0000)
    wait_ms(100)
    try :
      with open('/sd/test.txt', 'r+') as fs:
        read_data = fs.read()
        print(read_data)
        spk.playTone(int((int(read_data) / 250000)), 1, volume=0)
        rgb.setColorAll(0x33cc00)
      pass
    except:
      print('cannot read, please check the sdcard')
      rgb.setColorAll(0xff0000)
    flag = 0
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_init_sdcard.svg">

```python
spk._tf.init_sdcard(33, 19, 23, 20000000)
```

- 初始化 SD 卡的 SPI 通信接口，指定 MISO、MOSI 和 SCK 引脚的连接，并设置通信频率为20MHz。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_open_sdcard_file.svg">

```python
with open('/sd/', 'a')
  pass
```

- 打开指定路径的文件，模式为"a"(追加模式)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_play_cloud_wav.svg">

```python
passspk.playCloudWAV('', volume=0)
```

- 播放来自云端的 WAV 格式音频文件，并设置音量为0(静音)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_play_sing.svg">

```python
spk.playTone(220, 1, volume=0)
```

- 播放低 A 音符，持续1拍，音量为0。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_play_tone.svg">

```python
spk.playTone(220, 1, volume=0)
```

- 以220Hz 频率播放音调，持续1拍，音量为0。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_play_wav_dropdown.svg">

```python
spk.playWAV('', volume=0)
```

- 播放本地的 WAV 文件，音量为0(静音)，文件暂时为空。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_play_wav_file.svg">

```python
spk.playWAV('', volume=0)
```

- 播放本地文件夹中的 WAV 格式音频文件，音量为0。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_play_wav_rate.svg">

```python
spk.playWAV('', rate=44100, data_format=Speaker.F16B, channel=Speaker.CHN_LR, volume=0)
```

- 用于从 SD 卡或本地文件系统中读取 WAV 格式的音频文件并进行播放，适合用于本地音乐或提示音的播放场景
    - Play local WAV file：指定要播放的本地 WAV 文件路径。
    - samplerate 44100：音频的采样率设置为44100Hz，这是 CD 音质的标准采样率。
    - data format 16Bit：指定数据格式为16位，这是常见的音频位深，表示每个采样点的位数。
    - channel left and right：选择立体声输出，使用左声道和右声道一起播放音频。  
    - volume 0：设置音量为0，表示静音播放。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_file_get_seek.svg">

```python
fs.tell()
```

- ui 获取当前文件指针的位置，文件指针指示了文件中当前位置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_file_read.svg">

```python
fs.read(0)
```

- 从文件中读取指定的字节数(X 为读取的字节数)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_file_read_all.svg">

```python
fs.read()
```

- 读取文件的全部内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_file_read_line.svg">

```python
fs.readline()
```

- 从文件中读取一行数据，适用于文本文件逐行读取。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_file_set_seek.svg">

```python
fs.seek(0)
```

- 设置文件指针的位置，用于控制从文件的哪个位置开始读写操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_file_write.svg">

```python
fs.write('')
```

- 将指定的文本内容写入文件。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_isdirectory.svg">

```python
spk._tf.is_folder_exist('')
```

- 检查指定路径的文件夹是否存在。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_isfile.svg">

```python
spk._tf.is_file_exist('')
```

- 检查指定路径下的文件是否存在。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_listdir.svg">

```python
spk._tf.show_directory('')
```

- 显示指定路径下的文件和文件夹列表，列出目录中的内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_mkdir.svg">

```python
spk._tf.create_folder('')
```

- 在指定路径下创建一个新的文件夹。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_remove.svg">

```python
spk._tf.delete_file('')
```

- 删除指定路径下的文件。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_rename.svg">

```python
spk._tf.rename_file('','')
```

- 重命名文件，将文件从旧路径移动到新路径，或者更改文件名。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/spk/uiflow_block_base_spk_sdcard_rmdir.svg">

```python
spk._tf.delete_folder('')
```

- 删除指定路径下的文件夹。

