arr = [1,2,2,1,2,1,1,1,1]
uni = []
freq = []
for i in arr :
  if i not in uni:
    uni.append(i)
    freq.append(1)

  else:
    t = uni.index(i)
    freq[t] += 1

for i in  range(len(uni)):
  print(f"element : {uni[i]} , freq is : {freq[i]}")

minele  = uni[0]
maxfreq = freq[0]

for i in range(len(freq)):
  if freq[i] > maxfreq :
    if uni[i] < minele :
      minele = uni[i]
      maxfreq = freq[i]

output = []
i = 0
while(i < len(arr)):
  if(arr[i-1] != arr[i]):
    if(I+1 != arr)



print(output)
