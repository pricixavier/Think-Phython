m=int(input())
l=list(map(int,input().split()))
a_ha=0
b_ha=0
l.sort(reverse=True)
for i in l:#loopstarts
  s=a_ha+i
  if b_ha>s:
    a_ha=s
  else:
    a_ha=b_ha
    b_ha=s#loopends
print(a_ha,b_ha)
