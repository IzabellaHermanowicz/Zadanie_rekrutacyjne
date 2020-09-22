import json

with open('12.json') as f:
  data_json = json.load(f)

def getItems(X, dict):
    obj={}
   
    dict=dict['data']
    for x in dict:
        if x.get('amount') < X:
            obj.update(x)

    new_json= json.dumps(obj)
    print(new_json)

getItems(5, data_json)