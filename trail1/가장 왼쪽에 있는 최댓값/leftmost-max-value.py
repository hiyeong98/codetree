n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

tot_index = []
max_index = len(arr)  # 처음엔 다 돌기

# 맨 처음 인덱스 1이 나올때까지 반복하기
while True:
    max_num = 0
    for i in range(max_index):

        if arr[i] > max_num:
            max_num = arr[i]

    # max_index값으로 최댓값의 왼쪽만 돌게끔 설정해주기
    max_index = arr.index(max_num)

    if max_index != 0:
        tot_index.append(max_index + 1)

    elif max_index == 0:
        tot_index.append(max_index + 1)
        break

print(*tot_index)
