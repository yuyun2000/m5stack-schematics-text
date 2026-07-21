# CoreMP135网络管理

以下指令中的`eth0`替换为你实际要操作的网卡

## ifconfig 操作命令

```bash
# 查看所有的网络接口
ifconfig -a

# 查看开启的网络
ifconfig 

# 开启 eth0 网络接口
ifconfig eth0 up

# 关闭eth0网卡
ifconfig eth0 down  

# 配置网卡信息
ifconfig eth0 192.168.2.10 netmask 255.255.255.0 broadcast 192.168.2.255 

# 修改网卡 eth0 MAC地址
ifconfig eth0 hw ether AA:AA:BB:CC:dd:EE  

```

## ip 操作命令
```bash
# 显示网络接口信息
ip link show 

# 开启网卡
ip link set eth0 up 

# 关闭网卡
ip link set eth0 down 

# 开启网卡的混合模式
ip link set eth0 promisc on 

# 关闭网卡的混个模式
ip link set eth0 promisc offi 

# 设置网卡队列长度
ip link set eth0 txqueuelen 1200 

# 设置网卡最大传输单元
ip link set eth0 mtu 1400 

# 显示网卡IP信息
ip addr show 

# 设置eth0网卡IP地址192.168.0.1
ip addr add 192.168.0.1/24 dev eth0 

# 删除eth0网卡IP地址
ip addr del 192.168.0.1/24 dev eth0 

# 显示系统路由
ip route show 

# 设置系统默认路由
ip route add default via 192.168.1.254 

# 查看路由信息
ip route list 

# 设置192.168.4.0网段的网关为192.168.0.254,数据走eth0接口
ip route add 192.168.4.0/24 via 192.168.0.254 dev eth0 

# 设置默认网关为192.168.0.254
ip route add default via 192.168.0.254 dev eth0 

# 删除192.168.4.0网段的网关
ip route del 192.168.4.0/24 

# 删除默认路由
ip route del default 

# 删除路由
ip route delete 192.168.1.0/24 dev eth0 
```

## 以太网静态ip配置

```bash
# 如果没有开启网络接口
ifconfig eth0 up

# 设置 eth0 网口的静态 ip
ifconfig eth0 192.168.1.100
```

## 以太网动态ip配置

```bash
# 如果没有开启网络接口
ifconfig eth0 up

# 获取动态 ip
dhclient eth0
```


