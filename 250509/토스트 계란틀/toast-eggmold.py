"""
BFS로 현재 계란으로부터 합칠 대상의 계란범위를 구할 수 있음.
이번 단계에서 계란이동이 발생한 경우에 대해서 기록하는 Matrix가 필요함.
"""
import math
from collections import deque

n, L, R = map(int, input().split())
egg_mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
egg_group = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
bfs_q = deque()


def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def is_target_egg(x, y, from_egg):
    if not is_in_range(x, y):
        return False
    
    egg_diff = abs(egg_mat[x][y] - from_egg)
    
    return not visited[x][y] and L <= egg_diff <= R

def bfs():
    while bfs_q:
        x, y = bfs_q.popleft()

        for _dx, _dy in zip(dx, dy):
            nx = x + _dx
            ny = y + _dy
            
            if is_target_egg(nx, ny, egg_mat[x][y]):
                bfs_q.append((nx, ny))
                egg_group.append((nx, ny))
                visited[nx][ny] = True

def get_egg_avg(egg_group):
    egg_sum = 0
    for x, y in egg_group:
        egg_sum += egg_mat[x][y]
    
    return math.floor(egg_sum / len(egg_group))

def mix_egg(egg_group):
    egg_avg = get_egg_avg(egg_group)
    for x, y in egg_group:
        egg_mat[x][y] = egg_avg

def move_egg():
    global egg_group
    visited = [[False for _ in range(n)] for _ in range(n)]
    is_mixed = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                egg_group = []

                bfs_q.append((i, j))
                visited[i][j] = True

                bfs()

                if len(egg_group) > 1:
                    mix_egg(egg_group)
                    is_mixed = True
    return is_mixed
    
egg_move_count = 0
while True: 
    step_mixed = move_egg()
    if not step_mixed:
        break
    egg_move_count += 1


print(egg_move_count)