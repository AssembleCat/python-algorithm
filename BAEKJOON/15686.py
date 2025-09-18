"""
치킨 거리 - 집과 가장 가까운 치킨 집 거리
도시의 치킨 거리 - 모든집의 치킨거리의 합

0 빈칸, 1 집, 2 치킨

현재 치킨집 중 M개를 선택하여 도시의 치킨 거리가 가장 작은 케이스를 찾아라

1. 치킨집 위치를 담은 list확보, 이 중 M개를 선택하는 백트래킹 작성
2. 치킨집 list(set으로 넘기는게 검사 효율이 좋을듯)를 보고 각 집에서 BFS
3. 현재 구조에서 도시의 치킨거리 반환
"""
from collections import deque


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def distance(x, y, ex, ey):
    return abs(x - ex) + abs(y - ey)


def get_list(grid):
    chicken, house = [], []
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 2:
                chicken.append((x, y))
                grid[x][y] = 0
            elif grid[x][y] == 1:
                house.append((x, y))
    return chicken, house


directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
chicken_list, house_list = get_list(grid)


def check(min_dist, chickens):
    global grid, house_list

    chicken_dist = 0
    for house in house_list:
        x, y = house
        min_dist = min([distance(x, y, cx, cy) for cx, cy in chickens])
        chicken_dist += min_dist

    return chicken_dist


def simulate(chicken_list):
    global grid
    min_dist = 2 ** 31 - 1

    def find_combo(limit, curr_group, start):
        nonlocal min_dist, chicken_list
        if len(curr_group) == limit:
            # print(f"{curr_group}")
            dist = check(min_dist, curr_group)
            if min_dist > dist:
                min_dist = dist
            return

        for i in range(start, len(chicken_list)):
            x, y = chicken_list[i]
            grid[x][y] = 2
            curr_group.append((x, y))
            find_combo(limit, curr_group, i + 1)
            grid[x][y] = 0
            curr_group.pop(-1)

    find_combo(M, [], 0)

    return min_dist


result = simulate(chicken_list)
print(result)
