#coding=utf8
__author__ = 'zhangwj'
from pandas.util.testing import DataFrame
import random
import tensorflow.contrib.learn as skflow
import pandas as pd
from sklearn import metrics
import tensorflow as tf
import math

def data_preprocess(path,train=True):
    # data with title in csv file, read csv data to DataFrame
    ori_data = pd.read_csv(path,header=0)
    x_data = ori_data[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
    x_data.Sex = x_data.Sex.map( {'female': 1, 'male': 0} )
    x_data.Age.fillna(value=random.randint(1, 100),inplace=True)    # inplace，replace original column data.
    x_data.Embarked.fillna('C',inplace=True)
    x_data.Embarked = x_data.Embarked.map( {'C': 1, 'S':2, 'Q':3, '':4 } )
    x_data.Fare.fillna(value=random.randint(0,20),inplace=True)
    # add log(f) as a new feature for each f in training set.
    # to avoid log0, each log(x) is changed to log(x+1), x+0.1 will be better
    x_data['Pclass_Log'] = x_data['Pclass'].map(lambda x: math.log(x))
    x_data['Sex_Log'] = x_data['Sex'].map(lambda x: math.log(x+0.1))
    x_data['Age_Log'] = x_data['Age'].map(lambda x: math.log(x))
    x_data['SibSp_Log'] = x_data['SibSp'].map(lambda x: math.log(x+0.1))
    x_data['Parch_Log'] = x_data['Parch'].map(lambda x: math.log(x+0.1))
    x_data['Fare_Log'] = x_data['Fare'].map(lambda x: math.log(x+0.1))
    x_data['Embarked_Log'] = x_data['Embarked'].map(lambda x: math.log(x))

    if(train==True):
        y_data = ori_data['Survived']
        return x_data,y_data
    else:
        test_id = ori_data['PassengerId']
        return x_data,test_id

# 3 layer neural network with hyperbolic tangent activation.
def dnn_tanh(X, y):
    layers = skflow.ops.dnn(X, [10, 20, 10], tf.tanh)
    return skflow.models.logistic_regression(layers, y)

path = '../resources/train_titanic.csv'
x_data,y_data = data_preprocess(path)

random.seed(42)

classifier = skflow.TensorFlowEstimator(model_fn=dnn_tanh,n_classes=2, batch_size=128, steps=2000, learning_rate=0.02)
classifier.fit(X=x_data, y=y_data)
score = metrics.accuracy_score(y_data, classifier.predict(x_data))
print("Accuracy: %f" % score)   #0.823793


path2 = '../resources/test_titanic.csv'
x_data2,passengerIds = data_preprocess(path2,train=False)

test_predict = classifier.predict(x_data2)
data = {'PassengerId':passengerIds,'Survived':test_predict}
result = DataFrame(data)

# save DataFrame to csv file
result.to_csv('result.csv',index=False)#0.75598
