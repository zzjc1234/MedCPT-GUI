import os
from typing import List

from downloader import download_paper
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from search_engine import search_queries

app = FastAPI()

# 允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    queries: List[str]


class DownloadRequest(BaseModel):
    pmids: List[str]
    save_path: str


@app.post("/search")
def search(request: QueryRequest):
    print(request.queries)
    return search_queries(request.queries)


@app.post("/download")
def download(request: DownloadRequest):
    if not os.path.exists(request.save_path):
        os.makedirs(request.save_path)

    results = [download_paper(pmid, request.save_path) for pmid in request.pmids]
    return {"downloads": results}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
