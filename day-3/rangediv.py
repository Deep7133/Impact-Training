n=int(input("enter the starting number "))
m=int(input("enter the ending number"))
for _ in range(m):
    quotent=n//7 or m//9 or m//7 or m//9
    lower =quotent*n or quotent*m
    upper =(quotent+1)*n or (quotent+1)*m
    print(lower, end='')
