arr = [1,2,3,4,5,6]
k = 2

for i in range(len(arr)//2):
  arr[i],arr[len(arr) - 1 -i] = arr[len(arr) - 1 -i],arr[i]

for i in range(0,k//2):
  arr[i],arr[k-i-1] = arr[k-i-1],arr[i]

a = (len(arr)-k) / 2
i = 0
while(i!=a):
  arr[k+i],arr[len(arr)-1 - i] = arr[len(arr)-1 - i],arr[k+i]
  i += 1

print(arr)

# Time Complexity : O(n)
# Time Complexity : O(1)
