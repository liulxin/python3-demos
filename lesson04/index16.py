import json

json_str = '[{"name": "lisi", "age": "18"}, {"name": "zhangsan", "age": "19"}]'

student = json.loads(json_str)

print(student) # [{'name': 'lisi', 'age': '18'}, {'name': 'zhangsan', 'age': '19'}]

print(type(student)) # <class 'list'>