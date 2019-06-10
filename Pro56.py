n,t=map(int,input().split())
secs=list(map(int,input().split()))
c=0
for j in secs:
  t1=86400-j
  t=t-t1
  c=c+1
  if t<=0:
    break
  
print(c)
