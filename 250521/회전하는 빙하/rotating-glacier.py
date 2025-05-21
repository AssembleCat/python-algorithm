from collections import deque

n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)]

class Board():
    def __init__(self, grid):
        self.grid = grid
    
    def rotation(self, level):
        if level == 0:
            return

        # 회전 레벨을 받아서 Grid를 회전
        n = len(self.grid)
        new_grid = [[0 for _ in range(n)] for _ in range(n)]
        
        group_size, half_size = 1 << level, 1 << (level - 1)
        for i in range(0, n, group_size):
            for j in range(0, n, group_size):
                self.rotate_group(new_grid, i, j, half_size, 0)
                self.rotate_group(new_grid, i, j + half_size, half_size, 1)
                self.rotate_group(new_grid, i + half_size, j + half_size, half_size, 3)
                self.rotate_group(new_grid, i + half_size, j, half_size, 2)
        self.grid = new_grid

    def rotate_group(self, new_grid, x, y, half_size, direction):
        dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
        for i in range(x, x + half_size):
            for j in range(y, y + half_size):
                #print(f"rotations in {i, j}, direction: {direction}")
                nx, ny = i + dx[direction] * half_size, j + dy[direction] * half_size
                new_grid[nx][ny] = self.grid[i][j]

    def in_range(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid)
                
    def melting(self):
        # 사방 3칸에 얼음이 있으면 안녹음, 그 외에는 얼음이 녹음 -1
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
        n = len(self.grid)
        ice_count_grid = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                ice_count = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if self.in_range(nx, ny) and self.grid[nx][ny] > 0:
                        ice_count += 1
                ice_count_grid[i][j] = ice_count
        
        for i in range(n):
            for j in range(n):
                if ice_count_grid[i][j] < 3 and self.grid[i][j] > 0:
                    self.grid[i][j] -= 1

    def get_total_ice(self):
        return sum(sum(row) for row in self.grid)
    
    def group_size(self, x, y):
        q = deque()
        visited = [[False for _ in range(len(self.grid))] for _ in range(len(self.grid))]
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        group = [(x, y)]
        visited[x][y] = True
        q.append((x, y))

        while q:
            cx, cy = q.popleft()
            #print(f"{cx, cy} track")
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if not self.in_range(nx, ny):
                    continue
                if visited[nx][ny]:
                    continue
                if self.grid[nx][ny] == 0:
                    continue
                
                q.append((nx, ny))
                visited[nx][ny] = True
                group.append((nx, ny))

        #print(f"{x, y}: {group}")
        return len(group)

    def get_biggest_group(self):
        n = len(self.grid)
        biggest_size = 0

        for i in range(n):
            for j in range(n):
                if self.grid[i][j] > 0:
                    biggest_size = max(biggest_size, self.group_size(i, j))

        return biggest_size
                
        
board = Board(grid)
levels = list(map(int, input().split()))
for level in levels: 
    board.rotation(level)
    board.melting()
print(board.get_total_ice())
print(board.get_biggest_group())
