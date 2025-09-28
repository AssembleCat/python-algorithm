"""
수빈 - N, 동생 - K

수빈이 겉거나 순간이동,
- 이동: 1초 후에 X-1 or X+1
- 순간이동: 0초만에 2*X

N에서 3가지 방법이 있음.
- N-1, N+1, N*2
- 3가지를 순서대로 큐에 집어넣고 dp[위치] = 시간 형식으로 저장
"""
from collections import deque

infinite = 2 ** 31 - 1
N, K = map(int, input().split())

dp = [infinite] * 100001
dp[N] = 0

q = deque([(N * 2, 0), (N - 1, 1), (N + 1, 1)])
while q:
    target, time = q.popleft()

    if target < 0 or target > 100000:
        continue

    if dp[target] > time:
        dp[target] = time

        q.append((target * 2, time))
        q.append((target - 1, time + 1))
        q.append((target + 1, time + 1))

print(dp[K])
