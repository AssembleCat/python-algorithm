"""
명령 1: Go k 현재 방향으로 k칸 이동 1~3칸
명령 2: Turn dir(left, right) 90도 회전함

grid에 0은 이동가능, 1은 이동 불가능

현재 지점에서 목적지까지 몇번의 이동/회전 명령이 있어야하는지 최소명령수를 구하기
"""
from collections import deque

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
new_dir = {
    0: (2, 3),
    1: (2, 3),
    2: (0, 1),
    3: (0, 1)
}
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
sx, sy, sd = [int(x) - 1 for x in input().split()]
ex, ey, ed = [int(x) - 1 for x in input().split()]
result = 0


def in_range(x, y):
    return 0 <= x < M and 0 <= y < N


visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]
q = deque([(sx, sy, sd, 0)])
while q:
    x, y, d, cost = q.popleft()

    # 도착하면 출력
    if (x, y, d) == (ex, ey, ed):
        result = cost
        break

    # 1~3칸 이동
    dx, dy = directions[d]
    for i in range(1, 4):
        nx, ny = x + (dx * i), y + (dy * i)
        if not in_range(nx, ny) or grid[nx][ny] == 1:
            break
        if not visited[nx][ny][d]:
            visited[nx][ny][d] = True
            q.append((nx, ny, d, cost + 1))
    # 좌/우 회전
    for nd in new_dir[d]:
        if not visited[x][y][nd]:
            visited[x][y][nd] = True
            q.append((x, y, nd, cost + 1))

print(result)
