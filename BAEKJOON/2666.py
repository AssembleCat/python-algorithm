INF = 2 ** 31 - 1

N = int(input())
door1, door2 = map(int, input().split())
orders = []
M = int(input())
for _ in range(M):
    orders.append(int(input()))

dp = [[[INF] * (N + 1) for _ in range(N + 1)] for _ in range(M + 1)]
dp[0][min(door1, door2)][max(door1, door2)] = 0

for k in range(M):
    target = orders[k]
    for d1 in range(1, N + 1):
        for d2 in range(d1 + 1, N + 1):
            if dp[k][d1][d2] == INF:  # 도달하지않은 정보에서는 문을 움직일 수 없음.
                continue

            # door1을 움직이는 경우
            cost = abs(target - d1)
            new_d1, new_d2 = min(target, d2), max(target, d2)
            dp[k + 1][new_d1][new_d2] = min(dp[k + 1][new_d1][new_d2], dp[k][d1][d2] + cost)

            # door2를 움직이는 경우
            cost = abs(target - d2)
            new_d1, new_d2 = min(target, d1), max(target, d1)
            dp[k + 1][new_d1][new_d2] = min(dp[k + 1][new_d1][new_d2], dp[k][d1][d2] + cost)

# 결과는 M에서 최댓값
min_move = INF
for d1 in range(1, N + 1):
    for d2 in range(d1 + 1, N + 1):
        min_move = min(min_move, dp[M][d1][d2])
print(min_move)
