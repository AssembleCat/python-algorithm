"""
조합을 생성하고 저장해두는 것은 케이스 숫자가 클때 불리함. 생성한 당시 결과값을 추출할 수 있으면 조합을 저장하지 않는 방향으로 가야함.
남겨둘 병원의 조합을 생성하고 사람마다 최소거리를 구하는 컨셉을 맞았는데 시간 복잡도를 고려하지않았음.
"""
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

hospital = []
humans = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            hospital.append((i, j))
        elif mat[i][j] == 1:
            humans.append((i, j))

min_total_distance = float('inf')

def calculate_distance(selected):
    total = 0
    for hx, hy in humans:
        min_dist = float('inf')
        for cx, cy in selected:
            min_dist = min(min_dist, abs(hx - cx) + abs(hy - cy))
        total += min_dist
    return total

def dfs(start, comb):
    global min_total_distance

    if len(comb) == m:
        dist = calculate_distance(comb)
        min_total_distance = min(min_total_distance, dist)
        return

    for i in range(start, len(hospital)):
        dfs(i + 1, comb + [hospital[i]])

dfs(0, [])
print(min_total_distance)
