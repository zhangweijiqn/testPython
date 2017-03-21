import sys
# wirte（）方法把字符串写入文件，writelines（）方法可以把列表中存储的内容写入文件。

# 写文件方式一
f = file("hello.txt", "w+")  # 如果需要保留文件中原有的内容，只是需要追加新的内容，可以使用“a+”模式
li = ["hello world\n", "hello china\n"]
f.writelines(li)
f.close()

# 写文件方式二
print "hello"
# python testFileOp.py > hello.txt

# 读文件方式一
f1 = open('./tids_quality')
for line in f1.readlines():
    print line
f1.close()

#读文件方式二
# python testFileOp.py < hello.txt
for line in sys.stdin:
    print line