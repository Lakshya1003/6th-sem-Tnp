arr = [1,2,3,4,2,21,12,1,1,2,1,21,221]
non = []
target = 2

for i in range(len(arr)):
  if arr[i] == target:
    pass
  else :
    non.append(arr[i])
arr.clear()
arr = non
del(non)
print(arr)

# Time Complexity : O(n)
# space Complexity : O(1)
