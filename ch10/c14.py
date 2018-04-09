# 反序列化 JSON
import json

# json_str = '{"name":"bojie", "age":18}'
json_str = '[{"name":"bojie", "age":18, "flag":false}, {"name":"haha", "age":20}]'

student = json.loads(json_str)
print(student)
print(type(student))
# print(student['name'])
# print(student['age'])

# JSON object --> dict
# JSON array --> list
