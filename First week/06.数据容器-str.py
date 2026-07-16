#字符串 基本操作 -------->不可变的(无法修改)
s = "Hello-Python"

print(s[4])
print(s[-8])

for i in s:
    print(i)


#切片
print(s[0:5:1])
print(s[:5])

#字符串常用方法(由于字符串不可变，所以所有方法不会改变原字符串本身)
s = "Hello-Python-Hello-World"

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

# count() 统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)

# upper() 转为大写
su = s.upper()
print(su)

# lower() 转为小写
sl = s.lower()
print(sl)

# split() 将字符串按照指定字符串切割 - 列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空格
ss = s.strip()
print(ss)

# replace() 将字符串中的指定子串替换为新的内容
sr = s.replace("-", "_")
print(sr)

# startswith() / endswith() 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))