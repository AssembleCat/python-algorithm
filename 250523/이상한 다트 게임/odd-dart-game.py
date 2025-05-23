import math

class Board():
    def __init__(self, grid, n, m):
        self.grid = grid
        self.n = n
        self.m = m

    def rotation(self, x, d, k):
        # 원판 대상, 회전 방향, 회전 칸수를 받아 회전을 실행시킴 0 - 시계, 1 - 반시계
        target_idx = x - 1
        while target_idx < len(self.grid):
            if d == 0: # 시계 방향 회전 [1, 2, 3, 4] -> [4, 1, 2, 3]
                self.grid[target_idx] = self.grid[target_idx][self.m - k:] + self.grid[target_idx][:self.m - k]
            else:
                self.grid[target_idx] = self.grid[target_idx][k:] + self.grid[target_idx][:k] 
            target_idx += x

    def in_range(self, x):
        return 0 <= x < self.n

    def remove(self):
        # 인접한 숫자를 제거
        remove_target = set()
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        for i in range(self.n): # 원판 
            for j in range(self.m): # 원판 내 숫자
                if self.grid[i][j] == -1: # 삭제된 수는 제거검사할필요 없음.
                    continue

                for d in range(4): # direction
                    nx, ny = i + dx[d], (j + dy[d] + self.m) % self.m 
                    if not self.in_range(nx): # 원판은 index를 벗어나면 안됨.
                        continue
                    if self.grid[i][j] == self.grid[nx][ny]:
                        remove_target.add((i, j))
                        remove_target.add((nx, ny))
        
        for i, j in list(remove_target):
            self.grid[i][j] = -1
        
        return len(remove_target) > 0

    def generalized(self):
        total = self.get_total()
        count = sum([
            1
            for i in range(self.n)
            for j in range(self.m)
            if self.grid[i][j] != -1
        ])

        if count == 0:
            return 

        avg = total // count
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == -1:
                    continue
                if self.grid[i][j] == avg: # 평균과 같으면 스킵 
                    continue
                if self.grid[i][j] > avg:
                    self.grid[i][j] -= 1
                else:
                    self.grid[i][j] += 1

    def is_removed(self):
        removed_count = sum([
            1
            for i in range(self.n)
            for j in range(self.m)
            if self.grid[i][j] == -1
        ])
        
        return removed_count > 0

    def get_total(self):
        total = sum([
            self.grid[i][j]
            for i in range(self.n)
            for j in range(self.m)
            if self.grid[i][j] != -1
        ])

        return total

n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
rotate_type = [list(map(int, input().split())) for _ in range(q)]

board = Board(grid, n, m)
for r_type in rotate_type:
    x, d, k = r_type
    board.rotation(x, d, k)
    if not board.remove():
        board.generalized()

print(board.get_total())