arr = [1,2,1,3,1,4,45,15,51,15]
uni = []
for i in arr:
  if i not in uni:
    uni.append(i)

arr.clear()
arr = uni
del(uni)
print(arr)

# Time complexity : O(n)
# Space complexity : O(1)