y1,y2 = map(int,input().split())
n = list(map(int,input().split()))
amount = int(input())
total = (sum(n)-n[y2])//2
if amount == total:
  print("Bon Appetit")
else:
  print(amount-total)
