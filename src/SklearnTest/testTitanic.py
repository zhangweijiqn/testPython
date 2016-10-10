#coding=utf8
from sklearn.svm import LinearSVC

__author__ = 'zhangwj'
from pandas.util.testing import DataFrame
import random
import pandas as pd
import math

import numpy as np


def data_preprocess(path, train=True):
    # data with title in csv file, read csv data to DataFrame
    ori_data = pd.read_csv(path, header=0)
    x_data = ori_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
    x_data.Sex = x_data.Sex.map({'female': 1, 'male': 0})
    x_data.Age.fillna(value=random.randint(1, 100),
                      inplace=True)  # inplace,replace original column data.
    x_data.Embarked.fillna('C', inplace=True)
    x_data.Embarked = x_data.Embarked.map({'C': 1, 'S': 2, 'Q': 3, '': 4})
    x_data.Fare.fillna(value=random.randint(1, 100),
                       inplace=True)
    # add log(f) as a new feature for each f in training set.
    # to avoid log0, each log(x) is changed to log(x+1), x+0.1 will be better
    x_data['Pclass_Log'] = x_data['Pclass'].map(lambda x: math.log(x))
    x_data['Sex_Log'] = x_data['Sex'].map(lambda x: math.log(x + 0.1))
    x_data['Age_Log'] = x_data['Age'].map(lambda x: math.log(x))
    x_data['SibSp_Log'] = x_data['SibSp'].map(lambda x: math.log(x + 0.1))
    x_data['Parch_Log'] = x_data['Parch'].map(lambda x: math.log(x + 0.1))
    x_data['Fare_Log'] = x_data['Fare'].map(lambda x: math.log(x + 0.1))
    x_data['Embarked_Log'] = x_data['Embarked'].map(lambda x: math.log(x))
    # judge if train or test
    if (train == True):
        y_data = ori_data['Survived']
        return x_data, y_data
    else:
        test_id = ori_data['PassengerId']
        return x_data, test_id


path = '../resources/train_titanic.csv'
x_data, y_data = data_preprocess(path)
# transform pandas DataFrame to Numpy ndarray
X = np.array(x_data,np.float32)
y = np.array(y_data,np.float32)

from sklearn.ensemble import RandomForestClassifier
# Train uncalibrated random forest classifier on whole train and validation
# data and evaluate on test data
# clf = RandomForestClassifier(n_estimators=50,criterion='entropy')  # n_estimators,The number of trees in the forest.
clf = LinearSVC(penalty='l2',   #The ‘l2’ penalty is the standard used in SVC. The ‘l1’ leads to coef_ vectors that are sparse.
                loss='squared_hinge',   #Specifies the loss function. ‘hinge’ is the standard SVM loss (used e.g. by the SVC class) while ‘squared_hinge’ is the square of the hinge loss.
                dual=True,
                tol=0.0001,
                C=1.0,
                multi_class='ovr',
                fit_intercept=True,
                intercept_scaling=1,
                class_weight=None,
                verbose=0,
                random_state=None,
                max_iter=1000)
clf.fit(X[:], y[:])

path2 = '../resources/test_titanic.csv'
x_data2, passengerIds = data_preprocess(path2, train=False)
X2 = np.array(x_data2,np.float32)
clf_label = clf.predict(X2)
data = {'PassengerId': passengerIds, 'Survived': np.int32(clf_label)}
result = DataFrame(data)

# save DataFrame to csv file
result.to_csv('result.csv', index=False)  # 0.75598
