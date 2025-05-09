"""
전체 병원 갯수중 m개를 남기는 조합을 생성
각 사람별로 가장 가까운 병원거리를 연산 -> 전체 병원거리 연산
"""

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
hospital, humans = [], []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            hospital.append([i, j])
        elif mat[i][j] == 1:
            humans.append([i, j])
visited = [False for _ in range(len(hospital))]
minimum = 10000000

def calculate_distance(comb):
    global minimum 
    #print(f"{comb} 조합 계산")
    distance = 0
    for human in humans:
        shortest = 200
        for h in comb:
            if abs(human[0] - hospital[h][0]) + abs(human[1] - hospital[h][1]) < shortest:
                shortest = abs(human[0] - hospital[h][0]) + abs(human[1] - hospital[h][1])
        distance += shortest

    if distance < minimum:
        minimum = distance

def find_h_comb(start, comb):
    if len(comb) == m:
        calculate_distance(comb)
        return
    
    for i in range(start, len(visited)):
        if not visited[i]:
            visited[i] = True
            find_h_comb(start+1, comb + [i])
            visited[i] = False
    
find_h_comb(0, [])
print(minimum)