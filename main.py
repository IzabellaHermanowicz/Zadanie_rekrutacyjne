from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/scan")

@app.post("/api/results")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}