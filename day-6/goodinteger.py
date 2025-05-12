size=int(input("enter the size of array "))
arr=list(map(int, input("enter the numbers ").split()))
for i in arr:
    x=1
    y=int(i**(1/3))
    while x<=y:
        if x**3+y**3==i:
            print(i)
            break
        elif x**3+y**3<i:
            x+=1
        elif x**3+y**3>i:
            y-=1
