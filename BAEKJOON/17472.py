"""
섬끼리 바다로 연결하기

- 상하좌우로 붙어있어야지 같은 섬
- 바다에만 다리설치, 다리의 방향이 변경되면 안됨, 길이는 2 이상

완전 그래프 문제
- 각 섬의 각 좌표에서 '가로'/'세로' 2개 방향으로 다리를 놓아본다
- 2개이상 놓을 수 있고, 다른 섬에 맞닿으면 양방향 그래프 추가 (a, b, cost)
- cost로 정렬, 아직 정점이 포함되지않았으면 추가

MST를 확보하는 과정에서 find-union 과정을 고려하지않음. MST문제들을 좀 더 풀어보자
"""
import heapq as hq
from collections import deque, defaultdict


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 각 섬을 고유한 숫자로 칠하기
island_num, island_count = 2, 0
visited = [[False] * M for _ in range(N)]
for x in range(N):
    for y in range(M):
        if grid[x][y] == 1 and not visited[x][y]:
            visited[x][y] = True
            grid[x][y] = island_num
            q = deque([(x, y)])

            while q:
                cx, cy = q.popleft()

                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        grid[nx][ny] = island_num
                        q.append((nx, ny))

            island_num += 1
            island_count += 1

graph = set()  # (다리길이, 시작, 도착)
for x in range(N):
    for y in range(M):
        if grid[x][y] > 1:
            # 상,하,좌,우로 다리 놓기 시도
            curr_island = grid[x][y]

            for dx, dy in directions:
                bridge_len = 1
                while True:  # 다른 섬을 만나면 탈출
                    nx, ny = x + (dx * bridge_len), y + (dy * bridge_len)

                    if not in_range(nx, ny):
                        break

                    if grid[nx][ny] == 0:  # 0, 바다인 경우
                        bridge_len += 1
                    elif grid[nx][ny] == curr_island:  # 같은 섬쪽으로는 확장불가능
                        break
                    elif grid[nx][ny] != 0 and grid[nx][ny] != curr_island:
                        if bridge_len > 2:  # 3 이상 이동했을때 다른 섬인 경우 -> 다리길이는 -1
                            graph.add((bridge_len - 1, curr_island, grid[nx][ny]))
                        break

q = list(graph)
hq.heapify(q)
edge_count, total_cost = 0, 0
parent = {i: i for i in range(2, island_num)}


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


while q:
    cost, start, end = hq.heappop(q)

    if find(start) != find(end):
        union(start, end)
        edge_count += 1
        total_cost += cost

if edge_count != island_count - 1:
    print(-1)
else:
    print(total_cost)
