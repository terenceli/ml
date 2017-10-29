import numpy as np
import matplotlib.pyplot as plt


def ridge_regression(X, y, lam):
    m, n = X.shape
    return np.linalg.inv((X.T.dot(X) + lam * np.eye(n))).dot(X.T).dot(y)

def load_data(filename):
    data = np.loadtxt(filename)
    m, n = data.shape
    x = np.hstack((np.ones((m,1)), data[:,:-1]))
    y = data[:, -1:]
    return x, y

def error(X, y, w):
    y_predict = np.sign(X.dot(w))
    return np.sum(y!=y_predict) / float(y.size)

if __name__ == "__main__":
    train_X, train_y = load_data("hw4_train.dat")
    test_X, test_y = load_data("hw4_test.dat")
    w = ridge_regression(train_X, train_y, 11.26)
    print w
    print error(train_X, train_y, w)
    print error(test_X, test_y, w)