n, m, k = map(int, input().split())
# x, y - 위치, s - 거리, d - 이동 방향, b - 크기  
dusts = [list(map(int, input().split())) for _ in range(k)]
dusts.sort(lambda x: (x[1], x[0])) # 열 순으로 정렬 
total_collect = 0

for idx, dust in enumerate(dusts):
    x, y, s, d, b = dust
    dusts[idx] = [x-1, y-1, s, d-1, b]

print(dusts)

# 열별로 탐색 
def collect(j):
    global total_collect
    # j - 검사 대상 열
    for i in range(n):
        for dust in dusts:
            x, y, _, _, b = dust
            if (i, j) == (x, y):
                print(f"find {i, j} collect {b}")
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
    return x, y

# 공팡이 이동
def move():
    print(dusts)
    for idx, dust in enumerate(dusts):
        
        x, y, s, d, b = dust
        nx, ny = cover_range(x, y, d, s)
        print(f"dust({x, y} move to {nx, ny})")
        dusts[idx] = (nx, ny, s, d, b)

# 이동 후 충돌 구현      
def check_collision():
    for i in range(n):
        for j in range(m):
            curr_dust = []
            for dust in dusts:
                x, y, 
    
for i in range(m):
    collect(i)
    move()