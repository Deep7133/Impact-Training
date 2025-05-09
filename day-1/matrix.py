rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

total = rows * cols

num = int(input(f"Enter the position number (1 to {total}): "))

if num < 1 or num > total:
    print(f"Invalid number. Please enter a number between 1 and {total}.")
else:
    row = (num - 1) // cols
    col = (num - 1) % cols

    if row == 0 or col == 0 or col == cols - 1:
        print("supporter")
    else:
        print("mango")
