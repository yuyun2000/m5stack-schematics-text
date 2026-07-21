# [Atomic TF Card Base](/zh_CN/atom/Atomic%20TF-Card%20Reader)

## 案例程序

该程序使用 SD 卡进行文件和文件夹的创建、删除、重命名和读写操作。主要步骤如下：
1. 配置 SD 卡引脚并删除`m5test.txt`文件和`m5 folder`文件夹(如果存在)。
2. 创建并写入文本文件`m5.txt`，内容为“welcome to M5”，然后读取并打印文件内容。
3. 检查`m5test.txt`文件是否存在，并打印检查结果。
4. 重命名`m5.txt`文件为`m5test.txt`，并再次检查其是否存在。
5. 在`m5 folder`中创建`m5test.txt`文件并追加写入“hello to M5”，然后读取并打印全部内容。 Base

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_atomic_base_tfcard_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.TF_Card import TFCARD

tf = TFCARD()

tf.init_sdcard(33, 19, 23, 20000000)
tf.delete_file('m5test.txt')
tf.delete_folder('m5 folder')
with open('/sd/m5.txt', 'w+') as fs:
  fs.write('welcome to M5')
with open('/sd/m5.txt', 'r+') as fs:
  print(fs.read())
print(tf.show_directory(''))
if tf.is_file_exist('m5test.txt'):
  print('file is exist')
else:
  print('file is not exist')
tf.rename_file('m5.txt','m5test.txt')
tf.create_folder('m5 folder')
print(tf.show_directory(''))
if tf.is_file_exist('m5test.txt'):
  print('file is exist')
else:
  print('file is not exist')
with open('/sd/m5test.txt', 'a') as fs:
  fs.write('hello to M5')
with open('/sd/m5test.txt', 'r+') as fs:
  print(fs.read())
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_init_sdcard.svg">

```python
tf.init_sdcard(33, 19, 23, 20000000)
```

- 初始化 SD 卡的接口配置，指定了 MISO、MOSI、SCK 引脚和工作频率。此操作用于 SD 卡的通信设置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_file_get_seek.svg">

```python
fs.tell()
```

- 获取文件的当前读取位置(seek)。这用于文件操作中记录文件指针位置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_file_read.svg">

```python
fs.read(0)
```

- 从文件中读取指定字节数的数据。该语句用于读取文件内容，读取的字节数可以在参数中设定。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_file_read_all.svg">

```python
fs.read()
```

- 读取文件中的所有内容。该功能块一次性读取整个文件内容，适合处理较小的文件。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_file_read_line.svg">

```python
fs.readline()
```

- 读取文件中的一行内容。用于按行处理文本文件的数据读取操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_file_set_seek.svg">

```python
fs.seek(0)
```

- 设置文件的读取位置。可以将文件指针移动到文件的某个特定位置，以便进行读取或写入操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_file_write.svg">

```python
fs.write('')
```

- 将文本写入文件。这个语句将指定的文本内容写入文件中，通常用于记录或保存数据到 SD 卡。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_isdirectory.svg">

```python
tf.is_folder_exist('')
```

- 检查指定路径下的文件夹是否存在。如果文件夹存在，将返回真(True)，否则返回假(False)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_isfile.svg">

```python
tf.is_file_exist('')
```

- 检查指定路径下的文件是否存在。返回的结果与文件夹存在检查相似。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_listdir.svg">

```python
tf.show_directory('')
```

- 显示指定路径下的文件和文件夹列表。这是列出某个目录内容的操作，方便用户查看存储的文件和文件夹。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_mkdir.svg">

```python
tf.create_folder('')
```

- 在指定路径创建一个新的文件夹。如果路径有效且权限允许，系统会在该路径下生成一个新的文件夹。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_open_tfcard_file.svg">

```python
with open('/sd/', 'a')
```

- 打开指定路径下的文件，并根据设定的模式(例如读取、写入等模式)对文件进行操作。不同的模式控制文件的打开方式(例如读、写、追加等)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_remove.svg">

```python
passtf.delete_file('')
```

- 删除指定路径下的文件。该功能块用于从存储介质中移除某个文件。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_rename.svg">

```python
tf.rename_file('','')
```

- 将一个文件从旧路径重命名为新路径。你可以通过提供文件的旧路径和想要的新路径来完成文件的重命名操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/tf_card/uiflow_block_base_tfcard_rmdir.svg">

```python
tf.delete_folder('')
```

- 用于删除指定路径下的文件夹。只要指定文件夹的路径，系统将会删除该文件夹及其内容(如果支持删除非空文件夹)。

