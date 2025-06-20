"""
2차원 배열 회전 테크닉을 새로 알았다!!
90도 회전 = list(zip(*mat[::-1]))

mat = [
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
]

mat[::-1] = [
    [7, 8, 9]
    [4, 5, 6]
    [1, 2, 3]
]

zip은 내부에 제공한 iterabel한 객체의 같은 index끼리 묶어주는 역할을 함.
따라서 [7, 8, 9], [4, 5, 6], [1, 2, 3]의 같은 index끼리 묶어서 다시 반환함.
zip(*mat[::-1]) = [
    [7, 4, 1]
    [8, 5, 2]
    [9, 6, 3]
]

"""

import sys
import copy

n, m, k = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 실제 인덱스와 같게 스케일링
humans = [tuple(map(lambda x: int(x)-1, sys.stdin.readline().split())) for _ in range(m)]
exit_x, exit_y = map(lambda x: int(x)-1, sys.stdin.readline().split())

# 방향 벡터: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_moves = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_humans():
    global humans, total_moves
    new_humans = []
    for x, y in humans:
        moved = False
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if not in_range(nx, ny):
                continue
            if maze[nx][ny] > 0:
                continue
            if abs(exit_x - x) + abs(exit_y - y) > abs(exit_x - nx) + abs(exit_y - ny):
                new_humans.append((nx, ny))
                total_moves += 1
                moved = True
                break
        if not moved:
            new_humans.append((x, y))
    humans = [pos for pos in new_humans if pos != (exit_x, exit_y)] # 탈출구에 존재하는 사람은 제외

def find_square():
    for size in range(2, n+1):
        for x in range(n - size + 1):
            for y in range(n - size + 1):
                if not (x <= exit_x < x + size and y <= exit_y < y + size):
                    continue
                for hx, hy in humans:
                    if x <= hx < x + size and y <= hy < y + size:
                        return x, y, size
    return None

def rotate_maze(x, y, size):
    global maze, humans, exit_x, exit_y
    temp = [row[y:y+size] for row in maze[x:x+size]]
    for i in range(size):
        for j in range(size):
            if temp[i][j] > 0:
                temp[i][j] -= 1
    rotated = list(zip(*temp[::-1]))
    for i in range(size):
        for j in range(size):
            maze[x+i][y+j] = rotated[i][j]
    new_humans = []
    for hx, hy in humans:
        if x <= hx < x + size and y <= hy < y + size:
            nx = x + (hy - y)
            ny = y + size - 1 - (hx - x)
            new_humans.append((nx, ny))
        else:
            new_humans.append((hx, hy))
    humans = new_humans
    if x <= exit_x < x + size and y <= exit_y < y + size:
        ex = exit_x
        ey = exit_y
        exit_x = x + (ey - y)
        exit_y = y + size - 1 - (ex - x)

for _ in range(k):
    if not humans:
        break
    move_humans()
    square = find_square()
    if square:
        rotate_maze(*square)

print(total_moves)
print(exit_x + 1, exit_y + 1)
