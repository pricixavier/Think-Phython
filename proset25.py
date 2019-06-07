w=int(raw_input())
l=list(map(int,raw_input().split()))
p=[]
c=1
for i in range(n-1):
	if l[i]<l[i+1]:
		c+=1
	else:
		p.append(c)
		c=1
p.append(c)
print(max(p))
