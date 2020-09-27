from typing import Optional
from fastapi import FastAPI, Response, status
import csv
import json

app = FastAPI()
json_data = []

@app.get("/api/results", status_code=200)
def results():
    return json_data

@app.post("/api/scan", status_code=200)
def scan(response: Response):
    global json_data
    try:
        json_data = [json.dumps(d) for d in csv.DictReader(open('tags.csv'))]
    except:
        json_data = []
        response.status_code = status.HTTP_404_NOT_FOUND
        return{"status":"File not found"}
    return {"status":"ok"}