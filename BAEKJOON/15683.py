directions = ([-1, 0], [1, 0], [0, -1], [0, 1])  # 상 하 좌 우
num_dir = (
    [],  # 0번 없음.
    [[0], [1], [2], [3]],  # 1번
    [[0, 1], [2, 3]],  # 2번
    [[0, 3], [3, 1], [1, 2], [2, 0]],  # 3번
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],  # 4번
    [[0, 1, 2, 3]]  # 5번
)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cctvs = []
min_blind_space = 2 ** 31 - 1
for x in range(N):
    for y in range(M):
        if 0 < grid[x][y] < 6:
            cctvs.append((x, y, grid[x][y]))  # (x, y, cctv 종류)


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def simulate(cctv, cctv_directions, curr_grid):
    global min_blind_space
    change_log = []
    for c, cd in zip(cctv, cctv_directions):  # (x, y, cctv종류), cctv 방향
        x, y, cctv_num = c

        for d in num_dir[cctv_num][cd]:
            dx, dy = directions[d]
            for i in range(1, 10):
                nx, ny = x + (dx * i), y + (dy * i)
                if not in_range(nx, ny) or grid[nx][ny] == 6:
                    break
                if curr_grid[nx][ny] == 0:
                    curr_grid[nx][ny] = -1
                    change_log.append((nx, ny))

    blind_space = count_blind(curr_grid)
    if blind_space < min_blind_space:
        min_blind_space = blind_space

    return change_log


def count_blind(curr_grid):
    blind_space = 0
    for x in range(N):
        for y in range(M):
            if curr_grid[x][y] == 0:
                blind_space += 1

    return blind_space


def restore_grid(curr_grid, log):
    for x, y in log:
        curr_grid[x][y] = 0


def main(cctv):
    def combo(cctv_directions, idx):
        global grid
        if len(cctv_directions) == len(cctv):
            change_log = simulate(cctv, cctv_directions, grid)
            restore_grid(grid, change_log)
            return

        curr_cctv_num = cctv[idx][2]  # cctv 번호
        for i in range(len(num_dir[curr_cctv_num])):
            cctv_directions.append(i)
            combo(cctv_directions, idx + 1)
            cctv_directions.pop(-1)

    combo([], 0)


main(cctvs)
print(min_blind_space)
