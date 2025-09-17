M, K, N = map(int, input().split())
grid = [[False] * M for _ in range(N)]
result = -1

# y, y+1 줄을 x위치에서 연결한다는 뜻
for _ in range(K):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    grid[x][y] = True


def check():
    for i in range(M):
        col = i
        for row in range(N):
            if col < M - 1 and grid[row][col]:
                col += 1
            elif col > 0 and grid[row][col - 1]:
                col -= 1

        if col != i:
            return False

    return True


def simulate(target_line, curr_line, curr_row):
    global result

    if target_line == curr_line:
        return check()

    for x in range(curr_row, N):
        for y in range(M - 1):
            if (y == 0 and not grid[x][y] and not grid[x][y + 1]) or (y == M - 1 and not grid[x][y - 1]) or (
                    not grid[x][y] and not grid[x][y] and not grid[x][y]):
                grid[x][y] = True

                if simulate(target_line, curr_line + 1, x):
                    return True

                grid[x][y] = False

    return False


for i in range(4):
    if i == 0:
        if check():
            result = 0
            break
    else:
        if simulate(i, 0, 0):
            result = i
            break

print(result)
