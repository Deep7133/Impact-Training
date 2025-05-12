nums=list(map(int, input("enter the elements").split()))
d=list(set(nums))
n=len(d)
for i in range(n):
    for j in range(n-1):
        if d[j]>d[j+1]:
            d[j],d[j+1]=d[j+1],d[j]
print(d)
print(n)
# print(type(d))
# l=sorted(nums)
# print(l)