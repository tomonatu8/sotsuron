import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math

#kernelを計算する。

rootpi=1/np.sqrt(np.pi)

L=[]
for LL in range(30):
    L.append(0.7)
#12
B=[]
B_num=[]
for i in range(len(L)):
    bb=np.random.binomial(1, L[i], size=1)[0]
    B.append(bb)
    if bb==1:
        B_num.append(i)

n=sum(B)

print(n)
print(B_num)

#これ正定値じゃない説

def K(x,y):
    vec=0
    for i in B_num:
        vec+= 1/np.pi * 1/math.factorial(i) * math.e**(-1/2 * (x**2+y**2)) *  complex(x,y)**i
    return vec

#phiは得られた点配置



#papangelou intensityを計算する。
def c(x,phi):
    A=np.ones((len(phi),len(phi)),dtype=np.complex)
    for x1 in range(len(phi)):
        for x2 in range(len(phi)):
            print(phi[x1])
            A[x1][x2]=K(phi[x1],phi[x2])
    print("A=",A)
    inv_A=np.linalg.inv(A)
    print("inv_A=",inv_A)
    b=np.ones(len(phi),dtype=np.complex)
    for x3 in range(len(phi)):
        b[x3]=K(x,phi[x3])
    print(A)
    print(b)
    cc=np.linalg.solve(A,b)
    print(cc)
    D=np.dot(cc,np.dot(A,cc))
    print("cc^TAcc=",D)
    print("K(x,x)=",K(x,x))
    return K(x,x)- D

print(c(0.49,[0.5,0.1,0.4]))
