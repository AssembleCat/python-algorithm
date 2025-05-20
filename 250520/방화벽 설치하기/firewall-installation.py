import copy

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

class Board():
    def __init__(self, grid, n, m):
        self.grid = grid
        self.n = n
        self.m = m
    
    def set_extra_wall(self, walls):
        for x, y in walls:
            self.grid[x][y] = 1
    
    def fire_on(self):
        def can_go(x, y):
            return 0 <= x < self.n and 0 <= y < self.m and self.grid[x][y] != 1

        def dfs(x, y):
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not can_go(nx, ny):
                    continue
                if self.grid[nx][ny] == 0:
                    self.grid[nx][ny] = 2
                    dfs(nx, ny)

        for i in range(n):
            for j in range(m):
                if self.grid[i][j] == 2: # if fire
                    dfs(i, j)               
    
    def get_unfire_size(self):
        count = sum([
            1
            for i in range(self.n)
            for j in range(self.m)
            if self.grid[i][j] == 0
        ])

        return count

def find_combo(position):
    combo = set()
    
    def tracking(start, group):
        if len(group) == 3:
            combo.add(tuple(group))
            return
        
        for i in range(start, len(position)):
            tracking(i+1, group + [position[i]])

    tracking(0, [])
    return list(combo)

empty_position = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            empty_position.append((i, j))

combinations = find_combo(empty_position)
max_unfire_size = -1
for combo in combinations:
    board = Board(copy.deepcopy(grid), n, m)
    board.set_extra_wall(combo)
    board.fire_on()
    max_unfire_size = max(max_unfire_size, board.get_unfire_size())

print(max_unfire_size)        