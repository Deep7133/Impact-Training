for row in range(5):
    for col in range(5): 
        if col == 0 or (col == 4 and row != 0 and row != 4) or (row == 0 or row == 4) and col < 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    for col in range(5): 
        if col == 0 or row == 0 or row == 2 or row == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    for col in range(5):  
        if col == 0 or row == 0 or row == 2 or row == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    for col in range(5):
        if col == 0 or (row == 0 or row == 2) and col < 4 or col == 4 and row in [1]:
            print("*", end="")
        else:
            print(" ", end="")
    print()
