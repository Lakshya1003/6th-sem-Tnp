arr = [3,4,5,12,6,7,11,10]

# Approach sort and call

# Applying bubble sort

for i in range(len(arr)):
  for j in range(len(arr) - 1):

    if arr[j] > arr[j+1]:
      arr[j],arr[j+1] = arr[j+1],arr[j]
      break

print(f"The secound max element is : {arr[len(arr)-2]}")

# Time Complexity: O(n^2)
# Space Complexity: O(1)
