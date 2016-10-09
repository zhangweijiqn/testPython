#coding=utf8
__author__ = 'zhangwj'
import numpy as np

# reference: http://lib.csdn.net/article/machinelearning/34918
# Ordinary Least Squares : 16 methods

def testLinearRegression1():
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    X = np.array([[0, 0, 1, 2], [1, 1, 2, 3], [2, 2, 3, 4]])
    Y = np.array([0, 1, 2])
    reg.fit(X, Y)
    print reg.coef_


def testLinearRegression2():
    #　普通的普通最小二乘法 |y^-y|2
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn import datasets, linear_model

    # Load the diabetes dataset
    diabetes = datasets.load_diabetes()
    print diabetes.data.shape

    # Use only one feature
    diabetes_X = diabetes.data[:, np.newaxis, 2]

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
          % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

    # Plot outputs
    plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
    plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
             linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()

def testRidgeRegression():
    #岭回归 目标函数加入了对ｗ的惩罚
    print(__doc__)

    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import linear_model
    #构造一个hilbert矩阵10*10
    X = 1. / (np.arange(1,11) + np.arange(0,10)[:,np.newaxis])
    y = np.ones(10) #10个1

    n_alphas = 200
    alphas = np.logspace(-10,-2,n_alphas) #等比数列，200个，作为岭回归的系数
    clf = linear_model.Ridge(fit_intercept=False)
    coefs = []
    for a in alphas:
        clf.set_params(alpha=a)
        clf.fit(X,y)
        coefs.append(clf.coef_) #得到200个不同系数所训练出常数参数值

    ax = plt.gca()
    ax.set_color_cycle(['b', 'r', 'g', 'c', 'k', 'y', 'm'])
    ax.plot(alphas,coefs)
    ax.set_xscale('log') #转为极坐标系
    ax.set_xlim(ax.get_xlim()[::-1]) #反转x轴
    plt.xlabel('alpha')
    plt.ylabel('weight')
    plt.title('Ridge coefficients as a function of the regularization')
    plt.axis('tight')
    plt.show()

def testLasso():
    #　目标函数加入了对ｗ和样本个数的惩罚
    # 基于稀疏模型的情况，进行线性拟合，这时的效果较好
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.metrics import r2_score
    #我们先手动生成一些稀疏数据
    print np.random.seed(42)
    n_samples, n_features = 50, 200
    X = np.random.randn(n_samples, n_features)
    coef = 3 * np.random.randn(n_features) #这个就是实际的参数
    inds = np.arange(n_features)
    np.random.shuffle(inds) #打乱
    coef[inds[10:]] = 0 #生成稀疏数据
    y = np.dot(X, coef) #参数与本地点乘
    #来点噪音
    y += 0.01 * np.random.normal((n_samples,))

    X_train, y_train = X[:n_samples/2], y[:n_samples/2]
    X_test, y_test = X[n_samples/2:], y[n_samples/2:]

    from sklearn.linear_model import Lasso
    alpha = 0.1
    lasso = Lasso(alpha=alpha)

    y_pred_lasso = lasso.fit(X_train,y_train).predict(X_test)
    r2_score_lasso = r2_score(y_test, y_pred_lasso) #这里是0.38
    print lasso
    print "r2_score's result is %f" % r2_score_lasso

    from sklearn.linear_model import ElasticNet
    enet = ElasticNet(alpha=alpha, l1_ratio=0.7)
    y_pred_enet = enet.fit(X_train,y_train).predict(X_test)
    r2_score_enet = r2_score(y_test, y_pred_enet) #0.24 没有lasso好
    print enet
    print "nent's result is %f" % r2_score_enet

    plt.plot(enet.coef_, label='Elastic net coefficients')
    plt.plot(lasso.coef_, label='Lasso coefficients')
    plt.plot(coef, '--', label='original coefficients')
    plt.legend(loc="best")
    plt.title("Lasso R^2: %f, Elastic Net R^2: %f"
              % (r2_score_lasso, r2_score_enet))
    plt.show()

def testMulti_taskLasso():
    # 多元lasso，一元的lasso是根据y=X*x（y是结果，X是矩阵，x是方程系数）来倒推x,多任务lasso中的y从一维度变成二维度。
    import numpy as np
    from sklearn.linear_model import MultiTaskLasso, Lasso
    rng = np.random.RandomState(42)
    # Generate some 2D coefficients with sine waves with random frequency and phase
    n_samples, n_features, n_tasks = 100, 30, 40
    n_relevant_features = 5
    coef = np.zeros((n_tasks, n_features))
    times = np.linspace(0, 2 * np.pi, n_tasks)
    for k in range(n_relevant_features):
        coef[:, k] = np.sin((1. + rng.randn(1)) * times + 3 * rng.randn(1))

    X = rng.randn(n_samples, n_features)
    Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)

    coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
    coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.).fit(X, Y).coef_

def testElasticNet():
    #弹性网络,对ｗ同时进行L1和L2规范化，并对样本数惩罚
    pass

def testMulti_taskElasticNet():
    pass

def testLeastAngleRegression():
    #最小角回归,针对高维数据开发的
    pass

def testLARSLasso():
    #最小角回归Lasso,最小角回归方法运用到lasso上
    pass

def testOrthogonalMatchingPursuit():
    #正交匹配追踪
    pass

def testBayesianRegression():
    #贝叶斯回归
    pass

def testBayesianRidgeRegression():
    #贝叶斯岭回归
    pass

def testLogistisRegression():
    #逻辑回归
    pass

# testLinearRegression2()
testRidgeRegression()
