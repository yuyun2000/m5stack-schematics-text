# SDCard

## 案例程序

- SDCard 文件读写操作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *
from hardware import sdcard
setScreenColor(0x222222)

sdcard.SDCard(20000000)
with open('/sd/test.txt', 'w+') as fs:
  fs.write('Hello World')
with open('/sd/test.txt', 'r') as fs:
  print(fs.read())

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_init_clock.svg"> 


```python
sdcard.SDCard(20000000)
```

- 设置 SDCard 总线时钟频率


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_open.svg"> 


```python
with open('/sd/test.txt', 'w+') as fs:
    pass

```

- 打开指定文件， 并在其内部执行读或写操作，r 和 r+状态下必须存在此文件，否则将出现错误。a、w 和 w+模式如果不存在文件会自动创建。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_write.svg"> 


```python
fs.write('Hello World')
```

- 向文件内写入内容


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_seek.svg"> 


```python
fs.seek(0)
```

- 操作文件光标移动位置


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_mkdir.svg"> 


```python
os.mkdir('/sd/new_folder')
```

- 创建文件夹

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_remove.svg"> 


```python
os.remove('/sd/filename')
```

- 删除指定路径文件


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_rmdir.svg"> 


```python
os.rmdir('/sd/folder')
```

- 删除指定路径文件夹


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_rename.svg"> 


```python
os.rename('/sd/old', '/sd/new')
```

- 重命名文件

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_read_all.svg"> 


```python
fs.read()
```

- 读取全部数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_read_bytes.svg"> 


```python
fs.read(1024)
```

- 读取指定长度数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_read_line.svg"> 


```python
fs.readline()
```

- 读取一行数据


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_get_seek.svg"> 


```python
fs.tell()
```

- 读取当前文件光标位置


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_listdir.svg"> 


```python
os.listdir('/sd/')
```

- 查看目录文件

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_is_file.svg"> 


```python
os.stat('/sd/')[0] == 0x8000
```

- 检查路径是否为文件

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_is_directory.svg"> 


```python
os.stat('/sd/')[0] == 0x4000
```

- 检查路径是否为目录


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/sdcard/uiflow_block_sd_file_exist.svg"> 


```python
'' in os.listdir('/sd/')
```

- 检查路径中是否包含某文件

