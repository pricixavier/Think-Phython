import sys,string, math, itertools

s1 = input()
M = s1.split('|')
s = input()
#print(M,s)
n1 = abs(len(M[0])-len(M[1]))
#print(n1)
if n1==0 :
    print('Impossible')
    sys.exit()
if n1 != len(s) :
    print('Impossible')
    sys.exit()
if len(s) >= n1 :
    if len(M[0]) < len(M[1]) :
        s2 = M[0] + s + '|' + M[1]
    else :
        s2 = M[0] + '|' + M[1] + s
    print(s2)
else :
    print('Impossible')
