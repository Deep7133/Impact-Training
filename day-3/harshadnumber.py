n=int(input("enter the number "))
sum_digits=0
while n != 0: 
    n = n // 10
    digit = n % 10
    sum_digits+=digit
if n%sum_digits==0:
    print("harshad number")
else:
    print("not harshad number")