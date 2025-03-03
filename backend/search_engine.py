import json

import faiss
import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer

# 加载数据
pubmed_embeds = np.load("data/embeds_chunk_36.npy").astype(np.float32)
pmids = json.load(open("data/pmids_chunk_36.json"))
torch.set_num_threads(1)

# 初始化 FAISS
index = faiss.IndexFlatIP(768)
index.add(pubmed_embeds)

# 加载模型
model = AutoModel.from_pretrained("ncbi/MedCPT-Query-Encoder")
tokenizer = AutoTokenizer.from_pretrained("ncbi/MedCPT-Query-Encoder")


def search_queries(queries, k=10):
    """执行 FAISS 搜索"""
    with torch.no_grad():
        encoded = tokenizer(
            queries, padding=True, truncation=True, return_tensors="pt", max_length=64
        )
        embeds = (
            model(**encoded).last_hidden_state[:, 0, :].cpu().numpy().astype(np.float32)
        )

    scores, indices = index.search(embeds, k)

    results = []
    for idx, query in enumerate(queries):
        results.append(
            {
                "query": query,
                "results": [
                    {"pmid": pmids[i], "score": float(scores[idx][j])}
                    for j, i in enumerate(indices[idx])
                ],
            }
        )
    return results
