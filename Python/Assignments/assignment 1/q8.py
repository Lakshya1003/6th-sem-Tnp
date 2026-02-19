arr = [0,1,2,3,4,5,6,7,8,9]
target = 9
for i in arr:
  for j in arr:
    if i + j == target:
      print(f"({i},{j})")


# Time Complexity : O(n^2)
# Space Complexity : O(1)