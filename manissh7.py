a=[[3,5,6],[9,8,7],[4,6,],[22,10]]
i=0
b=[]
while i<len(a):
    j=0
    n=a[i]
    sum=0
    while j<len(n):
        sum+=a[i][j]
        # b.append(sum)
        j+=1
    b.append(sum)
    i+=1
print(b)