# RaspberryPi Docker 安装说明

1. **更新 apt 源**

```bash
sudo apt update
```

2. **安装依赖包**

```bash
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
```

3. **获取 Docker 官方 GPG 密钥**

```bash
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

4. **添加 Docker 官方 apt 仓库地址**

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5. **再次更新 apt 源**

```bash
sudo apt update
```

6. 安装 Docker 及相关组件

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

7. 把当前用户加入 docker 组

```bash
sudo usermod -aG docker $USER
newgrp docker
```