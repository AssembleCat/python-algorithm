a = input()
b = input()

row = len(a) + 1
col = len(b) + 1
dp = [[0] * col for _ in range(row)]

for i in range(1, row):
    for j in range(1, col):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

#for row in dp:
#    print(*row)

print(max(max(row) for row in dp))
