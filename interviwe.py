a=[['M','A','N'],['P','R','E','E','T']]
i=0
while i<len(a):
    n=a[i]+a[i+1]
    j=0
    while j<len(n):
        h=n[j]
        k=h.lower()
        if k[0]==True:
            pass
        if k=="m":
            print(k.upper(),end="")
        else:
            print(k,end="")
        j+=1
        i+=1
        
a='ashwini'
i=0
while i<len(a):
        if a[i]=='a':
                print(a[i].upper(),end="")
        else:
                print(a[i],end="")
        i+=1