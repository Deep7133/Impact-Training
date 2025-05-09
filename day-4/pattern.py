# n=1
# for i in range(3): 
#     for j in range(3): 
#         print(n, end=" ")
#         n += 1
#     print() 


# stair case 
# n=3
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*",end=" ")
#     print()

n=3
for i in range(0, n+1):
    for j in range(0,n-i):
        print(" ", end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()
