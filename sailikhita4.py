l=["p","q"]
i=0
b=[]
while i<len(l):
    j=1
    while j<=5:
        p=str(j)
        k=l[i]+p
        b.append(k)
        j+=1
    i+=1
print(b)