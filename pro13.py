N,Q=map(int,raw_input().split())
a=list(map(int,raw_input().split()))
for i in range(0,Q):
  U,V=map(int,raw_input().split())
  c=a[U-1:V]
  print(min(c))
