num = int(input("Enter a number: "))

# Convert to positive (like Math.abs in Java)
num = abs(num)

# Get last digit
last_digit = num % 10

# Get first digit
first_digit = num
while first_digit >= 10:
    first_digit //= 10

# Sum of first and last digits
total = first_digit + last_digit

print("Sum of first and last digit:", total)
