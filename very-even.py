a=[13]
i=0
sum=0,
while i<len(a):
    j=0
    n=a[i]
    while i<len(str(n)):
        m=int(n)
        if m%2==0:
            sum+=a[j]
        elif (int(sum))%2==0:
            print("very even")
        else:
            print("not perfect even")
        i+=1