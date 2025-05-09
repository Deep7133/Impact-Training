n=int(input("enter the number \n"))
count=1
for _ in range(n):
    count+=1
    print(n, end=" ")
    if n%2==1:
        n=3*n+1
    else :
        n=n//2
print(1)
print(count)