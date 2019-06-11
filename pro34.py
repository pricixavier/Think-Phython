num,k=map(int,input().split())
l=[]
m=0
for i in range(num):
    l.append(input())
for i in range(num):
    for j in range(k-1):
        if l[i][j]=="R" and l[i][j+1]=="R":
            m=m+5
        elif l[i][j]=="G" and l[i][j+1]=="G":
            m=m+3
print(m)
