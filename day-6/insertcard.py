n=int(input("enter the size of array "))
nums=list(map(int , input("enter the numbers").split()))
pos = int(input("Enter the position "))
val = int(input("Enter the value to insert"))
if 0 <= pos <= len(nums):
    nums.insert(pos, val)
    for item in nums:
        print(item, end=' ')
