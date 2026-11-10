N = int(input())
arr = list(map(int, input().split()))

count = 0 
index = 0
for num in arr :
    index += 1
    if num == 2 :
        count += 1

    if count == 3 :
        break
        
        
print(index)
    