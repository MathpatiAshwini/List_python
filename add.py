a=[12,67,98,34]
i=0
b=[]
while i<len(a):
    result=0
    while a[i]>0:
        digit=a[i]%10
        result=result+digit
        a[i]//=10
    b.append(result)
    i=i+1
print(b)