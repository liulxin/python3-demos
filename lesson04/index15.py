import json

json_str = '{"name": "lisi", "age": "18"}'

student = json.loads(json_str)

print(student) # {'name': 'lisi', 'age': '18'}

print(type(student)) # <class 'dict'>