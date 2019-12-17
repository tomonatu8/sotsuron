import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math

np.random.seed()
N = 100000
#U = scipy.stats.uniform(loc=0.0, scale=1.0).rvs(size=N)





#L=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
L=[]
for LL in range(10):
    L.append(0.3)
for LL in range(10):
    L.append(0.7)
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
"""
fig=plt.figure()
ax=fig.add_subplot('111',projection='3d')
#X,Y =np.meshgrid(x,y)
#Z=pn(X,Y)
#ax.scatter(x,y,pnlist)
#plt.show()
#plt.plot(x,y,pnlist,"red")
print(pnlist)
"""

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
plt.hist(ylist, bins=100, normed=True,alpha=0.5)
plt.show()
"""
plt.figure(figsize=(10, 10), dpi=50)
for i in range(n-1):
    plt.plot(ylist[i][0],ylist[i][1],marker="*",color="blue")
plt.show()

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

print(Xlist)

"""
plt.figure(figsize=(10, 10), dpi=50)
for X in Xlist:
    plt.plot(X[0],X[1],marker="*",color="blue")
plt.show()

plt.figure(figsize=(10, 10), dpi=50)
for X in Xlist:
    plt.plot(np.random.uniform(-5, 5),np.random.uniform(-5, 5),marker="*",color="red")
plt.show()
"""
