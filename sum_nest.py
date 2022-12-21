#  marks=[
    # [78,76,94,86,88]
    # [91,71,98,65,76]
    # [95,45,78,52,49]
    # ]


# a=[1,2,3,4,5]
# b=[6,7,8,9]
# # print(a+b)
# c=a+b
# c+=[2]
# print(c)


# a=[1,2,3,4,5]
# b=a*2
# print(b)


a=input("enter the number")
b=len(a)
if b==10:
	print("("+a[0:3]+")"+a[3:6]+"_"+a[6:])
else:
	print("no")