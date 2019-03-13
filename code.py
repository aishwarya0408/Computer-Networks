def xor(a,b):
    r=""
    for i in range(1,len(b)):
        r+=str(int(a[i])^int(b[i]))
    return(r)
n=int(input())
d=input()
m=int(input())
divisor=input()
data=d+("0"*(m-1))
k=m
z=len(data)
t=data[:m]
while(k<z):
    if(t[0]=="1"):
        t=xor(divisor,t)+d[m]
    else:
        t=xor("0"*(len(divisor)),t)+d[m]
    k+=1
if(t[0]=="1"):
    t=xor(divisor,t)
else:
    t=xor("0"*(m),t)
print(t)