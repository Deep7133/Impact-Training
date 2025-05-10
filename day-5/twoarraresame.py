nums1=list(map(int, input("enter the num").split()))
nums2=list(map(int, input("enter the nums").split()))
a=len(nums1)
b=len(nums2)
result=nums1[0]
for num in nums1[1:]:
    result+=num
res=nums2[0]
for num in nums2[1:]:
    res+=num
print(nums1)
print(result)
print(nums2)
print(res)
if result==res and a==b :
    print("same")
else:
    print("not same")