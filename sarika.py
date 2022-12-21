a='a man , a plan , a canal : panama'
i=0
b=""
while i<len(a):
    if a[i].isalpha()==True:
        b=b+a[i]
    i=i+1
print(b)