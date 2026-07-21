# EzData2 Device 接口文档

## 1. 概述

EzData2 目前提供了 MQTT 和 WebSocket 两种连接方式，可供设备端实现数据交互。设备接入前需使用硬件设备 Mac 地址调用注册接口获取 Device Token。完成注册并成功获取 Device Token 后，访问 [my.m5stack.com](https://my.m5stack.com/ezdata2/workflow) 登录个人账户，点击 `Add Group`，选择 `Token` 选项。复制粘贴 Device Token 进行创建，即可完成 Device Token 与账户的绑定。单个设备的 Device Token 相当于一个数据集 Group。设备端参考下方通信协议，基于 Device Token 进行登录验证后，即可对数据字段进行增删改查。

## 2. 基础定义

### 2.1 命令与响应 (CMD / RequestType)

| 代码    | 类型     | 描述                   |
| ------- | -------- | ---------------------- |
| **100** | 数据操作 | 设备端新增数据         |
| **101** | 数据操作 | 设备端修改数据         |
| **102** | 数据操作 | 设备端删除数据         |
| **103** | 数据查询 | 设备端查询数据列表     |
| **104** | 数据查询 | 设备端查询数据详情     |
| **105** | 文件上传 | 设备端上传文件（通知） |
| **106** | 用户操作 | 用户端扫码             |
| **107** | 用户操作 | 用户端修改数据         |
| **108** | 用户操作 | 用户端删除数据         |
| **109** | 用户操作 | 用户端新增数据         |
| **500** | 错误     | 设备端请求错误         |

## 3. HTTP 接口

### 3.1 设备注册

**请求接口：**

- URL： `https://ezdata2.m5stack.com/api/v2/device/registerMac`
- 方法： `POST`
- 描述： 通过 MAC 地址注册设备并生成 `deviceToken`。

**请求参数：**

| 参数       | 类型   | 描述                                                                                                        |
| ---------- | ------ | ----------------------------------------------------------------------------------------------------------- |
| deviceType | string | 参考 [开发板定义](https://github.com/m5stack/m5stack-board-id/blob/main/board.csv) 中的 `Product name` 字段 |
| mac        | string | 设备 MAC 地址，无 ":" 分隔符，大小写均可                                                                    |

```json
{
  "deviceType": "basic",
  "mac": "AABBCCDDEEFF"
}
```

**响应参数**：

| 参数 | 类型   | 描述               |
| ---- | ------ | ------------------ |
| code | int    | 状态码 (0 为成功)  |
| data | string | 返回的 deviceToken |
| msg  | string | 响应消息           |

```json
{
  "code": 0,
  "data": "4fbb52fb5b6243e083377f45d216820f",
  "msg": "success"
}
```

### 3.2 设备文件上传

**请求接口：**

- URL： `https://ezdata2.m5stack.com/api/v2/device/uploadDeviceFile`
- 方法： `POST (multipart/form-data)`
- 描述： 通过 HTTP 上传文件。上传成功后，服务器会通过 WebSocket/MQTT 下发 `cmd: 105` 的响应消息。

**请求参数：**

| 参数        | 类型   | 描述       |
| ----------- | ------ | ---------- |
| deviceToken | string | 设备令牌   |
| file        | file   | 上传的文件 |

**响应参数：**

| 参数 | 类型 | 描述                |
| ---- | ---- | ------------------- |
| code | int  | 状态码 (200 为成功) |

## 4. 连接协议

### 4.1 WebSocket 连接

**请求接口：**

- URL： `wss://ezdata2.m5stack.com/ws`
- 方法： `WebSocket`

#### 4.1.1 登录

**请求接口：**

- 消息类型： 登录请求
- 描述： 使用 deviceToken 连接到 WebSocket 服务器

**请求参数：**

| 参数        | 类型   | 描述     |
| ----------- | ------ | -------- |
| deviceToken | string | 设备令牌 |

```json
{
  "deviceToken": "4fbb52fb5b6243e083377f45d216820f"
}
```

**响应参数：**

| 参数 | 类型   | 描述             |
| ---- | ------ | ---------------- |
| -    | string | 登录成功提示信息 |

```text
device Login successful
```

#### 4.1.2 心跳 (Heartbeat)

**请求接口：**

- 消息类型： 心跳请求
- 描述： 保持 WebSocket 连接活跃

**请求参数：**

| 参数        | 类型   | 描述                      |
| ----------- | ------ | ------------------------- |
| deviceToken | string | 设备令牌                  |
| body        | string | 心跳信号 (固定值: "ping") |

```json
{
  "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
  "body": "ping"
}
```

**响应参数：**

| 参数 | 类型   | 描述     |
| ---- | ------ | -------- |
| -    | string | 心跳应答 |

```text
pong
```

### 4.2 MQTT 连接

**请求接口：**

- 服务器地址： `uiflow2.m5stack.com`
- 端口： `1883`
- 协议： `MQTT 3.1.1`

**连接参数：**

| 参数     | 类型   | 描述                         |
| -------- | ------ | ---------------------------- |
| 名称     | string | `ez{mac}ez`                  |
| ClientId | string | `ez{mac}ez`                  |
| 用户名   | string | `{deviceToken}` (设备 Token) |
| Password | string | 无需密码                     |

**Topic**：

| 主题                         | 方向 | 描述     |
| ---------------------------- | ---- | -------- |
| `$ezdata/{deviceToken}/up`   | 发布 | 上行数据 |
| `$ezdata/{deviceToken}/down` | 订阅 | 下行数据 |

> **说明**：
> - mac: 设备 MAC 地址，无 ":" 分隔符，大小写均可
> - deviceToken: 通过注册接口获取

## 5. 业务数据交互 (Payload)

以下内容为 WebSocket 或 MQTT 的消息体内容。

### 5.1 新增数据 (CMD: 100)

**请求接口：**

- 命令码： `100`
- 类型： 数据操作
- 描述： 设备端新增数据字段

**请求参数：**

| 参数             | 类型   | 描述                   |
| ---------------- | ------ | ---------------------- |
| deviceToken      | string | 设备令牌               |
| body.name        | string | 数据字段名称           |
| body.value       | string | 数据字段值             |
| body.requestType | int    | 请求类型 (固定值: 100) |

```json
{
  "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
  "body": {
    "name": "adasd",
    "value": "ddsad",
    "requestType": 100
  }
}
```

**响应参数：**

| 参数             | 类型   | 描述                |
| ---------------- | ------ | ------------------- |
| cmd              | int    | 命令码 (100)        |
| code             | int    | 状态码 (200 为成功) |
| body.deviceToken | string | 设备令牌            |
| body.name        | string | 数据字段名称        |
| body.value       | string | 数据字段值          |

```json
{
  "body": {
    "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
    "name": "adasd",
    "value": "ddsad"
  },
  "cmd": 100,
  "code": 200
}
```

### 5.2 修改数据 (CMD: 101)

**请求接口：**

- 命令码： `101`
- 类型： 数据操作
- 描述： 设备端修改数据字段

**请求参数：**

| 参数             | 类型   | 描述                   |
| ---------------- | ------ | ---------------------- |
| deviceToken      | string | 设备令牌               |
| body.name        | string | 数据字段名称           |
| body.value       | string | 数据字段值             |
| body.requestType | int    | 请求类型 (固定值: 101) |

```json
{
  "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
  "body": {
    "name": "adasd",
    "value": "ddsad",
    "requestType": 101
  }
}
```

**响应参数：**

| 参数             | 类型   | 描述                |
| ---------------- | ------ | ------------------- |
| cmd              | int    | 命令码 (101)        |
| code             | int    | 状态码 (200 为成功) |
| body.deviceToken | string | 设备令牌            |
| body.name        | string | 数据字段名称        |
| body.value       | string | 数据字段值          |

```json
{
  "body": {
    "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
    "name": "adasd",
    "value": "ddsad"
  },
  "cmd": 101,
  "code": 200
}
```

### 5.3 删除数据 (CMD: 102)

**请求接口：**

- 命令码： `102`
- 类型： 数据操作
- 描述： 设备端删除数据字段

**请求参数：**

| 参数             | 类型   | 描述                   |
| ---------------- | ------ | ---------------------- |
| deviceToken      | string | 设备令牌               |
| body.name        | string | 数据字段名称           |
| body.value       | string | 数据字段值             |
| body.requestType | int    | 请求类型 (固定值: 102) |

```json
{
  "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
  "body": {
    "name": "adasd(3)",
    "value": "ddsad",
    "requestType": 102
  }
}
```

**响应参数：**

| 参数             | 类型   | 描述                |
| ---------------- | ------ | ------------------- |
| cmd              | int    | 命令码 (102)        |
| code             | int    | 状态码 (200 为成功) |
| body.deviceToken | string | 设备令牌            |
| body.name        | string | 数据字段名称        |
| body.value       | string | 数据字段值          |

```json
{
  "body": {
    "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
    "name": "adasd(3)",
    "value": "ddsad"
  },
  "cmd": 102,
  "code": 200
}
```

### 5.4 查询数据列表 (CMD: 103)

**请求接口：**

- 命令码： `103`
- 类型： 数据查询
- 描述： 设备端查询数据列表

**请求参数：**

| 参数             | 类型   | 描述                   |
| ---------------- | ------ | ---------------------- |
| deviceToken      | string | 设备令牌               |
| body.requestType | int    | 请求类型 (固定值: 103) |

```json
{
  "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
  "body": {
    "requestType": 103
  }
}
```

**响应参数：**

| 参数              | 类型   | 描述                  |
| ----------------- | ------ | --------------------- |
| cmd               | int    | 命令码 (103)          |
| code              | int    | 状态码 (200 为成功)   |
| body[].id         | string | 数据ID                |
| body[].dataToken  | string | 数据令牌              |
| body[].name       | string | 数据字段名称          |
| body[].value      | string | 数据字段值            |
| body[].createTime | long   | 创建时间 (毫秒时间戳) |
| body[].updateTime | long   | 更新时间 (毫秒时间戳) |

```json
{
  "body": [
    {
      "createTime": 1751274100000,
      "dataToken": "6a330c4bf0924da3a2b11c833f9c2db1",
      "id": "6a330c4bf0924da3a2b11c833f9c2db1",
      "name": "adasd",
      "updateTime": 1751274100000,
      "value": "ddsad"
    },
    {
      "createTime": 1751274119000,
      "dataToken": "60ea29ff4df446358b7bf2151939abb4",
      "id": "60ea29ff4df446358b7bf2151939abb4",
      "name": "adasd(1)",
      "updateTime": 1751274119000,
      "value": "ddsad"
    }
  ],
  "cmd": 103,
  "code": 200
}
```

### 5.5 查询单个详情 (CMD: 104)

**请求接口：**

- 命令码： `104`
- 类型： 数据查询
- 描述： 设备端查询单个数据详情

**请求参数：**

| 参数             | 类型   | 描述                   |
| ---------------- | ------ | ---------------------- |
| deviceToken      | string | 设备令牌               |
| body.name        | string | 数据字段名称           |
| body.requestType | int    | 请求类型 (固定值: 104) |

```json
{
  "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
  "body": {
    "name": "adasd",
    "requestType": 104
  }
}
```

**响应参数：**

| 参数            | 类型   | 描述                  |
| --------------- | ------ | --------------------- |
| cmd             | int    | 命令码 (104)          |
| code            | int    | 状态码 (200 为成功)   |
| body.id         | string | 数据ID                |
| body.dataToken  | string | 数据令牌              |
| body.name       | string | 数据字段名称          |
| body.value      | string | 数据字段值            |
| body.createTime | long   | 创建时间 (毫秒时间戳) |
| body.updateTime | long   | 更新时间 (毫秒时间戳) |

```json
{
  "body": {
    "createTime": 1751274100000,
    "dataToken": "6a330c4bf0924da3a2b11c833f9c2db1",
    "id": "6a330c4bf0924da3a2b11c833f9c2db1",
    "name": "adasd",
    "updateTime": 1751274100000,
    "value": "ddsad"
  },
  "cmd": 104,
  "code": 200
}
```

### 5.6 文件上传结果通知 (CMD: 105)

**说明：**

该消息由 HTTP 接口上传触发，设备端通过长连接接收响应。

**请求接口：**

- 触发源： HTTP `https://ezdata2.m5stack.com/api/v2/device/uploadDeviceFile`
- 命令码： `105`
- 类型： 文件上传
- 描述： 服务器通过 WebSocket/MQTT 返回文件上传结果

**响应参数 (WebSocket/MQTT):**

| 参数             | 类型   | 描述                |
| ---------------- | ------ | ------------------- |
| cmd              | int    | 命令码 (105)        |
| code             | int    | 状态码 (200 为成功) |
| body.deviceToken | string | 设备令牌            |
| body.name        | string | 文件字段名称        |
| body.value       | string | 文件 URL            |

```json
{
  "body": {
    "deviceToken": "4fbb52fb5b6243e083377f45d216820f",
    "name": "deviceFile",
    "value": "https://ezdata2-oss-dev.m5stack.com/37a6259cc0c1dae299a7866489dff0bd/deviceFile/deviceFile.jpg"
  },
  "cmd": 105,
  "code": 200
}
```
