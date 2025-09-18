"""
조건을 명확히 보고 구현도 잘햇음! 특히 eat_fish로 동작을 구분하고 BFS과정도 잘했지만 아기상어의 크기가 9이상이 될
가능성을 배제했음. 물고기가 1~6사이니까 해당 범위만 잡아먹었어야했는데 아기상어 크기가 9이상이 될때 본인을 먹는다고 판단하여
본인자리를 결과에 포함시켜버려서 경로가 아예없는 결과가 포함됐음.
"""

from collections import deque


def find_fish(grid):
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 9:
                return x, y


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


directions = ((-1, 0), (0, -1), (0, 1), (1, 0))  # 북서동남
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
fish_size, grown_count = 2, 0
fx, fy = find_fish(grid)


def eat_fish(fish_size, grown_count):
    grown_count += 1
    if grown_count == fish_size:
        fish_size += 1
        grown_count = 0
    return fish_size, grown_count


def find_target(x, y, grid, fish_size):
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    all_path, min_dist = [], 2 ** 31 - 1
    q = deque([(x, y, [])])

    while q:
        x, y, curr_path = q.popleft()

        if len(curr_path) > min_dist:
            continue

        if grid[x][y] < fish_size and grid[x][y] != 0 and grid[x][y] != 9:
            if len(curr_path) < min_dist:
                all_path = [curr_path[-1]]
                min_dist = len(curr_path)
            elif len(curr_path) == min_dist:
                all_path.append(curr_path[-1])

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] <= fish_size and not visited[nx][ny]:
                visited[nx][ny] = True
                new_path = curr_path[:]
                new_path.append((nx, ny))
                q.append((nx, ny, new_path))

    if not all_path:
        return None, 0

    # x큰, y큰
    all_path.sort()

    return all_path[0], min_dist


time = 0
while True:
    target, dist = find_target(fx, fy, grid, fish_size)
    if not target:
        break
    time += dist
    fish_size, grown_count = eat_fish(fish_size, grown_count)
    grid[fx][fy] = 0
    fx, fy = target
    grid[fx][fy] = 9

print(time)
