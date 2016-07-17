#coding=utf8
tmp = {}
tmp["a"]="aaa1"
tmp["b"]="bbb2"
tmp["d"]="ddd3"

print tmp["a"]
# print tmp["c"]    #直接获取会抛出异常
print tmp.get("c")  #返回None

str = " aaa%s,bbb%s,ccc%s"%(tmp.get("a"),tmp.get("c"),tmp.get("d"))
print str