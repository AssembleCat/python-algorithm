import heapq as hq

INF = 2 ** 31 - 1


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


case = 0
while True:
    case += 1
    N = int(input())

    if N == 0:
        break

    lost = [[INF] * N for _ in range(N)]
    grid = [list(map(int, input().split())) for _ in range(N)]
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    q = [(grid[0][0], 0, 0)]  # lost, x, y
    hq.heapify(q)

    while q:
        curr_lost, x, y = hq.heappop(q)
        if lost[x][y] > curr_lost:
            lost[x][y] = curr_lost

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    hq.heappush(q, (curr_lost + grid[nx][ny], nx, ny))

    print(f"Problem {case}: {lost[N - 1][N - 1]}")
