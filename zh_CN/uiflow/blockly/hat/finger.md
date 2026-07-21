# [Hat Finger](/zh_CN/hat/hat-finger)

## 案例程序

串口打印指纹的 id，权限和识别状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_Finger_0 = hat.get(hat.FINGER)

hat_Finger_0.addUser(1, 1)
while True:
  print(hat_Finger_0.state)
  print(user_id)
  print(access)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_add_user.svg">

```python
hat_Finger_0.addUser(1, 1)
```

- 添加用户指纹 ID，并指定访问权限

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_getUnknown.svg">

```python
hat_Finger_0.readFingerCb(callback=hat_Finger_0_cb)
```

- 获取未知用户的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_get_access.svg">

```python
access
```

- 获取指纹用户的访问权限信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_get_id.svg">

```python
print((str('id:') + str((user_id))))
```

- 获取指纹用户的 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_get_state.svg">

```python
user_id
```

- 获取指纹识别模块的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_read.svg">

```python
hat_Finger_0.state
```

- 读取具有特定 ID 和访问权限的用户信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_removeAll.svg">

```python
hat_Finger_0.removeAllUser()
```

- 删除所有已存储的用户数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/finger/uiflow_block_hat_finger_remove_user.svg">

```python
hat_Finger_0.removeUser(1)
```

- 删除指定 ID 的指纹用户

