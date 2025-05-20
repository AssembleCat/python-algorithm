"""
1. grow_tree 나무를 성장시킴, 주변 나무의 갯수만큼 성장함. 
2. 나무 전파, (벽, 다른나무, 제초제) 3가지가 없는 칸에 주변나무 / 번식가능한 칸 을 나눈값을 펼침
3.  
"""

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
        # 검사할칸이 나무일때, 주변에 퍼져나갈 수 있는 칸을 검사 = 빈칸이기만 하면됨
        def can_spread(x, y):
            return (0 <= x < self.n and 0 <= y < self.n and self.grid[x][y] == 0 and self.killing_grid[x][y] == 0)

        def check_empty(x, y):
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            count, positions = 0, []
            
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if can_spread(nx, ny):
                    count += 1
                    positions.append((nx, ny))
            #print(f"{x, y} can spread to {positions}")
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
        def can_spread(x, y):
            return 0 <= x < self.n and 0 <= y < self.n and self.grid[x][y] > 0
        def simulate_kill(x, y):
            total_kill, killed_position = self.grid[x][y], []
            # kill north-west
            for i in range(1, self.k + 1):  
                nx, ny = x - (1*i), y - (1*i)
                if not can_spread(nx, ny):
                    break
                total_kill += self.grid[nx][ny]
                killed_position.append((nx, ny))
            # kill north-east
            for i in range(1, self.k + 1):
                nx, ny = x - (i*1), y + (1*i)
                if not can_spread(nx, ny):
                    break
                total_kill += self.grid[nx][ny]
                killed_position.append((nx, ny))
            # kill south-west
            for i in range(1, self.k + 1):
                nx, ny = x + (i*1), y - (1*i)
                if not can_spread(nx, ny):
                    break
                total_kill += self.grid[nx][ny]
                killed_position.append((nx, ny))
            # kill south-east
            for i in range(1, self.k + 1):
                nx, ny = x + (i*1), y + (1*i)
                if not can_spread(nx, ny):
                    break
                total_kill += self.grid[nx][ny] 
                killed_position.append((nx, ny))          
            #print(f"kill spot({x, y} can kill: {total_kill}), {killed_position}")
            return total_kill, killed_position

        max_tree_killed, max_killed_spot, kill_spot = 0, [], None
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] > 0:
                    tree_killed, killed_positions = simulate_kill(i, j)
                    if max_tree_killed < tree_killed:
                        max_tree_killed = tree_killed
                        max_killed_spot = killed_positions
                        kill_spot = (i, j)
        
        self.grid[kill_spot[0]][kill_spot[1]] = 0
        self.killing_grid[kill_spot[0]][kill_spot[1]] = self.c + 1
        for x, y in max_killed_spot:
            self.grid[x][y] = 0
            self.killing_grid[x][y] = self.c + 1
        
        return max_tree_killed

    def one_year_later(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.killing_grid[i][j] > 0:
                    self.killing_grid[i][j] -= 1    

board = Board(grid, n, k, c)
total_tree_kill = 0
#print(f"1. start grid")
#for row in grid:
#    print(row)
for _ in range(m):
    #print("killing_grid")
    #for row in board.killing_grid:
        #print(row)
    board.grow_tree()
    #print("2. after grow")
    #for row in board.grid:
        #print(row)
    board.spread_tree()
    #print("3. after spread")
    #for row in board.grid:
        #print(row)
    total_tree_kill += board.set_kill_spot()
    #print("4. after kill")
    #for row in board.grid:
        #print(row)
    board.one_year_later()

print(total_tree_kill)