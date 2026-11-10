arr = list(map(int, input().split()))

# 500 미만의 가장 큰 수 구하기 
numbers_max = []
max_num = 0
for num in arr : 
    if num < 500:
        numbers_max.append(num)
for num in numbers_max :
    if num > max_num :
        max_num = num 

#  500 초과 가장 작은 수 
numbers_min = []
min_num = float('inf')
for num in arr : 
    if num > 500:
        numbers_min.append(num)
for num in numbers_min :
    if num < min_num :
        min_num = num 

print(max_num, min_num)