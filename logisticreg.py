import random
import math
import numpy as np

def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split()
        featArr = [float(feat) for feat in lineArr[0:20]]
        #tmp = [1.0]
        #tmp.extend(featArr)
        dataMat.append(featArr)
        labelMat.append(int(lineArr[20]))
    return dataMat, labelMat

def sigmoid(x):
  return float(1.0) / (1 + math.exp(-x))

def sign(x, y):
    sum = 0.0
    for i in range(len(x)):
        sum += x[i] * y[i]
    if sum > 0.0:
        return 1
    else:
        return -1

def matrixMulty(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * y[i]
    return sum

def matraxPlus(x, y):
    return [x[i] + y[i] for i in range(len(x))]


def matrixMultipyConst(x, c):
    return [x[i] * c for i in range(len(x))]

def matrixDivide(x, c):
    return [x[i] / float(c) for i in range(len(x)) ]

def matrixMinus(x, y):
    return [x[i] - y[i] for i in range(len(x))]

def check(data, label, w):
    error = 0
    for i in range(len(data)):
        if (sign(data[i], w) != label[i]):
            error += 1
    return error


def logisticReg(dataMat, labelMat):
    m = len(dataMat)
    n = len(dataMat[0])
    w = [0 for _ in range(n)]
    count = 0

    gradient = [0 for _ in range(n)]
    while count <= 2000:
        for i in range (m):
            mmm = matrixMulty(w, dataMat[i])
            gradient = matraxPlus(matrixMultipyConst(dataMat[i], sigmoid(-labelMat[i]*mmm)*(-labelMat[i])), gradient)
        w = matrixMinus(w, matrixMultipyConst(gradient, 0.001 / float(m)))
        count += 1
        #w = matrixMinus(w,matrixMultipyConst(gradient, 0.001/float(m)))
        print count, w
    return w


if __name__ == '__main__':
    data, label = loadDataSet("hw3_train.dat")
    tdata, tlabel = loadDataSet("hw3_test.dat")
    totalErrors = 0

    w = logisticReg(data, label)
    print w
    error = check(data, label, w)
    totalErrors += error
    print float(totalErrors) / (len(tdata))
    totalErrors = 0
    error = check(tdata, tlabel, w)
    totalErrors += error
    print float(totalErrors) / ( len(tdata))





