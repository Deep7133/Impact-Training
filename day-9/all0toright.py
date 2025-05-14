# n=int(input("enter the number"))
# s=str(n)
# non_zero=[]
# zero=0
# for digit in s:
#     if digit != '0':
#         non_zero.append(digit)
#     else:
#         zero+=1
# c= ''.join(non_zero)+ '0'*zero
# d=int(c)
# print(d)
# print(type(d))


# or 
T = int(input())
for _ in range(T):
    binary = input().strip()
    ones = ''.join([ch for ch in binary if ch == '1'])
    zeros = ''.join([ch for ch in binary if ch == '0'])
    result = ones + zeros
    print(result)
