n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    while left < n and arr[left] % 2 == 0:
        left += 1
    while right >= 0 and arr[right] % 2 != 0:
        right -= 1
    if left < right:
        arr[left], arr[right] = arr[right], arr[left]

print(' '.join(map(str, arr)))
