a=[25,22,10,6,35]
i=0
c=0
b=0
v=[]
n=[]
while i<len(a):
    if a[i]%2==0:
        c+=1
        v.append(a[i])
    if a[i]%2!=0:
        b+=1
        n.append(a[i])
    i+=1
print(v,"even no.=",c)
print(n,"odd no.=",b)