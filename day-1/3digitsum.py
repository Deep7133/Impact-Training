num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    a = num // 100         # hundreds digit
    b = (num // 10) % 10   # tens digit
    c = num % 10           # units digit
    total = a + b + c
    print("Sum of digits:", total)
else:
    print("Please enter a valid 3-digit number.")
