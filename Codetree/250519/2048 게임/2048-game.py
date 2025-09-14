import copy

class Board():
    def __init__(self, n):
        self.n = n
        self.grid = [[0 for _ in range(n)] for _ in range(n)]

    def force_gravity(self, direction):
        # 0 - up, 1 - down, 2 - left, 3 - right
        if direction == 0:
            self.force_down()
        elif direction == 1:
            self.force_up()
        elif direction == 2:
            self.force_left()
        else:
            self.force_right()            
                
    def get_max_block(self):
        result = max(max(row) for row in self.grid)
        return result
    
    def compress(self, numbers):
        if len(numbers) < 2:
            return numbers
        
        compressed = []
        last_num = numbers[0]
        for i in range(1, len(numbers)):
            # 이전 숫자와 현재 숫자가 같으면 현재숫자 *2를 결과에 추가함. 그리고 직전 숫자를 초기화함.
            # 이전 숫자와 현재 숫자가 다르면 이전 숫자를 결과에 추가하고 현재 숫자를 이전 숫자에 할당 
            # 직전 숫자가 없거나 초기화되어 있으면 현재 숫자를 마지막 숫자로 할다
            if last_num == None:
                last_num = numbers[i]
            elif last_num == numbers[i]:
                compressed.append(last_num * 2)
                last_num = None
            elif last_num != numbers[i]:
                compressed.append(last_num)
                last_num = numbers[i]

        if last_num is not None:
            compressed.append(last_num)

        return compressed
    
    def force_down(self):
        for k in range(self.n):
            non_zero = []
            for i in range(self.n):
                for j in range(self.n):
                    if j == k and self.grid[i][j] != 0:
                        non_zero.append(self.grid[i][j])
                        self.grid[i][j] = 0
            
            new_col = self.compress(list(reversed(non_zero)))
            for i, element in enumerate(new_col):
                self.grid[self.n - i - 1][k] = element
    
    def force_up(self):
        for k in range(self.n):
            non_zero = []
            for i in range(self.n):
                for j in range(self.n):
                    if j == k and self.grid[i][j] != 0:
                        non_zero.append(self.grid[i][j])
                        self.grid[i][j] = 0
            
            new_col = self.compress(non_zero)
            for i, element in enumerate(new_col):
                self.grid[i][k] = element

    def force_left(self):
        for k in range(self.n):
            non_zero = []
            for i in range(self.n):
                for j in range(self.n):
                    if k == i and self.grid[i][j] != 0:
                        non_zero.append(self.grid[i][j])
                        self.grid[i][j] = 0
            
            new_row = self.compress(non_zero)
            for i, element in enumerate(new_row):
                self.grid[k][i] = element
    
    def force_right(self):
        for k in range(self.n):
            non_zero = []
            for i in range(self.n):
                for j in range(self.n):
                    if k == i and self.grid[i][j] != 0:
                        non_zero.append(self.grid[i][j])
                        self.grid[i][j] = 0
            
            new_row = self.compress(list(reversed(non_zero)))
            for i, element in enumerate(new_row):
                self.grid[k][self.n - i - 1] = element
        

def simulation(board, gravities):
    for gravity in gravities:
        board.force_gravity(gravity)
    
    return board.get_max_block()

max_block = -1
def dfs(board, combo, n):
    global max_block
    if len(combo) == 5:
        copy_board = Board(n)
        copy_board.grid = copy.deepcopy(board.grid)
        max_block = max(max_block, simulation(copy_board, combo))
        return
    
    for i in range(4):
        # 0 - up, 1 - down, 2 - left, 3 - right
        copy_board = Board(n)
        copy_board.grid = copy.deepcopy(board.grid)
        dfs(copy_board, combo + [i], n)    

n = int(input())
board = Board(n)
board.grid = [list(map(int, input().split())) for _ in range(n)]
dfs(board, [], n)
print(max_block)