n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_num = float('inf')
min_count = 0 

for num in a :
    if num < min_num:
        min_num = num 

for num in a :
    if num == min_num:
        min_count += 1

print(min_num, min_count)