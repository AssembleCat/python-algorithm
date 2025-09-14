import math 

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dust_grid = [ # left - down - right - up
    [
        [0, 0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5, 0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [2, 7, 0, 7, 2],
        [0, 10, 0, 10, 0],
        [0, 0, 5, 0, 0]
    ],
    [
        [0, 0, 2, 0, 0],
        [0, 1, 7, 10, 0],
        [0, 0, 0, 0, 5],
        [0, 1, 7, 10, 0],
        [0, 0, 2, 0, 0]
    ],
    [
        [0, 0, 5, 0, 0],
        [0, 10, 0, 10, 0],
        [2, 7, 0, 7, 2],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
]

direction, move_count = 0, 1
curr_x, curr_y = n // 2, n // 2
total_lose_dust = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def end():
    return not curr_x and not curr_y

def add_dust(x, y, dust):
    global total_lose_dust
    
    if not in_range(x, y):
        total_lose_dust += dust
    else: 
        grid[x][y] += dust

def move():
    global curr_x, curr_y
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    curr_x, curr_y = curr_x + dx[direction], curr_y + dy[direction]

    added_dust = 0
    for i in range(5):
        for j in range(5):
            dust = grid[curr_x][curr_y] * dust_grid[direction][i][j] // 100
            add_dust(curr_x - 2 + i, curr_y - 2 + j, dust) 

            added_dust += dust
    
    add_dust(curr_x + dx[direction], curr_y + dy[direction], grid[curr_x][curr_y] - added_dust)

while not end():
    for _ in range(move_count):
        move()

        if end():
            break
    
    direction = (direction + 1) % 4
    if direction == 0 or direction == 2:
        move_count += 1

print(total_lose_dust)