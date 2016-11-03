import numpy as np
from sklearn.metrics import roc_auc_score
y_true = np.array([1,1,1,1,1,0,0,0,0,0])
y_scores = np.array([0.94,0.8,0.73,0.6,0.7,0.3,0.1,0.2,0.01,0.92])
print roc_auc_score(y_true, y_scores)
