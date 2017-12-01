import random as rd
import numpy as np
from preprocess import getdata

# distance mode: 1-manhattan, 2-euclidean, 3++
distmode = 2
# number of cluster
numcluster = 2
# number of data
numdata = 10
# number of attribute
numatt = 3
# weird mysterious variable
m = 2
# maximum iteration
maxiter = 100
# epsilon
eps = 0.2
# matrix U
mat = []
# old matrix U
oldmat = []
# data
x = []
# centroid
c = []


def minkowski(p, q, deg):
    i = 0
    sum = 0
    while i < len(p):
        sum = sum + pow(abs(p[i] - q[i]), deg)
        i = i + 1
    return sum ** (1. / deg)


def vectorScalarProduct(v, s):
    vec = []
    for x in v:
        vec.append(x * s)
    return vec


def vectorScalarDivision(v, s):
    vec = []
    for x in v:
        vec.append(x / s)
    return vec


def vectorVectorSum(v1, v2):
    vec = []
    for i in range(len(v1)):
        vec.append(v1[i] + v2[i])
    return vec


def createData():
    print 'createData'
    global x
    x = getdata().as_matrix()
    global numdata
    numdata = x.shape[0]
    global numatt
    numatt = x.shape[1]
    # initialize matrix U
    global mat
    mat = [[0 for ix in range(numcluster)] for y in range(numdata)]
    global oldmat
    oldmat = [[0 for ix in range(numcluster)] for y in range(numdata)]
    # initialize cluster centroid
    for it in range(numcluster):
        merged = []
        fi = x[rd.randint(0, numdata)][:numatt/3]
        se = x[rd.randint(0, numdata)][numatt/3:numatt/3*2]
        th = x[rd.randint(0, numdata)][numatt/3*2:]
        merged.extend(fi)
        merged.extend(se)
        merged.extend(th)
        c.append(merged)


def calculateU(i, j):
    power = 2 / (m - 1)
    sigma = 0
    k = 0
    while k < len(c):
        upper = minkowski(x[i], c[j], distmode)
        lower = minkowski(x[i], c[k], distmode)
        sigma = sigma + (upper / lower)
        k = k + 1
    return 1 / (pow(sigma, power))


def calculateC(j):
    print 'calculateC'
    # 3 dimension vector 'upper'
    upper = [0 for it in range(numatt)]
    lower = 0
    for i in range(numdata):
        s = pow(mat[i][j], m)
        v = vectorScalarProduct(x[i], s)
        upper = vectorVectorSum(upper, v)
        lower = lower + s
    return vectorScalarDivision(upper, lower)


def updateU():
    print 'updateU'
    for i in range(numdata):
        for j in range(numcluster):
            mat[i][j] = calculateU(i, j)


def updateC():
    print 'updateC'
    for j in range(numcluster):
        c[j] = calculateC(j)


def copyMat():
    print 'copyMat'
    for i in range(numdata):
        for j in range(numcluster):
            oldmat[i][j] = mat[i][j]


def findMaxDif():
    print 'findMaxDif'
    maxi = 0
    for i in range(numdata):
        for j in range(numcluster):
            dif = abs(oldmat[i][j] - mat[i][j])
            if dif > maxi:
                maxi = dif
    return maxi


createData()
updateU()
print np.matrix(mat)

it = 0
while (it < maxiter) and (findMaxDif() >= eps):
    it = it + 1
    print 'Epoch', it
    copyMat()
    updateC()
    updateU()
    print findMaxDif()

if it < maxiter:
    print 'Converged!'
print 'U Matrix'
print np.matrix(mat)

outc = open('out_centroid', 'w')
outm = open('out_matrix', 'w')

for centroid in c:
    for item in centroid[:-1]:
        outc.write(str(item))
        outc.write(', ')
    outc.write(str(centroid[-1:][0]))
    outc.write('\r\n')

outc.close()

for node in mat:
    for item in node[:-1]:
        outm.write(str(item))
        outm.write(', ')
    outm.write(str(node[-1:][0]))
    outm.write('\r\n')

outm.close()
