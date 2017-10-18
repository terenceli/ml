def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open("hw1_15_train.dat")
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
    return 1 if sum > 0 else -1

def matraxPlus(x, y):
    return [x[i] + y[i] for i in range (len(x))]

def matrixMultipyConst(x, c):
    return [x[i] * c for i in range (len(x))]

def check(data, label, w):
    for i in range (len(data)):
        if (sign(data[i], w) != label[i]):
            print "Something wrong"
    print "Every sample is ok"

def pla(dataMat, labelMat):
    m = len(dataMat)
    n = len(dataMat[0]) - 1
    w = [0 for _ in range(n + 1)]
    allOk = False
    count = 0
    while allOk == False:
        allOk = True
        for i in range(m):
            if sign(w, dataMat[i]) != labelMat[i]:
                w = matraxPlus(w, matrixMultipyConst(dataMat[i], labelMat[i]))
                count += 1
                allOk = False
                break
            
    print count 
    print w
    return w

if __name__ == '__main__':
    data,label = loadDataSet()
    w = pla(data, label)
    check(data, label, w)





