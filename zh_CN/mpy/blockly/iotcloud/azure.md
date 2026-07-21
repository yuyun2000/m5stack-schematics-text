## Azure

>连接Azure IoT云服务平台。


#### Micropython API IoT_Hub

```python

# 初始化连接
azure = IoT_Hub(connection_string='')

# 证书接入方式
azure = IoT_Hub(device_id='', host_name='', ssl=True, cert_file_path='', private_key_path='')

# 启用连接
azure.start()

# direct_method信息订阅
azure.subscribe_direct_method(topic, azure_direct_fun)

# 监听云端数据callback
azure.subscribe_C2D_message(azure_C2D_cb)

# 发布数据至云端
azure.publish_D2C_message()

# 上传数据至云端设备实例(Device Twin)
azure.update_twin_reported_properties(key1='value',key2='value')

# 传数据至云端设备实例(Device Twin) 响应callback
azure.subscribe_twin_desired_response(azure_desired_cb)

# 获取云端设备实例(Device Twin)拥有的属性
azure.retrieve_twin_properties()

```

#### Micropython API IoT_Central

```python

# 初始化连接
azure = IoT_Central(scope_id='', device_id='', device_key='')

# 启用连接
azure.start()

# direct_method信息订阅
azure.subscribe_direct_method(topic, azure_direct_fun)

# 监听云端数据callback
azure.subscribe_C2D_message(azure_C2D_cb)

# 发布数据至云端
azure.publish_D2C_message()

# 上传数据至云端设备实例(Device Twin)
azure.update_twin_reported_properties(key1='value',key2='value')

# 传数据至云端设备实例(Device Twin) 响应callback
azure.subscribe_twin_desired_response(azure_desired_cb)

# 获取云端设备实例(Device Twin)拥有的属性
azure.retrieve_twin_properties()

```