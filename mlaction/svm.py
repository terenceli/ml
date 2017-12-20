import numpy as np
from sklearn.cross_validation import  train_test_split
from sklearn import preprocessing
from sklearn.svm import SVC, LinearSVC

import os

def image2vector(filename):
    ret = np.zeros((1,1024))
    f = open(filename)
    count = 0
    for line in f.readlines():
        for bi in line.rstrip():
            ret[0, count] = int(bi)
            count += 1
    return ret

def file2matrix(filename):
    numEntry = os.listdir(filename)
    m = len(numEntry)
    x = np.zeros((m, 1024))
    y = []
    for i in range(m):
        label = int(numEntry[i].split("_")[0])
        y.append(label)
        x[i, :] = image2vector(filename + "/" + numEntry[i])
    return x, y



if __name__ == "__main__":
    x_train, y_train = file2matrix("trainingDigits")
    x_test, y_test = file2matrix("testDigits")
    clf = SVC()
    clf.fit(x_train, y_train)
    answer = clf.predict(x_test)
    print(np.mean(answer != y_test))
    for i in range(len(answer)):
        if answer[i] != y_test[i]:
            print ("predict: ", answer[i], " ,real: ", y_test[i])
