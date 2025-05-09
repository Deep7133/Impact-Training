# n=int(input("enter the number"))
# for i in str(n):
#     print(i)
n = int(input("Enter the number: "))
while n > 0:
    
    digit = n % 10
    n = n // 10
    print(digit)
    
