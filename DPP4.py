import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math


np.random.seed()
N = 100000
m=4


#L=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
L=[]
for LL in range(10):
    L.append(0.5)
B=[]
for l in L:
    B.append(np.random.binomial(1, l, size=1)[0])

B.append(1)
n=sum(B)

print(n)

#点の個数を指定

#[-pi,pi]
rootpi=1/np.sqrt(np.pi)
def v(x,y):
    vec=[]
    for i in range(n):
        vec.append(1/np.pi * 1/math.factorial(i) * math.e**(-1/2 * (x**2+y**2)) *  complex(x,y)**i)
    return vec

#K(x1,x2) = v(x2)^T v(x1)
def pn(x,y):
    #print(v(x,y))
    return (np.linalg.norm(v(x,y), ord=2))**2 / n

def pi(x,y,i):
    hiku=0
    for j in range(i):
        hiku=hiku+np.dot(e[j],v(x,y))**2
    return (np.linalg.norm(v(x,y), ord=2)**2 - hiku) / i


XXlist=[]

for num in range(3):

    x = np.linspace(-np.pi,np.pi,100)
    y = np.linspace(-np.pi,np.pi,100)
    pnlist=[]
    for xx in x:
        for yy in y:
            pnlist.append(pn(xx,yy))

    #plt.plot(x,pnlist,"red")
    #plt.show()
    print(max(pnlist))
    #棄却サンプリング

    pn_samplelist=[]
    ylist=[]
    for i in range(100):
        x=np.random.uniform(-np.pi, np.pi)
        y=np.random.uniform(-np.pi, np.pi)
        sn=(max(pnlist))
        pn_sam=np.random.uniform(0, sn)
        if pn_sam <= pn(x,y):
            pn_samplelist.append(pn_sam)
            ylist.append([x,y])


    Xn=ylist[0]
    e_1=v(Xn[0],Xn[1])/np.linalg.norm(v(Xn[0],Xn[1]), ord=2)
    e=[e_1]
#正規直交基底の集合
    Xlist=[Xn]



    print("1")
    for i in range(n-1):
        x = np.linspace(-np.pi,np.pi,100)
        y = np.linspace(-np.pi,np.pi,100)
        pilist=[]
        for xx in x:
            for yy in y:
                pilist.append(pi(xx,yy,i+1))

        #plt.plot(x,pilist,"red")

        print("2")
        #棄却サンプリング
        pi_samplelist=[]
        Xi=0
        for j in range(100):
            x=np.random.uniform(-np.pi, np.pi)
            y=np.random.uniform(-np.pi, np.pi)
            print(max(pilist))
            sn=(max(pilist))
            pi_sam=np.random.uniform(0, sn)
            if pi_sam <= pi(x,y,i+1):
                Xi=[x,y]
                break
        w=v(Xi[0],Xi[1])
        Xlist.append(Xi)
        #print(w)
        for j in range(i+1):
            w = np.array(w) - np.dot(e[j],v(Xi[0],Xi[1])) * np.array(e[j])
        e_new=w / np.linalg.norm(w, ord=2)
        e.append(e_new)

    XXlist.append(Xlist)



print(XXlist)
FinXlist=[]
#for li in XXlist:
#    FinXlist=FinXlist+li
"""
#以下は刈り上げ
for Xlist in XXlist:
    for li in Xlist:
        if random.randrange(3) == 0:
            FinXlist.append(li)
"""
"""
plt.figure(figsize=(10, 10), dpi=50)
plt.xlim(-np.pi,np.pi)
plt.ylim(-np.pi,np.pi)
for X in FinXlist:
    plt.plot(X[0],X[1],marker="*",color="blue")
plt.show()
"""
#print(ylist)
"""
plt.figure(figsize=(10, 10), dpi=50)
plt.xlim(-np.pi,np.pi)
plt.ylim(-np.pi,np.pi)
for i in range(n):
    plt.plot(ylist[i+1][0],ylist[i+1][1],marker="*",color="red")
plt.show()
"""


#確率距離を計算。
