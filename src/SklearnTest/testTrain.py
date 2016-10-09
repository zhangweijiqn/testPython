import numpy as np

from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score
np.random.seed(0)

# Generate data
X, y = make_blobs(n_samples=1000, n_features=20, centers=3, random_state=42, cluster_std=5.0)
X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:800], y[600:800]
X_train_valid, y_train_valid = X[:800], y[:800]
X_test, y_test = X[800:], y[800:]

# Train uncalibrated random forest classifier on whole train and validation
# data and evaluate on test data
clf = RandomForestClassifier(n_estimators=25)       #n_estimators：The number of trees in the forest.
clf.fit(X_train_valid, y_train_valid)
clf_label = clf.predict(X_test)
accuracy = accuracy_score(y_test, clf_label)
# clf_probs = clf.predict_proba(X_test)
# score = log_loss(y_test, clf_probs)

print accuracy
