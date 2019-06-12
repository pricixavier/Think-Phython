import sys,string
# Program to find maximum value of maximum of minimums of k segments.

def maxOfSegmentMins(L, m, k):
    if k == 1:
        return min(L)
    if k == 2 :
        return max(L[0], L[m - 1])
    return max(L)

m,k = input().split()
m,k = int(m),int(k)
L = [ int(x) for x in input().split()]
m = len(L)
ans = maxOfSegmentMins(L, m, k)
print(ans)
