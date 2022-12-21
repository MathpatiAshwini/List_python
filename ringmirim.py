# a=[2,1,7,5,3,8]
# # o/p[3,3,1,9,8,1]
# i=0  
# j=1
# b=[]
# while i<len(a):
#     n=a[i]+j
#     b.append(n)
#     j+=1
#     i+=1
# print(b)

a=[2,1,7,5,3,8]
# o/p[3,3,1,9,8,1]
i=0
j=1
b=[]
while i<len(a):
    n=str(a[i]*j-1)
    if len(n)>1:
            v=n[1]
            l=int(v)
            b.append(l)
    else:
        h=int(n)
        b.append(h)
    i+=1
    j+=1
print(b)


