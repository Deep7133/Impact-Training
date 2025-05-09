n=int(input("enter the number \n"))
if n <100:
    f=n//10
    l=n%10
    sum=f+l
    product=f*l
    total=sum+product
    if total==n:
        print("the number is magic")
    else :
        print("the number is not magic")