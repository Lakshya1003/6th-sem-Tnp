arr = [1,2,3,4,5,7,8,10]
sort = True

for i in range(1,len(arr)):
  if arr[i] < arr[i-1]:
    sort = False
    break
if sort:
  print("Array is sorted")
else:
  print("Array is not sorted")

  # Time Complexity : O(n)
  # Space Complexity : O(1)