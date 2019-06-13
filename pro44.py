n,p,q,s=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for i in range(0,len(l)):#loopstarts
	for j in range(i,len(l)):
		for k in range(j,len(l)):
			c.append(p*l[i]+q*l[j]+s*l[k])#loopends
print(max(c))
