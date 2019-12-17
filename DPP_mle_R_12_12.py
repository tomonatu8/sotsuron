import subprocess
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random
import math
import csv
import pprint
import sympy
from tqdm import tqdm
import time

m=40
#データ
X6=[[0.3792867335276325, 1.950488939292105], [0.12836889952507655, 0.20422533212852556], [0.489839037603313, 1.0273893483232186], [2.335239047338269, 2.511976341084248], [1.3055910883453483, 2.637418599488819], [2.9759270608282127, 0.07360707763577042], [1.330170795446663, 1.0778910731277673], [1.2100331530385762, 0.6106031429272996], [0.5709854814314912, 2.6092288209158254], [1.1097074958185458, 2.011440897921088], [1.9132724540760757, 1.203330056366217], [0.6482589481773727, 2.8543958151486577], [2.825262683728557, 0.8930673855843748], [2.075748714827975, 2.839466302721716], [2.6076559478388375, 2.1927193749081915], [1.464884193220323, 1.5249772140336393], [0.9052726934361649, 1.9970141000243289], [0.5617283790619311, 1.1748829956169933], [2.9802233404979397, 1.2824176965655991], [2.998508951911826, 2.1119687394629825], [2.8250395472042946, 2.982804664611138], [0.2806847789120289, 2.431655871357795], [1.7245952111918592, 2.3166104208351617], [0.16081087645167588, 0.14508724965147393], [0.5160095277486658, 1.3812410548991672], [1.4742473505336864, 2.051746673773112], [2.5543864162375267, 2.304326182639277], [1.323556787893661, 1.1926374540175682], [2.0793921344001975, 0.8567381201411894]]

n=len(X6)

sympy.var('k')

sum_c=5

#カーネルの基底
def phi(x,y,i):
    return 2/np.pi  * math.sin((i+1)*x)*math.sin((i+1)*y)


def v(i):
    vec=[]
    #print("sssssssssssss")
    for X in X6:
        vec.append(phi(X[0],X[1],i))
    #print("vec=",vec)
    return vec

#コンパニオン行列を用いて方程式を解く。f(x)=x^5−15x^4+85x^3−225x^2+274x−120
#vec=np.array([-120,274,-225,85,-15])
#print(solve(vec))
def solve(vec,is_complex=False):
    dim =len(vec)
    if is_complex:
        A = np.zeros((dim,dim),dtype=complex)
    else:
        A = np.zeros((dim,dim))
    A[np.arange(dim-1),1+np.arange(dim-1)] =1
    A[-1,:] = -vec
    ans,vec = np.linalg.eig(A)
    return ans

#c=[c[0],...,c[m-1]]から、多項式を作る。
def make_poly_k(c):
    v=1
    for i in range(len(c)):
        v=v*(c[i]*k+1)
    poly=sympy.poly(k**n-v)
    #print(poly)
    ef=poly.all_coeffs()
    ef.reverse()
    b=[]
    for i in range(len(ef)-1):
        b.append(ef[i]/ef[-1])
    return np.array(b)

def selc_real(klist):
    klist_real=[]
    for ki in klist:
        if ki.imag==0.0:
            klist_real.append(ki)
    klist_real=np.array(klist_real)
    return klist_real

def selc_true_lam(klist,c):
    lamli=[]
    for ki in klist:
        lamlist=[]
        for i in range(m):
            lamlist.append(c[i]*ki.real/(c[i]*ki.real+1))
        if lamlist[0] > 0:
            lamli.append(lamlist)
    return lamli

def K(x,y,lam):
    vec=0.0
    #print("sssssssssssss")
    for i in range(m):
        vec+= lam[i]/(1.0-lam[i]) * phi(x[0],x[1],i) * phi(y[0],y[1],i)
    #print("vec=",vec)
    return vec

def Det_J(lam):
    A=np.ones((len(X6),len(X6)))
    for x1 in range(len(X6)):
        for x2 in range(len(X6)):
            A[x1][x2]=K(X6[x1],X6[x2],lam)
    #print(A)
    return np.linalg.det(A)

def log1(lam):
    vv=0
    for i in range(m):
        vv+=math.log(1-lam[i])
    return vv

def density(lam):
    KKK=Det_J(lam)
    #print(KKK)
    #print("logdet(K')=",math.log(KKK))
    dens=log1(lam)+math.log(KKK)
    return dens


if __name__ == '__main__':
    philist=[]
    for i in range(m):
        philist.append(v(i))

    filename='data_40.csv'
    with open(filename,'w') as f:
        writer = csv.writer(f)
        for i in range(m):
            writer.writerow(philist[i])

    subprocess.call(["Rscript" ,"lam2.R"])

    filename2='test.csv'
    with open(filename2) as f:
        reader = csv.reader(f)
        l = [row for row in reader]
    c=[float(l[i+1][1]) for i in range(len(l)-1)]

    #ここから、sum_cを選択すべき。
    true_lam_list=[]
    denslist=[]
    max_dens=-10000
    for sum_c in tqdm(np.arange(0, 25, 0.1)):
        time.sleep(0.1)
        #print(c)
        cc=sum_c*np.array(c)
        poly_vec=make_poly_k(cc)
        #print(poly_vec)
        klist=solve(poly_vec)
        #print(klist)
        klist_real=selc_real(klist)
        #print(klist_real)

        true_lam=selc_true_lam(klist_real,c)
        #print(true_lam)
        if not true_lam==[]:
            for i in range(len(true_lam)):
                #print(true_lam[i])
                densi=density(true_lam[i])
                if densi > max_dens:
                    max_dens=densi
                    max_lam=true_lam[i]
                denslist.append(densi)
        slist=[]
        for i in range(len(true_lam)):
            slist.append(sum(true_lam[i]))
        #print(slist)
        #if not true_lam==[]:
        true_lam_list.append(true_lam)
        #print("-----")
        #print(true_lam_list)

    plt.plot(range(len(denslist)),denslist)
    #plt.hlines([8.5],1,len(ffflist)-1,"green",label="true value")
    #plt.hlines([8.99],1,len(ffflist)-1,"red",label="estimated value")
    plt.xlabel("sum_c")
    plt.ylabel("logf(φ)")
    plt.show()

    print("max_dens=",max_dens)
    print("max_lam=",max_lam)
