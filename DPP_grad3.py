import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math
import csv
import pprint

X6=[[1.786525446443986, 2.9571325416425904],[1.2174661714935322, 2.286560039668559], [2.0647448477879684, 2.574106072554886], [0.4383059844205601, 0.021703779300330447], [2.340398889135444, 0.5493984443013916], [0.5234037182163223, 0.03607478607012122], [1.8642790714687176, 0.7640355893859928], [2.8873092788474923, 1.1055509317904708], [1.6683566170591557, 3.038537692691724], [0.8958897272808974, 3.0466985130765902]]

lam0=[0.3]
for i in range(4):
    lam0.append(0.2)
for i in range(5):
    lam0.append(0.2)
for i in range(5):
    lam0.append(0.9)
for i in range(5):
    lam0.append(0.8)

lam0=[]
for i in range(10):
    lam0.append(0.5)
for i in range(10):
    lam0.append(0.5)

lam0= [0.17397395,0.50131619, 0.19159321, 0.29777511 ,0.16042299 ,0.52558708,
 0.43399619, 0.40356739, 0.62043384 ,0.5407287 , 0.30299614 ,0.40185023,
 0.83365997, 0.8214737,  0.74879525,0.93045914, 0.56966527 ,0.8694791,
 0.99642495, 0.75297378]

m=len(lam0)
print(sum(lam0))

n=len(X6)
print(n)
s=-(m-1)/(n*(1-lam0[0]))-(lam0[0]-n)/(n*(1-lam0[0])*lam0[0])

print("s=",s)

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

def v(X,i):
    vec=[]
    #print("sssssssssssss")
    for x in X:
        vec.append(2/np.pi  * math.sin((i+1)*x[0])*math.sin((i+1)*x[1]))
    #print("vec=",vec)
    return vec


print("innner",np.dot(v(X6,7),v(X6,7)))

lam=lam0
Kinv=np.linalg.inv(Phi(lam,X6))
Kmat=[]
for i in range(m):
    Kmat.append(dPhi(lam,X6,i))
Kmat=np.array(Kmat)

dlogf=[]
for i in range(m):
    dlogf.append(-1/(1-lam[i]) + np.trace(np.dot(Kinv,Kmat[i])))

print(dlogf)
print(max(np.abs(dlogf)))

def ddK(x,y,lam,i):
    vec= 1/((1.0-lam[i])*lam[i]) * 4/(np.pi)**2 * math.sin((i+1)*x[0])*math.sin((i+1)*x[1])  * math.sin((i+1)*y[0])*math.sin((i+1)*y[1])
    #print("vec=",vec)
    return vec

def ddPhi(lam,phi,i):
    A=np.ones((len(phi),len(phi)))
    for x1 in range(len(phi)):
        for x2 in range(len(phi)):
            A[x1][x2]=ddK(phi[x1],phi[x2],lam,i)
    #print(A)
    #print(math.log(np.linalg.det(A).real))
    return A



def nK(x,y,lam,i):
    vec=  4/(np.pi)**2 * math.sin((i+1)*x[0])*math.sin((i+1)*x[1])  * math.sin((i+1)*y[0])*math.sin((i+1)*y[1])
    #print("vec=",vec)
    return vec

def nPhi(lam,phi,i):
    A=np.ones((len(phi),len(phi)))
    for x1 in range(len(phi)):
        for x2 in range(len(phi)):
            A[x1][x2]=nK(phi[x1],phi[x2],lam,i)
    #print(A)
    #print(math.log(np.linalg.det(A).real))
    return A

print(nPhi(lam,X6,1))
print(nPhi(lam,X6,2))
A=np.ones((len(X6),len(X6)))
for i in range(m):
    A+=lam[i]/(1-lam[i]) * nPhi(lam,X6,i)
B=n/(1-lam[i])*nPhi(lam,X6,0)
print(np.dot(np.linalg.inv(nPhi(lam,X6,1)),nPhi(lam,X6,2)))
print("A=",A)
print("B=",B)
