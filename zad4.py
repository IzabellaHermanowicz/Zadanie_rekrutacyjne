from typing import Optional
from fastapi import FastAPI
import csv
import json

json_data = [json.dumps(d) for d in csv.DictReader(open('tags.csv'))]

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/scan")

@app.post("/api/results")