# [Faces Finger](/zh_CN/module/faces_finger)

## 案例程序

添加一个具有指定用户 ID 和访问权限的指纹用户，然后循环打印该用户的访问权限、ID 和状态，最后删除该用户的信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_face_finger_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import face

setScreenColor(0x222222)

faces_finger = face.get(face.FINGER)

faces_finger.addUser(1, 1)
while True:
  print((str('access：') + str((access))))
  print((str('id：') + str((user_id))))
  print((str('state：') + str((faces_finger.state))))
  faces_finger.removeUser(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_faces_finger_add_user.svg">

```python
faces_finger.addUser(1, 1)
```

- 添加一个用户指纹，指定用户 ID 和访问级别

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_faces_finger_getUnknown.svg">

```python
def faces_finger_unknownCb():
	# global params
  pass
faces_finger.getUnknownCb(faces_finger_unknownCb)
```

- 获取未注册的指纹信息，通常用于检测是否有新指纹未被识别

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_faces_finger_get_access.svg">

```python
access
```

- 获取当前指纹的访问权限级别

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_faces_finger_get_id.svg">

```python
user_id
```

- 获取当前指纹的用户 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_faces_finger_get_state.svg">

```python
faces_finger.state
```

- 获取当前指纹的状态信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_faces_finger_read.svg">

```python
def faces_finger_cb(user_id, access):
  # global params
  pass
faces_finger.readFingerCb(callback=faces_finger_cb)
```

- 读取具有特定用户 ID 和访问权限的用户信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_faces_finger_removeAll.svg">

```python
  faces_finger.removeAllUser()
```

- 删除所有存储的指纹用户信息。这一操作将清除所有已注册的用户数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/face_finger/uiflow_block_faces_finger_remove_user.svg">

```python
 faces_finger.removeUser(1)
```

- 删除指定 ID 的指纹用户信息。通过输入用户 ID，可以删除对应的指纹用户数据

