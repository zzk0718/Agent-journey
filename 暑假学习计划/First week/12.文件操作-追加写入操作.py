#文件的追加写入操作(与前两种基本一致)

#打开文件
f = open("C:\\Users\\Lenovo\\Desktop\\暑假计划安排\\agent-journey\\测试.txt","a",encoding="UTF-8")

# write写入
f.write("\n好词！好词！")

# flush刷新
f.flush()

# close关闭
f.close()