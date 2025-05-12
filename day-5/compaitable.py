nums1=list(map(int, input("enter the num").split()))
nums2=list(map(int, input("enter the nums").split()))
a=len(nums1)
b=len(nums2)
if a==b:
    for i in range(a):
        if nums1[i]!=nums2[i]:
            print(" not compaitable")
            break
    else:
        print("compaitable")
else:
    print("not compaitable")