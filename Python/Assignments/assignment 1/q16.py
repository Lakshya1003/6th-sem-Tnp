arr1 = [1,2,3,4,5,6]
arr2 = [6,4,5,2,1,3]

for i in arr1:
  if i in arr2:
    pass
  else:
    print("arrays are not equal")
    break

# Time Complexity : O(n)
# Space Complexity : O(1)