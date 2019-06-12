import sys,string
# Program to find maximum value of maximum of minimums of k segments.

def maxOfSegmentMins(M, n, k):
    if k == 1:
        return min(M)
    if k == 2 :
        return max(L[0], M[n - 1])
    return max(M)

n,k = input().split()
n,k = int(n),int(k)
M = [ int(x) for x in input().split()]
n = len(L)
ans = maxOfSegmentMins(M, n, k)
print(ans)
