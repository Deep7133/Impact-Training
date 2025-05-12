nums=list(map(int, input().split()))
result_odd =0
result_even=0
for num in nums:
    if num % 2 == 0:
        result_even+=num

    else:
        result_odd+=num
max=max(nums)
print(max)
print(result_odd)
print(result_even)
