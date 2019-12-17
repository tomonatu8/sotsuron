import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math

X4=[[0.3617775054260548, 1.164667388283024], [0.35887969854727864, 1.752040376145506], [-0.5918620193186293, -2.181619484627153], [-1.7267389745603623, 1.240948668964549], [-0.06679897566948512, 1.7574102530311722], [1.1751777198311162, -0.07564445497138728], [1.6102209310230737, -1.2026069315686105], [-1.117769967094835, 1.7302349204452971], [-0.24286021602332486, -1.8851616236339308], [0.014655304012714865, -1.9655004806588283], [1.8580815817165401, 0.4067409937058697], [-2.1002100179056136, -1.3614354561158883], [-0.1888278452487846, -1.7525237011127826], [-1.8622337692861701, -0.5194687426521671], [-1.1340327383197204, 0.7389069517638402], [-1.6540214360051095, 1.33557601133829], [-2.1296970053238837, 0.9632503146870386], [-0.02774346794413951, 1.6287193595987501]]
m=30
lis=[i for i in range(m)]
"""
lam_num_list=[]
for i in range(100):
    lam_num=sorted(random.sample(lis,len(X4)))
    if not lam_num in lam_num_list:
        lam_num_list.append(lam_num)
    if len(lam_num_list)==50:
        break
"""

#print(lam_num_list)

def K(x,y,lam):
    vec=0.0
    #print("sssssssssssss")
    for i in range(m):
        vec+= lam[i]/(1.0-lam[i]) * 1.0/np.pi * 1.0/math.factorial(i) * math.e**(-0.5 * (x[0]**2.0+x[1]**2.0)) * np.complex(x[0],x[1])**i * math.e**(- 0.5 * (y[0]**2.0+y[1]**2.0)) * np.complex(y[0],-y[1])**i
    #print("vec=",vec)
    return vec

def Phi(lam,phi):
    A=np.ones((len(phi),len(phi)),dtype=np.complex)
    for x1 in range(len(phi)):
        for x2 in range(len(phi)):
            #print(phi[x1])
            #print(lam)
            #print("dede")
            #print(K(phi[x1],phi[x2],lam))
            A[x1][x2]=K(phi[x1],phi[x2],lam)
    #print(A)
    #print(math.log(np.linalg.det(A).real))
    return np.linalg.det(A)

def log1(lam):
    vv=0
    for i in lis:
        vv+=math.log(1-lam[i])
    return vv

lamda=[0.0,0.2,0.4,0.6,0.8]

lamlist=[]
for i in range(500):
    lam=[]
    for i in range(m):
        lam.append(lamda[np.random.randint(0,len(lamda))])
    if not lam in lamlist:
        lamlist.append(lam)
print(lamlist)

#lamの組み合わせと、lam_numの組み合わせを決定した。全部の尤度を計算する。
flist=[]
for i in range(len(lamlist)):
    KK=Phi(lamlist[i],X4)
    print("det(K')=",KK)
    f=log1(lamlist[i])+math.log(KK.real)
    print("lamda=",lamlist[i])
    print("logf(phi)=",f)
    ff=math.e**f
    print("f(phi)=",ff)
    flist.append(f)

print(flist)
print(lamlist[flist.index(max(flist))])

#plt.figure(figsize=(10, 10), dpi=50)
#for i in range(len(lamlist)):
plt.plot(range(len(flist)),flist)
plt.show()
