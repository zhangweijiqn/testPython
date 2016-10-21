#coding=utf8
import codecs
from gensim import corpora,models
import os
import jieba

stopwords = codecs.open('stop_words_zh_UTF-8.txt','r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]

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

def TfIdf(filelist):
    path = '/home/zhangwj/scikit_learn_data/docs/'
    train_set = []  #存取100份文档的分词结果
    for ff in filelist :
        fname = path + ff
        f = open(fname,'r+')
        content = f.read()
        words = []
        for word in jieba.cut(content):
            word = word.strip()
            if word.encode('utf-8') not in stopwords:
                words.append(word)
        train_set.append( words )
        f.close()
    dic = corpora.Dictionary(train_set)
    corpus = [dic.doc2bow(text) for text in train_set]      #转换为词包
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    return dic,corpus,corpus_tfidf

def LDA(dic,corpus,corpus_tfidf):
    lda = models.LdaModel(corpus_tfidf, id2word = dic, num_topics = 20)
    lda.print_topics(20)

    for i in range(0, 20):
        print i, lda.print_topic(i)

    for train in corpus:
        print lda.get_document_topics( train )

if __name__ == "__main__":
    (allfile,path) = getFilelist(["","/home/zhangwj/scikit_learn_data/docs/"])
    for ff in allfile :
        print "Using jieba on "+ff
    dic,corpus,corpus_tfidf = TfIdf(allfile)
    LDA(dic,corpus,corpus_tfidf)
