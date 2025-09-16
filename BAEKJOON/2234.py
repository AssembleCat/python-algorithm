from collections import deque

directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
room_num_grid = [[0] * N for _ in range(M)]
room_dict = {}  # {번호: 그룹}


def in_range(x, y):
    return 0 <= x < M and 0 <= y < N


def bfs():
    visited = [[False] * N for _ in range(M)]
    group_num = 1
    for i in range(M):
        for j in range(N):
            curr_group = []
            if not visited[i][j]:
                visited[i][j] = True
                curr_group.append((i, j))

                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()

                    for d, (dx, dy) in enumerate(directions):
                        nx, ny = x + dx, y + dy
                        # print(f"{grid[nx][ny]}, {(1 << d)}")
                        if in_range(nx, ny) and grid[x][y] & (1 << d) == 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            curr_group.append((nx, ny))

            if len(curr_group) > 0:
                room_dict[group_num] = curr_group
                group_num += 1


# 연결된 방들을 확보
bfs()
room_count, max_room = len(room_dict), max([len(group) for group in room_dict.values()])
for room_num, group in room_dict.items():
    for (x, y) in group:
        room_num_grid[x][y] = room_num

# 벽 하나 제거했을때 가장 큰 방 크기
removed_max_room = -1
for x in range(M):
    for y in range(N):
        for d, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[x][y] & (1 << d) != 0 and room_num_grid[x][y] != room_num_grid[nx][ny]:  # 격자내고, 벽이 존재함.
                removed_size = len(room_dict[room_num_grid[x][y]]) + len(room_dict[room_num_grid[nx][ny]])
                if removed_size > removed_max_room:
                    removed_max_room = removed_size

print(room_count)
print(max_room)
print(removed_max_room)
