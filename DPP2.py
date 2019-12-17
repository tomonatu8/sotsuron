import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import math

np.random.seed()
N = 100000
U = scipy.stats.uniform(loc=0.0, scale=1.0).rvs(size=N)

m=4


L=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5
,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
B=[]
for l in L:
    B.append(np.random.binomial(1, l, size=1)[0])

B.append(1)
n=sum(B)
print(n)
#[-pi,pi]
rootpi=1/np.sqrt(np.pi)

def v(x):
    vec=[]
    for i in range(n):
        vec.append(rootpi * np.cos((i+1)*x))
    return vec

#K(x,y) = v(y)^T v(x)
def pn(x):
    return (np.linalg.norm(v(x), ord=2))**2 / n

x = np.linspace(-np.pi,np.pi,100)
pnlist=[]
for xx in x:
    pnlist.append(pn(xx))

plt.plot(x,pnlist,"red")


#棄却サンプリング
pn_samplelist=[]
ylist=[]
for i in range(10000):
    y=np.random.uniform(-np.pi, np.pi)
    sn=(max(pnlist)+0.1)
    pn_sam=np.random.uniform(0, sn)
    if pn_sam <= pn(y):
        pn_samplelist.append(pn_sam)
        ylist.append(y)

plt.hist(ylist, bins=100, normed=True,alpha=0.5)
plt.show()

Xn=ylist[0]
e_1=v(Xn)/np.linalg.norm(v(Xn), ord=2)
e=[e_1]
#正規直交基底の集合
Xlist=[Xn]

def pi(x,i):
    hiku=0
    for j in range(i):
        hiku=hiku+np.dot(e[j],v(x))**2
    return (np.linalg.norm(v(x), ord=2)**2 - hiku) / i

for i in range(n-1):
    x = np.linspace(-np.pi,np.pi,100)
    pilist=[]
    for xx in x:
        pilist.append(pi(xx,i+1))

    #plt.plot(x,pilist,"red")


    #棄却サンプリング
    pi_samplelist=[]
    ylist=[]
    Xi=0
    for j in range(100):
        y=np.random.uniform(-np.pi, np.pi)
        sn=(max(pilist)+0.1)
        pi_sam=np.random.uniform(0, sn)
        if pi_sam <= pi(y,i+1):
            #pi_samplelist.append(pi_sam)
            #ylist.append(y)
            Xi=y
            break
    w=v(Xi)
    Xlist.append(Xi)
    #print(w)
    for j in range(i+1):
        w = np.array(w) - np.dot(e[j],v(Xi)) * np.array(e[j])
    e_new=w / np.linalg.norm(w, ord=2)
    e.append(e_new)

x0,y0=[],[]

for _x in np.linspace(-180,180,360):
    x0.append(math.sin(math.radians(_x)))
    y0.append(math.cos(math.radians(_x)))

plt.plot(x0,y0,color="green")

print(Xlist)
for X in Xlist:
    plt.plot(math.sin(X),math.cos(X),marker="*",color="blue")
plt.show()

plt.plot(x0,y0,color="green")

for X in Xlist:
    theta=np.random.uniform(-np.pi, np.pi)
    plt.plot(math.sin(theta)
    ,math.cos(theta),marker="*",color="red")
plt.show()
