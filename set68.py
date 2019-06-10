y1,y2=input().split()
if(y1.isdigit() and y2.isdigit()):
              y1,y2=int(y1),int(y2)
              if(y2==1):
                  print("1 2")
              else:
                 print("1 "+str(y1-y2))
