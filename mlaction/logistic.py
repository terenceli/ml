import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

def testSet():
    datas = np.loadtxt("testSet.txt")
    x = datas[:, :-1]
    y = datas[:,-1]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
    lr = LogisticRegression()
    lr.fit(x_train,y_train)
    ans = lr.predict(x_test)
    print (np.mean(ans != y_test))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x1 = []; y1 = []
    x2 = []; y2 =[]
    for i in range(len(x)):
        if y[i] == 0:
            x1.append(x[i][0])
            y1.append(x[i][1])
        else:
            x2.append(x[i][0])
            y2.append(x[i][1])

    ax.scatter(x1, y1, s=30, c='red', marker='s')
    ax.scatter(x2, y2, s=30, c='green')

    coef = lr.coef_
    coef = coef[0]
    intercept = lr.intercept_[0]
    print (intercept)
    print (coef)
    x = np.arange(-3, 3, 0.1)
    y = (-intercept-coef[0]*np.array(x))/coef[1]
    ax.plot(x, y)
    plt.show()


def testHorse():
    trains = np.loadtxt("horseColicTraining.txt")
    x_train = trains[:, :-1]
    y_train = trains[:, -1]
    tests = np.loadtxt("horseColicTest.txt")
    x_test = tests[:, :-1]
    y_test = tests[:, -1]

    lr = LogisticRegression(solver="sag")
    lr.fit(x_train, y_train)
    ans = lr.predict(x_test)
    print (np.mean(ans != y_test))

if __name__ == "__main__":
    testSet()
    testHorse()