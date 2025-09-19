"""
1. 각 단계별로 증가하는 기준이 어떻게 되는지 명확하게 이해하자,
2. vip좌석단위로 경우의 수가 곱해지는 것은 정확했음.
3. 증가하는 기준이 피보나치인건 스스로 알지못함. DP숙련도가 떨어지는 증거다!
4. DP에 피보나치 정보를 저장해두고 그 사이의 인원수만큼 곱한것은 아이디어가 좋았음.
"""

N = int(input())
M = int(input())
dp = [0] * 41
dp[0], dp[1] = 1, 1

for i in range(2, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
vips = [0]
for _ in range(M):
    vips.append(int(input()))
vips.append(N + 1)

for i in range(1, len(vips)):
    result *= dp[vips[i] - vips[i - 1] - 1]

print(result)
