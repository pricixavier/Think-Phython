import sys, string, math

b,k = input().split()
b,k = int(a),int(k)
L = [ int(x) for x in input().split()]
L.sort()
cnt = 0
b = b // 3
#print(b)
for i in range(0,b) :
    L2 = L[3*i : 3*(i+1)]
    #print(L2)
    if 5-max(L2) >= k :
        cnt += 1
print(cnt)
