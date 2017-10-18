import random 
def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open("train.dat")
    for line in fr.readlines():
        lineArr = line.strip().split()
        featArr = [float(feat) for feat in lineArr[0:4]]
        tmp = [1.0]
        tmp.extend(featArr)
        dataMat.append(tmp)
        labelMat.append(int(lineArr[4]))
    return dataMat, labelMat

def loadAllData():
    ret = []
    fr = open("train.dat")
    for line in fr.readlines():
        lineArr = line.strip().split()
        tmp = [float(feat) for feat in lineArr]
        tmp.insert(0,1.0)
        ret.append(tmp)
    return  ret 
  

def sign(x, y):
    sum = 0.0
    for i in range(len(x)):
        sum += x[i] * y[i]
    if (sum < 0):
        return -1
    else:
        return 1

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
    print m, n
    w = [0 for _ in range(n + 1)]
    allOk = False
    count = 0
    while allOk == False:
        allOk = True
        for i in range(m):
            if sign(w, dataMat[i]) != labelMat[i]:
                w = matraxPlus(w, matrixMultipyConst(dataMat[i], float(labelMat[i])))
                count += 1
                allOk = False
                break
            
    print count 
    return w, count 

if __name__ == '__main__':
    datas = loadAllData()
    print datas 
    sumCount = 0
    for i in range(2000):
        random.shuffle(datas)
        data = []
        label = []
        for l in range(len(datas)):
            m = datas[l][:5]
            n = datas[l][5]
            data.append(m)
            label.append(n)
        w, count  = pla(data, label)
        print w 
        sumCount += count 
    #sumCount += count 
    print sumCount / 2000


