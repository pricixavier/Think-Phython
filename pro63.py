b=input()
lis=[]
for i in b:
    if i not in lis:
        lis.append(i)
        #print(i)
    else:
        break
print(len(lis))
