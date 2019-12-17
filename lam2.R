library("sdpt3r", lib.loc="/Library/Frameworks/R.framework/Versions/3.4/Resources/library")
#library("spatstat", lib.loc="/Library/Frameworks/R.framework/Versions/3.4/Resources/library")

args <- commandArgs(trailingOnly = T)
default_args<-c("data_40.csv")
default_fig<-is.na(args[1])
args[default_fig] <- default_args[default_fig]


filename <- args[1]
print(filename)
list<-c(1,2)
print(list)
x <- read.csv(filename,header=F)
print(length(x))

out<-doptimal((t(x)))

y30<-out$y
print(y30)
write.csv(y30, "test.csv")
