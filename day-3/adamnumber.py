n=int(input("ENTER THE NUMBER"))
square_n=n*n
reverse_n=int(str(n)[::-1])
square_n2=reverse_n*reverse_n
reverse_square_n=int(str(square_n2) [::-1])
if square_n==reverse_square_n:
    print("adam number  ")
else:
    print("it is not adam number")