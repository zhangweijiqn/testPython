# coding=utf8
tmp = {}
tmp["a"] = "aaa1"
tmp["b"] = "bbb2"
tmp["d"] = "ddd3"

print tmp["a"]
# print tmp["c"]    #直接获取会抛出异常
print tmp.get("c")  # 返回None

str = " aaa%s,bbb%s,ccc%s" % (tmp.get("a"), tmp.get("c"), tmp.get("d"))
print str

# sort according to value
d = {1: 5, 2: 3, 3: 2, 4: 1, 5: 4}
sorted(d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

# sort according to key
[(k, d[k]) for k in sorted(d.keys(), reverse=True)]

# delete key
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x.pop(1)
print x

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
del x[1]
print x