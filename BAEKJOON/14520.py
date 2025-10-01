"""
N*M 직사각형

0 / 1 / 2
빈칸 / 벽 / 바이러스

- 벽을 3개 세웠을때 만들 수 있는 최대의 안전영역
- 3개의 벽을 세울 케이스 -> 빈칸 전체를 대상으로?
- 벽 3개의 위치를 입력받아 2부터 BFS
- 0 카운트
"""
from itertools import combinations
from collections import deque

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

empty_cells = []
for x in range(N):
    for y in range(M):
        if grid[x][y] == 0:
            empty_cells.append((x, y))


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def bfs(temp_grid, virus_q):
    while virus_q:
        cx, cy = virus_q.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if in_range(nx, ny) and temp_grid[nx][ny] == 0:
                temp_grid[nx][ny] = 2  # 바이러스 확산
                virus_q.append((nx, ny))


def count_safe_area(grid):
    # 안전 영역 크기 계산
    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                count += 1
    return count


maximum_empty = 0
walls_combo = combinations(empty_cells, 3)

for combo in walls_combo:
    temp_grid = [row[:] for row in grid]

    for wx, wy in combo:
        temp_grid[wx][wy] = 1

    virus_q = deque()
    for i in range(N):
        for j in range(M):
            if temp_grid[i][j] == 2:
                virus_q.append((i, j))

    bfs(temp_grid, virus_q)

    safe_count = count_safe_area(temp_grid)
    maximum_empty = max(maximum_empty, safe_count)

print(maximum_empty)
