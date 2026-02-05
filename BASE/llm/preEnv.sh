# 1. 安装 huggingface_hub 和 transformer：
#   huggingface_hub 可以从Python代码侧下载管理LLM
#   transformers 用来加载下载的LLM 
conda activate ahumAI 
pip install huggingface_hub transformers
## 如果因为网络的问题，无法从huggingface_hub 上 download model，可以尝试在modelscope上下载
## pip 安装modelscope
pip install modelscope

## BGE-M3 官方发布时明确说明应通过 sentence-transformers
pip install sentence-transformers
