test = [22,33,44,55,66,77,88,99]
for i in range (len(test) // 2):
    temp = test[i]
    test[i] = test[len(test)-1-i]
    test[len(test)-1-i] = temp

print(test)


# Time Complexity : O(n)
# Time Complexity : O(1)
