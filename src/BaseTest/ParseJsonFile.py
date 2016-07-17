__author__ = 'zhangwj'
# -*- coding: utf-8 -*-
import json
#本文件用来解析json文件

def test():
    print "this is a test for json"
    with open('/home/zhangwj/Applications/Scrapy/tutorial/files/data.json', 'r') as f:
        for file in f:
            data = json.loads(file)
            print data["name"],",",data["url"],",",data["introduct"]
            for k,v in data["info"].items():
                print k,"：",v
            print "\n"

if __name__=='__main__':
    test()
