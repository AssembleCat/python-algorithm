"""
1. 먼지 확산 함수
    - 돌풍, 벽으로는 확산되지않음.
    - 새로운 Grid를 작성해서 해당 Grid에 순차적으로 적용
    - 기존 Grid에 New Grid 덮어씌우기
2. 반시계, 시계 방향 이동 함수
    - 
"""
import math

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and grid[x][y] != -1

def spread_dust():
    global grid
    new_grid = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == -1:
                new_grid[i][j] = -1

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            valid_grid = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if can_go(nx, ny) and grid[i][j] != -1:   
                    valid_grid += 1
            # 확산될 먼지량
            avg_dust = math.floor(grid[i][j] / 5)
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if can_go(nx, ny) and grid[i][j] != -1:   
                    new_grid[nx][ny] += avg_dust
            if grid[i][j] != -1:
                new_grid[i][j] += grid[i][j] - (valid_grid * avg_dust)
            #print(f"좌표: ({i}, {j}), 확산대상 {valid_grid}칸, 확산먼지량 {avg_dust}")
    grid = new_grid

def find_starting_point():
    point = [
        i
        for i in range(n)
        for j in range(m)
        if grid[i][j] == -1
    ]
    return point

def cleaning():
    global grid
    top_x, bottom_x = find_starting_point()

    top_dust_idx, top_dust_value = [], []
    bottom_dust_idx, bottom_dust_value = [], []
    
    for y in range(1, m): # 윗칸 아랫면
        top_dust_idx.append((top_x, y))
    for x in range(top_x - 1, 0, -1): # 윗칸 오른쪽면
        top_dust_idx.append((x, m-1))
    for y in range(m-1, 0, -1): # 윗칸 윗면
        top_dust_idx.append((0, y)) 
    for x in range(0, top_x): # 윗칸 왼쪽면
        top_dust_idx.append((x, 0))
    for x, y in top_dust_idx: # 좌표의 실제 값을 확보
        top_dust_value.append(grid[x][y])

    for y in range(1, m): # 아랫칸 윗면
        bottom_dust_idx.append((bottom_x, y))
    for x in range(bottom_x + 1, n): # 아랫칸 오른쪽면
        bottom_dust_idx.append((x, m-1))
    for y in range(m-2, 0, -1): # 아랫칸 아랫면
        bottom_dust_idx.append((n-1, y))
    for x in range(n-1, bottom_x, -1): # 아랫칸 왼쪽면
        bottom_dust_idx.append((x, 0))
    for x, y in bottom_dust_idx:
        bottom_dust_value.append(grid[x][y])

    top_dust_value = [0] + top_dust_value[:len(top_dust_value) - 1]
    bottom_dust_value = [0] + bottom_dust_value[:len(bottom_dust_value) - 1]

    #print(top_dust_idx)  
    #print(top_dust_value)
    #print(bottom_dust_idx)
    #print(bottom_dust_value)

    for idx, dust in zip(top_dust_idx, top_dust_value):
        x, y = idx
        grid[x][y] = dust
    for idx, dust in zip(bottom_dust_idx, bottom_dust_value):
        x, y = idx
        grid[x][y] = dust

for _ in range(t):
    spread_dust()
    cleaning()

#print(grid)

total = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] != -1:
            total += grid[i][j]
print(total)