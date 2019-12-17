import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math
import csv
import pprint


X6=[[1.786525446443986, 2.9571325416425904],[1.2174661714935322, 2.286560039668559], [2.0647448477879684, 2.574106072554886], [0.4383059844205601, 0.021703779300330447], [2.340398889135444, 0.5493984443013916], [0.5234037182163223, 0.03607478607012122], [1.8642790714687176, 0.7640355893859928], [2.8873092788474923, 1.1055509317904708], [1.6683566170591557, 3.038537692691724], [0.8958897272808974, 3.0466985130765902]]
lam0=[]
for i in range(5):
    lam0.append(0.7)
for i in range(5):
    lam0.append(0.7)
for i in range(5):
    lam0.append(0.7)
for i in range(5):
    lam0.append(0.7)
lam0=np.array(lam0)
m=len(lam0)

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
            #print(phi[x1])
            #print(lam)
            #print("dede")
            #print(K(phi[x1],phi[x2],lam))
            A[x1][x2]=K(phi[x1],phi[x2],lam)
    #print(A)
    #print(math.log(np.linalg.det(A).real))
    return A

def dK(x,y,lam,i):
    vec= 1/(1.0-lam[i])**2 * 4/(np.pi)**2 * math.sin((i+1)*x[0])*math.sin((i+1)*x[1])  * math.sin((i+1)*y[0])*math.sin((i+1)*y[1])
    #print("vec=",vec)
    return vec

def dPhi(lam,phi,i):
    A=np.ones((len(phi),len(phi)))
    for x1 in range(len(phi)):
        for x2 in range(len(phi)):
            A[x1][x2]=dK(phi[x1],phi[x2],lam,i)
    #print(A)
    #print(math.log(np.linalg.det(A).real))
    return A

def K1(x,y,lam):
    vec=0.0
    #print("sssssssssssss")
    for i in range(m):
        vec+= lam[i]/(1.0-lam[i]) * 4/(np.pi)**2  * math.sin((i+1)*x[0])*math.sin((i+1)*x[1])  * math.sin((i+1)*y[0])*math.sin((i+1)*y[1])
    #print("vec=",vec)
    return vec

def Phi1(lam,phi):
    A=np.ones((len(phi),len(phi)))
    for x1 in range(len(phi)):
        for x2 in range(len(phi)):
            #print(phix1)
            #print(lam)
            #print("dede")
            #print(K(phix1,phix2,lam))
            A[x1][x2]=K1(phi[x1],phi[x2],lam)
    #print(A)
    #print(math.log(np.linalg.det(A).real))
    return np.linalg.det(A)

lis=[i for i in range(m)]

def log1(lam):
    vv=0
    for i in lis:
        vv+=math.log(1-lam[i])
    return vv

dlam=1000
alpha=0.01
ffflist=[]
sumlist=[]

lam=lam0
dlam=100*np.array(lam0)
for count in range(1000):
    print("count=",count)
    #if max(lam)>1:
    #    break
    if max(np.abs(np.array(dlam)))<0.0005:
        break
    Kinv=np.linalg.inv(Phi(lam,X6))
    Kmat=[]
    for i in range(m):
        Kmat.append(dPhi(lam,X6,i))
    Kmat=np.array(Kmat)
    dlogf=[]
    for i in range(m):
        dlogf.append(-1/(1-lam[i]) + np.trace(np.dot(Kinv,Kmat[i])))
    print("newlam=",lam+dlam)
    print("dlam=",dlam)
    dlam=alpha*np.array(dlogf)
    #if min(lam+dlam)<0:
    #    break
    print("newlam=",lam+dlam)
    print("dlam=",dlam)
    #if max(lam+dlam)>1:
    #    break
    #else:
    lam=lam+dlam
    sumlist.append(sum(lam))
    if max(np.abs(np.array(dlam)))<0.0005:
        break
    print("dlam=",dlam)
    print("lam=",lam)
    #if min(lam+dlam)<0:
    #    break
    #if max(lam+dlam)>1:
    #    break
    if max(np.abs(np.array(dlam)))<0.0005:
        break
    KKK=Phi1(lam,X6)
    #print("logdet(K')=",math.log(KKK))
    fff=log1(lam)+math.log(KKK)
    #print("log1(Xreal)=",log1(Xreal))
    #print("lamda=",Xreal)
    #print("logf(phi)=",fff)
    ffflist.append(fff)

print("lam0=",lam0)
print("lam=",lam)
print("logf(phi)=",fff)
print("sum_lam=",sum(lam))


plt.plot(range(len(ffflist)),ffflist)
plt.xlabel("trial")
plt.ylabel("logf(φ)")
plt.show()

plt.plot(range(len(sumlist)),sumlist)
plt.xlabel("trial")
plt.ylabel("sum(lam)")
plt.show()
