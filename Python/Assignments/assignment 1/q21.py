arr = [1,2,4,3,7,6,5,9]
for i in range(len(arr)):
  for j in range(len(arr)-1):
    if arr[j] > arr[j+1]:
      arr[j],arr[j+1] = arr[j+1],arr[j]

k = int(input("Enter the valuse less than 9 : "))
print(arr[k-1])

# Time Complexity : O(n^2)
# Space Complexity : O(1)