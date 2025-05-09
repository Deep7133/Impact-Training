n=int(input("enter the number 0-9\n"))
if n<= 9:
    if n%2==0:
        print("Even")
    elif n%2!=0:
        print("Odd")
else :
    print("Invalid")