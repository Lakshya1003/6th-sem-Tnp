arr = [1,-1,3,2,1,-2]
cs = arr[0]
ms = arr[0]

for i in range(1,len(arr)):
  cs = max(cs,cs + arr[i])
  ms = max(ms,cs)

print(ms)

# Time Complexity : O(n)
# Space Complexity : O(1)