a=[2,3,4,5,6,7]
# o/p[23,45,67]
# o/p[4,8,0]
i=0
j=[-1]
b=[]
while i<len(a):
    n=str(a[i]*j)
    if len(n)>1:
    
            v=n[1]
            l=int(v)
            b.append(l)
    else:
        h=int(n)
        b.append(h)
    i+=1
    j+=1
print(b)