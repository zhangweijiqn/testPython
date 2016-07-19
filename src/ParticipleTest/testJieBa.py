# encoding=utf-8
import jieba
# IDEA auto install jieba package
"""
https://github.com/fxsjy/jieba

简单测试分词
"""

def test1():
    #简单测试分词
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

    seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))

def test2():
    # 测试词性标注
    import jieba.posseg as pseg
    words = pseg.cut("病毒性感冒")
    for word, flag in words:
        print('%s %s' % (word, flag))

def test3():
    #测试自定义词典
    jieba.load_userdict("/home/zhangwj/MyProjects/testProjects/TestLanguageTech/testPython/src/ParticipleTest/dict.txt")
    seg_list = jieba.cut("病毒性感冒", cut_all=False)  #字典中同时含有病毒，性，感冒，病毒性感冒
    print("Default Mode: " + "/ ".join(seg_list))
    # Default Mode: 病毒性感冒
    #在default mode下，进行的是最大匹配

if __name__=='__main__':
    test3()