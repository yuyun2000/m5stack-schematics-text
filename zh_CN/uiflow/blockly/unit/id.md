# [Unit ID](/zh_CN/unit/id)

## 案例程序

生成公钥、创建消息签名和验证签名

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_id_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
ID_0 = unit.get(unit.ID, unit.PORTA)


public = None
signature = None
message = None
recv_msg = None

message=[0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
  0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F]
if ID_0.get_info():
  print('Read Device Info Sucess')
else:
  print('Read Device Info Unsucess')
if ID_0.readConfigZone():
  print('Read Config Sucess')
else:
  print('Read Config Unsucess')
if (ID_0.configLockStatus) or (ID_0.dataOTPLockStatus) or (ID_0.slot0LockStatus):
  print('Read Config Status Sucess')
  if ID_0.generatePublicKey(0x0000):
    public = ID_0.publicKey64Bytes
    if ID_0.createSignature(message, 0x0000):
      signature = ID_0.signature
      recv_msg=[0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F]
      if ID_0.verifySignature(recv_msg, signature, public):
        print('Verify Sucess')
      else:
        print('Verify UnSucess')
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_config_lock_status.svg">

```python
print((str('status:') + str((ID_0.configLockStatus))))
```

- 获取配置锁定状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_config_zone.svg">

```python
print(ID_0.configZone)
```

- 获取配置参数区域

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_create_keypair.svg">

```python
print((str('new key pair:') + str((ID_0.createNewKeyPair(0x0000)))))
```

- 获取创建的密钥对

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_create_signature.svg">

```python
print((str('create signature:') + str((ID_0.createSignature(, 0x0000)))))
```

- 获取创建数字签名数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_data_otp_status.svg">

```python
print((str('status:') + str((ID_0.dataOTPLockStatus))))
```

- 获取OTP数据状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_generate_public_key.svg">

```python
print((str('public key:') + str((ID_0.generatePublicKey(0x0000)))))
```

- 获取生成公钥

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_get_info.svg">

```python
print(ID_0.get_info())
```

- 读取芯片基础信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_key_config.svg">

```python
print(ID_0.KeyConfig)
```

- 设置密钥存储槽的权限参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_lock_config.svg">

```python
print(ID_0.lock_config())
```

- 获取锁定配置信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_lock_data_otp.svg">

```python
print(ID_0.lockDataAndOTP())
```

- 获取锁定OTP数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_lock_data_slot.svg">

```python
print(ID_0.lockDataSlot0())
```

- 获取锁定数据槽

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_public_Key_64Bytes.svg">

```python
print((str('key:') + str((ID_0.publicKey64Bytes))))
```

- 获取符合ECC-P256标准的64字节公钥格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_random_min_max.svg">

```python
print(ID_0.random_min_max(0, 0))
```

- 获取范围随机数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_read_config.svg">

```python
print(ID_0.readConfigZone())
```

- 从配置区提取当前安全参数设置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_revision_number.svg">

```python
print(ID_0.revisionNumber)
```

- 获取芯片固件版本号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_serial_number.svg">

```python
print(ID_0.serialNumber)
```

- 读取芯片唯一标识序列号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_sha256.svg">

```python
print((str('sha256 message:') + str((ID_0.sha256(, 0)))))
```

- 获取硬件加速的SHA-256哈希运算数据长度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_signature.svg">

```python
print(ID_0.signature)
```

- 获取数字签名

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_slot_config.svg">

```python
print(ID_0.SlotConfig)
```

- 获取存储槽配置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_slot_status.svg">

```python
print((str('status:') + str((ID_0.slot0LockStatus))))
```

- 获取存储槽状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_update_random_32bytes.svg">

```python
print(ID_0.updateRandom32Bytes())
```

- 获取更新的32字节数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_verify_signature.svg">

```python
print((str('create message:') + str((ID_0.verifySignature(, , )))))
```

- 获取验证签名数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_wakeup.svg">

```python
print(ID_0.wakeup())
```

- 获取唤醒状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/id/uiflow_block_unit_id_write_config_zone.svg">

```python
print(ID_0.writeConfigZone())
```

- 获取写入配置区数据

