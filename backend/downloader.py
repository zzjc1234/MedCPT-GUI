import os

import requests

BASE_URL = "https://pubmed.ncbi.nlm.nih.gov/"


def download_paper(pmid, save_path):
    """下载 PubMed 文献"""
    url = f"{BASE_URL}{pmid}/"
    response = requests.get(url)

    if response.status_code == 200:
        file_path = os.path.join(save_path, f"{pmid}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        return {"pmid": pmid, "status": "success", "path": file_path}
    else:
        return {"pmid": pmid, "status": "failed"}
