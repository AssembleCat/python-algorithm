import copy
import math

n, m, k, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

class Board():
    def __init__(self, grid, n, k, c):
        self.grid = grid        
        self.killing_grid = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.k = k
        self.c = c

    def grow_tree(self):
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        def can_go(nx, ny):
            return 0 <= nx < self.n and 0 <= ny < self.n

        for i in range(self.n):
            for j in range(self.n):                    
                if self.grid[i][j] > 0: # current is tree
                    tree_count = 0
                    for d in range(4): # check_surround
                        nx, ny = i + dx[d], j + dy[d]
                        if can_go(nx, ny) and self.grid[nx][ny] > 0:
                            tree_count += 1
                    self.grid[i][j] += tree_count

    def spread_tree(self):
        new_grid = copy.deepcopy(self.grid)

        def can_spread(x, y):
            return (0 <= x < self.n and 0 <= y < self.n and 
                    self.grid[x][y] == 0 and self.killing_grid[x][y] == 0)

        def check_empty(x, y):
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            count, positions = 0, []
            
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if can_spread(nx, ny):
                    count += 1
                    positions.append((nx, ny))
            return count, positions

        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] > 0:
                    empty_count, empty_positions = check_empty(i, j)
                    if empty_count == 0:
                        continue  
                    avg_spread = math.floor(self.grid[i][j] / empty_count)
                    for sx, sy in empty_positions:
                        new_grid[sx][sy] += avg_spread

        self.grid = new_grid

    def set_kill_spot(self):
        def in_bound(x, y):
            return 0 <= x < self.n and 0 <= y < self.n

        def simulate_kill(x, y):
            total_kill = self.grid[x][y]
            killed_position = []
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for dx, dy in directions:
                for i in range(1, self.k + 1):
                    nx, ny = x + dx * i, y + dy * i
                    if not in_bound(nx, ny):
                        break
                    if self.grid[nx][ny] == -1:
                        break
                    elif self.grid[nx][ny] == 0:
                        killed_position.append((nx, ny))
                        break
                    else:
                        total_kill += self.grid[nx][ny]
                        killed_position.append((nx, ny))
            return total_kill, killed_position

        max_tree_killed, max_killed_spot, kill_spot = 0, [], None
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] > 0:
                    tree_killed, killed_positions = simulate_kill(i, j)
                    if tree_killed > max_tree_killed:
                        max_tree_killed = tree_killed
                        max_killed_spot = killed_positions
                        kill_spot = (i, j)

        if kill_spot is None:
            return max_tree_killed

        x, y = kill_spot
        self.grid[x][y] = 0
        self.killing_grid[x][y] = self.c + 1
        for a, b in max_killed_spot:
            self.grid[a][b] = 0
            self.killing_grid[a][b] = self.c + 1

        return max_tree_killed

    def one_year_later(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.killing_grid[i][j] > 0:
                    self.killing_grid[i][j] = max(0, self.killing_grid[i][j] - 1)

board = Board(grid, n, k, c)
total_tree_kill = 0

for _ in range(m):
    board.grow_tree()
    board.spread_tree()
    total_tree_kill += board.set_kill_spot()
    board.one_year_later()

print(total_tree_kill)
