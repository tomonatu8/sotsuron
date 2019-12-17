import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math
import csv
import pprint

Xlist= [[0.7318329592654084, 3.126842756110727], [0.8633945765886946, 0.46616121167724045], [3.0426692020989443, 3.0255750626999776], [1.5922461993059676, 1.4865844710013558], [1.9385656247966256, 2.659621544392795], [3.070134378902318, 1.825531870206595], [0.9573359674088086, 2.807678900328862], [2.9226940805314476, 2.7159442113061028], [2.954376630672791, 0.5586682949404801], [3.1062653168813625, 2.5732009892381704], [1.652673632229772, 0.5104478183470778], [0.20935092756121204, 1.6862248136153442], [0.12985461348891555, 0.8186185108522548]]

m=40
L=[]
for LL in range(10):
    L.append(0.1)
for LL in range(10):
    L.append(0.7)
for LL in range(20):
    L.append(0.3)

filename='test.csv'
lam=[]
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        lam.append(row[1])

lam = lam[1:]
print(lam)
lam2=[]
for l in lam:
    lam2.append(float(l))
print(lam2)
print(sum(lam2))

lis=[i for i in range(m)]

def K(x,y,lam):
    vec=0.0
    #print("sssssssssssss")
    for i in range(m):
        vec+= lam[i]/(1.0-lam[i]) * 4/(np.pi)**2  * math.sin((i+1)*x[0])*math.sin((i+1)*x[1])  * math.sin((i+1)*y[0])*math.sin((i+1)*y[1])
    #print("vec=",vec)
    return vec

def Phi(lam,phi):
    A=np.ones((len(phi),len(phi)))
    for x1 in range(len(phi)):
        for x2 in range(len(phi)):
            A[x1][x2]=K(phi[x1],phi[x2],lam)
    #print(A)
    #print(math.log(np.linalg.det(A).real))
    return np.linalg.det(A)

def log1(lam):
    vv=0
    for i in lis:
        vv+=math.log(1-lam[i])
    return vv

def K0(x,y,lam):
    vec=0.0
    #print("sssssssssssss")
    for i in range(m):
        vec+= lam[i] * 4/(np.pi)**2  * math.sin((i+1)*x[0])*math.sin((i+1)*x[1])  * math.sin((i+1)*y[0])*math.sin((i+1)*y[1])
    #print("vec=",vec)
    return vec

def Phi0(lam,phi):
    A=np.ones((len(phi),len(phi)))
    for x1 in range(len(phi)):
        for x2 in range(len(phi)):
            A[x1][x2]=K0(phi[x1],phi[x2],lam)
    #print(A)
    #print(math.log(np.linalg.det(A).real))
    return np.linalg.det(A)

Xreal=L
print(Xreal)
print(len(Xreal))

print("--------------")
print("-----Xreal------")
KKK=Phi(Xreal,Xlist)
print("logdet(K')=",math.log(KKK))
fff=log1(Xreal)+math.log(KKK)
print("log1(Xreal)=",log1(Xreal))
print("lamda=",Xreal)
print("sum(lamda)=",sum(Xreal))
print("logf(phi)=",fff)
efff=math.e**fff
print("f(phi)=",efff)
print("--------------")

X=[]
for l in lam2:
    X.append(l*14)

Xreal2=[]
for l in Xreal:
    Xreal2.append(l/14)
lam2[-1]=0.0
KKK=Phi0(Xreal2,Xlist)
print("logdet0(K')=",math.log(KKK))
KKK=Phi0(lam2,Xlist)
print("logdet0(K')=",math.log(KKK))

print("--------------")
print("-----hat(X)------")
KKK=Phi(X,Xlist)
print("logdet(K')=",math.log(KKK))
fff=log1(X)+math.log(KKK)
print("log1(X)=",log1(X))
print("lamda=",X)
print("sum(lamda)=",sum(X))
print("logf(phi)=",fff)
efff=math.e**fff
print("f(phi)=",efff)
print("--------------")
print(max(X))

lam3=[]
for x in X:
    if x < 0.001:
        lam3.append(0)
    else:
        lam3.append(x)
print(lam3)
plt.plot(Xreal)
plt.plot(lam3)

plt.show()

s=0
for i in range(len(X)):
    s+=(X[i]-Xreal[i])**2

print(s)
