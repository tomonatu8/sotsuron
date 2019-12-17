import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math
import csv
import pprint

X6=[[1.786525446443986, 2.9571325416425904],[1.2174661714935322, 2.286560039668559], [2.0647448477879684, 2.574106072554886], [0.4383059844205601, 0.021703779300330447], [2.340398889135444, 0.5493984443013916], [0.5234037182163223, 0.03607478607012122], [1.8642790714687176, 0.7640355893859928], [2.8873092788474923, 1.1055509317904708], [1.6683566170591557, 3.038537692691724], [0.8958897272808974, 3.0466985130765902]]

m=1

def K(x,y):
    vec=4/(np.pi)**2  * math.sin((i+1)*x[0])*math.sin((i+1)*x[1])  * math.sin((i+1)*y[0])*math.sin((i+1)*y[1])
    #print("vec=",vec)
    return vec

def KD(c,X6):
    A=np.ones((len(X6),len(X6)))
    for i in range(m):
        Phi=np.ones((len(X6),len(X6)))
        for x1 in range(len(X6)):
            for x2 in range(len(X6)):
                Phi[x1][x2]=K(X6[x1],X6[x2])
        A=A+c[i]*Phi
    return A

c=[]
for i in range(m):
    c.append(100000.0)

cc=c
for count in range(10000000):
    A=KD(cc,X6)
    dc=[]
    for i in range(m):
        Phi=np.ones((len(X6),len(X6)))
        for x1 in range(len(X6)):
            for x2 in range(len(X6)):
                Phi[x1][x2]=K(X6[x1],X6[x2])
        dc.append(0.1*np.trace(np.dot(np.linalg.inv(A),Phi)))
    #if count==0:
    print(dc)
    #print("-----------")
    cc=np.array(cc)+np.array(dc)
    #print(cc)
    if max(abs(np.array(dc)))<0.00001:
        break

print(cc)
