## SSH登录

#>打开命令行终端,输入下方指令,并输入默认密码,通过ssh访问设备。

```cpp

ssh m5stack@10.254.239.1 

//user: m5stack
//pwd: 12345678


//user: root
//pwd: 7d219bec161177ba75689e71edc1835422b87be17bf92c3ff527b35052bf7d1f

```

用户默认目录结构

```cpp

//存储Jupyter Notebook中编辑的文件
/home/notebook

//存储识别功能服务文件资源,和一些模型文件
/home/m5stack 

```

## WIFI

### 添加配置信息

#>通过`SSH`访问设备, 配置`wpa_supplicant.conf`文件, 并添加WiFi连接信息。在修改配置文件前, 我们需要通过`wpa_passpharse`创建加密信息(psk), 参考下方命令输入SSID与PASSWORD, 获取打印输出的。

```python

#输入命令
sudo wpa_passphrase ssid password

#返回结果
network={
        ssid="ssid"
        #psk="password"
        psk=44116ea881531996d8a23af58b376d70f196057429c258f529577a26e727ec1b
}

```

>将生成的`Wi-Fi`凭证信息, 添加到`wpa_supplicant.conf`文件中并保存

```python
#打开配置文件
sudo nano /etc/wpa_supplicant.conf

#添加配置信息
network={
    ssid="ssid"
    psk=44116ea881531996d8a23af58b376d70f196057429c258f529577a26e727ec1b
}
```

>完成配置后, 可通过`ping`指令, 测试当前网络状态。

```cpp
sudo ping m5stack.com

PING m5stack.com (120.77.157.90): 56 data bytes
64 bytes from 120.77.157.90: seq=0 ttl=52 time=12.792 ms
64 bytes from 120.77.157.90: seq=1 ttl=52 time=9.838 ms
64 bytes from 120.77.157.90: seq=2 ttl=52 time=47.202 ms

```

#>若始终无法正常连接网络, 可以尝试重启网卡或断电重启设备`sudo reboot`。

```python

#停用网卡
sudo ifconfig wlan0 down

#启用网卡
sudo ifconfig wlan0 up

```

### 配置多个连接

#>`wpa_supplicant.conf`中支持配置多个WiFi信息, 通过添加`priority`字段可设置连接的优先级 (priority越大则优先级越高)

```python

network={
    ssid="network-1"
    psk="very secret passphrase"
    priority=5
}
network={
    ssid="network-2"
    psk="very secret passphrase"
    priority=6
}

```

## 配置脚本自启

#>root用户登录，并访问一下路径，添加或修改已有的启动`Sn`(n代表着启动顺序优先级，由序号小的依次开始执行， 内置应用服务的自启文件为S85runpayload)配置文件。注: 为避免设备无法正常启动，请确保所配置的命令能够正常执行且不存在阻塞现象。出现异常，可尝试重新更新固件修复。

```shell
/etc/init.d
```
