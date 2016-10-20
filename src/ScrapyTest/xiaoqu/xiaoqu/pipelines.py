# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )   #不加这段代码会报错：UnicodeEncodeError: 'ascii' codec can't encode characters in position
from scrapy import log

import codecs
import json

class XiaoquPipeline(object):
    def __init__(self):
        self.file = codecs.open('xiaoqu.txt', 'wb',encoding='utf-8')
    def process_item(self, item, spider):
        try:
            line = item['name']+","+item['address']+"\n"
            self.file.write(line)
        except BaseException,x:
            print 'Error:',x
            print item
            log.err(x.message)
        return item

    def spider_closed(self):
        self.file.close()
