import copy
from collections import deque


class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(5)] for _ in range(5)]

    def rotate(self, x, y, rotation_time):
        result = Board()
        result.grid = copy.deepcopy(self.grid)

        def rotate_90(x, y, grid):
            targets = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1)]
            values = []

            for x, y in targets:
                values.append(grid[x][y])

            values = values[-2:] + values[:-2]

            for idx, value in zip(targets, values):
                nx, ny = idx
                grid[nx][ny] = value

            return grid

        for i in range(rotation_time):
            result.grid = rotate_90(x, y, result.grid)

        return result


    def calculate_score(self):
        selected = [[False for _ in range(5)] for _ in range(5)]
        visited = [[False for _ in range(5)] for _ in range(5)]

        def can_go(x, y):
            return 0 <= x < 5 and 0 <= y < 5

        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        for i in range(5):
            for j in range(5):
                if visited[i][j]:
                    continue

                queue = deque()
                group = []
                value = self.grid[i][j]

                queue.append((i, j))
                visited[i][j] = True
                group.append((i, j))

                while queue:
                    x, y = queue.popleft()
                    for dir in range(4):
                        nx, ny = x + dx[dir], y + dy[dir]
                        if not can_go(nx, ny):
                            continue
                        if visited[nx][ny]:
                            continue
                        if self.grid[nx][ny] == value:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            group.append((nx, ny))

                if len(group) >= 3:
                    for x, y in group:
                        selected[x][y] = True

        score = 0
        for i in range(5):
            for j in range(5):
                if selected[i][j]:
                    score += 1
                    self.grid[i][j] = -1

        return score

    def fill_grid(self, relics):
        for j in range(5):
            for i in range(4, -1, -1):
                if self.grid[i][j] == -1:
                    self.grid[i][j] = relics.popleft()


def simulation():
    k, m = map(int, input().split())
    board = Board()
    relics = deque()
    for i in range(5):
        board.grid[i] = list(map(int, input().split()))
    for relic in list(map(int, input().split())):
        relics.append(relic)

    for _ in range(k):
        max_score = 0
        max_board = None

        for r in range(1, 4):
            for j in range(1, 4):  # 중심점을 i, j로 두는 9가지 경우
                for i in range(1, 4):  # 회전을 1~3 몇번 실행할 것인지 3가지 경우
                    rotated = board.rotate(i, j, r)
                    score = rotated.calculate_score()

                    if score > max_score:
                        max_score = score
                        max_board = rotated

        if max_board is None:
            break

        board = max_board

        while True:
            board.fill_grid(relics)
            chained_score = board.calculate_score()

            if chained_score == 0:
                break

            max_score += chained_score

        print(max_score, end=" ")

simulation()
