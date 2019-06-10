n,k = map(int,input().split())
z = list(map(int,input().split()))
b,c = 0,[]
for i in range(0,len(z)):
  t = i
  for p in range(0,len(z)):
    for l in range(0,k):
      if l == k-1:
        try:
          b += z[p+i]
        except IndexError:
            t = t-1
            b +=z[t]
      else:
        b += z[i]
    c.append(b)
    b = 0
for i in range(0,len(z),k):
  b = sum(z[i:i+k])
  c.append(b)
print(*sorted(set(c)))
