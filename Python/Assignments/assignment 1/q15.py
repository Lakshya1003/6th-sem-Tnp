arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

for i in arr1:
  if i not in arr2:
    arr2.append(i)

print(arr2)

# Time Complexity : O(n)
# Space Complexity : O(1)