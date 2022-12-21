l=[1256,1276,1296,1206,1226]
result = True 
d = str(l[0])
for i in l:
    c = str(i)
    if d[:-1] != c[:-1]:
        result = False
        break
    else:
        continue
print(result)