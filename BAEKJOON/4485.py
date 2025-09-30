for case in range(1, 4):
    N = int(input())
    minimum_lost = 2 ** 31 - 1
    visited = [[False] * N for _ in range(N)]
    grid = [list(map(int, input().split())) for _ in range(N)]
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))


    def in_range(x, y):
        return 0 <= x < N and 0 <= y < N


    def dfs(x, y, curr_lost):
        global minimum_lost
        if curr_lost > minimum_lost:
            return

        if (x, y) == (N - 1, N - 1):
            if curr_lost < minimum_lost:
                minimum_lost = curr_lost
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, curr_lost + grid[nx][ny])
                visited[nx][ny] = False


    visited[0][0] = True
    dfs(0, 0, grid[0][0])

    print(f"Problem {case}: {minimum_lost}")
