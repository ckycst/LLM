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
## 2. 启动导入命令,验证是否能导入
python3 -c "import faiss; print('✅ Faiss imported successfully!')"
## 3. 版本及路径验证
python3 ahum_faiss_ver&path.py
## 4. 验证是否原生，结果中有 arm64 说明是原生
(faiss) carlos@anonymous faiss % lipo -info /Users/carlos/miniconda3/envs/faiss/lib/python3.11/site-packages/faiss/_swigfaiss.so
Non-fat file: _swigfaiss.so is architecture: arm64
### /Users/carlos/miniconda3/envs/faiss/lib/python3.11/site-packages/faiss 是我的faiss 环境目录

## 5. 检查是否使用多线程（M1 多核加速标志）
python3 ahum_faiss_test.py
## 6. 检查faiss-cpu on Mac M1 上的性能
### M1 16GB 预期：
### 时间：约 0.5 ～ 1.5 秒
### 内存占用：约 300MB（10万×768×4字节）
### 如果在这个范围，说明 Faiss 正在高效利用 M1 的 CPU 和内存带宽！
python3 ahum_faiss_test2.py
### 实际的结果
### ✅ Searched 100 queries over 100,000 vectors (768D) in 0.09 seconds
### ✅ Searched 100 queries over 100,000 vectors (768D) in 0.03 seconds
### ✅ Searched 100 queries over 100,000 vectors (768D) in 0.03 seconds
### ✅ Searched 100 queries over 100,000 vectors (768D) in 0.03 seconds
### ✅ Searched 100 queries over 100,000 vectors (768D) in 0.03 seconds
### ✅ Searched 100 queries over 100,000 vectors (768D) in 0.03 seconds
### 连续 6 次，其中第一次相对时间长一点，为 0.09 秒，其他 5 次都是 0.03 秒

