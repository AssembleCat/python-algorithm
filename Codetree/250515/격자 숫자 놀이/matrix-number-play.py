r, c, k = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(3)]
grid = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    for j in range(3):
        grid[i][j] = numbers[i][j]

def count(elements):
    count_map = {}
    for el in elements:
        if el == 0:
            continue
        count_map[el] = count_map.get(el, 0) + 1
    
    count_map = sorted(count_map.items(), key=lambda x: (x[1], x[0]))
    new_elements = []
    for v, c in count_map:
        new_elements.extend([v, c])
    
    if len(new_elements) > 100:
        return new_elements[:100]
    
    return new_elements

def do_row():
    global grid
    new_grid = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(len(grid)):
        i_row_count = count(grid[i])
        if len(i_row_count) > 0:
            #print(i_row_count)
            for idx, value in enumerate(i_row_count):
                new_grid[i][idx] = value
    grid = new_grid

def do_col():
    global grid
    new_grid = [[0 for _ in range(100)] for _ in range(100)]
    for k in range(len(grid[0])):
        k_col = [
            grid[i][j]
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if k == j
        ]

        k_col_count = count(k_col)
        if len(k_col_count) > 0:
            #print(k_col_count)
            for idx, value in enumerate(k_col_count):
                new_grid[idx][k] = value
    grid = new_grid

def find_row_col_len():
    row_len, col_len = 0, 0
    for i in range(len(grid)):
        i_col_len = sum([1 for j in range(len(grid)) if grid[i][j] != 0])
        i_row_len = sum([1 for j in range(len(grid)) if grid[j][i] != 0])
        row_len = max(row_len, i_row_len)
        col_len = max(col_len, i_col_len)
    
    return row_len, col_len

time = 0
while time <= 100:
    if grid[r-1][c-1] == k:
        break

    row, col = find_row_col_len()
    #print(f"{time} 단계 {row, col}")

    if row >= col:
        #print("행 기준 정렬")
        do_row()
    else:
        #print("열 기준 정렬")
        do_col()
    time += 1

if time > 100:
    print(-1)
else: 
    print(time)