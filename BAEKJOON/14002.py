N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_len = max(dp)
print(max_len)

result = []
for i in range(N - 1, -1, -1):
    if dp[i] == max_len:
        result.append(arr[i])
        max_len -= 1

result.reverse()
print(*result)
