# UiFlow2 设备数据共享(EzData 2.0)

> EzData 2.0 是 M5Stack 提供的一个 IoT 云端数据储存服务，不同的设备之间可以通过`唯一 token`，向储存队列中插入或提取数据，实现数据共享。

<img src="https://static-cdn.m5stack.com/resource/docs/static/image/iotservice/ezdata/ezdata_01.webp" width="70%">

## 创建 EzData 数据

### 1.EzData Manager 创建 EzData 数据

点击 UiFlow2 WebIDE 下方 EzData 图标，选择管理数据的设备，点击 Add key 添加键值对，存储数据到云端。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_01.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_02.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_03.png" width="70%">

### 2.EzData Blockly 创建 EzData 数据

拖到 EzData Blockly 模块设计程序，实现云端数据的存储，查阅，更改和删除等基础操作。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_04.png" width="70%">

### 3.EzData 控制面板创建 EzData 数据

登录[EzData 控制面板](https://ezdata2.m5stack.com/doc.html#/home)，通过后台接口调用，传入设备唯一的`token`实现数据的增删改查等基础操作。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_05.png" width="70%">

## 创建数据集合

DataSet Manager 是集中管理零散的 EzData 数据的模块，创建的集合不会影响云端保存的 EZData 数据。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_06.png" width="70%">

## UiFlow2 访问云端数据

使用 UiFlow2 访问云端数据步骤如下：

- 1.设备必须使用 `Wi-Fi` 连接 UiFlow2 WebIDE
- 2.在 EzData Manager 拿到设备唯一 `token ：795efd86c2a6478eb9c3bb414376bb6b`
- 3.拖动 blockly 块设置程序，点击 `Run`

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_07.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_08.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_09.png" width="70%">

## EzData 控制面板调试

[EzData 控制面板](https://ezdata2.m5stack.com/doc.html#/home)当前账号下绑定所有设备的云端数据存储的可视化平台，通过调用后台 API 接口实现数据基本操作。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/ezdata_manager/ezda_10.png" width="70%">

#>**_注意事项:_** | 1. 以下所有操作都依赖于`唯一 token`，该 token 在同一浏览器环境下是固定的， 使用前请复制 token。<br/>2. 半年时间内没有进行数据操作，则清空该 token 对应的数据队列。<br/>3. 数据将按照插入时间，降序排序(最后插入的数据，在列表的首位)，数据会累积保存。
