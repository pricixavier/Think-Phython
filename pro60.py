import sys,string, math, itertools

a = int(input())
b = 3
n = b
while a > 0 :
    if n == 0 :
        b = 2*b
        n = b
    if a==1 :
        print(n)
        sys.exit()
    a -= 1
    n -= 1
