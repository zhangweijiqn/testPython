# coding=utf8
import math

import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

# preprocess
path = '/Users/zhangweijian01/Downloads/data.csv'
ori_data = pd.read_csv(path, header=0, sep='\t')
y_data = ori_data['Y']
x_data = ori_data.ix[:, 3:]
x_data = x_data.fillna(x_data.mean())
y_data = y_data.fillna(y_data.mean())

# to handle missing values
imp = Imputer(missing_values='NaN', strategy='median', axis=0)
imp.fit(x_data)
data_imp = imp.transform(x_data)
x_scaler = data_imp

# scalar
x_scaler = StandardScaler().fit_transform(data_imp)
x_scaler = x_scaler.astype(np.float64, copy=False)

for i in range(0, len(x_scaler)):
    for j in range(0, len(x_scaler[i])):
        x_scaler[i][j] = float('%.4f' % (x_scaler[i][j]))

# sava preprocessed data to file
np.savetxt("newdata2.csv", x_scaler, delimiter=",")

f = open('newdata1.csv', 'w')
for i in range(0, len(x_scaler)):
    line = str(y_data[i])
    for j in range(0, len(x_scaler[i])):
        line = line + ',' + str(x_scaler[i][j])
    line += '\n'
    f.write(line)
f.close()

# trans dataframe to numpy
X = np.array(x_scaler, np.float64)
y = np.array(y_data, np.float64)

# train model
from sklearn import linear_model

reg = linear_model.Lasso(alpha=0.01)

reg.fit(X, y)
mse = 0
for i in range(0, len(X)):
    print str(reg.predict(X[i])) + "," + str(y[i])
    mse += math.pow(reg.predict(X[i]) - y[i], 2)
mse = math.sqrt(mse)
print reg.coef_
print mse
