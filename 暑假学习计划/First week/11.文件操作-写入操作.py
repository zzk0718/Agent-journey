#文件的写入操作
#如果文件不存在则会创建新文件，写入内容。若文件存在，则会将输入内容覆盖原有的内容！

#打开文件
f = open("C:\\Users\\Lenovo\\Desktop\\暑假计划安排\\agent-journey\\测试.txt","w",encoding="UTF-8")

# write写入

f.write("好词！好词！")

# flush刷新
f.flush()

f.close() #close()内置了flush的功能