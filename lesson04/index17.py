import json

student = [{'name': 'lisi', 'age': '18'}, {'name': 'zhangsan', 'age': '19'}]

json_str = json.dumps(student)

print(json_str) # [{"name": "lisi", "age": "18"}, {"name": "zhangsan", "age": "19"}]

print(type(json_str)) # <class 'str'>
