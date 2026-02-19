arr = [3,4,5,12,6,7,11,10]

a = arr[0]
b = arr[0]

for i in arr:
  if i > a :
    a = i
  if i < b:
    b = i

print(f"Max element is : {a}")
print(f"Min element is : {b}")

# Time cmplexity : O(n)
# Space cmplexity : O(1)