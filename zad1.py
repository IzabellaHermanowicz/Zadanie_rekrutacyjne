import json

with open('12.json') as f:
  data_json = json.load(f)

def getTotals(typ, dict):
    total_cost = 0
    total_amount = 0
    dict=dict['data']
    for x in dict:
        if typ in x.values():
            

getTotals('A',data_json)