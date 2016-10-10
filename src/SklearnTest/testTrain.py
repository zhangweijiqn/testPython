# coding=utf8
import numpy as np

from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score

np.random.seed(0)


def getData():
    # Generate data
    X, y = make_blobs(n_samples=1000, n_features=20, centers=3, random_state=42, cluster_std=5.0)
    X_train, y_train = X[:600], y[:600]
    X_valid, y_valid = X[600:800], y[600:800]
    X_train_valid, y_train_valid = X[:800], y[:800]
    X_test, y_test = X[800:], y[800:]
    return X_train_valid, y_train_valid, X_test, y_test


def testRF():
    # http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier
    # Train uncalibrated random forest classifier on whole train and validation
    # data and evaluate on test data
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=10,   #number of trees
                                 criterion="entropy",  # gini or entropy
                                 max_depth=None,
                                 min_samples_split=2,
                                 min_samples_leaf=1,
                                 min_weight_fraction_leaf=0.,
                                 max_features="auto",
                                 max_leaf_nodes=None,
                                 min_impurity_split=1e-7,
                                 bootstrap=True,
                                 oob_score=False,
                                 n_jobs=1,
                                 random_state=None,
                                 verbose=0,
                                 warm_start=False,
                                 class_weight=None)  # n_estimators：The number of trees in the forest.
    return clf


def testSVC():
    # http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC
    # The implementation is based on libsvm
    from sklearn import svm
    clf = svm.SVC(C=1.0,
                  kernel='sigmoid', #It must be one of 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' or a callable.
                  degree=3,
                  gamma='auto',
                  coef0=0.0,
                  shrinking=True,
                  probability=False,
                  tol=1e-3,
                  cache_size=200,
                  class_weight=None,
                  verbose=False,
                  max_iter=-1,
                  decision_function_shape=None,# Whether to return a one-vs-rest (‘ovr’) decision function of shape (n_samples, n_classes) as all other classifiers,
                    # or the original one-vs-one (‘ovo’) decision function of libsvm which has shape (n_samples, n_classes * (n_classes - 1) / 2).
    random_state=None)
    # get support vectors
    clf.support_vectors_
    # get indices of support vectors
    clf.support_
    # get number of support vectors for each class
    clf.n_support_
    return clf

def testNuSVC():
    # http://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC
    # Similar to SVC but uses a parameter to control the number of support vectors.Also the implementation is based on libsvm
    from sklearn.svm import NuSVC
    clf = NuSVC(nu=0.5,#An upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1].
                kernel='sigmoid',
                degree=3,
                gamma='auto',
                coef0=0.0,
                shrinking=True,
                probability=False,
                tol=0.001,
                cache_size=200,
                class_weight=None,
                verbose=False,
                max_iter=-1,
                decision_function_shape=None,
                random_state=None)
    return clf

def testLinearSVC():
    # http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC
    #Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.
    from sklearn.svm import LinearSVC
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
    return clf

if __name__ == '__main__':
    X_train, Y_train, X_test, Y_test = getData()
    # clf = testRF()
    # clf = testSVC()
    # clf = testNuSVC()
    clf = testLinearSVC()
    clf.fit(X_train, Y_train)
    clf_label = clf.predict(X_test)
    accuracy = accuracy_score(Y_test, clf_label)
    # clf_probs = clf.predict_proba(X_test)
    # score = log_loss(y_test, clf_probs)
    print accuracy
