"""
演示JSON数据和Python字典的相互转换
"""

import json

# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name":"小张","age":19},{"name" :"小李","age":11},{"name" : "小王","age":23}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)
# 准备字典，将字典转换为JSON
py_dict = {"title": "Python教程", "price": 49.9}
# 字典转JSON
dict_json = json.dumps(py_dict, ensure_ascii=False)
print("\n字典转JSON:", dict_json)

# 将JSON字符串转换为Python数据类型[{k: v, k: v}, {k: v, k: v}]
s = '''[{"name":"小张","age":19},{"name":"小李","age":11},{"name":"小王","age":23}]'''
l = json.loads(s)
print(type(l))
print(l)
# 将JSON字符串转换为Python数据类型{k: v, k: v}
# JSON字符串转字典
dict_str = '{"title":"Python教程","price":49.9}'
res_dict = json.loads(dict_str)
print(type(dict_str))
print(dict_str)