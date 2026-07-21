# 虚拟内存调整

1. 创建 swap 文件。

```bash
fallocate -l 4G /swapfile
```

2. 设置权限并初始化 swap 分区头。

```bash
chmod 600 /swapfile
mkswap /swapfile
```

3. 启用 swap 并验证状态。

```bash
swapon /swapfile
swapon --show
free -h
```

4. 创建 systemd 服务实现自动挂载。

```bash
tee /etc/systemd/system/enable-swapfile.service >/dev/null <<'EOF'
[Unit]
Description=Enable swapfile via swapon
After=local-fs.target
Requires=local-fs.target

[Service]
Type=oneshot
ExecStart=/sbin/swapon /swapfile
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF
```

5. 设置开机自启。

```bash
systemctl daemon-reload
systemctl enable enable-swapfile.service
```
