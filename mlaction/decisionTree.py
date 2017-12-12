import numpy as np
from sklearn import tree
from sklearn.cross_validation import  train_test_split
from sklearn import preprocessing
import graphviz

datas = np.loadtxt("lenses.txt", delimiter="\t", dtype=str)

x = np.array(datas[: , :-1])
y = np.array(datas[:, -1])

m = len(x[0])
for i in range(m):
    le = preprocessing.LabelEncoder()
    #print x[:,i]
    le.fit(x[:,i])
    x[:,i] = le.transform(x[:,i])
    #print x[:,i]

le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)



print x
print y
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
clf = tree.DecisionTreeClassifier(criterion="entropy")

#clf.fit(x_train,y_train)
clf.fit(x,y)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("lenses")

answer = clf.predict(x_test)
print np.mean(answer == y_test)
