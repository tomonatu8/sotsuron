import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math
import csv
import pprint


X6=[[0.3792867335276325, 1.950488939292105], [0.12836889952507655, 0.20422533212852556], [0.489839037603313, 1.0273893483232186], [2.335239047338269, 2.511976341084248], [1.3055910883453483, 2.637418599488819], [2.9759270608282127, 0.07360707763577042], [1.330170795446663, 1.0778910731277673], [1.2100331530385762, 0.6106031429272996], [0.5709854814314912, 2.6092288209158254], [1.1097074958185458, 2.011440897921088], [1.9132724540760757, 1.203330056366217], [0.6482589481773727, 2.8543958151486577], [2.825262683728557, 0.8930673855843748], [2.075748714827975, 2.839466302721716], [2.6076559478388375, 2.1927193749081915], [1.464884193220323, 1.5249772140336393], [0.9052726934361649, 1.9970141000243289], [0.5617283790619311, 1.1748829956169933], [2.9802233404979397, 1.2824176965655991], [2.998508951911826, 2.1119687394629825], [2.8250395472042946, 2.982804664611138], [0.2806847789120289, 2.431655871357795], [1.7245952111918592, 2.3166104208351617], [0.16081087645167588, 0.14508724965147393], [0.5160095277486658, 1.3812410548991672], [1.4742473505336864, 2.051746673773112], [2.5543864162375267, 2.304326182639277], [1.323556787893661, 1.1926374540175682], [2.0793921344001975, 0.8567381201411894]]

lam0=[]
for i in range(10):
    lam0.append(0.8)
for i in range(10):
    lam0.append(0.3)
for i in range(20):
    lam0.append(0.3)
lam0=np.array(lam0)
m=40

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
    if max(lam)>1:
        break
    if max(np.abs(np.array(dlam)))<0.005:
        break
    Kinv=np.linalg.inv(Phi(lam,X6))
    Kmat=[]
    for i in range(40):
        Kmat.append(dPhi(lam,X6,i))
    Kmat=np.array(Kmat)
    dlogf=[]
    for i in range(40):
        dlogf.append(-1/(1-lam[i]) + np.trace(np.dot(Kinv,Kmat[i])))
    dlam=alpha*np.array(dlogf)
    if max(lam+dlam)>1:
        break
    else:
        lam=lam+dlam
    sumlist.append(sum(lam))
    if max(np.abs(np.array(dlam)))<0.005:
        break
    print("dlam=",dlam)
    print("lam=",lam)
    if max(lam+dlam)>1:
        break
    if max(np.abs(np.array(dlam)))<0.005:
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
#plt.hlines([8.5],1,len(ffflist)-1,"green",label="true value")
#plt.hlines([8.99],1,len(ffflist)-1,"red",label="estimated value")
plt.xlabel("trial")
plt.ylabel("logf(φ)")
plt.show()

plt.plot(range(len(sumlist)),sumlist)
plt.xlabel("trial")
plt.ylabel("sum(lam)")
plt.show()
