# AI Pyramid - Git LFS 安装指南

Git LFS（Large File Storage）是 Git 的扩展工具，用于高效管理大型文件。在使用 HuggingFace 上的模型仓库时，通常需要安装 Git LFS 以正确获取和处理大文件。

## 1. 更新软件包管理器

首先更新系统的软件包索引：

```bash
apt update
```

## 2. 安装 Git LFS

执行以下命令安装 git-lfs 包：

```bash
apt install git-lfs
```

## 3. 初始化 Git LFS

安装完成后，执行以下命令初始化 Git LFS：

```bash
git lfs install
```

初始化成功后，Git LFS 将被集成到 Git 的工作流中，您可以正常使用 `git clone` 命令来获取包含大文件的仓库。