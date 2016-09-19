import random

"""https://github.com/tensorflow/skflow"""
__author__ = 'zhangwj'
import tensorflow.contrib.learn as skflow
from sklearn import datasets, metrics


#Simple linear classification:
iris = datasets.load_iris()
classifier = skflow.TensorFlowLinearClassifier(n_classes=3)
classifier.fit(iris.data, iris.target)
score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
print("Accuracy: %f" % score)

#Deep Neural Network
classifier = skflow.TensorFlowDNNClassifier(hidden_units=[10, 20, 10], n_classes=3)
classifier.fit(iris.data, iris.target)
score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
print("Accuracy: %f" % score)

#Custom model
def my_model(X, y):
    """This is DNN with 10, 20, 10 hidden layers, and dropout of 0.5 probability."""
    layers = skflow.ops.dnn(X, [10, 20, 10], dropout=0.5)
    return skflow.models.logistic_regression(layers, y)

classifier = skflow.TensorFlowEstimator(model_fn=my_model, n_classes=3)
classifier.fit(iris.data, iris.target)
score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
print("Accuracy: %f" % score)


def DnnTest(x_data,y_data):
    global classifier, score
    classifier = skflow.TensorFlowLinearClassifier(n_classes=2)
    classifier.fit(X=x_data, y=y_data)
    score = metrics.accuracy_score(y_data, classifier.predict(x_data))
    print("Accuracy: %f" % score)
    # 3 layer neural network with rectified linear activation.
    random.seed(42)
    classifier = skflow.TensorFlowDNNClassifier(hidden_units=[10, 20, 10], n_classes=2, batch_size=128, steps=500,
                                                learning_rate=0.05)
    classifier.fit(X=x_data, y=y_data)
    score = metrics.accuracy_score(y_data, classifier.predict(x_data))
    print("Accuracy: %f" % score)  # 0.712682