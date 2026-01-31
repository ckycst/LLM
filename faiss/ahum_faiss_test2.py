import time
import numpy as np
import faiss

# 更大规模测试（10万向量）
d = 768          # 常见嵌入维度（如 BERT）
nb = 100_000
nq = 100

xb = np.random.random((nb, d)).astype('float32')
xq = np.random.random((nq, d)).astype('float32')

index = faiss.IndexFlatIP(d)  # 内积（余弦相似度需先归一化）
index.add(xb)

t0 = time.time()
D, I = index.search(xq, k=5)
print(f"✅ Searched {nq} queries over {nb:,} vectors ({d}D) in {time.time() - t0:.2f} seconds")
