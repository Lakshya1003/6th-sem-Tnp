arr = [1,2,1,3,1,4,2,3,2,1,5]
uni = []
freq = []
for i in range(len(arr)):
  if arr[i] not in uni:
    uni.append(arr[i])
    temp = uni.index(arr[i])
    freq.append(1)

  else :
    temp = uni.index(arr[i])
    freq[temp] += 1


for i in range(len(uni)):
  if freq[i] > 1:
    print(f"element : {uni[i]}")


# Time Complexity : O(n)
# Space Complexity : O(n)
