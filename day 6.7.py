Mean,Median,modeklist=list(map(int, input("enter a list :").split()))
total=sum(klist)
nlen=len(klist)
mean=total/nlen
print("Mean is:",mean)
klist.sort()
if nlen%2==0:
 median1=klist[nlen//2]
 median2=klist[nlen//-1]
 median=(median1+median2) /2
else:
 median=klist[nlen//2]
print("Median is :"+str(median))
mode=klist[0]
c=0
l=0
for i in range (len(klist)-1):
 if(klist[i]==klist[i+1]):
    c=c+1
 else:
  if(c>l):
    mode=klist[i]
 l=c
c=0
print("Mode is :", mode)

