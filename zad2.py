import json

with open('12.json') as f:
  data_json = json.load(f)

def getItems(X, dict):
   
    dict=dict['data']
    for x in dict:
        if x.get('amount') < X:
            print(x)


getItems(5, data_json)