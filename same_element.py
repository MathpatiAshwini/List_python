l=[12,12,12,12,12]
result = True 
d = str(l[0])
for i in l:
    c = str(i)
    if d[:] != c[:]:
        result = False
        break
    else:
        continue
print(result)