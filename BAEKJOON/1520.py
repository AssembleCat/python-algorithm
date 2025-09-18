import sys
sys.setrecursionlimit(100000)

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))


def in_range(x, y):
    return 0 <= x < M and 0 <= y < N


def dfs(x, y):
    if (x, y) == (M - 1, N - 1):
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] < grid[x][y]:
            ways += dfs(nx, ny)
    dp[x][y] = ways

    return dp[x][y]


print(dfs(0, 0))
