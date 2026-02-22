arr = [1,2,3,4,5,6,7,9]
for i in range(len(arr) - 1):
  l = arr[i] + 1
  r = arr[i+1]
  if(l == r):
    pass
  else:
    print("Array is not sorted")
    break