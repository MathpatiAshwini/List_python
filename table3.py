 a=[1,2,3,4,5,6,7,8,9]
a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
b=[]
while i<len(a):
    b.append(a[i]+a[i]+a[i])
    i+=1
print(b)
