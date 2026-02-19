arr = [0,1,2,3,0,1,2,4,1,0,5,2,0,6,7]
zc = 0
non = []
for i in arr:
  if i == 0:
    zc += 1
  else :
    non.append(i)

for i in range(0,zc):
  non.append(0)

arr.clear()
arr = non
del(non)
print (arr)

# Time Complexity : O(n)
# Space Complexity : O(1)