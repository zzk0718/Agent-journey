"""
文件操作三大步：
打开
读或写
关闭
"""

#open(name,mode,encoding)
#name:是打开的目标文件名的字符串(可以包含文件所在的具体路径)
#mode:设置打开文件的模式(访问模式):只读，写入，追加等
#encoding:编码格式(推荐使用UTF-8)

f = open("C:\\Users\\Lenovo\\Desktop\\暑假计划安排\\agent-journey\\测试.txt",'r',encoding="UTF-8")
print(type(f))

#读取文件-read()
print(f"读取五个字节的结果是:{f.read(5)}")
print(f"read方法读取全部内容的结果是:{f.read()}")
print("--------------------------")

#读取文件-readlines()
lines = f.readlines() #读取文件的全部行，封装到列表中
print(f"lines对象的类型:{type(lines)}")
print(f"lines对象的内容是:{lines}")

#读取文件-readline()
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()

print(f"{line1}")
print(f"{line2}")
print(f"{line3}")

#for循环读取文件行
for line in f:
    print(f"每一行数据是:{line}")

#文件关闭
f.close

# with open 语法操作文件(操作执行完后自动关闭文件)
with open("C:\\Users\\Lenovo\\Desktop\\暑假计划安排\\agent-journey\\测试.txt",'r',encoding="UTF-8") as f:
    for line in f:
     print(f"每一行数据是:{line}")