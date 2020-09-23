import json

def getTotals(typ):
  with open('12.json') as f:
    data_json = json.load(f)
    total_cost = 0
    total_amount = 0
    dict=data_json['data']
    for x in dict:
        if typ in x.values():
            total_cost+=x.get('cost')
            total_amount+=x.get('amount')
    
    print('{ "total_cost": ', total_cost,', "total_amount": ',total_amount,' }')

getTotals('A')
getTotals('B')
getTotals('C')