import numpy as np
from sklearn.ensemble import AdaBoostClassifier

def testHorse():
    trains = np.loadtxt("horseColicTraining2.txt")
    x_train = trains[:, :-1]
    y_train = trains[:, -1]
    tests = np.loadtxt("horseColicTest2.txt")
    x_test = tests[:, :-1]
    y_test = tests[:, -1]

    lr = AdaBoostClassifier()
    lr.fit(x_train, y_train)
    ans = lr.predict(x_test)
    print (np.mean(ans != y_test))

if __name__ == "__main__":
    testHorse()