import sys

N, M = map(int, input().split())
seq = list(map(int, input().split()))

count = 0
end = 0
interval_sum = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += seq[end]
        end += 1

    if interval_sum == M:
        count += 1

    interval_sum -= seq[start]

print(count)