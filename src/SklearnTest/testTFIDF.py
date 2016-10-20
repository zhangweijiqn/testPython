#coding=utf8
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import codecs
from sklearn.datasets import fetch_20newsgroups

def test2():
    with codecs.open('/home/zhangwj/Applications/Scrapy/baike/files/data_fenci.txt', 'rb',encoding='utf-8') as f:
        data_samples = f.read()
    n_features = 1000
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,   #CountVectorizer是通过fit_transform函数将文本中的词语转换为词频矩阵
                                       max_features=n_features,stop_words=u"应该"
                                       ) #TfidfTransformer是统计vectorizer中每个词语的tf-idf权值
    tfidf = tfidf_vectorizer.fit_transform(data_samples)  # return sparse matrix, [n_samples, n_features],Tf-idf-weighted document-term matrix.
    tfidf_vectorizer.get_feature_names() #上面输出的是tfidf的权重矩阵 sample*feature, 该函数打印feature names, 一个sample是一篇文档

def test1():
    n_samples = 2000
    n_features = 1000
    print("Loading dataset...")
    dataset = fetch_20newsgroups(shuffle=True, random_state=1,
                                 remove=('headers', 'footers', 'quotes'))
    data_samples = dataset.data[:n_samples]

    # Use tf-idf features for NMF.
    print("Extracting tf-idf features for NMF...")
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                       max_features=n_features,
                                       stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(data_samples)  #sparse matrix, [n_samples, n_features],Tf-idf-weighted document-term matrix.
    tfidf_vectorizer.get_feature_names() #上面输出的是tfidf的权重矩阵 sample*feature, 该函数打印feature names, 一个sample是一篇文档

test1()
test2()#中文存在问题
