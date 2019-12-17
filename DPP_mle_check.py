import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math
import csv
import pprint

np.random.seed()


m=40

#40こ

L=[]
for LL in range(10):
    L.append(0.1)
for LL in range(10):
    L.append(0.7)
for LL in range(20):
    L.append(0.3)
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

#点の個数を指定

#[-pi,pi]
rootpi=1/np.sqrt(np.pi)
def v(x,y):
    vec=[]
    for i in B_num:
        vec.append(2/np.pi  * math.sin((i+1)*x)*math.sin((i+1)*y))
    return vec

#K(x1,x2) = v(x2)^T v(x1)
def pn(x,y):
    #print(v(x,y))
    return (np.linalg.norm(v(x,y), ord=2))**2 / n


x = np.linspace(0,np.pi,100)
y = np.linspace(0,np.pi,100)
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
for i in range(200):
    x=np.random.uniform(0,np.pi)
    y=np.random.uniform(0,np.pi)
    sn=(max(pnlist))
    pn_sam=np.random.uniform(0, sn)
    if pn_sam <= pn(x,y):
        pn_samplelist.append(pn_sam)
        ylist.append([x,y])

"""
plt.figure(figsize=(10, 10), dpi=50)
for i in range(n-1):
    plt.plot(ylist[i][0],ylist[i][1],marker="*",color="blue")
plt.show()
"""
#ylistはポアソン点過程になる。
print(ylist)

Xn=ylist[0]
e_1=v(Xn[0],Xn[1])/np.linalg.norm(v(Xn[0],Xn[1]), ord=2)
e=[e_1]
#正規直交基底の集合
Xlist=[Xn]

def pi(x,y,i):
    hiku=0
    for j in range(i):
        hiku=hiku+np.dot(e[j],v(x,y))**2
    return (np.linalg.norm(v(x,y), ord=2)**2 - hiku) / i

print("1")
for i in range(n-1):
    print(i)
    x = np.linspace(0,np.pi,100)
    y = np.linspace(0,np.pi,100)
    pilist=[]
    for xx in x:
        for yy in y:
            pilist.append(pi(xx,yy,i+1))

    #plt.plot(x,pilist,"red")

    print("2")
    #棄却サンプリング
    pi_samplelist=[]
    ylist=[]
    Xi=0
    for j in range(100):
        x=np.random.uniform(0,np.pi)
        y=np.random.uniform(0,np.pi)
        print(max(pilist))
        sn=(max(pilist))
        pi_sam=np.random.uniform(0, sn)
        if pi_sam <= pi(x,y,i+1):
            #pi_samplelist.append(pi_sam)
            #ylist.append(y)
            Xi=[x,y]
            break
    w=v(Xi[0],Xi[1])
    Xlist.append(Xi)
    #print(w)
    for j in range(i+1):
        w = np.array(w) - np.dot(e[j],v(Xi[0],Xi[1])) * np.array(e[j])
    e_new=w / np.linalg.norm(w, ord=2)
    e.append(e_new)

print("Xlist=",Xlist)

def v(i):
    vec=[]
    #print("sssssssssssss")
    for X in Xlist:
        vec.append( 2/np.pi  * math.sin((i+1)*X[0])*math.sin((i+1)*X[1]))
    #print("vec=",vec)
    return vec


philist=[]
for i in range(m):
    philist.append(v(i))

print(philist)
print(np.array(philist).size)
print(len(philist))

filename='data_1.csv'
with open(filename,'w') as f:
    writer = csv.writer(f)
    for i in range(m):
        writer.writerow(philist[i])

print(L)
"""
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
"""
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
    print(A)
    #print(math.log(np.linalg.det(A).real))
    return np.linalg.det(A)

def log1(lam):
    vv=0
    for i in lis:
        vv+=math.log(1-lam[i])
    return vv
