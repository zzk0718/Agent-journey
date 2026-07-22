# type()-------> 获取指定字面量或变量的类型

print(type(100)) #int
print(type("Hello")) #str

# isinstance(数据，类型)------> bool值------>判断这个数据是否是指定的类型

print(isinstance(100,int))
print(isinstance(6.66,str))

#字符串
#定义字符串的三种方式
s1 = 'zzk'
s2 = "zzk"
s3 = """zzk666
        zzk888""" #只有三引号支持换行

#字符串拼接
s4 = "gdut"
s5 = "的学生"

print("我是" + s4 + s5) # +号只能拼接字符串

#字符串格式化
s6 = 18
s7 = "广东工业大学"

#方法一 
print("我今年%s岁,是%s的学生" %(s6,s7)) #类似c语言中的printf函数(并且不用做类型转换如:6是int类型)

#方法二
print(f"我今年{s6}岁，是{s7}的学生") #推荐方式