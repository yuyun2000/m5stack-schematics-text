# EzData2 快速上手

## 1. 功能说明

EzData2 是 M5Stack 提供的一个 IoT 云端数据交互服务，提供灵活的跨端数据管理能力，帮助开发者更好地构建物联网应用。

## 2. EzData2 Web 控制台

EzData2 Web 控制台集成于 My M5Stack 平台，为用户提供直观、高效的数据管理与可视化能力。 通过该控制台，用户可以实时查看设备数据状态，并追踪历史数据变化趋势，便于调试、监控与分析。

访问 [my.m5stack.com](https://my.m5stack.com/ezdata2/workflow) ，使用 M5Stack 社区账户进行登录。 (该账户与 UiFlow2、M5Stack 官方论坛以及 M5Burner 烧录工具共用，无需重复注册。) 侧边栏选择 `Data` 选项即可打开当前账户下的 EzData2 数据面板。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_dashboard_layout_02.jpg" width="70%">

## 3. 相关概念

### 3.1 Group

Group 是一个数据集合，可以将其理解为一个文件夹，里面可以包含多个不同类型的数据字段。Group 可以在 EzData2 Web 控制台中直接创建。

一些出厂固件集成 EzData2 功能的设备 (如 PowerHub， StamPLC)，在启动后也可以通过一系列的用户绑定操作，将设备本身的一些数据字段 (如继电器状态，电压状态等)，集成为一个 Group 添加到用户列表中。

其中存在两个特殊的 Group：`System` 和 `Desktop`，这是两个固有的数据集合，不允许删除。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_dashboard_layout_01.jpg" width="70%">

### 3.2 System Group

System Group 中包含了一些用户级数据字段，能够用于查询账户信息。 System Group 中的字段是固有的，不允许增加或删除。

- DevicesCount: 用户账户下绑定的设备数量
- ApplicationsCount: 用户账户下的应用数量
- AccountName: 用户名称
- AccountToken: 账户级 Token (最高级别 Token，使用该 Token 能够访问账户下所有数据内容)
- Time: UTC+8 时间
- Date: UTC+8 日期
- DateTime: UTC+8 时间 + 日期

### 3.3 Desktop Group

Desktop Group 是一个自由的数据工作面板，能够自由地添加和删除数据，一些临时或者不需要进行分类的数据，可以放置到 Desktop Group 中。也可以将其他的 Group 中的数据移动，或是发送快捷方式到 Desktop Group 进行集中显示，方便查看。

### 3.4 Data

EzData2 中的最小数据单元，用于存储数据字段，归属于 Group，支持在不同的 Group 中进行移动。支持记录 500 条历史数据。

## 4. Group 创建

点击工具栏的`Add Group`按钮，输入新的 Group 名称进行创建。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_add_group_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_add_group_02.jpg" width="70%">

## 5. 数据创建

选中已经创建的 Group，点击`Add Data`按钮创建新的数据字段，同时指定数据的类型。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_add_data_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_add_data_02.jpg" width="70%">

在已经创建的数据上单击鼠标右键，能够打开操作菜单，对数据进行修改、移动、分享和删除等操作。其中，移动操作将直接修改数据所属的 Group；快捷方式操作，将在其他的 Group 中创建一个数据的副本，指向原数据。修改原始数据或副本任意一方，另一方将自动同步更新。当快捷方式删除时，不影响原始数据。 原始数据删除时，快捷方式数据将一同删除。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_add_data_03.jpg" width="70%">

双击已经创建的数据，能够打开数据编辑框。编辑框中，可查看数据变更历史，以及实时修改数据。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_add_data_04.jpg" width="70%">

## 6. 数据分享

### 6.1 数据 Token

在已经创建的数据上单击鼠标右键，通过 `Share` 选项，可以复制并分享当前数据字段的 Token 或 URL。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_share_data_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_share_data_02.jpg" width="70%">

其他用户在可以在创建数据的时候，选择 `From Share` 或 ` From URL` 选项，能够导入所分享的字段，实现数据分享。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_share_data_03.jpg" width="70%">

### 6.2 Group Token

在已经创建的 Group 上单击鼠标右键 ，通过 `Share` 选项，可以复制并分享当前 Group 的 Token，其他用户在可以在创建 Group 的时候，选择 `Token` 选项，导入整个 Group 的数据，实现多个数据分享。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_share_group_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1212/ezdata2_share_group_02.jpg" width="70%">

## 7. 通信协议

EzData2 目前提供了 MQTT 和 WebSocket 两种连接方式，可供设备端实现数据交互。

- [EzData2 通信协议](/zh_CN/guide/ezdata/ezdata_v2_protocol)
