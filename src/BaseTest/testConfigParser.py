#coding=utf8
# 在传递键值对数据时，会将键名 全部转化为小写
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read("test_config")
print config.get('section', 'name')
print config.get('DEFAULT', 'default')
print config.get("My Section", "foodir")
