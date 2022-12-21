a=[1,2,3,4,5,6,7,8,9,10]
i=0
sum=0
b=[]
while i<len(a):
    k=a[i]**2
    sum+=k
    i+=1
    b.append(sum)
print(b)