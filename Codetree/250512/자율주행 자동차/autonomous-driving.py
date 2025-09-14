n, m = tuple(map(int, input().split()))
curr_x, curr_y, curr_dir = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]


def can_go(x, y):
    # grid가 도로(0)이고 아직 방문하지 않은 칸
    return not grid[x][y] and not visited[x][y]


def simulations():
    global curr_x, curr_y, curr_dir
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[curr_x][curr_y] = True

    # 1. 4 방향중 갈 수 있는 칸이 있다면 전진
    for _ in range(4):
        left_dir = (curr_dir + 3) % 4
        nx = curr_x + dx[left_dir]
        ny = curr_y + dy[left_dir]

        if can_go(nx, ny):
            curr_x, curr_y = nx, ny
            curr_dir = left_dir
            return True
        else:
            curr_dir = left_dir

    # 2. 갈 수 있는 방향이 없다면 후진
    back_dir = (curr_dir + 2) % 4
    back_x = curr_x + dx[back_dir]
    back_y = curr_y + dy[back_dir]

    # 3. 후진할 수 있으면 가 (grid값이 0 인경우는 갈 수 있음!)
    if not grid[back_x][back_y]:
        curr_x, curr_y = back_x, back_y
        return True
    # 4. 후진도 못하면 종료
    else:
        return False


while True:
    moved = simulations()

    if not moved:
        break
    
count = sum([
    1
    for i in range(n)
    for j in range(m)
    if visited[i][j] == True
    ])
print(count)
    
