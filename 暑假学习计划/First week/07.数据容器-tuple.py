#元组的基本操作 - tuple(不支持修改)
#定义
t1 = tuple()
t1 = (80,1,354,6754,23)

#索引访问
print(t1[0])
print(t1[-1])

#切片
print(t1[0:3:1])

#count()统计元素个数
print(t1.count(80))

#index()获取元素的索引(第一个元素的位置)
print(t1.index(80))