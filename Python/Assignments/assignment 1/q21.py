arr = [1,2,4,3,7,6,5,9]
k = int(input("Enter the valuse less than 9 : "))
min = arr[0]
ks = k - 1
j = 0
for i in range(len(arr)):
  if arr[i] < min:
    min = arr[i]
    j+=1
  if j >= k :
    ks = i
    break

print(arr[ks])

# Time Complexity : O(n^2)
# Space Complexity : O(1)