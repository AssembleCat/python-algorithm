from collections import deque

R, C, K = map(int, input().split())
room_map = [list(map(int, input().split())) for _ in range(R)]
W = int(input())

walls = set()
for _ in range(W):
    x, y, t = map(int, input().split())
    r, c = x - 1, y - 1
    if t == 0:
        wall = ((r - 1, c), (r, c))
    else:
        wall = ((r, c), (r, c + 1))
    walls.add(wall)

heaters = []
check_locations = []
for r in range(R):
    for c in range(C):
        if 1 <= room_map[r][c] <= 4:
            heaters.append((r, c, room_map[r][c]))
        elif room_map[r][c] == 5:
            check_locations.append((r, c))

temp_map = [[0] * C for _ in range(R)]
chocolate = 0

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]


def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C


def has_wall(r1, c1, r2, c2):
    if (r1, c1) > (r2, c2):
        r1, c1, r2, c2 = r2, c2, r1, c1
    return ((r1, c1), (r2, c2)) in walls


def spread_wind():
    temp_increase = [[0] * C for _ in range(R)]
    for hr, hc, d in heaters:
        start_r, start_c = hr + dr[d], hc + dc[d]
        if not is_valid(start_r, start_c):
            continue

        q = deque([(start_r, start_c, 5)])
        visited = set([(start_r, start_c)])
        temp_increase[start_r][start_c] += 5

        while q:
            r, c, temp = q.popleft()
            if temp == 1:
                continue

            nr, nc = r + dr[d], c + dc[d]
            if is_valid(nr, nc) and not has_wall(r, c, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                temp_increase[nr][nc] += temp - 1
                q.append((nr, nc, temp - 1))

            if d <= 2:
                nr1, nc1 = r - 1, c + dc[d]
                if is_valid(nr1, nc1) and not has_wall(r, c, r - 1, c) and not has_wall(r - 1, c, nr1, nc1) and (nr1, nc1) not in visited:
                    visited.add((nr1, nc1))
                    temp_increase[nr1][nc1] += temp - 1
                    q.append((nr1, nc1, temp - 1))

                nr2, nc2 = r + 1, c + dc[d]
                if is_valid(nr2, nc2) and not has_wall(r, c, r + 1, c) and not has_wall(r + 1, c, nr2, nc2) and (nr2, nc2) not in visited:
                    visited.add((nr2, nc2))
                    temp_increase[nr2][nc2] += temp - 1
                    q.append((nr2, nc2, temp - 1))
            else:
                nr1, nc1 = r + dr[d], c - 1
                if is_valid(nr1, nc1) and not has_wall(r, c, r, c - 1) and not has_wall(r, c - 1, nr1, nc1) and (nr1, nc1) not in visited:
                    visited.add((nr1, nc1))
                    temp_increase[nr1][nc1] += temp - 1
                    q.append((nr1, nc1, temp - 1))

                nr2, nc2 = r + dr[d], c + 1
                if is_valid(nr2, nc2) and not has_wall(r, c, r, c + 1) and not has_wall(r, c + 1, nr2, nc2) and (nr2, nc2) not in visited:
                    visited.add((nr2, nc2))
                    temp_increase[nr2][nc2] += temp - 1
                    q.append((nr2, nc2, temp - 1))

    for r in range(R):
        for c in range(C):
            temp_map[r][c] += temp_increase[r][c]


def regulate_temperature():
    delta = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if c + 1 < C and not has_wall(r, c, r, c + 1):
                diff = abs(temp_map[r][c] - temp_map[r][c + 1]) // 4
                if temp_map[r][c] > temp_map[r][c + 1]:
                    delta[r][c] -= diff
                    delta[r][c + 1] += diff
                else:
                    delta[r][c] += diff
                    delta[r][c + 1] -= diff

            if r + 1 < R and not has_wall(r, c, r + 1, c):
                diff = abs(temp_map[r][c] - temp_map[r + 1][c]) // 4
                if temp_map[r][c] > temp_map[r + 1][c]:
                    delta[r][c] -= diff
                    delta[r + 1][c] += diff
                else:
                    delta[r][c] += diff
                    delta[r + 1][c] -= diff

    for r in range(R):
        for c in range(C):
            temp_map[r][c] += delta[r][c]


def decrease_outer_temperature():
    for c in range(C):
        if temp_map[0][c] > 0:
            temp_map[0][c] -= 1
        if temp_map[R - 1][c] > 0:
            temp_map[R - 1][c] -= 1

    for r in range(1, R - 1):
        if temp_map[r][0] > 0:
            temp_map[r][0] -= 1
        if temp_map[r][C - 1] > 0:
            temp_map[r][C - 1] -= 1


def check_temperature():
    for r, c in check_locations:
        if temp_map[r][c] < K:
            return False
    return True


while chocolate <= 100:
    spread_wind()
    regulate_temperature()
    decrease_outer_temperature()
    chocolate += 1
    if check_temperature():
        print(chocolate)
        break
else:
    print(101)