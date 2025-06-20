n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
rotations = list(map(int, input().split()))
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

class Cube():
    def __init__(self):
        self.bottom_top = (0, 0)
        self.left_right = (0, 0)
        self.front_back = (0, 0)
    
    def get_side_number(self, direction):
        if direction == 1:
            return self.left_right[1]
        elif direction == 2:
            return self.left_right[0]
        elif direction == 3:
            return self.front_back[0]
        else:
            return self.front_back[1]

    def rotation(self, direction, num):
        # 1 - east, 2 - west, 3 - north, 4 - south
        # 방향과 바닥면에 들어갈 숫자를 제시해야함.
        if direction == 1:
            self.left_right, self.bottom_top = self.bottom_top, (num, self.left_right[0])
        elif direction == 2:
            self.left_right, self.bottom_top = (self.bottom_top[1], self.bottom_top[0]), (num, self.left_right[1])
        elif direction == 3:
            self.front_back, self.bottom_top = (self.bottom_top[1], self.bottom_top[0]), (num, self.front_back[1])
        else:
            self.front_back, self.bottom_top = self.bottom_top, (num, self.front_back[0])

    def get_top_side_number(self):
        return self.bottom_top[1]

    def cube_tostring(self):
        print(f"bottom_top({self.bottom_top}, left_right({self.left_right}), front_back({self.front_back})")

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m

cube = Cube()
for rotation in rotations:
    nx, ny = x + dx[rotation - 1], y + dy[rotation - 1]
    # print(f"new_position({nx, ny})")
    if not can_go(nx, ny):
        # print(f"unreachable ignore({nx, ny})")
        continue
    # 1. 도달 좌표가 0 이면 주사위 바닥면의 숫자를 해당 칸에 복사하여 넣음.
    if grid[nx][ny] == 0:
        # print(f"grid({nx, ny} is zero )")
        cube.rotation(rotation, cube.get_side_number(rotation))
        grid[nx][ny] = cube.bottom_top[0]
    # 2. 도달 좌표가 0이 아니면 해당 숫자를 주사위 바닥면에 할당하고, 해당 좌표는 0이됨
    elif grid[nx][ny] != 0:
        # print(f"grid({nx, ny}) is not zero")
        cube.rotation(rotation, grid[nx][ny])
        grid[nx][ny] = 0
    
    # print(cube.cube_tostring())

    x, y = nx, ny
    
    print(cube.get_top_side_number())

        
    
