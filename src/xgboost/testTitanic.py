#coding=utf8
from pandas.util.testing import DataFrame
import random
import pandas as pd
import math
import numpy as np
import xgboost as xgb

# data with title in csv file
ori_data = pd.read_csv('../resources/train_titanic.csv',header=0)
x_data = ori_data[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
x_data.Sex = x_data.Sex.map( {'female': 1, 'male': 0} )
x_data.Age.fillna(value=random.randint(1, 100),inplace=True)
x_data.Embarked.fillna('C',inplace=True)
x_data.Embarked = x_data.Embarked.map( {'C': 1, 'S':2, 'Q':3, '':4 } )
x_data['Pclass_Log'] = x_data['Pclass'].map(lambda x: math.log(x))
x_data['Sex_Log'] = x_data['Sex'].map(lambda x: math.log(x+1))
x_data['Age_Log'] = x_data['Age'].map(lambda x: math.log(x))
x_data['SibSp_Log'] = x_data['SibSp'].map(lambda x: math.log(x+1))
x_data['Parch_Log'] = x_data['Parch'].map(lambda x: math.log(x+1))
x_data['Fare_Log'] = x_data['Fare'].map(lambda x: math.log(x+1))
x_data['Embarked_Log'] = x_data['Embarked'].map(lambda x: math.log(x))
y_data = ori_data['Survived']

# specify parameters via map
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
num_round = 2
dtrain = xgb.DMatrix(np.array(x_data),np.array(y_data))
bst = xgb.train(param, dtrain, num_round)

test_data = pd.read_csv('../resources/test_titanic.csv',header=0)
x_data2 = test_data[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
x_data2.Sex = x_data2.Sex.map( {'female': 1, 'male': 0} )
x_data2.Age.fillna(value=random.randint(1, 100),inplace=True)
x_data2.Fare.fillna(value=x_data2.Fare.mean(),inplace=True)
x_data2.Embarked.fillna('C',inplace=True)
x_data2.Embarked = x_data2.Embarked.map( {'C': 1, 'S': 2, 'Q':3, '':4 } )
x_data2['Pclass_Log'] = x_data2['Pclass'].map(lambda x: math.log(x))
x_data2['Sex_Log'] = x_data2['Sex'].map(lambda x: math.log(x+1))
x_data2['Age_Log'] = x_data2['Age'].map(lambda x: math.log(x))
x_data2['SibSp_Log'] = x_data2['SibSp'].map(lambda x: math.log(x+1))
x_data2['Parch_Log'] = x_data2['Parch'].map(lambda x: math.log(x+1))
x_data2['Fare_Log'] = x_data2['Fare'].map(lambda x: math.log(x+1))
x_data2['Embarked_Log'] = x_data2['Embarked'].map(lambda x: math.log(x))

dtest = xgb.DMatrix(np.array(x_data2))
preds = bst.predict(dtest)
# print(preds)
data = {'PassengerId':test_data['PassengerId'],'Survived':preds}
result = DataFrame(data)
#
result.to_csv('result.csv',index=False)#0.75598
