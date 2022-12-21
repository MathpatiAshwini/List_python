a=[8,2,3,4,5,6]
i=0
b=[]
c=[]
sum=0
sum1=0
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
        sum+=a[i]
    else:
        c.append(a[i])
        sum1+=a[i]
    i=i+1
print(sum1)
print(sum)