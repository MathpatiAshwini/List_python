# n=3
# s=0
# def ismagicsquare(mat):
#     for i in range(0,n):
#         s+=mat[i][i]
#     for i in range(0,n):
#         rowsum=0
#         for j in range(0,n):
#             rowsum+=mat[i][i]
#         if (rowsum!=s):
#             return False
#     for i in range(0,n):
#         colsum=0
#         for j in range(0,n):
#             colsum+=mat[i][i]
#         if (s!=colsum):
#             return False
#         return True
#     mat=[
#         [5,3,7]
#         [1,8,9]
#         [6,4,2]
#     ]
#     if (ismagicsquare):
#         print("magic square")
#     else:
#         print("not a magic square")
        