import numpy as np
from sklearn import neighbors
from sklearn.metrics import classification_report
from sklearn.cross_validation import  train_test_split
from sklearn import preprocessing

datas = np.loadtxt("datingTestSet2.txt")


x = np.array(datas[: , :-1])
x = preprocessing.scale(x)
y = np.array([int(i) for i in datas[:, -1]])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

clf = neighbors.KNeighborsClassifier(n_neighbors=3, algorithm='brute')
clf.fit(x_train, y_train)

answer = clf.predict(x_test)
print np.mean(answer == y_test)
