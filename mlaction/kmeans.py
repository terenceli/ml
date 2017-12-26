import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def test(filename, k):
    datas = np.loadtxt(filename)

    kmeans = KMeans(n_clusters=k, random_state=0).fit(datas)

    center = kmeans.cluster_centers_
    print center
    f1 = plt.figure(1)
    plt.subplot(211)
    plt.scatter(datas[:,0],datas[:,1])
    plt.scatter(center[:,0],center[:,1],marker="+")
    plt.show()

def portland():
    datas = np.loadtxt("places.txt", delimiter ="\t", dtype=str)
    x = datas[:, -2:]
    print x
    kmeans = KMeans(n_clusters=9, random_state=0).fit(x)

    center = kmeans.cluster_centers_
    print center
    f1 = plt.figure(1)
    plt.subplot(211)
    plt.scatter(x[:,0],x[:,1])
    plt.scatter(center[:,0],center[:,1],marker="+")
    plt.show()

test("testSet.txt", 4)
test("testSet2.txt", 3)
portland()