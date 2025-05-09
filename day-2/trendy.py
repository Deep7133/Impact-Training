n = int(input("Enter the number: \n"))

if 100 <= n <= 999:
    m = (n // 10) % 10 
    if m % 3 == 0:
        print("Trendy")
    else:
        print("Not trendy number")
else:
    print("Not a 3-digit number")
