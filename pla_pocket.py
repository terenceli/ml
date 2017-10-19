import random

def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split()
        featArr = [float(feat) for feat in lineArr[0:4]]
        tmp = [1.0]
        tmp.extend(featArr)
        dataMat.append(tmp)
        labelMat.append(int(lineArr[4]))
    return dataMat, labelMat

def sign(x, y):
    sum = 0.0
    for i in range(len(x)):
        sum += x[i] * y[i]
    if sum > 0.0:
        return 1
    else:
        return -1

def matraxPlus(x, y):
    return [x[i] + y[i] for i in range (len(x))]

def matrixMultipyConst(x, c):
    return [x[i] * c for i in range (len(x))]

def check(data, label, w):
    error = 0
    for i in range (len(data)):
        if (sign(data[i], w) != label[i]):
            error += 1
    return error

def pla(dataMat, labelMat):
    m = len(dataMat)
    n = len(dataMat[0]) - 1
    w = [0 for _ in range(n + 1)]
    allOk = False
    count = 0
    while allOk == False:
        allOk = True
        for i in range(m):
            print sign(w, dataMat[i])
            if sign(w, dataMat[i]) != labelMat[i]:
                w = matraxPlus(w, matrixMultipyConst(dataMat[i], labelMat[i]))
                count += 1
                allOk = False
                break
            
    print count
    print w
    return w

def getErrorCount(dataMat, labelMat, w):
    count = 0
    error = []
    for i in range (len(dataMat)):
        if (sign(dataMat[i], w) != labelMat[i]):
            count += 1
            error.append(i)
    return count


def pocket_pla(dataMat, labelMat):
    m = len(dataMat)
    n = len(dataMat[0]) - 1
    w = [ 0 for _ in range(n+1)]
    bestw = w
    count = 0
    bestError = getErrorCount(dataMat, labelMat, w)
    while count <= 100:
        choice = 0
        l = random.randint(0, m - 1)
        #print sign(dataMat[l], w)
        if(sign(dataMat[l], w) != int(labelMat[l])):
            count += 1
            w = matraxPlus(w, matrixMultipyConst(dataMat[l], labelMat[l]))
            currError = getErrorCount(dataMat, labelMat, w)
            if(currError < bestError):
                count += 1
                bestw = w
                bestError = currError
    return bestw,count

if __name__ == '__main__':
    data,label = loadDataSet("hw1_18_train.dat")
    tdata, tlabel = loadDataSet("hw1_18_test.dat")
    totalErrors = 0
    for i in range(100):
        w, count = pocket_pla(data, label)
        error = check(tdata, tlabel, w)
        totalErrors += error
    print float(totalErrors)/(100*len(tdata))





