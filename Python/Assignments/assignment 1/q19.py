arr = [1,2,3,5,7,9]
s = 0
cs = 0
target = 12

for i in range(len(arr)):
    cs += arr[i]

    while cs> target:
        cs -= arr[s]
        s += 1

    if cs == target:
        print(arr[s:i+1])


# Time Complexity : O(n^2)
# Space Complexity : O(1)




