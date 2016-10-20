#coding=utf8
'''http://www.cnblogs.com/chenbjin/p/3851165.html
scikit-learn包进行TF-IDF分词权重计算主要用到了两个类：CountVectorizer和TfidfTransformer。其中
　　CountVectorizer是通过fit_transform函数将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在第i个文本下的词频。
    即各个词语出现的次数，通过get_feature_names()可看到所有文本的关键字，通过toarray()可看到词频矩阵的结果.
    TfidfTransformer是统计vectorizer中每个词语的tf-idf权值
'''

import os
import jieba
import sys
import string
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

reload(sys)
sys.setdefaultencoding('utf8')

#获取文件列表（该目录下放着100份文档）
def getFilelist(argv) :
    path = argv[1]
    filelist = []
    files = os.listdir(path)
    for f in files :
        if(f[0] == '.') :
            pass
        else :
            filelist.append(f)
    return filelist,path

#对文档进行分词处理
def fenci(argv,path) :
    #保存分词结果的目录
    sFilePath = './segfile'
    if not os.path.exists(sFilePath) :
        os.mkdir(sFilePath)

    #读取文档
    filename = argv
    f = open(path+filename,'r+')
    file_list = f.read()
    f.close()

    #对文档进行分词处理，采用默认模式
    seg_list = jieba.cut(file_list,cut_all=True)

    #对空格，换行符进行处理
    result = []
    for seg in seg_list :
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n") :
            result.append(seg)

    #将分词后的结果用空格隔开，保存至本地。比如"我来到北京清华大学"，分词结果写入为："我 来到 北京 清华大学"
    f = open(sFilePath+"/"+filename+"-seg.txt","w+")
    f.write(' '.join(result))
    f.close()

#读取100份已分词好的文档，进行TF-IDF计算
def Tfidf(filelist) :
    path = './segfile/'
    corpus = []  #存取100份文档的分词结果
    for ff in filelist :
        fname = path + ff + "-seg.txt"
        f = open(fname,'r+')
        content = f.read()
        f.close()
        corpus.append(content)

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    word = vectorizer.get_feature_names() #所有文本的关键字
    weight = tfidf.toarray()              #对应的tfidf矩阵

    sFilePath = './tfidffile'
    if not os.path.exists(sFilePath) :
        os.mkdir(sFilePath)

    # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
    for i in range(len(weight)) :
        print u"--------Writing all the tf-idf in the",i,u" file into ",sFilePath+'/'+string.zfill(i,5)+'.txt',"--------"
        f = open(sFilePath+'/'+string.zfill(i,5)+'.txt','w+')
        for j in range(len(word)) :
            f.write(word[j]+"    "+str(weight[i][j])+"\n")
        f.close()

if __name__ == "__main__" :
    (allfile,path) = getFilelist(["","/home/zhangwj/scikit_learn_data/docs/"])
    for ff in allfile :
        print "Using jieba on "+ff
        fenci(ff,path)

    Tfidf(allfile)
