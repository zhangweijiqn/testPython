#coding=utf8

# build on ubuntu: https://github.com/dmlc/xgboost/blob/master/doc/build.md
# git clone --recursive https://github.com/dmlc/xgboost
# cd xgboost;  make -j4
# cd python-package;  sudo python setup.py install

#get started: https://github.com/dmlc/xgboost/blob/master/doc/get_started/index.md

import xgboost as xgb   #在这里还要手工在IDEA中install一下
# read in data
dtrain = xgb.DMatrix('/home/zhangwj/Applications/XGBoost/xgboost/demo/data/agaricus.txt.train')
dtest = xgb.DMatrix('/home/zhangwj/Applications/XGBoost/xgboost/demo/data/agaricus.txt.test')
# specify parameters via map
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
num_round = 2
bst = xgb.train(param, dtrain, num_round)
# make prediction
preds = bst.predict(dtest)
print preds