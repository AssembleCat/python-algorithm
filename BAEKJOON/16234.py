from collections import deque

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))  # 동서남북
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def target_population_diff(a, b):
    diff = abs(a - b)
    return L <= diff <= R


def union():
    global grid
    all_groups = []
    is_moved = False

    # 연결된 연합들 연산
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                curr_group = [(i, j)]
                population = grid[i][j]

                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()

                    for d, (dx, dy) in enumerate(directions):
                        nx, ny = x + dx, y + dy
                        if in_range(nx, ny) and target_population_diff(grid[x][y], grid[nx][ny]) and not visited[nx][ny]:
                            is_moved = True
                            visited[nx][ny] = True
                            curr_group.append((nx, ny))
                            population += grid[nx][ny]
                            q.append((nx, ny))

                all_groups.append((curr_group, population))

    if not is_moved:
        return False

    for group, population in all_groups:
        for x, y in group:
            grid[x][y] = population // len(group)

    return True


turn = 0
while True:
    is_moved = union()
    if not is_moved:
        break
    turn += 1

print(turn)
