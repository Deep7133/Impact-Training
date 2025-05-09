num=int(input("enter the number "))
m=int(input("enter the dividend"))
if num%m==0:
    print("the number is divisible",num//m)
else:
    nearest = num - (num % m)
    n=nearest+m

    if n-num < num-nearest :
        print("the nearest number is",n)
    elif n-num == num-nearest :
        print("the nearezxt number is ",n)
    else:
        print("the nearest number is",nearest)

# num=int(input("enter the number "))
# m=int(input("enter the div number"))
# if num%m==0:
#     print("the number is divisible",num//m)
# else:
#     q=num//m
#     l=q*m
#     u=(q+1)*m
#     if u-num < num-l:
#         print("the number is",u)
#     elif u-num == l-num:
#         print("the number is",l)
#     else:
#         print("the number is",u)
    
    