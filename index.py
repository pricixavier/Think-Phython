b=raw_input()
length=len(b)
for i in range(0,length):
	if(b[i]=="k"):
		print b[i]
		break
	elif(b[i]=="K"):
		print b[i]
		break
	else:
		print b[i],
