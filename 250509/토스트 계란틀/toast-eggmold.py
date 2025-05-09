"""
전역변수로 visited, egg_group을 지정하여 동작별로 공유하는 컨셉은 별로였음.
visited와 같은 동작별로 구분되는 변수들은 사용되는 시점을 엄밀히 기억하여 그때그때 생성하여 사용하는 전략으로 가자
"""
import math
from collections import deque

n, L, R = map(int, input().split())
egg_mat = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def is_target_egg(x, y, from_egg, visited):
    if not is_in_range(x, y):
        return False
    egg_diff = abs(egg_mat[x][y] - from_egg)
    return not visited[x][y] and L <= egg_diff <= R

def bfs(i, j, visited):
    bfs_q = deque()
    bfs_q.append((i, j))
    egg_group = [(i, j)]
    visited[i][j] = True

    while bfs_q:
        x, y = bfs_q.popleft()
        for _dx, _dy in zip(dx, dy):
            nx = x + _dx
            ny = y + _dy

            if is_target_egg(nx, ny, egg_mat[x][y], visited):
                bfs_q.append((nx, ny))
                egg_group.append((nx, ny))
                visited[nx][ny] = True

    return egg_group

def get_egg_avg(egg_group):
    egg_sum = sum(egg_mat[x][y] for x, y in egg_group)
    return math.floor(egg_sum / len(egg_group))

def mix_egg(egg_group):
    egg_avg = get_egg_avg(egg_group)
    for x, y in egg_group:
        egg_mat[x][y] = egg_avg

def move_egg():
    visited = [[False for _ in range(n)] for _ in range(n)]
    is_mixed = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                egg_group = bfs(i, j, visited)
                if len(egg_group) > 1:
                    mix_egg(egg_group)
                    is_mixed = True
    return is_mixed

egg_move_count = 0
while True:
    if not move_egg():
        break
    egg_move_count += 1

print(egg_move_count)
