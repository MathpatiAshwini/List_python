a=['hello',10,20,40,20,60,40,30]
i=0
b=[]
while i<len(a):
    if a[i]>1:
        b.append(a[i])
    i+=1
print(b)