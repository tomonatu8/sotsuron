import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math
import sympy


X6=[[0.3792867335276325, 1.950488939292105], [0.12836889952507655, 0.20422533212852556], [0.489839037603313, 1.0273893483232186], [2.335239047338269, 2.511976341084248], [1.3055910883453483, 2.637418599488819], [2.9759270608282127, 0.07360707763577042], [1.330170795446663, 1.0778910731277673], [1.2100331530385762, 0.6106031429272996], [0.5709854814314912, 2.6092288209158254], [1.1097074958185458, 2.011440897921088], [1.9132724540760757, 1.203330056366217], [0.6482589481773727, 2.8543958151486577], [2.825262683728557, 0.8930673855843748], [2.075748714827975, 2.839466302721716], [2.6076559478388375, 2.1927193749081915], [1.464884193220323, 1.5249772140336393], [0.9052726934361649, 1.9970141000243289], [0.5617283790619311, 1.1748829956169933], [2.9802233404979397, 1.2824176965655991], [2.998508951911826, 2.1119687394629825], [2.8250395472042946, 2.982804664611138], [0.2806847789120289, 2.431655871357795], [1.7245952111918592, 2.3166104208351617], [0.16081087645167588, 0.14508724965147393], [0.5160095277486658, 1.3812410548991672], [1.4742473505336864, 2.051746673773112], [2.5543864162375267, 2.304326182639277], [1.323556787893661, 1.1926374540175682], [2.0793921344001975, 0.8567381201411894]]

m=40
n=2
#nは次元
rootpi=1/np.sqrt(np.pi)

def v(i):
    vec=[]
    #print("sssssssssssss")
    for X in X6:
        vec.append( 2/np.pi  * math.sin((i+1)*X[0])*math.sin((i+1)*X[1]))
    #print("vec=",vec)
    return vec

def F(X,phi1):
    sum=0
    for t in phi1:
        for i in range(n):
            sum+=1/(X[i]-X6[t][i])
    return sum

def dF(X,phi1,j):
    dsum=0
    #jはn以下
    for Y in phi1:
        dsum+=-1/(X[j]-Y[j])**2
    return dsum

def remove1(phi,x):
    li=[]
    for y in phi:
        if not y==x:
            li.append(y)
    return li




mat=[]
for i in range(len(X6)):
    for i in range(len(X6)):
        mat.append(1)

K=sympy.Matrix(len(X6),len(X6),mat)
print(K)
m=40

for j in range(len(X6)):
    for k in range(len(X6)):
        kjk=0
        for i in range(m):
            kk=2/np.pi  * math.sin((i+1)*X6[j][0]) * math.sin((i+1)*X6[j][1])*2/np.pi  * math.sin((i+1)*X6[k][0])*math.sin((i+1)*X6[k][1])
            kint=int(100*kk)/100
            kjk+=kint*2.3
            print(kjk)
        K[j,k]=kjk

print(K)
#A=K.subs(x1,2.3).subs(x2,2.3).subs(x3,2.3).subs(x4,2.3).subs(x5,2.3)
#print(A)
B=K.inv()
print(B)
print(B[0,1])
print(B[1,0])


def dK0(X,j):
    vec=0
    #print("sssssssssssss")
    for i in range(m):
        vec+= lam[i]* 2/np.pi *2*(i+1) * math.sin((i+1)*X[j])*math.cos((i+1)*X[j]) * 2/np.pi  * math.sin((i+1)*X[1-j])*math.sin((i+1)*X[1-j])
    #print("vec=",vec)
    return vec

def dK(X,Y,j):
    vec=0
    #print("sssssssssssss")
    for i in range(m):
        vec+= lam[i]* 2/np.pi *(i+1) * math.cos((i+1)*X[j])*math.sin((i+1)*X[1-j]) * 2/np.pi  * math.sin((i+1)*Y[j])*math.sin((i+1)*Y[1-j])
    #print("vec=",vec)
    return vec




sympy.var('x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20')
sympy.var('x01,x02,x03,x04,x05,x06,x07,x08,x09,x010,x011,x012,x013,x014,x015,x016,x017,x018,x019,x020')
lam=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20]
lam=lam+[x01,x02,x03,x04,x05,x06,x07,x08,x09,x010,x011,x012,x013,x014,x015,x016,x017,x018,x019,x020]
m=40


C=[]
for j in range(n):
    Cj=0
    for s in range(len(X6)):
        print("s=",s)
        a=[l for l in range(len(X6))]
        phi=remove1(a,s)
        sum=B[s,s]*dK0(X6[s],j)
        for t in phi:
            sum+=2*B[s,t]*dK(X6[s],X6[t],j)
        print(sum)
        Cj+=sum*F(X6[s],phi)
    C.append(Cj)

print(C)

print(sympy.solve(C-[-40552330.80682875, -74850.90905187737]))

C2=C[0].subs(x1,2.3).subs(x2,2.3).subs(x3,2.3).subs(x4,2.3).subs(x5,2.3)
C3=C2.subs(x6,2.3).subs(x7,2.3).subs(x8,2.3).subs(x9,2.3).subs(x10,2.3)
C4=C3.subs(x11,2.3).subs(x12,2.3).subs(x13,2.3).subs(x14,2.3).subs(x15,2.3)
C5=C4.subs(x16,2.3).subs(x17,2.3).subs(x18,2.3).subs(x19,2.3).subs(x20,2.3)

C6=C5.subs(x01,2.3).subs(x02,2.3).subs(x03,2.3).subs(x04,2.3).subs(x05,2.3)
C7=C6.subs(x06,2.3).subs(x07,2.3).subs(x08,2.3).subs(x09,2.3).subs(x010,2.3)
C8=C7.subs(x011,2.3).subs(x012,2.3).subs(x013,2.3).subs(x014,2.3).subs(x015,2.3)
C9=C8.subs(x016,2.3).subs(x017,2.3).subs(x018,2.3).subs(x019,2.3).subs(x020,2.3)

print(-C9)
