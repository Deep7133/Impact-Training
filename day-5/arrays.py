size=int(input("enter the size of arr "))
nums = list(map(int, input("Enter the numbers ").split()))
print("You entered:", nums)
result=nums[0]
for num in nums[1:]:
    result-=num
print(result)
