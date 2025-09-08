from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def melting(grid):
    new_grid = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:
                water_count = 0
                for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and grid[nx][ny] == 0:
                        water_count += 1
                new_level = grid[i][j] - water_count
                if new_level < 0:
                    new_level = 0
                new_grid[i][j] = new_level
    return new_grid


def bfs(grid):
    visited = [[False for _ in range(M)] for _ in range(N)]
    all_parts = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j] > 0:
                visited[i][j] = True
                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()
                    for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                        nx, ny = x + dx, y + dy
                        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] > 0:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                all_parts += 1
    return all_parts


year = 0
while True:
    part_count = bfs(grid)
    if part_count >= 2:
        print(year)
        break
    elif part_count == 0:
        print(0)
        break
    grid = melting(grid)
    year += 1
