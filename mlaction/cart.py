import numpy as np
from sklearn import tree
from sklearn.cross_validation import  train_test_split
from sklearn import preprocessing


datas = np.loadtxt("ex00.txt")

x = np.array(datas[:, :-1])
y = np.array(datas[:, -1])

clf = tree.DecisionTreeRegressor(max_depth=1)

#clf.fit(x_train,y_train)
clf.fit(x,y)


with open("ex00.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)


