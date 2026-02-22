arr = [1,2,3,4,5]
subarr = []
for i in range(len(arr)):
  temp = []
  temp.append(arr[i])
  for j in range(i+1,len(arr)):
    temp.append(arr[j])
    subarr.append(temp.copy())


  subarr.append(temp)

print(subarr)

# Time Complexity : O(n^2)
# Space Complexity : O(n)