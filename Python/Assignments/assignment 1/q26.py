arr = [1,2,3,2,4,2,5,2,5,2,6,2,2]

uni = []
freq = []
for i in range(len(arr)):
  if arr[i] not in uni:
    uni.append(arr[i])
    freq.append(1)
  else :
    temp = uni.index(arr[i])
    freq[temp] += 1

max = 0

for i in freq:
  if i > max:
    max = i

if max > len(arr)//2 :
  print(uni[freq.index(max)])

else :
  print("-1")