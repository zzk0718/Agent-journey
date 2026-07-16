#字典 ----key不能重复(如果重复后面的值会覆盖前面的值)
#定义字典
dict1 = {}
dict1 = dict()
dict1 = {"王林":6700, "李慕妍":6008, "徐立国":5880, "黄立":6888}

#访问
print(dict1["徐立国"]) #获取
dict1["徐立国"] = 8888 #修改
print(dict1["徐立国"])

# -------------------- 字典 常见操作 --------------------
dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"] = 550
print(dict1)

# 修改 - key存在就是修改
dict1["涛哥"] = 620
print(dict1)

# 查询
print(dict1["涛哥"])       # 根据key获取value
print(dict1.get("涛哥"))   # 根据key获取value

print(dict1.keys())       # 获取所有的key
print(dict1.values())     # 获取所有的value
print(dict1.items())      # 获取所有的键值对 key:value

# 删除
score = dict1.pop("许立国")
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)