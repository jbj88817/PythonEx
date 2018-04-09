# 反序列化 JSON
import json

# json_str = '{"name":"bojie", "age":18}'
json_str = '{"personData":[{"age":12,"name":"nate","schoolInfo":[{"School_name":"清华"},{"School_name":"北大"}],"url":"http://pic.yesky.com/uploadImages/2014/345/36/E8C039MU0180.jpg"},{"age":24,"name":"jack"}],"result":1}'

student = json.loads(json_str)
print(student)
print(type(student))
# print(student['name'])
# print(student['age'])
print(student['personData'][0]['url'])

# JSON object --> dict
# JSON array --> list
