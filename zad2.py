import json
import pprint

def getItems(X):
  with open('12.json') as f:
    data_json = json.load(f)
    obj=[]
    dict=data_json['data']
    for x in dict:
        if X > x.get('amount'):
            obj.append(x)
    pprint.pprint(json.dumps(obj))         

getItems(5)
getItems(10)
getItems(15)