#列表操作
#定义
s = [56,99,54,2,56,'a',"helllo"]

print(type(s))

#访问列表元素
#获取
for i in s:
  print(i)
 
print(s[-1])


#修改
s[5]="zzk"

#删除
del s[-1]
print(s)

#-------------------列表list切片--------------------
a = ['A','C','H','L','B','D','X','C','U']

#切片操作 s[开始索引：结束索引：步长]
print(a[0:5:1]) #结束索引不会打印
print(a[:6:2])
print(a[1::1])
print(a[-9::1])

#------------------列表list常用方法------------------
b = [1,2,3,4,5,6,7,8,9]

#append():在列表尾部追加元素
b.append(10)
print(b)

#insert(index,object):在指定索引之前插入元素
b.insert(0,0)
print(b)

#remove()移除列表中第一个匹配的元素
b.remove(10)
print(b)

#pop()删除列表中指定索引元素并返回(如果未指定则默认删除最后一个)
i = b.pop()
print(i)

#sort():排序
#reverse():反转链表元素
b.reverse()
print(b)

