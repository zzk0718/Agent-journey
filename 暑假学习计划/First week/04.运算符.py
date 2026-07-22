#算术运算符
print("10 + 4 = ", 10 + 4)  # 加
print("10 - 4 = ", 10 - 4)  # 减
print("10 * 4 = ", 10 * 4)  # 乘
print("10 / 4 = ", 10 / 4)  # 除 - 2.5
print("10 // 4 = ", 10 // 4) # 整除(结果为整数) - 2
print("10 % 4 = ", 10 % 4)  # 取余/求模 - 2
print("10 ** 4 = ", 10 ** 4) # 幂指数，10的4次方 - 10000

#赋值运算符
num = 85

num += 10  # num = num + 10
print("num += 10 后, num = ", num)

num -= 10  # num = num - 10
print("num -= 10 后, num = ", num)

num *= 10  # num = num * 10
print("num *= 10 后, num = ", num)

num /= 10  # num = num / 10
print("num /= 10 后, num = ", num)

num //= 10  # num = num // 10
print("num //= 10 后, num = ", num)

num %= 3  # num = num % 3
print("num %= 3 后, num = ", num)

num **= 3  # num = num ** 3
print("num **= 3 后, num = ", num)

#比较运算符 ==  !=  >  >=  <  <= 
print("100 == 100 吗 : ", 100 == 100)      #True
print("'100' == '100' 吗 : ", "100" == "100") #True
print("100 != 100 吗 : ", 100 != 100)      #False

print("100 < 100 吗 : ", 100 < 100)        #False
print("100 <= 100 吗 : ", 100 <= 100)      #True

print("100 > 100 吗 : ", 100 > 100)        #False
print("100 >= 100 吗 : ", 100 >= 100)      #True

#逻辑运算符 and or not
print(1 and 0)
print(1 and 1)

print(1 or 0)
print(1 or 1)

print(not 1)
print(not 0)


