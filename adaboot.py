import numpy as np
import math

def choice(X, y, u):
    size = X.size
    sortedx = np.sort(X)
    thetas = []
    thetas.append(sortedx[0] - 1)
    for i in range(size - 2):
        thetas.append((sortedx[i] + sortedx[i+1]) / 2)
    err = 1
    for currtheta in thetas:
        currs = 1
        y_pre = np.sign(X-currtheta)
        currerr = np.sum((y != y_pre)*u) / size
        currerr2 = np.sum((y != (-1*y_pre))*u) / size
        if currerr2 < currerr:
            currerr = currerr2
            currs = -1
        if currerr < err:
            s = currs
            theta = currtheta
            err = currerr
    return s, theta, err


def decision_stump(X, y, u):
    m, n = X.shape
    err = 1
    for i in range(n):
        currs, currtheta, currerr = choice(X[:,i], y, u)
        if currerr < err:
            err = currerr
            s = currs
            theta = currtheta
            feature = i
    return s, theta, err, feature

def error(X, y, A_list, alpha_list):
    T = len(alpha_list)
    total = 0
    for i in range(T):
        A = A_list[i]
        alpha = alpha_list[i]
        y_pre = A[0] * np.sign(X[:, A[3]] - A[1])
        total += alpha * y_pre
    return np.sum(np.sign(total) != y) / float(len(y))

def adaboot(X, y, T):
    m, n = X.shape
    u = np.ones(m) / m
    alpha_list = []
    A_list = []

    for i in range(T):
        A = decision_stump(X, y, u)
        A_list.append(A)
        y_pre = A[0]*np.sign(X[:, A[3]] - A[1])
        et = A[2]*m/np.sum(u)
        delta = math.sqrt((1-et)/et)
        u = np.where(y!=y_pre, u * delta, u/delta)
        alpha = math.log(delta)
        alpha_list.append(alpha)
    return A_list, alpha_list


train_data = np.loadtxt("hw2_adaboost_train.dat")
trainX = train_data[:,:-1]
trainy = train_data[:,-1]
A_list, alpha_list = adaboot(trainX, trainy, 300)
print A_list, alpha_list
print error(trainX, trainy, A_list, alpha_list)


testdata = np.loadtxt("hw2_adaboost_test.dat")
testX = testdata[:,:-1]
testy = testdata[:,-1]
print error(testX, testy, A_list, alpha_list)




