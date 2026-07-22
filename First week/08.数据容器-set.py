#集合set(无序的，不可重复的，可修改的)
#定义

s1 = set()
s1 = {5,32,1,2,3,1,5,76}  #(自动去重)
print(s1)

# 常见方法：
# add()：添加元素到集合
s1 = {100,200,300,400,500,600,700,800}
print(s1)

s1.add(1200)
print(s1)

# remove()：移除集合中的指定元素(指定元素不存在将报错)
s1.remove(200)
print(s1)

# pop()：随机删除集合中的元素并返回
e = s1.pop()
print(e)
print(s1)

# clear()：清空集合
s1.clear()
print(s1)

s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}

# difference()：求两个集合的差集（存在于第一个集合，但不存在于第二个集合）
s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}

print(s2.difference(s3))
print(s3.difference(s2))

# union() ：求两个集合的并集
print(s2.union(s3))
print(s2.union(s3))

# intersection()：求两个集合的交集
print(s2.intersection(s3))
print(s2.intersection(s3))