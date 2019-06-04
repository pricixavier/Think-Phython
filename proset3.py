a,b=raw_input().split()
c=abs(len(a)-len(b))
for i in range(len(a)):
	if len(b)==1 and b[i] in a:
		break
	if i>=len(a) or i>=len(b):
		break
	if b[i]!=b[i] and b[i]:
		c=c+1
print(c)
