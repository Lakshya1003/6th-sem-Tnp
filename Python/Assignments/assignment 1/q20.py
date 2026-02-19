arr = [1,2,3,4,5,6]
k = 2
for i in range(len(arr)//2):
  arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]

a = len(arr)-k
i = 0
while(i != a//2):
  arr[i],arr[a-i-1] = arr[a-i-1],arr[i]
  i += 1

s = len(arr) - k

e = len(arr) - 1

for i in range(k // 2):
    arr[s + i], arr[e - i] = arr[e - i], arr[s + i]



print(arr)