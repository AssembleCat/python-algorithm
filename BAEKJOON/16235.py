from collections import deque
import sys

directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
N, M, K = map(int, sys.stdin.readline().split())
input_grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
energy_grid = [[5 for _ in range(N)] for _ in range(N)]
grid = [[deque([]) for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    x, y = x - 1, y - 1
    grid[x][y].append(age)

for x in range(N):
    for y in range(N):
        if grid[x][y]:
            grid[x][y] = deque(sorted(grid[x][y]))


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def spring():
    global grid, energy_grid
    duplicate_task = []

    for x in range(N):
        for y in range(N):
            if not grid[x][y]:  # 비어있으면 스킵
                continue

            new_tree = deque([])

            while grid[x][y]:
                age = grid[x][y].popleft()

                if energy_grid[x][y] >= age:
                    energy_grid[x][y] -= age
                    new_tree.append(age + 1)
                    if (age + 1) % 5 == 0:
                        duplicate_task.append((x, y))
                else:
                    energy_grid[x][y] += age // 2
                    break

            while grid[x][y]:
                age = grid[x][y].popleft()
                energy_grid[x][y] += age // 2

            grid[x][y] = new_tree
    return duplicate_task


def autumn(task):
    for x, y in task:  # 번식대상!
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                grid[nx][ny].appendleft(1)


def winter():
    for x in range(N):
        for y in range(N):
            energy_grid[x][y] += input_grid[x][y]


def total_tree():
    total = 0
    for x in range(N):
        for y in range(N):
            if grid[x][y]:
                total += len(grid[x][y])

    return total


for _ in range(K):
    task = spring()
    autumn(task)
    winter()
print(total_tree())
