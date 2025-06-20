n, m, h, k = map(int, input().split())

finder = (n // 2, n // 2)

runners = [
    list(map(int, input().split()))
    for _ in range(m)
]
for idx, runner in enumerate(runners):
    x, y, d = runner
    if d == 1:
        runners[idx] = [x-1, y-1, d, 1]
    else: 
        runners[idx] = [x-1, y-1, d, 2]

trees = [
    [False] * n
    for _ in range(n)
]
for _ in range(h):
    x, y = tuple(map(int, input().split()))
    trees[x-1][y-1] = True

is_foward = True
foward, backward = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 상우하좌
def generate_path():
    # 각 칸마다 방향을 계산 
    move_count, move_dir = 1, 0
    x, y = n // 2, n // 2

    while True:
        for i in range(move_count):
            foward[x][y] = move_dir
            x, y = x + dx[move_dir], y + dy[move_dir]
            backward[x][y] = (move_dir + 2) % 4
            
            if not x and not y:
                return

        move_dir = (move_dir + 1) % 4

        if move_dir % 2 == 0:
            move_count += 1   

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def distance_to_finder(x, y):
    return abs(finder[0] - x) + abs(finder[1] - y)

def move_runner():
    # 도망자의 움직임을 구현
    # 술래로부터 3칸내의 도망자만 움직임.
    # d가 1이면 좌우, 2면 상하로 움직임.
    # 범위를 벗어나는 경우 방향을 180도 변경
    # 도달하는 칸에 술래가 있다면 움직이지않음.
    for idx, runner in enumerate(runners):
        x, y, d, dir = runner
        if distance_to_finder(x, y) > 3: # 거리가 3칸 초과면 움직이지않음
            continue
        
        nx, ny = x + dx[dir], y + dy[dir]
        if not in_range(nx, ny):
            dir = (dir + 2) % 4
            nx, ny = x + dx[dir], y + dy[dir]

        if (nx, ny) == finder:
            continue

        runners[idx] = [nx, ny, d, dir]       

def move_finder():
    # 정해진 경로로만 주행함.
    # 정주행, 역주행이 정해져있음
    global is_foward, finder

    x, y = finder
    dir, nx, ny = -1, -1, -1

    if is_foward:
        dir = foward[x][y]
    else:
        dir = backward[x][y]

    nx, ny = x + dx[dir], y + dy[dir]
    finder = (nx, ny)

    if (nx, ny) == (0, 0):
            is_foward = False
    elif (nx, ny) == (n // 2, n // 2):
            is_foward = True

def check_runners(turn):
    # 현재 위치, 방향을 이용해 3칸 이내의 도망자를 삭제 시킴 
    # 턴수 * 답은 도망자 수 = 점수 계산도 진행 
    global is_foward, finder, trees, runners

    x, y = finder
    dir = None
    if is_foward:
        dir = foward[x][y]
    else:
        dir = backward[x][y]
    
    catched_runner = []
    for i in range(3):
        # 나무 있으면 어차피 계산 못함 예외
        # 범위넘어가면 안됨 
        nx, ny = x + dx[dir] * i, y + dy[dir] * i   
        
        if not in_range(nx, ny):
            continue
        if trees[nx][ny]:
            continue
        
        for runner in runners:
            rx, ry, _, _ = runner
            if (nx, ny) == (rx, ry):
                catched_runner.append(runner)
    
    runners = [r for r in runners if r not in catched_runner]
    return turn * len(catched_runner)

generate_path()
point = 0
for i in range(k):
    # 도망자 움직임
    move_runner()
    # 술래 움직임 
    move_finder()
    # 잡히는지 검사 
    point += check_runners(i+1)

print(point)
