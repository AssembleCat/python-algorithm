"""
1. bfs로 같은 범위 계산 
2. 각 그룹별 조합을 연산하고 -> 조합별 조화점수 계산
3. 십자, 격자부분 회전
"""
import copy
from collections import deque

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
new_grid = [
    [0] * n 
    for _ in range(n)
    ]

group_n = 0
group_count = [0] * ((n * n) + 1)
group = [
    [-1] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    # (1) 현재칸과 가려는 칸이 같은 값을 가질때
    # (2) visited에서 아직 방문하지 않은 칸일때
    # (3) 범위를 벗어나지 않을때 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not in_range(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        if grid[x][y] == grid[nx][ny]:
            visited[nx][ny] = True
            group[nx][ny] = group_n
            group_count[group_n] += 1 
            bfs(nx, ny)

def find_part():
    global group_count, visited, group_n
    
    group_n = 0
    group_count = [0] * ((n * n) + 1)
    visited = [
        [False] * n
        for _ in range(n)
    ]   
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = True
                group[i][j] = group_n
                group_count[group_n] = 1
                bfs(i, j)      

    
def get_art_score():
    art_score = 0

    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if in_range(nx, ny) and grid[i][j] != grid[nx][ny]:
                    group_size1, group_size2 = group_count[group[i][j]], group_count[group[nx][ny]] 
                    num1, num2 = grid[i][j], grid[nx][ny]
                    art_score += (group_size1 + group_size2) * num1 * num2
    
    return art_score // 2

def get_score():
    find_part()

    return get_art_score()

def rotate_square(x, y, square_size):
    for i in range(x, x+square_size):
        for j in range(y, y+square_size):
            nx, ny = i - x, j - y
            rx, ry = ny, square_size - nx - 1
            new_grid[rx + x][ry + y] = grid[i][j]

def rotate():
    global grid, new_grid
    new_grid = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if j == n // 2:
                new_grid[j][i] = grid[i][j]
            elif i == n // 2:
                new_grid[n - j - 1][i] = grid[i][j]

    square_size = n // 2
    rotate_square(0, 0, square_size)
    rotate_square(0, square_size + 1, square_size)
    rotate_square(square_size + 1, 0, square_size)
    rotate_square(square_size + 1, square_size + 1, square_size)

    grid = copy.deepcopy(new_grid)

total_art_score = get_score()
for _ in range(3):
    rotate()

    total_art_score += get_score()

print(total_art_score)
