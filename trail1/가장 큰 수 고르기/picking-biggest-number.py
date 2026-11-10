arr = list(map(int, input().split()))

max_num = 0 

for num in arr : 
    if num > max_num :
        max_num = num 

print(max_num)
