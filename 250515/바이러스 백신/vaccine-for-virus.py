"""
1. m개의 병원을 선택하는 조합을 추출 -> 순열이 아니라 조합임.
2. 각 병원별로 BFS를 실행 -> 주변 칸에 바이러스가 존재하거나, 가장 적은 칸으로 도달 할경우 재귀 발생
3. BFS가 종료된 후 Grid에서 가장 큰 값을 선택 -> 바이러스가 여전히 존재하는지도 확인해야함.
"""
from collections import deque

INIT_SCORE = 500
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visit_score = [[INIT_SCORE for _ in range(n)] for _ in range(n)]
min_time = INIT_SCORE

def find_hospital():
    # 병원 좌표를 담은 배열 반환
    hospital = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                hospital.append((i, j))
    return hospital

def can_go(x, y):
    # 해당 좌표가 도달가능한지 검사
    return 0 <= x < n and 0 <= y < n and grid[x][y] != 1

def reset_visit_score():
    global visit_score
    visit_score = [[INIT_SCORE for _ in range(n)] for _ in range(n)]

def calculate_time(hospitals):
    global min_time
    complete_time = -1
    for i in range(n):
        for j in range(n):
            if visit_score[i][j] != INIT_SCORE and visit_score[i][j] > complete_time and grid[i][j] == 0:
                complete_time = visit_score[i][j]
    min_time = min(min_time, complete_time)
    #print(f"완료시간: {complete_time}, 현재 최소시간: {min_time}")

# 1. 애초에 바이러스가 없으면 진행할 필요가 없음 초기에 0이 없는지 검사
# 2. 바이러스 제거 성공여부를 검사하여 성공한 케이스가 없다면 -1 출력
def is_virus_exist():
    virus = sum([
        1
        for i in range(n)
        for j in range(n)
        if grid[i][j] == 0
    ])
    return virus > 0

def is_virus_removed():
    for i in range(n):
        for j in range(n):
            if visit_score[i][j] == INIT_SCORE and grid[i][j] == 0:
                return False
    return True

def bfs(hospitals):
    global visit_score
    bfs_q = deque()
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    # 1. 4방향을 갈 수 있는지 검사 -> 못간다면 bfs 종료
    # 2. 갈 수 있는 자리에 이미 더 낮은 Score가 존재한다면 실행 종료
    for x, y in hospitals:
        bfs_q.append((x, y, 0))
        visit_score[x][y] = 0
    
    while bfs_q:
        cx, cy, score = bfs_q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not can_go(nx, ny):
                continue
            if visit_score[nx][ny] > score + 1:
                visit_score[nx][ny] = score + 1
                bfs_q.append((nx, ny, score + 1))

def simulation():
    hospitals = find_hospital()
    def combinations(start, comb):
        if len(comb) == m:
            #print(f"현재 조합({comb})으로 BFS 실행")
            reset_visit_score()
            bfs(comb)
            if is_virus_removed():
                calculate_time(comb)
            return
        
        for i in range(start, len(hospitals)):
            combinations(i + 1, comb + [hospitals[i]])
    
    combinations(0, [])
        
if is_virus_exist():
    simulation()
    if min_time == INIT_SCORE:
        print(-1)
    else:
        print(min_time)
else:
    print(0)