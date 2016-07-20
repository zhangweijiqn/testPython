#encoding=utf-8
import word2vec

def testWord2Phrase():
    #Run word2phrase to group up similar words "Los Angeles" to "Los_Angeles"
    #This will create a text8-phrases that we can use as a better input for word2vec.
    # #Note that you could easily skip this previous step and use the origial data as input for word2vec.
    word2vec.word2phrase('/D/test/text8/text8', '/D/test/text8/text8-phrases', verbose=True)

def testWord2Vec():
    #Train the model using the word2phrase output.
    #That generated a text8.bin file containing the word vectors in a binary format.
    word2vec.word2vec('/D/test/text8/text8-phrases.txt', '/D/test/text8/text8-phrases.bin', size=100, verbose=True)

    #Predictions
    model = word2vec.load('/D/test/text8/text8-phrases.bin')

    #take a look at the vocabulaty as a numpy array
    print model.vocab   #vocabulaty

    #Or take a look at the whole matrix
    print model.vectors.shape   #word vector
    print model.vectors

    # retreive the vector of individual words
    print model['dog'].shape
    print model['dog'][:10]

    #We can do simple queries to retreive words similar to "socks" based on cosine similarity:
    indexes, metrics = model.cosine('socks')

    #Its possible to get the words of those indexes
    print model.vocab[indexes]

    #There is a helper function to create a combined response: a numpy record array
    print model.generate_response(indexes, metrics).tolist()


    #Since we trained the model with the output of word2phrase we can ask for similarity of "phrases"
    indexes, metrics = model.cosine('los_angeles')  #单词的索引和余弦相似度
    print model.generate_response(indexes, metrics).tolist()  #单词和余弦相似度


    #Its possible to do more complex queries like analogies such as: king - man + woman = queen This method returns the same as cosine the indexes of the words in the vocab and the metric
    indexes, metrics = model.analogy(pos=['king', 'woman'], neg=['man'], n=10)
    print model.generate_response(indexes, metrics).tolist()

def testWord2Cluter():
    """Cluster"""
    #Do the clustering of the vectors based on the trained model.
    #That created a text8-clusters.txt with the cluster for every word in the vocabulary
    word2vec.word2clusters('/D/test/text8/text8', '/D/test/text8/text8-clusters', 100, verbose=True)
    clusters = word2vec.load_clusters('/Users/drodriguez/Downloads/text8-clusters')
    print clusters['dog']
    print clusters.get_words_on_cluster(90).shape
    print clusters.get_words_on_cluster(90)[:10]