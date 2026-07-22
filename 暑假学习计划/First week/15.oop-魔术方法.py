# __init__(构造方法)
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __str__(字符串方法)
    def __str__(self):
            return f"Student类对象,name:{self.name},age:{self.age}"

    # __lt__【小(大)于符合比较方法】
    def __lt__(self, other):
            return self.age < other.age
    
    # __le__[小(大)于等于比较方法]
    #和__lt__方法一致

    # __eq__(比较运算符实现)
    def __eq__(self, other):
            return self.age == other.age




stu =  Student("小张",19)
stu1 = Student("小李",23)

print(stu.name,stu.age)


print(stu)
print(str(stu))  #若无__str__方法此时两种都是打印的地址，而不是想获取的字符串信息

print(stu < stu1)
print(stu > stu1) 
print(stu == stu1)   #返回值为布尔值

