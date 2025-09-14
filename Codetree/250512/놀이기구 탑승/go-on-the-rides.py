"""
학생이 위치할 칸을 찾는 함수
"""
n = int(input())
friend_map, seq = {}, []
for _ in range(n * n):
    request = list(map(int, input().split()))
    friend_map[request[0]] = request[1:]
    seq.append(request[0])
grid  = [[0 for _ in range(n)] for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n

def friend_and_empty(student, x, y):
    global friend_map
    friend_count, empty_count = 0, 0
    my_friend = friend_map[student]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not can_go(nx, ny):
            continue
        if grid[nx][ny] in my_friend:
            friend_count += 1
        elif grid[nx][ny] == 0:
            empty_count += 1
    return (friend_count, empty_count)

def find_spot(student):
    # 먼저 칸이 비어있는지 확인
    # 0. 4방향으로 좋아하는 친구가 몇명이 있는지 기록
    # 1. 4방향으로 비어있는 칸이 몇개나 있는지 기록
    # 2. 행번호
    # 3. 열번호
    target_spot = []
    for i in range(n):
        for j in range(n):
            # 칸이 비어있지않으면 스킵
            if grid[i][j]:
                continue
            
            friend, empty = friend_and_empty(student, i, j)
            curr_spot = (friend, empty, i, j)
            target_spot.append(curr_spot)
    target_spot.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    return target_spot[0]

def calculate():
    score = 0
    for i in range(n):
        for j in range(n):
            student = grid[i][j]
            my_friend = friend_map[student]
            friend_count = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if not can_go(nx, ny):
                    continue
                if grid[nx][ny] in my_friend:
                    friend_count += 1
            
            if friend_count == 0:
                score += 0
            elif friend_count == 1:
                score += 1
            else:
                score += 10 ** (friend_count - 1)
    return score

for student in seq:
    _, _, x, y = find_spot(student)            
    grid[x][y] = student

print(calculate())