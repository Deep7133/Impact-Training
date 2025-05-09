n=int(input("enter the number: "))
square_n=n*n
q=len((str(n)))
p1=int(str(square_n)[-q:])
p2=int(str(square_n)[:-q])
p=p1+p2
print(p)

# or 
# p1=square_n%100
# p2=square_n//100
# p=p1+p2
# print(p)