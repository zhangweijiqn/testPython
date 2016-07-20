#encoding=utf-8
import word2vec

# word2vec.word2vec("/home/zhangwj/Applications/Scrapy/baike/files/data_fenci.txt","/home/zhangwj/Applications/Scrapy/baike/files/data_fenci.bin",size=100,verbose=True)
# word2vec.word2vec是调用的构造函数，在scripts_interface.py文件中

model = word2vec.load("/home/zhangwj/Applications/Scrapy/baike/files/data_fenci.bin")
# print model.vocab
# print model.vectors.shape
# print model.vectors
# print model["dog"].shape
# print model["anarchism"][:10]


indexs,metrics = model.cosine(u'中国')
print indexs,metrics
# print model.vocab[indexs]
for ele,similarity in model.generate_response(indexs,metrics).tolist():
  print ele,similarity

  # indexs,metrics = model.cosine("los_angeles")
  # print model.generate_response(indexs,metrics).tolist()

