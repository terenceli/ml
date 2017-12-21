from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import  train_test_split
from sklearn.metrics import mean_squared_error
from numpy import mat

def lrtest():
    datas = np.loadtxt("ex0.txt")
    x = datas[:, :-1]
    y = datas[:, -1]
    lr = linear_model.LinearRegression()

    # cross_val_predict returns an array of the same size as `y` where each entry
    # is a prediction obtained by cross validation:
    predicted = cross_val_predict(lr, x, y, cv=10)

    fig, ax = plt.subplots()
    ax.scatter(y, predicted, edgecolors=(0, 0, 0))
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()

def lwlr(testPoint, x, y, k = 1.0):
    x = mat(x)
    y = mat(y).T
    m = np.shape(x)[0]
    weights = np.mat(np.eye(m))
    for i in range(m):
        diffMat = testPoint - x[i, :]
        weights[i, i] = np.exp(diffMat * diffMat.T/(-2.0*k**2))
    xTx = x.T * (weights * x)
    if np.linalg.det(xTx) == 0.0:
        print ("cann't do inverse")
        return
    ws = xTx.I * (x.T * (weights * y))
    return testPoint * ws

def lwlrTest(k):
    datas = np.loadtxt("ex0.txt")
    x = datas[:, :-1]
    y = datas[:, -1]
    m = np.shape(x)[0]
    yHat = np.zeros(m)
    for i in range(m):
        yHat[i] = lwlr(x[i], x, y, k)
    strIndx = x[:,1].argsort(0)
    print (strIndx)
    xSort = x[strIndx][:,1]
    print (xSort)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort, yHat[strIndx])
    ax.scatter(mat(x[:,1]).flatten().A[0], mat(y).T.flatten().A[0],s=2,c="red")
    plt.show()



def abalonetest():
    datas = np.loadtxt("abalone.txt")
    x = datas[:, :-1]
    y = datas[:, -1]
    # print (type(x))
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
    # lr = linear_model.LinearRegression()
    #
    # lr.fit(x_train, y_train)
    # #y_pred = lr.predict(x_test)
    # y_pred = np.zeros(len(y_test))
    # for i in range(len(x_test)):
    #     y_pred = lwlr(x_test[i], x_train, y_train, 0.01)
    y_pred = np.zeros(len(x))
    for i in range(len(x)):
        y_pred = lwlr(x[i], x, y, 10)
    print (mean_squared_error(y_pred, y)*len(y))
    # print ("coef: ", lr.coef_)
    # print ("mean squared error: ", mean_squared_error(y_pred, y_test)*len(y_test))
    # print (lr.score(x_test, y_test))





if __name__ == "__main__":
    #lrtest()
    abalonetest()
    lwlrTest(0.01)