from collections import defaultdict

n, m, k = map(int, input().split())
# x, y - 위치, s - 거리, d - 이동 방향, b - 크기  
dusts = [list(map(int, input().split())) for _ in range(k)]
total_collect = 0

for idx, dust in enumerate(dusts):
    x, y, s, d, b = dust
    dusts[idx] = [x-1, y-1, s, d-1, b]

# 열별로 탐색 
def collect(j):
    global dusts, total_collect
    # j - 검사 대상 열

    dusts.sort(lambda x: (x[1], x[0])) 
    for i in range(n):
        for dust in dusts:
            x, y, _, _, b = dust
            if (i, j) == (x, y):
                #print(f"find {i, j} collect {b}")
                total_collect += b
                dusts.remove(dust)
                return

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def cover_range(x, y, direction, speed):
    # speed를 연산에 포함시켜야함
    # 벽에 1번 튀기는게 아니라 10,000같이 말도안되는 속도가 존재할 수 있음.
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1] # 상 하 우 좌

    for _ in range(speed):
        nx, ny = x + dx[direction], y + dy[direction]
        if in_range(nx, ny):
            x, y = nx, ny
        else:
            x, y = x - dx[direction], y - dy[direction]
            if direction % 2 == 0:
                direction += 1
            else:
                direction -= 1
    return x, y, direction

# 공팡이 이동
def move():
    for idx, dust in enumerate(dusts):
        
        x, y, s, d, b = dust
        nx, ny, nd = cover_range(x, y, d, s)
        #print(f"dust({x, y} move to {nx, ny})")
        dusts[idx] = (nx, ny, s, nd, b)

# 이동 후 충돌 구현      
def check_collision():
    global dusts
    new_dusts_map = defaultdict(list)
    for dust in dusts:
        x, y, _, _, _ = dust
        new_dusts_map[(x, y)].append(dust)
    
    new_dusts = []
    for cell_dusts in new_dusts_map.values():
        #if len(cell_dusts) > 1:
            #print(f"곰팡이 포식 발생({cell_dusts})")
        cell_dusts.sort(lambda x: -x[4]) # 크기를 역순으로 정렬 
        new_dusts.append(cell_dusts[0])
    
    dusts = new_dusts                                
    
for i in range(m):
    collect(i)
    move()
    check_collision()

print(total_collect)