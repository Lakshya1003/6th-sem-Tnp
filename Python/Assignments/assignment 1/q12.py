arr = [1,2,3,4,5,7,8,9,10]
a = arr[len(arr)-1]
a = a*(a+1)/2
s = 0
for i in arr:
  s+=i


print(f"Missing number is : {a - s}")

# Time Complexity : O(n)
# Space Complexity : O(1)
