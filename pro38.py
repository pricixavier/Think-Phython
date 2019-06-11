import sys, string, math

p,k = input().split()
p,k = int(p),int(k)
L = [ int(x) for x in input().split()]
L.sort()
cnt = 0
p = p // 3
#print(p)
for i in range(0,p) :
    L2 = L[3*i : 3*(i+1)]
    #print(L2)
    if 5-max(L2) >= k :
        cnt += 1
print(cnt)
