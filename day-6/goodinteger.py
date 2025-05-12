size=int(input("enter the size of array "))
arr=list(map(int, input("enter the numbers ").split()))
count=0
for num in arr:
    x=min(arr)
    y=num
    if x**3+y**3==num:
        print(num)
    elif x**3+y**3<num:
        x+=1
    elif x**3+y**3>num:
        y-=1
print(num)