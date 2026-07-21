
## SD-Card

```python

import os

# 读文件
with open('/sd/FileName.*', 'r') as fs:
  print(fs.read())

# 写文件
with open('/sd/test.txt', 'w+') as fs:
  fs.write('Hello World')

# 文件读写模式
w 以写方式打开,
w+ 以读写模式打开
r 以读模式打开
r+ 以读写模式打开
a 以追加模式打开

# 设置文件光标
fs.seek(0)

# 查看目录
os.listdir('/sd/DirectoryPath')

# 判断路径是否为文件
os.stat('/sd/FilePath')[0] == 0x8000)

# 判断路径是否为目录
os.stat('/sd/DirectoryPath')[0] == 0x4000)

# 判断文件是否存在于指定目录
'FileName.*' in os.listdir('/sd/DirectoryPath')

```
