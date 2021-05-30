I=input
n=int(I())
x="NONE"
for i in range(2,n+1):
  if n%i==0:x=i;break
I(x)
