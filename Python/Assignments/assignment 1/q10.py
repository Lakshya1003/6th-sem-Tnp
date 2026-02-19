arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

arr1.extend(arr2)
for i in range(len(arr1)):
  for j in range(len(arr1)-1):
    if arr1[j] > arr1[j+1]:
      arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
      break

print(arr1)

# Time Complexity : O(n^2)
# Space Complexity : O(1)