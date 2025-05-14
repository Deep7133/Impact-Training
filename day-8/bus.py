n=int(input("enter the number of buses "))
m=int(input("enter thr no of capacity  "))
count=0
value=list(map(int, input().split()))
for i in range(n):
    if value[i]<m:
        value[i]+=1
        count+=1
print(count)