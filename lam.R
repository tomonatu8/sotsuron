x30 <- read.csv("Desktop/sotsuron/data_30.csv",header=F)
x31 <- read.csv("Desktop/sotsuron/data_31.csv",header=F)
x32 <- read.csv("Desktop/sotsuron/data_32.csv",header=F)
x33 <- read.csv("Desktop/sotsuron/data_33.csv",header=F)
x34 <- read.csv("Desktop/sotsuron/data_34.csv",header=F)
x35 <- read.csv("Desktop/sotsuron/data_35.csv",header=F)
x36 <- read.csv("Desktop/sotsuron/data_36.csv",header=F)
x37 <- read.csv("Desktop/sotsuron/data_37.csv",header=F)
x38 <- read.csv("Desktop/sotsuron/data_38.csv",header=F)
x39 <- read.csv("Desktop/sotsuron/data_39.csv",header=F)
x40 <- read.csv("Desktop/sotsuron/data_40.csv",header=F)
x41 <- read.csv("Desktop/sotsuron/data_41.csv",header=F)
x42 <- read.csv("Desktop/sotsuron/data_42.csv",header=F)
x43 <- read.csv("Desktop/sotsuron/data_43.csv",header=F)
x44 <- read.csv("Desktop/sotsuron/data_44.csv",header=F)

out30<-doptimal((t(x30)))
out31<-doptimal((t(x31)))
out32<-doptimal((t(x32)))
out33<-doptimal((t(x33)))
out34<-doptimal((t(x34)))
out35<-doptimal((t(x35)))
out36<-doptimal((t(x36)))
out37<-doptimal((t(x37)))
out38<-doptimal((t(x38)))
out39<-doptimal((t(x39)))
out40<-doptimal((t(x40)))
out41<-doptimal((t(x41)))
out42<-doptimal((t(x42)))
out43<-doptimal((t(x43)))
out44<-doptimal((t(x44)))

lam30<-numeric(40)
lam31<-numeric(40)
lam32<-numeric(40)
lam33<-numeric(40)
lam34<-numeric(40)
lam35<-numeric(40)
lam36<-numeric(40)
lam37<-numeric(40)
lam38<-numeric(40)
lam39<-numeric(40)
lam40<-numeric(40)
lam41<-numeric(40)
lam42<-numeric(40)
lam43<-numeric(40)
lam44<-numeric(40)

y30<-out30$y
y31<-out31$y
y32<-out32$y
y33<-out33$y
y34<-out34$y
y35<-out35$y
y36<-out36$y
y37<-out37$y
y38<-out38$y
y39<-out39$y
y40<-out40$y
y41<-out41$y
y42<-out42$y
y43<-out43$y
y44<-out44$y

for (i in 1:length(out30$y)){
  lam30[i]=y30[i]
}
for (i in 1:length(out31$y)){
  lam31[i]=y31[i]
}
for (i in 1:length(out32$y)){
  lam32[i]=y32[i]
}
for (i in 1:length(out33$y)){
  lam33[i]=y33[i]
}
for (i in 1:length(out34$y)){
  lam34[i]=y34[i]
}
for (i in 1:length(out35$y)){
  lam35[i]=y35[i]
}
for (i in 1:length(out36$y)){
  lam36[i]=y36[i]
}
for (i in 1:length(out37$y)){
  lam37[i]=y37[i]
}
for (i in 1:length(out38$y)){
  lam38[i]=y38[i]
}
for (i in 1:length(out39$y)){
  lam39[i]=y39[i]
}
for (i in 1:length(out40$y)){
  lam40[i]=y40[i]
}
for (i in 1:length(out41$y)){
  lam41[i]=y41[i]
}
for (i in 1:length(out42$y)){
  lam42[i]=y42[i]
}
for (i in 1:length(out43$y)){
  lam43[i]=y43[i]
}

for (i in 1:length(out44$y)){
  lam44[i]=y44[i]
}
print(lam30)
print(lam40)






slist=numeric(100)

s30<-0
for (i in 1:40){
  s30<-s30+(lam30[i]*29-0.7)**2
}
print(s30)
slist[1]=s30

s31<-0
for (i in 1:40){
  s31<-s31+(lam31[i]*29-0.7)**2
}
print(s31)
slist[2]=s31

s32<-0
for (i in 1:40){
  s32<-s32+(lam32[i]*29-0.7)**2
}
print(s32)
slist[3]=s32

s33<-0
for (i in 1:40){
  s33<-s33+(lam33[i]*29-0.7)**2
}
print(s33)
slist[4]=s33

s34<-0
for (i in 1:40){
  s34<-s34+(lam34[i]*29-0.7)**2
}
print(s34)
slist[5]=s34

s35<-0
for (i in 1:40){
  s35<-s35+(lam35[i]*29-0.7)**2
}
print(s35)
slist[6]=s35

s36<-0
for (i in 1:40){
  s36<-s36+(lam36[i]*29-0.7)**2
}
print(s36)
slist[7]=s36

s37<-0
for (i in 1:40){
  s37<-s37+(lam37[i]*29-0.7)**2
}
print(s37)
slist[8]=s37

s38<-0
for (i in 1:40){
  s38<-s38+(lam38[i]*29-0.7)**2
}
print(s38)
slist[9]=s38

s39<-0
for (i in 1:40){
  s39<-s39+(lam39[i]*29-0.7)**2
}
print(s39)
slist[10]=s39


s40<-0
for (i in 1:40){
  s40<-s40+(lam40[i]*29-0.7)**2
}

print(s40)
slist[11]=s40

s41<-0
for (i in 1:40){
  s41<-s41+(lam41[i]*29-0.7)**2
}

print(s41)
slist[12]=s41

s42<-0
for (i in 1:40){
  s42<-s42+(lam42[i]*29-0.7)**2
}

print(s42)
slist[13]=s42

s43<-0
for (i in 1:40){
  s43<-s43+(lam43[i]*29-0.7)**2
}

print(s43)
slist[14]=s43

s44<-0
for (i in 1:40){
  s44<-s44+(lam44[i]*29-0.7)**2
}

print(s44)
slist[15]=s44

plot(slist)
