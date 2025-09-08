N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
low, high = 0, max(el for row in grid for el in row)


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(grid, level):
    visited = [[False for _ in range(N)] for _ in range(N)]
    safe_groups = []

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > level:
                visited[i][j] = True
                q = [(i, j)]
                curr_safe_group = [(i, j)]

                while q:
                    x, y = q.pop(0)
                    for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                        nx, ny = x + dx, y + dy
                        if not in_range(nx, ny):
                            continue
                        if not visited[nx][ny] and grid[nx][ny] > level:
                            visited[nx][ny] = True
                            curr_safe_group.append([nx, ny])
                            q.append((nx, ny))
                safe_groups.append(curr_safe_group)

    return len(safe_groups)


max_safe_zone = 0
for level in range(low, high):
    curr_safe_zone = bfs(grid, level)
    if curr_safe_zone > max_safe_zone:
        max_safe_zone = curr_safe_zone

print(max_safe_zone)