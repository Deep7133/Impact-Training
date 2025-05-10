# stair case
# n=3
# for i in range(0, n+1):
#     for j in range(0,n-i):
#         print(" ", end=" ")
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print()


# rigt angle triangle 
# n=5
# for i in range(0, n+1):
#     for j in range(0,i+1):
#         print(" ", end=" ")
#     for j in range(0,n-i):
#         print("*", end=" ")
#     print()


# outer rectangle 
n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()