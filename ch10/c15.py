# JSON 序列化
import json

student = [
    {'name': 'bojie', 'age': 18, 'flag': False},
    {'name': 'qiyue', 'age': 18}
]

json_str = json.dumps(student)
print(type(json_str))
print(json_str)
