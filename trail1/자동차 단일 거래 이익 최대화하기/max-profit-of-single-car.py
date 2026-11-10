n = int(input())
prices = list(map(int, input().split()))

# Please write your code here.
max_profit = 0

for i in range(len(prices) - 1): #사는 연도 
    for j in range(i + 1, len(prices)): #파는 연도 
        # 이익 계산
        profit =  prices[j] - prices[i]
        # 최댓값 갱신 
        if profit > max_profit :
            max_profit = profit


print(max_profit)