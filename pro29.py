m=int(input())
list=[]
for i in range(1,m):
    rev=0
    temp=i
    while temp!=0:
        re=temp%10
        rev=rev+re
        temp=temp//10
    if i+rev==m:
        list.append(i)
print(len(list))
for j in range(0,len(list)):
    print(list[j])
