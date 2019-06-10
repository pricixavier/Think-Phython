val1=list(map(str,input()))
val2=list(map(str,input()))
for i in range(0,len(val2)):
    m1=m2=m3=0
    m2=ord(val1[i])
    m3=ord(val2[i])
    m1=m2+m3
    if m1>96 and m1<123:
        print(chr(m1),end="")
    elif (m1-96)<122 and(m1-96)>96:
        m1=m1-96
        print(chr(m1),end="")
    elif m1>148:
        m1=m1-96-26
        print(chr(m1), end="")
    else:
        m1=m1-26
        print(chr(m1), end="")
       
