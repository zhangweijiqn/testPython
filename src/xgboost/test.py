#coding=utf8

# build on ubuntu: https://github.com/dmlc/xgboost/blob/master/doc/build.md
# git clone --recursive https://github.com/dmlc/xgboost
# cd xgboost;  make -j4
# cd python-package;  sudo python setup.py install

#get started: https://github.com/dmlc/xgboost/blob/master/doc/get_started/index.md
from __future__ import print_function
import xgboost as xgb   #在这里还要手工在IDEA中install一下


def testTrain():
    # read in data
    dtrain = xgb.DMatrix('/home/zhangwj/Applications/xgboost/demo/data/agaricus.txt.train')
    dtest = xgb.DMatrix('/home/zhangwj/Applications/xgboost/demo/data/agaricus.txt.test')
    # specify parameters via map
    param = {'max_depth':20, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
    num_round = 100
    bst = xgb.train(param, dtrain, num_round)
    # make prediction
    preds = bst.predict(dtest)
    print(preds)

def testGridSearch():
    pass

def testsklearn():
    from  xgboost import XGBClassifier
    dtrain = XGBClassifier(max_depth=20, learning_rate=0.1, n_estimators=100, silent=True, objective='binary:logistic', nthread=-1, gamma=0, min_child_weight=1, max_delta_step=0, subsample=1, colsample_bytree=1, colsample_bylevel=1, reg_alpha=0, reg_lambda=1, scale_pos_weight=1, base_score=0.5, seed=0, missing=None)

testTrain()
