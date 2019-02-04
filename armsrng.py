val = int(input(""))
length = len(str(val))
sum = 0
temp = val
while (temp !=0):
  sum = sum + ((temp % 10) ** length)
	temp = temp // 10
if sum == val:
	print "yes"
else:
	print "no"
