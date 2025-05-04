import math

n = int(input())
m = int(input())
spot = list(map(int, input().split()))
space = []

for i in range(len(spot) - 1):
    space.append(math.ceil((spot[i + 1] - spot[i])/2))

space.append(spot[0] - 0)
space.append(n - spot[-1])

print(max(space))
