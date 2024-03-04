import json

json_string = '{"key": "value"}'
parsed = json.loads(json_string)
print(parsed)

data = {
    "name" : "Lovekesh",
    "age" : 21,
    "cars" : ['bmw','audi','ferrari']
    
}
jscomp = json.dumps(data)
print(jscomp)

import pickle
pickled_string = pickle.dumps([1,2,3,'a','b','c'])
print(pickle.loads(pickled_string))
print()

#Exercise

def add_employee(salaries_json,name,salary):
    data = json.loads(salaries_json)
    data[name] = salary
    salaries_json = json.dumps(data)
    return salaries_json

salaries = '{"Alfred" : 300 , "Jane" : 400}'
new_salaries = add_employee(salaries,"Me",800)

decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])

# output 300 400 800
