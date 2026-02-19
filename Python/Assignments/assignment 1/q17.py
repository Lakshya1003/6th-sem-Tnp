arr = [1,2,3,4,5,6,7,3,2,10]
lead = 0
for i in range(1,len(arr)):
  if arr[i] > arr[i-1]:
    lead = arr[i]

  else:
    break

print(lead)

# Time Complexity : O(n)
# Space Complexity : O(1)