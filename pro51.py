n=int(input())
l=list(map(int,input().split()))
t=[]
c=1
for o in range(n):
	for j in range(o,n):
		if j==n-1:
			break
		if (l[j]>0 and l[j+1]<0) or (l[j]<0 and l[j+1]>0):
			c=c+1
		else:
			break
	t.append(c)
	c=1
print(*t)
