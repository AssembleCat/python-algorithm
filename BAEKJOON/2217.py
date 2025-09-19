N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

max_weight = 0
for i, rope in enumerate(ropes):
    max_weight = max(max_weight, (i + 1) * rope)

print(max_weight)
