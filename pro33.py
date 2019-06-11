mn=input()
flag3=0
for i in range(0,len(mn)-1):
  for j in range(i+1,len(mn)):
    if mn[i]<mn[j]:
      flag3=1
      print(mn[j:])
      break
  if flag3==1:
    break
else:
  print(mn)
