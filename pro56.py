import sys,string, math, itertools

n,f = input().split()
n,f = int(n),int(f)
L = [ int(x) for x in input().split()]
#print(n,f, L)
for i in range(0,n) :
    if (86400-L[i]) >= f :
        print(i+1)
        sys.exit()
    f -= (86400-L[i])
