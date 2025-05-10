nums1=list(map(int, input("enter the num").split()))
nums2=list(map(int, input("enter the nums").split()))
a=len(nums1)
b=len(nums2)
for i in range(a):
        if nums1[i]==nums2[j]:
            i+=1
            j+=1
            print("compaitable")
        break
if a==b:
    print("compaitable")