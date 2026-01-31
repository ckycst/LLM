# 原本想在jetson nano 4GB 版本设备上使用faiss-gpu, 奈何硬件配置太低（对于faiss-gpu来说），最后选择在自己的Mac M1 16GB 上安装（我的mac上已经有太多东西了~~）
# 据说Apple Silicon 架构对 Faiss-CPU 有显著性能优势，那么让我们来试试吧！！！

# 安装 Miniforge（专为 Apple Silicon 优化的 Conda 发行版）
brew install miniforge

## 确认是否安装了miniforge
conda --version
conda info

## 通过查看 conda的目录判断是否是 miniforge
echo $CONDA_PREFIX
### 如果返回 /opt/miniforge3/bin/python 或 ～/miniforge3/bin/python，那就是 Miniforge,
### 我自己的环境因为之前已经安装过 miniconda，所以路径出现miniconda3,如下
(faiss) carlos@anonymous faiss_test % echo $CONDA_PREFIX
/Users/carlos/miniconda3/envs/faiss
### 在安装faiss-cpu 时，命令行显式加上“-c conda-forge” 即可
### 或者如果以后主要用科学计算包（如 PyTorch、Faiss、JAX 等），建议配置：
conda config --add channels conda-forge


## 创建并激活虚拟环境（建议使用 Python 3.9~3.11），先创建空环境，再安装（最稳妥）
### 创建最小环境的 faiss
conda create -n faiss -c conda-forge python=3.11 --no-default-packages -y
### 激活并安装 faiss-cpu
conda activate faiss

# 通过 conda-forge 安装 faiss-cpu（已预编译，支持 ARM64）
conda install -c conda-forge faiss-cpu

# 安装完了之后验证
## 1. 激活faiss
conda activate faiss
## 2. 启动导入命令
python3 -c "import faiss; print('✅ Faiss imported successfully!')"
## 3. 版本及路径验证
python3 ahum_faiss_ver&path.py

