"""
세로 - x값(아래가 증가)
가로 - y값(오른쪽이 증가)

오, 위, 왼, 하
"""
directions = ((0, 1), (-1, 0), (0, -1), (1, 0))

n = int(input())
curves = []
for _ in range(n):
    curves.append(list(map(int, input().split())))
grid = [[False] * 101 for _ in range(101)]

for curve in curves:
    x, y, d, g = curve
    lines = [d]

    for i in range(1, g + 1):
        for last_d in reversed(lines):
            lines.append((last_d + 1) % 4)

    grid[x][y] = True
    for line in lines:
        dx, dy = directions[line]
        x, y = x + dx, y + dy
        # print(f"{line} / {x, y}")
        grid[x][y] = True

count = 0
for x in range(101):
    for y in range(101):
        if grid[x][y] and grid[x + 1][y] and grid[x][y + 1] and grid[x + 1][y + 1]:
            count += 1

print(count)

