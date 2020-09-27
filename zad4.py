from typing import Optional
from fastapi import FastAPI
import csv
import json
from datetime import datetime, date, time, timezone

json_data = [json.dumps(d) for d in csv.DictReader(open('tags.csv'))]

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/scan")
def scan(data:json_data):
    return {"request":data}

@app.post("/api/results")
def results(Antenna_ID:int, Frequency:int, EPC_96:complex, Peak_RSSI:int, Phase:int, RF_Doppler_Frequency:int, Tags_Count:int, Seen:datetime):
    