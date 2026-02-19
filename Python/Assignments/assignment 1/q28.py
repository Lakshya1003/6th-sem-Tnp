test = [0,1,0,2,0,1,2,0,1,0]

# Im using Bubble Sort to sort this question

for i in range(len(test)):
  swap = False
  for j in range(len(test)-i-1):
    if test[j] > test[j+1]:
      test[j], test[j+1] = test[j+1], test[j]
      swap = True
  if swap == False:
    break

print(test)



# Time Complexity : O(n)
# space complexity : O(1)