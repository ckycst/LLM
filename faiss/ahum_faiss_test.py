import faiss
import numpy as np

# 创建随机向量
d = 64                           # 维度
nb = 1000                        # 库中向量数
nq = 10                          # 查询向量数

np.random.seed(0)
xb = np.random.random((nb, d)).astype('float32')
xq = np.random.random((nq, d)).astype('float32')

# 构建索引并搜索
index = faiss.IndexFlatL2(d)     # 精确 L2 搜索
index.add(xb)
D, I = index.search(xq, k=4)     # 每个查询返回 4 个最近邻

print("✅ Search completed!")
print("Distances shape:", D.shape)  # 应为 (10, 4)
print("Indices shape:", I.shape)    # 应为 (10, 4)
